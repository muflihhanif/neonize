"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class JID(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    RAWAGENT_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    INTEGRATOR_FIELD_NUMBER: builtins.int
    SERVER_FIELD_NUMBER: builtins.int
    User: builtins.str
    RawAgent: builtins.int
    Device: builtins.int
    Integrator: builtins.int
    Server: builtins.str
    def __init__(
        self,
        *,
        User: builtins.str | None = ...,
        RawAgent: builtins.int | None = ...,
        Device: builtins.int | None = ...,
        Integrator: builtins.int | None = ...,
        Server: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Device", b"Device", "Integrator", b"Integrator", "RawAgent", b"RawAgent", "Server", b"Server", "User", b"User"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Device", b"Device", "Integrator", b"Integrator", "RawAgent", b"RawAgent", "Server", b"Server", "User", b"User"]) -> None: ...

global___JID = JID

@typing_extensions.final
class UploadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    URL_FIELD_NUMBER: builtins.int
    DIRECTPATH_FIELD_NUMBER: builtins.int
    HANDLE_FIELD_NUMBER: builtins.int
    MEDIAKEY_FIELD_NUMBER: builtins.int
    FILEENCSHA256_FIELD_NUMBER: builtins.int
    FILESHA256_FIELD_NUMBER: builtins.int
    FILELENGTH_FIELD_NUMBER: builtins.int
    url: builtins.str
    DirectPath: builtins.str
    Handle: builtins.str
    MediaKey: builtins.bytes
    FileEncSHA256: builtins.bytes
    FileSHA256: builtins.bytes
    FileLength: builtins.int
    def __init__(
        self,
        *,
        url: builtins.str | None = ...,
        DirectPath: builtins.str | None = ...,
        Handle: builtins.str | None = ...,
        MediaKey: builtins.bytes | None = ...,
        FileEncSHA256: builtins.bytes | None = ...,
        FileSHA256: builtins.bytes | None = ...,
        FileLength: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["DirectPath", b"DirectPath", "FileEncSHA256", b"FileEncSHA256", "FileLength", b"FileLength", "FileSHA256", b"FileSHA256", "Handle", b"Handle", "MediaKey", b"MediaKey", "url", b"url"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["DirectPath", b"DirectPath", "FileEncSHA256", b"FileEncSHA256", "FileLength", b"FileLength", "FileSHA256", b"FileSHA256", "Handle", b"Handle", "MediaKey", b"MediaKey", "url", b"url"]) -> None: ...

global___UploadResponse = UploadResponse

@typing_extensions.final
class MessageSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHAT_FIELD_NUMBER: builtins.int
    SENDER_FIELD_NUMBER: builtins.int
    ISFROMME_FIELD_NUMBER: builtins.int
    ISGROUP_FIELD_NUMBER: builtins.int
    BROADCASTLISTOWNER_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    @property
    def Chat(self) -> global___JID: ...
    @property
    def Sender(self) -> global___JID: ...
    IsFromMe: builtins.bool
    IsGroup: builtins.bool
    @property
    def BroadcastListOwner(self) -> global___JID: ...
    ID: builtins.str
    def __init__(
        self,
        *,
        Chat: global___JID | None = ...,
        Sender: global___JID | None = ...,
        IsFromMe: builtins.bool | None = ...,
        IsGroup: builtins.bool | None = ...,
        BroadcastListOwner: global___JID | None = ...,
        ID: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["BroadcastListOwner", b"BroadcastListOwner", "Chat", b"Chat", "ID", b"ID", "IsFromMe", b"IsFromMe", "IsGroup", b"IsGroup", "Sender", b"Sender"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["BroadcastListOwner", b"BroadcastListOwner", "Chat", b"Chat", "ID", b"ID", "IsFromMe", b"IsFromMe", "IsGroup", b"IsGroup", "Sender", b"Sender"]) -> None: ...

global___MessageSource = MessageSource

@typing_extensions.final
class DeviceSentMeta(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DESTINATIONJID_FIELD_NUMBER: builtins.int
    PHASH_FIELD_NUMBER: builtins.int
    DestinationJID: builtins.str
    Phash: builtins.str
    def __init__(
        self,
        *,
        DestinationJID: builtins.str | None = ...,
        Phash: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["DestinationJID", b"DestinationJID", "Phash", b"Phash"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["DestinationJID", b"DestinationJID", "Phash", b"Phash"]) -> None: ...

global___DeviceSentMeta = DeviceSentMeta

@typing_extensions.final
class MessageInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGESOURCE_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    SERVERID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PUSHNAME_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    CATEGORY_FIELD_NUMBER: builtins.int
    MULTICAST_FIELD_NUMBER: builtins.int
    MEDIATYPE_FIELD_NUMBER: builtins.int
    EDITATTRIBUTE_FIELD_NUMBER: builtins.int
    @property
    def MessageSource(self) -> global___MessageSource: ...
    ID: builtins.str
    ServerID: builtins.str
    Type: builtins.str
    PushName: builtins.str
    Timestamp: builtins.int
    Category: builtins.str
    Multicast: builtins.bool
    MediaType: builtins.str
    EditAttribute: builtins.str
    def __init__(
        self,
        *,
        MessageSource: global___MessageSource | None = ...,
        ID: builtins.str | None = ...,
        ServerID: builtins.str | None = ...,
        Type: builtins.str | None = ...,
        PushName: builtins.str | None = ...,
        Timestamp: builtins.int | None = ...,
        Category: builtins.str | None = ...,
        Multicast: builtins.bool | None = ...,
        MediaType: builtins.str | None = ...,
        EditAttribute: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Category", b"Category", "EditAttribute", b"EditAttribute", "ID", b"ID", "MediaType", b"MediaType", "MessageSource", b"MessageSource", "Multicast", b"Multicast", "PushName", b"PushName", "ServerID", b"ServerID", "Timestamp", b"Timestamp", "Type", b"Type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Category", b"Category", "EditAttribute", b"EditAttribute", "ID", b"ID", "MediaType", b"MediaType", "MessageSource", b"MessageSource", "Multicast", b"Multicast", "PushName", b"PushName", "ServerID", b"ServerID", "Timestamp", b"Timestamp", "Type", b"Type"]) -> None: ...

global___MessageInfo = MessageInfo

@typing_extensions.final
class GroupName(google.protobuf.message.Message):
    """GROUP"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    NAMESETAT_FIELD_NUMBER: builtins.int
    NAMESETBY_FIELD_NUMBER: builtins.int
    Name: builtins.str
    NameSetAt: builtins.float
    @property
    def NameSetBy(self) -> global___JID: ...
    def __init__(
        self,
        *,
        Name: builtins.str | None = ...,
        NameSetAt: builtins.float | None = ...,
        NameSetBy: global___JID | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Name", b"Name", "NameSetAt", b"NameSetAt", "NameSetBy", b"NameSetBy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Name", b"Name", "NameSetAt", b"NameSetAt", "NameSetBy", b"NameSetBy"]) -> None: ...

global___GroupName = GroupName

@typing_extensions.final
class GroupTopic(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOPIC_FIELD_NUMBER: builtins.int
    TOPICID_FIELD_NUMBER: builtins.int
    TOPICSETAT_FIELD_NUMBER: builtins.int
    TOPICSETBY_FIELD_NUMBER: builtins.int
    TOPICDELETED_FIELD_NUMBER: builtins.int
    Topic: builtins.str
    TopicID: builtins.str
    TopicSetAt: builtins.float
    @property
    def TopicSetBy(self) -> global___JID: ...
    TopicDeleted: builtins.bool
    def __init__(
        self,
        *,
        Topic: builtins.str | None = ...,
        TopicID: builtins.str | None = ...,
        TopicSetAt: builtins.float | None = ...,
        TopicSetBy: global___JID | None = ...,
        TopicDeleted: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Topic", b"Topic", "TopicDeleted", b"TopicDeleted", "TopicID", b"TopicID", "TopicSetAt", b"TopicSetAt", "TopicSetBy", b"TopicSetBy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Topic", b"Topic", "TopicDeleted", b"TopicDeleted", "TopicID", b"TopicID", "TopicSetAt", b"TopicSetAt", "TopicSetBy", b"TopicSetBy"]) -> None: ...

global___GroupTopic = GroupTopic

@typing_extensions.final
class GroupLocked(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISLOCKED_FIELD_NUMBER: builtins.int
    isLocked: builtins.bool
    def __init__(
        self,
        *,
        isLocked: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["isLocked", b"isLocked"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["isLocked", b"isLocked"]) -> None: ...

global___GroupLocked = GroupLocked

@typing_extensions.final
class GroupAnnounce(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISANNOUNCE_FIELD_NUMBER: builtins.int
    ANNOUNCEVERSIONID_FIELD_NUMBER: builtins.int
    IsAnnounce: builtins.bool
    AnnounceVersionID: builtins.str
    def __init__(
        self,
        *,
        IsAnnounce: builtins.bool | None = ...,
        AnnounceVersionID: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["AnnounceVersionID", b"AnnounceVersionID", "IsAnnounce", b"IsAnnounce"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["AnnounceVersionID", b"AnnounceVersionID", "IsAnnounce", b"IsAnnounce"]) -> None: ...

global___GroupAnnounce = GroupAnnounce

@typing_extensions.final
class GroupEphemeral(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISEPHEMERAL_FIELD_NUMBER: builtins.int
    DISAPPEARINGTIMER_FIELD_NUMBER: builtins.int
    IsEphemeral: builtins.bool
    DisappearingTimer: builtins.int
    def __init__(
        self,
        *,
        IsEphemeral: builtins.bool | None = ...,
        DisappearingTimer: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["DisappearingTimer", b"DisappearingTimer", "IsEphemeral", b"IsEphemeral"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["DisappearingTimer", b"DisappearingTimer", "IsEphemeral", b"IsEphemeral"]) -> None: ...

global___GroupEphemeral = GroupEphemeral

@typing_extensions.final
class GroupIncognito(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISINCOGNITO_FIELD_NUMBER: builtins.int
    IsIncognito: builtins.bool
    def __init__(
        self,
        *,
        IsIncognito: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["IsIncognito", b"IsIncognito"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["IsIncognito", b"IsIncognito"]) -> None: ...

global___GroupIncognito = GroupIncognito

@typing_extensions.final
class GroupParent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISPARENT_FIELD_NUMBER: builtins.int
    DEFAULTMEMBERSHIPAPPROVALMODE_FIELD_NUMBER: builtins.int
    IsParent: builtins.bool
    DefaultMembershipApprovalMode: builtins.str
    def __init__(
        self,
        *,
        IsParent: builtins.bool | None = ...,
        DefaultMembershipApprovalMode: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["DefaultMembershipApprovalMode", b"DefaultMembershipApprovalMode", "IsParent", b"IsParent"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["DefaultMembershipApprovalMode", b"DefaultMembershipApprovalMode", "IsParent", b"IsParent"]) -> None: ...

global___GroupParent = GroupParent

@typing_extensions.final
class GroupLinkedParent(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINKEDPARENTJID_FIELD_NUMBER: builtins.int
    @property
    def LinkedParentJID(self) -> global___JID: ...
    def __init__(
        self,
        *,
        LinkedParentJID: global___JID | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["LinkedParentJID", b"LinkedParentJID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["LinkedParentJID", b"LinkedParentJID"]) -> None: ...

global___GroupLinkedParent = GroupLinkedParent

@typing_extensions.final
class GroupIsDefaultSub(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ISDEFAULTSUBGROUP_FIELD_NUMBER: builtins.int
    IsDefaultSubGroup: builtins.bool
    def __init__(
        self,
        *,
        IsDefaultSubGroup: builtins.bool | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["IsDefaultSubGroup", b"IsDefaultSubGroup"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["IsDefaultSubGroup", b"IsDefaultSubGroup"]) -> None: ...

global___GroupIsDefaultSub = GroupIsDefaultSub

@typing_extensions.final
class GroupParticipantAddRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CODE_FIELD_NUMBER: builtins.int
    EXPIRATION_FIELD_NUMBER: builtins.int
    Code: builtins.str
    Expiration: builtins.float
    def __init__(
        self,
        *,
        Code: builtins.str | None = ...,
        Expiration: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Code", b"Code", "Expiration", b"Expiration"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Code", b"Code", "Expiration", b"Expiration"]) -> None: ...

global___GroupParticipantAddRequest = GroupParticipantAddRequest

@typing_extensions.final
class GroupParticipant(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JID_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    ISADMIN_FIELD_NUMBER: builtins.int
    ISSUPERADMIN_FIELD_NUMBER: builtins.int
    DISPLAYNAME_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    ADDREQUEST_FIELD_NUMBER: builtins.int
    @property
    def JID(self) -> global___JID: ...
    @property
    def ID(self) -> global___JID: ...
    IsAdmin: builtins.bool
    IsSuperAdmin: builtins.bool
    DisplayName: builtins.str
    Error: builtins.int
    @property
    def AddRequest(self) -> global___GroupParticipantAddRequest: ...
    def __init__(
        self,
        *,
        JID: global___JID | None = ...,
        ID: global___JID | None = ...,
        IsAdmin: builtins.bool | None = ...,
        IsSuperAdmin: builtins.bool | None = ...,
        DisplayName: builtins.str | None = ...,
        Error: builtins.int | None = ...,
        AddRequest: global___GroupParticipantAddRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["AddRequest", b"AddRequest", "DisplayName", b"DisplayName", "Error", b"Error", "ID", b"ID", "IsAdmin", b"IsAdmin", "IsSuperAdmin", b"IsSuperAdmin", "JID", b"JID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["AddRequest", b"AddRequest", "DisplayName", b"DisplayName", "Error", b"Error", "ID", b"ID", "IsAdmin", b"IsAdmin", "IsSuperAdmin", b"IsSuperAdmin", "JID", b"JID"]) -> None: ...

global___GroupParticipant = GroupParticipant

@typing_extensions.final
class GroupInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _MemberAddMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MemberAddModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[GroupInfo._MemberAddMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        GroupMemberAddModeAdmin: GroupInfo._MemberAddMode.ValueType  # 1

    class MemberAddMode(_MemberAddMode, metaclass=_MemberAddModeEnumTypeWrapper): ...
    GroupMemberAddModeAdmin: GroupInfo.MemberAddMode.ValueType  # 1

    JID_FIELD_NUMBER: builtins.int
    OWNERJID_FIELD_NUMBER: builtins.int
    GROUPNAME_FIELD_NUMBER: builtins.int
    GROUPTOPIC_FIELD_NUMBER: builtins.int
    GROUPLOCKED_FIELD_NUMBER: builtins.int
    GROUPANNOUNCE_FIELD_NUMBER: builtins.int
    GROUPEPHEMERAL_FIELD_NUMBER: builtins.int
    GROUPINCOGNITO_FIELD_NUMBER: builtins.int
    GROUPPARENT_FIELD_NUMBER: builtins.int
    GROUPLINKEDPARENT_FIELD_NUMBER: builtins.int
    GROUPISDEFAULTSUB_FIELD_NUMBER: builtins.int
    GROUPCREATED_FIELD_NUMBER: builtins.int
    PARTICIPANTVERSIONID_FIELD_NUMBER: builtins.int
    PARTICIPANTS_FIELD_NUMBER: builtins.int
    @property
    def JID(self) -> global___JID: ...
    @property
    def OwnerJID(self) -> global___JID: ...
    @property
    def GroupName(self) -> global___GroupName: ...
    @property
    def GroupTopic(self) -> global___GroupTopic: ...
    @property
    def GroupLocked(self) -> global___GroupLocked: ...
    @property
    def GroupAnnounce(self) -> global___GroupAnnounce: ...
    @property
    def GroupEphemeral(self) -> global___GroupEphemeral: ...
    @property
    def GroupIncognito(self) -> global___GroupIncognito: ...
    @property
    def GroupParent(self) -> global___GroupParent: ...
    @property
    def GroupLinkedParent(self) -> global___GroupLinkedParent: ...
    @property
    def GroupIsDefaultSub(self) -> global___GroupIsDefaultSub: ...
    GroupCreated: builtins.float
    ParticipantVersionID: builtins.str
    @property
    def Participants(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GroupParticipant]: ...
    def __init__(
        self,
        *,
        JID: global___JID | None = ...,
        OwnerJID: global___JID | None = ...,
        GroupName: global___GroupName | None = ...,
        GroupTopic: global___GroupTopic | None = ...,
        GroupLocked: global___GroupLocked | None = ...,
        GroupAnnounce: global___GroupAnnounce | None = ...,
        GroupEphemeral: global___GroupEphemeral | None = ...,
        GroupIncognito: global___GroupIncognito | None = ...,
        GroupParent: global___GroupParent | None = ...,
        GroupLinkedParent: global___GroupLinkedParent | None = ...,
        GroupIsDefaultSub: global___GroupIsDefaultSub | None = ...,
        GroupCreated: builtins.float | None = ...,
        ParticipantVersionID: builtins.str | None = ...,
        Participants: collections.abc.Iterable[global___GroupParticipant] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["GroupAnnounce", b"GroupAnnounce", "GroupCreated", b"GroupCreated", "GroupEphemeral", b"GroupEphemeral", "GroupIncognito", b"GroupIncognito", "GroupIsDefaultSub", b"GroupIsDefaultSub", "GroupLinkedParent", b"GroupLinkedParent", "GroupLocked", b"GroupLocked", "GroupName", b"GroupName", "GroupParent", b"GroupParent", "GroupTopic", b"GroupTopic", "JID", b"JID", "OwnerJID", b"OwnerJID", "ParticipantVersionID", b"ParticipantVersionID"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["GroupAnnounce", b"GroupAnnounce", "GroupCreated", b"GroupCreated", "GroupEphemeral", b"GroupEphemeral", "GroupIncognito", b"GroupIncognito", "GroupIsDefaultSub", b"GroupIsDefaultSub", "GroupLinkedParent", b"GroupLinkedParent", "GroupLocked", b"GroupLocked", "GroupName", b"GroupName", "GroupParent", b"GroupParent", "GroupTopic", b"GroupTopic", "JID", b"JID", "OwnerJID", b"OwnerJID", "ParticipantVersionID", b"ParticipantVersionID", "Participants", b"Participants"]) -> None: ...

global___GroupInfo = GroupInfo
