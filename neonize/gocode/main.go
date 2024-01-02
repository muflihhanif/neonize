package main

/*

   #include <stdlib.h>
   #include "header/cstruct.h"

   typedef void (*ptr_to_python_function_string) (char*);

   static inline void call_c_func_string(ptr_to_python_function_string ptr, char* xStr) {
    (ptr)(xStr);
    }
	typedef void (*ptr_to_python_function_bytes)(const char*, size_t, const char*, size_t);

	static inline void call_c_func_bytes(ptr_to_python_function_bytes ptr, const char* data, size_t size, const char* msginfo, size_t msginfo_size) {
		(ptr)(data, size, msginfo, msginfo_size);
	}
*/
import "C"
import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"unsafe"

	"github.com/krypton-byte/neonize/neonize"
	"github.com/krypton-byte/neonize/utils"
	_ "github.com/mattn/go-sqlite3"
	"go.mau.fi/whatsmeow"
	"go.mau.fi/whatsmeow/store/sqlstore"
	"go.mau.fi/whatsmeow/types/events"

	waProto "go.mau.fi/whatsmeow/binary/proto"
	waLog "go.mau.fi/whatsmeow/util/log"
	"google.golang.org/protobuf/proto"
)

var clients = make(map[string]*whatsmeow.Client)

func getByteByAddr(addr *C.uchar, size C.int) []byte {
	var result []byte
	for i := 0; i < int(size); i++ {
		value := *(*C.uchar)(unsafe.Pointer(uintptr(unsafe.Pointer(addr)) + uintptr(i)))
		// 	fmt.Println(value)
		result = append(result, byte(value))
	}
	return result
}

func ReturnBytes(data []byte) C.struct_BytesReturn {
	size := C.size_t(len(data))
	ptr := (*C.char)(C.CBytes(data))
	// defer C.free(unsafe.Pointer(&ptr))
	return C.struct_BytesReturn{ptr, size}
}

//export Upload
func Upload(id *C.char, mediabuff *C.uchar, mediaSize C.int, mediatype C.int) C.struct_BytesReturn {
	client := clients[C.GoString(id)]
	data := getByteByAddr(mediabuff, mediaSize)
	response, err_upload := client.Upload(context.Background(), data, utils.MediaType[int(mediatype)])
	if err_upload != nil {
		panic(err_upload)
	}
	encoded := utils.EncodeUploadResponse(response)
	bytes, err := proto.Marshal(&encoded)
	fmt.Println(string(bytes))
	if err != nil {
		panic(err)
	}
	return ReturnBytes(bytes)
}

//export SendMessage
func SendMessage(id *C.char, JIDByte *C.uchar, JIDSize C.int, messageByte *C.uchar, messageSize C.int) {
	client := clients[C.GoString(id)]
	fmt.Print("unmarshaling jid ", JIDSize)
	jid := getByteByAddr(JIDByte, JIDSize)
	fmt.Println(jid, "jhid")
	var neonize_jid neonize.JID
	err := proto.Unmarshal(jid, &neonize_jid)
	if err != nil {
		panic(err)
	}
	fmt.Print("unmarshaling message")
	message_bytes := getByteByAddr(messageByte, messageSize)
	var message waProto.Message
	err_message := proto.Unmarshal(message_bytes, &message)
	if err_message != nil {
		panic(err)
	}
	go client.SendMessage(context.Background(), utils.DecodeJidProto(&neonize_jid), &message)
}

//export Neonize
func Neonize(db *C.char, id *C.char, qrCb C.ptr_to_python_function_string, logStatus C.ptr_to_python_function_string, messageCb C.ptr_to_python_function_bytes) {
	dbLog := waLog.Stdout("Database", "DEBUG", true)
	// Make sure you add appropriate DB connector imports, e.g. github.com/mattn/go-sqlite3 for SQLite
	container, err := sqlstore.New("sqlite3", fmt.Sprintf("file:%s?_foreign_keys=on", C.GoString(db)), dbLog)
	if err != nil {
		panic(err)
	}
	// If you want multiple sessions, remember their JIDs and use .GetDevice(jid) or .GetAllDevices() instead.
	deviceStore, err := container.GetFirstDevice()
	if err != nil {
		panic(err)
	}
	clientLog := waLog.Stdout("Client", "DEBUG", true)
	client := whatsmeow.NewClient(deviceStore, clientLog)
	clients[C.GoString(id)] = client
	eventHandler := func(evt interface{}) {
		switch v := evt.(type) {
		case *events.Message:
			// fmt.Println("Received a message!", v.Message.GetConversation())
			proto.Merge(v.Message, &waProto.Message{
				Chat: &waProto.Chat{
					DisplayName: &v.Info.PushName,
					Id:          &v.Info.ID,
				},
			})
			data, err := proto.Marshal(v.Message)
			if err != nil {
				panic(err)
			}
			// fname := "z.buf"
			// file, err := os.Create(fname)
			// if err != nil {
			// 	panic(err)
			// }
			// file.Write(data)
			// defer file.Close()
			// fmt.Println("dataproto: ", data)
			// if err != nil {
			// 	panic(err)
			// }
			messageSource := neonize.MessageSource{
				Chat:               utils.EncodeJidProto(v.Info.Chat),
				Sender:             utils.EncodeJidProto(v.Info.Sender),
				IsFromMe:           &v.Info.IsFromMe,
				IsGroup:            &v.Info.IsGroup,
				BroadcastListOwner: utils.EncodeJidProto(v.Info.BroadcastListOwner),
				ID:                 &v.Info.ID,
			}
			messageSourceBytes, err := proto.Marshal(&messageSource)
			if err != nil {
				panic(err)
			}
			messageSourceCDATA := (*C.char)(unsafe.Pointer(&messageSourceBytes[0]))
			messageSourceCSize := C.size_t(len(messageSourceBytes))
			CData := (*C.char)(unsafe.Pointer(&data[0]))
			// defer C.free(unsafe.Pointer(CData))
			CSize := C.size_t(len(data))
			// defer C.free(unsafe.Pointer(&CSize))
			C.call_c_func_bytes(messageCb, CData, CSize, messageSourceCDATA, messageSourceCSize)
			// C.free(unsafe.Pointer(CData))

		}
	}
	client.AddEventHandler(eventHandler)
	qrFuncCb := func(data string) {
		cstr := C.CString(data)
		defer C.free(unsafe.Pointer(cstr))
		C.call_c_func_string(qrCb, cstr)
	}
	logStatusCb := func(eventName string) {
		cstr := C.CString(eventName)
		defer C.free(unsafe.Pointer(cstr))
		C.call_c_func_string(logStatus, cstr)
	}
	if client.Store.ID == nil {
		// No ID stored, new login
		qrChan, _ := client.GetQRChannel(context.Background())
		err = client.Connect()
		if err != nil {
			panic(err)
		}
		for evt := range qrChan {
			if evt.Event == "code" {
				// Render the QR code here
				// e.g. qrterminal.GenerateHalfBlock(evt.Code, qrterminal.L, os.Stdout)
				// or just manually `echo 2@... | qrencode -t ansiutf8` in a terminal

				fmt.Println("QR code:", evt.Code)
				fmt.Println("Waduh")
				qrFuncCb(evt.Code)
				// fmt.Println(cstr)
				// C.free(unsafe.Pointer(cstr))
			} else {
				fmt.Println("Login event:", evt.Event)
				logStatusCb(evt.Event)
			}
		}
	} else {
		// Already logged in, just connect
		err = client.Connect()
		if err != nil {
			panic(err)
		}
	}

	// Listen to Ctrl+C (you can also do something else that prevents the program from exiting)
	c := make(chan os.Signal)
	signal.Notify(c, os.Interrupt, syscall.SIGTERM)
	<-c

	client.Disconnect()
}

//export Download
func Download(id *C.char, messageProto *C.uchar, size C.int) C.struct_BytesReturn {
	var message waProto.Message
	err := proto.Unmarshal(getByteByAddr(messageProto, size), &message)
	if err != nil {
		panic(err)
	}
	data_buff, err := clients[C.GoString(id)].DownloadAny(&message)
	if err != nil {
		panic(err)
	}
	return ReturnBytes(data_buff)

}

// /GROUP
//
//export GetGroupInfo
func GetGroupInfo(id *C.char, JIDByte *C.uchar, JIDSize C.int) {
	var neoJIDProto neonize.JID
	err := proto.Unmarshal(getByteByAddr(JIDByte, JIDSize), &neoJIDProto)
	if err != nil {

	}
	x, err := clients[C.GoString(id)].GetGroupInfo(utils.DecodeJidProto(&neoJIDProto))
	fmt.Println(x)
}

//export SetGroupName
func SetGroupName(id *C.char, JIDByte *C.uchar, JIDSize C.int, name *C.char) {
	jidbyte := getByteByAddr(JIDByte, JIDSize)
	var neoJIDProto neonize.JID
	err := proto.Unmarshal(jidbyte, &neoJIDProto)
	if err != nil {
		panic(err)
	}
	clients[C.GoString(id)].SetGroupName(utils.DecodeJidProto(&neoJIDProto), C.GoString(name))

}

///

func main() {

}
