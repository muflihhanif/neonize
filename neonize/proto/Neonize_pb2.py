# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Neonize.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import def_pb2 as def__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rNeonize.proto\x12\x07neonize\x1a\tdef.proto\"j\n\x03JID\x12\x0c\n\x04User\x18\x01 \x02(\t\x12\x10\n\x08RawAgent\x18\x02 \x02(\r\x12\x0e\n\x06\x44\x65vice\x18\x03 \x02(\r\x12\x12\n\nIntegrator\x18\x04 \x02(\r\x12\x0e\n\x06Server\x18\x05 \x02(\t\x12\x0f\n\x07IsEmpty\x18\x06 \x02(\x08\"\xb1\x02\n\x0bMessageInfo\x12-\n\rMessageSource\x18\x01 \x02(\x0b\x32\x16.neonize.MessageSource\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x10\n\x08ServerID\x18\x03 \x02(\x03\x12\x0c\n\x04Type\x18\x04 \x02(\t\x12\x10\n\x08Pushname\x18\x05 \x02(\t\x12\x11\n\tTimestamp\x18\x06 \x02(\x03\x12\x10\n\x08\x43\x61tegory\x18\x07 \x02(\t\x12\x11\n\tMulticast\x18\x08 \x02(\x08\x12\x11\n\tMediaType\x18\t \x02(\t\x12\x0c\n\x04\x45\x64it\x18\n \x02(\t\x12+\n\x0cVerifiedName\x18\x0b \x01(\x0b\x32\x15.neonize.VerifiedName\x12/\n\x0e\x44\x65viceSentMeta\x18\x0c \x01(\x0b\x32\x17.neonize.DeviceSentMeta\"\x92\x01\n\x0eUploadResponse\x12\x0b\n\x03url\x18\x01 \x02(\t\x12\x12\n\nDirectPath\x18\x02 \x02(\t\x12\x0e\n\x06Handle\x18\x03 \x02(\t\x12\x10\n\x08MediaKey\x18\x04 \x02(\x0c\x12\x15\n\rFileEncSHA256\x18\x05 \x02(\x0c\x12\x12\n\nFileSHA256\x18\x06 \x02(\x0c\x12\x12\n\nFileLength\x18\x07 \x02(\r\"\x96\x01\n\rMessageSource\x12\x1a\n\x04\x43hat\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12\x1c\n\x06Sender\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x10\n\x08IsFromMe\x18\x03 \x02(\x08\x12\x0f\n\x07IsGroup\x18\x04 \x02(\x08\x12(\n\x12\x42roadcastListOwner\x18\x05 \x02(\x0b\x32\x0c.neonize.JID\"7\n\x0e\x44\x65viceSentMeta\x12\x16\n\x0e\x44\x65stinationJID\x18\x01 \x02(\t\x12\r\n\x05Phash\x18\x02 \x02(\t\"\x82\x01\n\x0cVerifiedName\x12\x36\n\x0b\x43\x65rtificate\x18\x01 \x01(\x0b\x32!.defproto.VerifiedNameCertificate\x12:\n\x07\x44\x65tails\x18\x02 \x01(\x0b\x32).defproto.VerifiedNameCertificate.Details\"{\n\x14IsOnWhatsAppResponse\x12\r\n\x05Query\x18\x01 \x02(\t\x12\x19\n\x03JID\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x0c\n\x04IsIn\x18\x03 \x02(\x08\x12+\n\x0cVerifiedName\x18\x04 \x01(\x0b\x32\x15.neonize.VerifiedName\"y\n\x08UserInfo\x12+\n\x0cVerifiedName\x18\x01 \x01(\x0b\x32\x15.neonize.VerifiedName\x12\x0e\n\x06Status\x18\x02 \x02(\t\x12\x11\n\tPictureID\x18\x03 \x02(\t\x12\x1d\n\x07\x44\x65vices\x18\x04 \x03(\x0b\x32\x0c.neonize.JID\"s\n\x06\x44\x65vice\x12\x19\n\x03JID\x18\x01 \x01(\x0b\x32\x0c.neonize.JID\x12\x10\n\x08Platform\x18\x02 \x02(\t\x12\x15\n\rBussinessName\x18\x03 \x02(\t\x12\x10\n\x08PushName\x18\x04 \x02(\t\x12\x13\n\x0bInitialized\x18\x05 \x02(\x08\"M\n\tGroupName\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x11\n\tNameSetAt\x18\x02 \x02(\x03\x12\x1f\n\tNameSetBy\x18\x03 \x02(\x0b\x32\x0c.neonize.JID\"x\n\nGroupTopic\x12\r\n\x05Topic\x18\x01 \x02(\t\x12\x0f\n\x07TopicID\x18\x02 \x02(\t\x12\x12\n\nTopicSetAt\x18\x03 \x02(\x03\x12 \n\nTopicSetBy\x18\x04 \x02(\x0b\x32\x0c.neonize.JID\x12\x14\n\x0cTopicDeleted\x18\x05 \x02(\x08\"\x1f\n\x0bGroupLocked\x12\x10\n\x08isLocked\x18\x01 \x02(\x08\">\n\rGroupAnnounce\x12\x12\n\nIsAnnounce\x18\x01 \x02(\x08\x12\x19\n\x11\x41nnounceVersionID\x18\x02 \x02(\t\"@\n\x0eGroupEphemeral\x12\x13\n\x0bIsEphemeral\x18\x01 \x02(\x08\x12\x19\n\x11\x44isappearingTimer\x18\x02 \x02(\r\"%\n\x0eGroupIncognito\x12\x13\n\x0bIsIncognito\x18\x01 \x02(\x08\"F\n\x0bGroupParent\x12\x10\n\x08IsParent\x18\x01 \x02(\x08\x12%\n\x1d\x44\x65\x66\x61ultMembershipApprovalMode\x18\x02 \x02(\t\":\n\x11GroupLinkedParent\x12%\n\x0fLinkedParentJID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\".\n\x11GroupIsDefaultSub\x12\x19\n\x11IsDefaultSubGroup\x18\x01 \x02(\x08\">\n\x1aGroupParticipantAddRequest\x12\x0c\n\x04\x43ode\x18\x01 \x02(\t\x12\x12\n\nExpiration\x18\x02 \x02(\x02\"\xcc\x01\n\x10GroupParticipant\x12\x19\n\x03JID\x18\x01 \x01(\x0b\x32\x0c.neonize.JID\x12\x19\n\x03LID\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x0f\n\x07IsAdmin\x18\x03 \x02(\x08\x12\x14\n\x0cIsSuperAdmin\x18\x04 \x02(\x08\x12\x13\n\x0b\x44isplayName\x18\x05 \x02(\t\x12\r\n\x05\x45rror\x18\x06 \x02(\x05\x12\x37\n\nAddRequest\x18\x07 \x01(\x0b\x32#.neonize.GroupParticipantAddRequest\"\x83\x05\n\tGroupInfo\x12\x1e\n\x08OwnerJID\x18\x02 \x02(\x0b\x32\x0c.neonize.JID\x12\x19\n\x03JID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12%\n\tGroupName\x18\x03 \x02(\x0b\x32\x12.neonize.GroupName\x12\'\n\nGroupTopic\x18\x04 \x02(\x0b\x32\x13.neonize.GroupTopic\x12)\n\x0bGroupLocked\x18\x05 \x02(\x0b\x32\x14.neonize.GroupLocked\x12-\n\rGroupAnnounce\x18\x06 \x02(\x0b\x32\x16.neonize.GroupAnnounce\x12/\n\x0eGroupEphemeral\x18\x07 \x02(\x0b\x32\x17.neonize.GroupEphemeral\x12/\n\x0eGroupIncognito\x18\x08 \x02(\x0b\x32\x17.neonize.GroupIncognito\x12)\n\x0bGroupParent\x18\t \x02(\x0b\x32\x14.neonize.GroupParent\x12\x35\n\x11GroupLinkedParent\x18\n \x02(\x0b\x32\x1a.neonize.GroupLinkedParent\x12\x35\n\x11GroupIsDefaultSub\x18\x0b \x02(\x0b\x32\x1a.neonize.GroupIsDefaultSub\x12\x14\n\x0cGroupCreated\x18\x0c \x02(\x02\x12\x1c\n\x14ParticipantVersionID\x18\r \x02(\t\x12/\n\x0cParticipants\x18\x0e \x03(\x0b\x32\x19.neonize.GroupParticipant\"1\n\x12GroupMemberAddMode\x12\x1b\n\x17GroupMemberAddModeAdmin\x10\x01\"\xb8\x01\n\x13MessageDebugTimings\x12\r\n\x05Queue\x18\x01 \x02(\x03\x12\x0f\n\x07Marshal\x18\x02 \x02(\x03\x12\x17\n\x0fGetParticipants\x18\x03 \x02(\x03\x12\x12\n\nGetDevices\x18\x04 \x02(\x03\x12\x14\n\x0cGroupEncrypt\x18\x05 \x02(\x03\x12\x13\n\x0bPeerEncrypt\x18\x06 \x02(\x03\x12\x0c\n\x04Send\x18\x07 \x02(\x03\x12\x0c\n\x04Resp\x18\x08 \x02(\x03\x12\r\n\x05Retry\x18\t \x02(\x03\"s\n\x0cSendResponse\x12\x11\n\tTimestamp\x18\x01 \x02(\x03\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x10\n\x08ServerID\x18\x03 \x02(\x03\x12\x32\n\x0c\x44\x65\x62ugTimings\x18\x04 \x02(\x0b\x32\x1c.neonize.MessageDebugTimings\"W\n\x19SendMessageReturnFunction\x12\r\n\x05\x45rror\x18\x01 \x01(\t\x12+\n\x0cSendResponse\x18\x02 \x01(\x0b\x32\x15.neonize.SendResponse\"R\n\x1aGetGroupInfoReturnFunction\x12%\n\tGroupInfo\x18\x01 \x01(\x0b\x32\x12.neonize.GroupInfo\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"K\n\x1fJoinGroupWithLinkReturnFunction\x12\r\n\x05\x45rror\x18\x01 \x01(\t\x12\x19\n\x03Jid\x18\x02 \x01(\x0b\x32\x0c.neonize.JID\"E\n GetGroupInviteLinkReturnFunction\x12\x12\n\nInviteLink\x18\x01 \x01(\t\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"7\n\x16\x44ownloadReturnFunction\x12\x0e\n\x06\x42inary\x18\x01 \x01(\x0c\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"V\n\x14UploadReturnFunction\x12/\n\x0eUploadResponse\x18\x01 \x01(\x0b\x32\x17.neonize.UploadResponse\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"?\n\x1bSetGroupPhotoReturnFunction\x12\x11\n\tPictureID\x18\x01 \x02(\t\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"h\n\x1aIsOnWhatsAppReturnFunction\x12;\n\x14IsOnWhatsAppResponse\x18\x01 \x03(\x0b\x32\x1d.neonize.IsOnWhatsAppResponse\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"a\n\x1fGetUserInfoSingleReturnFunction\x12\x19\n\x03JID\x18\x01 \x01(\x0b\x32\x0c.neonize.JID\x12#\n\x08UserInfo\x18\x02 \x01(\x0b\x32\x11.neonize.UserInfo\"g\n\x19GetUserInfoReturnFunction\x12;\n\tUsersInfo\x18\x01 \x03(\x0b\x32(.neonize.GetUserInfoSingleReturnFunction\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"Q\n\x1b\x42uildPollVoteReturnFunction\x12#\n\x08PollVote\x18\x01 \x01(\x0b\x32\x11.defproto.Message\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"h\n\x1e\x43reateNewsLetterReturnFunction\x12\x37\n\x12NewsletterMetadata\x18\x01 \x01(\x0b\x32\x1b.neonize.NewsletterMetadata\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"R\n\x1aGetBlocklistReturnFunction\x12%\n\tBlocklist\x18\x01 \x01(\x0b\x32\x12.neonize.Blocklist\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"=\n\x1eGetContactQRLinkReturnFunction\x12\x0c\n\x04Link\x18\x01 \x02(\t\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"^\n)GetGroupRequestParticipantsReturnFunction\x12\"\n\x0cParticipants\x18\x01 \x03(\x0b\x32\x0c.neonize.JID\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"Q\n\x1dGetJoinedGroupsReturnFunction\x12!\n\x05Group\x18\x01 \x03(\x0b\x32\x12.neonize.GroupInfo\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\xb7\x01\n\x0eReqCreateGroup\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\"\n\x0cParticipants\x18\x02 \x03(\x0b\x32\x0c.neonize.JID\x12\x11\n\tCreateKey\x18\x03 \x02(\t\x12)\n\x0bGroupParent\x18\x04 \x01(\x0b\x32\x14.neonize.GroupParent\x12\x35\n\x11GroupLinkedParent\x18\x05 \x01(\x0b\x32\x1a.neonize.GroupLinkedParent\"&\n\x08JIDArray\x12\x1a\n\x04JIDS\x18\x01 \x03(\x0b\x32\x0c.neonize.JID\"\x1b\n\x0b\x41rrayString\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t\";\n\x15NewsLetterMessageMeta\x12\x0e\n\x06\x45\x64itTS\x18\x01 \x02(\x03\x12\x12\n\nOriginalTS\x18\x02 \x02(\x03\"\xba\x02\n\x07Message\x12\"\n\x04Info\x18\x01 \x02(\x0b\x32\x14.neonize.MessageInfo\x12\"\n\x07Message\x18\x02 \x01(\x0b\x32\x11.defproto.Message\x12\x13\n\x0bIsEphemeral\x18\x03 \x02(\x08\x12\x12\n\nIsViewOnce\x18\x04 \x02(\x08\x12\x14\n\x0cIsViewOnceV2\x18\x05 \x02(\x08\x12\x0e\n\x06IsEdit\x18\x06 \x02(\x08\x12.\n\x0cSourceWebMsg\x18\x07 \x01(\x0b\x32\x18.defproto.WebMessageInfo\x12\x1c\n\x14UnavailableRequestID\x18\x08 \x02(\t\x12\x12\n\nRetryCount\x18\t \x02(\x03\x12\x36\n\x0eNewsLetterMeta\x18\n \x01(\x0b\x32\x1e.neonize.NewsLetterMessageMeta\"L\n\x16\x43reateNewsletterParams\x12\x0c\n\x04Name\x18\x01 \x02(\t\x12\x13\n\x0b\x44\x65scription\x18\x02 \x02(\t\x12\x0f\n\x07Picture\x18\x03 \x02(\x0c\"\x97\x01\n\x16WrappedNewsletterState\x12=\n\x04Type\x18\x01 \x02(\x0e\x32/.neonize.WrappedNewsletterState.NewsletterState\">\n\x0fNewsletterState\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\r\n\tSUSPENDED\x10\x02\x12\x10\n\x0cGEOSUSPENDED\x10\x03\">\n\x0eNewsletterText\x12\x0c\n\x04Text\x18\x01 \x02(\t\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x12\n\nUpdateTime\x18\x03 \x02(\x03\"O\n\x12ProfilePictureInfo\x12\x0b\n\x03URL\x18\x01 \x02(\t\x12\n\n\x02ID\x18\x02 \x02(\t\x12\x0c\n\x04Type\x18\x03 \x02(\t\x12\x12\n\nDirectPath\x18\x04 \x02(\t\"\xb0\x01\n\x1aNewsletterReactionSettings\x12J\n\x05Value\x18\x01 \x02(\x0e\x32;.neonize.NewsletterReactionSettings.NewsletterReactionsMode\"F\n\x17NewsletterReactionsMode\x12\x07\n\x03\x41LL\x10\x01\x12\t\n\x05\x42\x41SIC\x10\x02\x12\x08\n\x04NONE\x10\x03\x12\r\n\tBLOCKLIST\x10\x04\"O\n\x11NewsletterSetting\x12:\n\rReactionCodes\x18\x01 \x02(\x0b\x32#.neonize.NewsletterReactionSettings\"\xd3\x03\n\x18NewsletterThreadMetadata\x12\x14\n\x0c\x43reationTime\x18\x01 \x02(\x03\x12\x12\n\nInviteCode\x18\x02 \x02(\t\x12%\n\x04Name\x18\x03 \x02(\x0b\x32\x17.neonize.NewsletterText\x12,\n\x0b\x44\x65scription\x18\x04 \x02(\x0b\x32\x17.neonize.NewsletterText\x12\x17\n\x0fSubscriberCount\x18\x05 \x02(\x03\x12X\n\x11VerificationState\x18\x06 \x02(\x0e\x32=.neonize.NewsletterThreadMetadata.NewsletterVerificationState\x12,\n\x07Picture\x18\x07 \x01(\x0b\x32\x1b.neonize.ProfilePictureInfo\x12,\n\x07Preview\x18\x08 \x02(\x0b\x32\x1b.neonize.ProfilePictureInfo\x12,\n\x08Settings\x18\t \x02(\x0b\x32\x1a.neonize.NewsletterSetting\";\n\x1bNewsletterVerificationState\x12\x0c\n\x08VERIFIED\x10\x01\x12\x0e\n\nUNVERIFIED\x10\x02\"\x8a\x02\n\x18NewsletterViewerMetadata\x12\x43\n\x04Mute\x18\x01 \x02(\x0e\x32\x35.neonize.NewsletterViewerMetadata.NewsletterMuteState\x12>\n\x04Role\x18\x02 \x02(\x0e\x32\x30.neonize.NewsletterViewerMetadata.NewsletterRole\"&\n\x13NewsletterMuteState\x12\x06\n\x02ON\x10\x01\x12\x07\n\x03OFF\x10\x02\"A\n\x0eNewsletterRole\x12\x0e\n\nSUBSCRIBER\x10\x01\x12\t\n\x05GUEST\x10\x02\x12\t\n\x05\x41\x44MIN\x10\x03\x12\t\n\x05OWNER\x10\x04\"\xcc\x01\n\x12NewsletterMetadata\x12\x18\n\x02ID\x18\x01 \x02(\x0b\x32\x0c.neonize.JID\x12.\n\x05State\x18\x02 \x02(\x0b\x32\x1f.neonize.WrappedNewsletterState\x12\x35\n\nThreadMeta\x18\x03 \x02(\x0b\x32!.neonize.NewsletterThreadMetadata\x12\x35\n\nViewerMeta\x18\x04 \x01(\x0b\x32!.neonize.NewsletterViewerMetadata\"6\n\tBlocklist\x12\r\n\x05\x44Hash\x18\x01 \x02(\t\x12\x1a\n\x04JIDs\x18\x02 \x03(\x0b\x32\x0c.neonize.JID\"\'\n\x08Reaction\x12\x0c\n\x04type\x18\x01 \x02(\t\x12\r\n\x05\x63ount\x18\x02 \x02(\x03\"\x8f\x01\n\x11NewsletterMessage\x12\x17\n\x0fMessageServerID\x18\x01 \x02(\x03\x12\x12\n\nViewsCount\x18\x02 \x02(\x03\x12)\n\x0eReactionCounts\x18\x03 \x03(\x0b\x32\x11.neonize.Reaction\x12\"\n\x07Message\x18\x04 \x02(\x0b\x32\x11.defproto.Message\"p\n(GetNewsletterMessageUpdateReturnFunction\x12\x35\n\x11NewsletterMessage\x18\x01 \x03(\x0b\x32\x1a.neonize.NewsletterMessage\x12\r\n\x05\x45rror\x18\x02 \x01(\t\"\xa5\x04\n\x0fPrivacySettings\x12\x39\n\x08GroupAdd\x18\x01 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x39\n\x08LastSeen\x18\x02 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x37\n\x06Status\x18\x03 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x38\n\x07Profile\x18\x04 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12=\n\x0cReadReceipts\x18\x05 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x38\n\x07\x43\x61llAdd\x18\x06 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\x12\x37\n\x06Online\x18\x07 \x02(\x0e\x32\'.neonize.PrivacySettings.PrivacySetting\"w\n\x0ePrivacySetting\x12\r\n\tUNDEFINED\x10\x01\x12\x07\n\x03\x41LL\x10\x02\x12\x0c\n\x08\x43ONTACTS\x10\x03\x12\x15\n\x11\x43ONTACT_BLACKLIST\x10\x04\x12\x13\n\x0fMATCH_LAST_SEEN\x10\x05\x12\t\n\x05KNOWN\x10\x06\x12\x08\n\x04NONE\x10\x07\x42\x0bZ\t./neonize')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Neonize_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\t./neonize'
  _globals['_JID']._serialized_start=37
  _globals['_JID']._serialized_end=143
  _globals['_MESSAGEINFO']._serialized_start=146
  _globals['_MESSAGEINFO']._serialized_end=451
  _globals['_UPLOADRESPONSE']._serialized_start=454
  _globals['_UPLOADRESPONSE']._serialized_end=600
  _globals['_MESSAGESOURCE']._serialized_start=603
  _globals['_MESSAGESOURCE']._serialized_end=753
  _globals['_DEVICESENTMETA']._serialized_start=755
  _globals['_DEVICESENTMETA']._serialized_end=810
  _globals['_VERIFIEDNAME']._serialized_start=813
  _globals['_VERIFIEDNAME']._serialized_end=943
  _globals['_ISONWHATSAPPRESPONSE']._serialized_start=945
  _globals['_ISONWHATSAPPRESPONSE']._serialized_end=1068
  _globals['_USERINFO']._serialized_start=1070
  _globals['_USERINFO']._serialized_end=1191
  _globals['_DEVICE']._serialized_start=1193
  _globals['_DEVICE']._serialized_end=1308
  _globals['_GROUPNAME']._serialized_start=1310
  _globals['_GROUPNAME']._serialized_end=1387
  _globals['_GROUPTOPIC']._serialized_start=1389
  _globals['_GROUPTOPIC']._serialized_end=1509
  _globals['_GROUPLOCKED']._serialized_start=1511
  _globals['_GROUPLOCKED']._serialized_end=1542
  _globals['_GROUPANNOUNCE']._serialized_start=1544
  _globals['_GROUPANNOUNCE']._serialized_end=1606
  _globals['_GROUPEPHEMERAL']._serialized_start=1608
  _globals['_GROUPEPHEMERAL']._serialized_end=1672
  _globals['_GROUPINCOGNITO']._serialized_start=1674
  _globals['_GROUPINCOGNITO']._serialized_end=1711
  _globals['_GROUPPARENT']._serialized_start=1713
  _globals['_GROUPPARENT']._serialized_end=1783
  _globals['_GROUPLINKEDPARENT']._serialized_start=1785
  _globals['_GROUPLINKEDPARENT']._serialized_end=1843
  _globals['_GROUPISDEFAULTSUB']._serialized_start=1845
  _globals['_GROUPISDEFAULTSUB']._serialized_end=1891
  _globals['_GROUPPARTICIPANTADDREQUEST']._serialized_start=1893
  _globals['_GROUPPARTICIPANTADDREQUEST']._serialized_end=1955
  _globals['_GROUPPARTICIPANT']._serialized_start=1958
  _globals['_GROUPPARTICIPANT']._serialized_end=2162
  _globals['_GROUPINFO']._serialized_start=2165
  _globals['_GROUPINFO']._serialized_end=2808
  _globals['_GROUPINFO_GROUPMEMBERADDMODE']._serialized_start=2759
  _globals['_GROUPINFO_GROUPMEMBERADDMODE']._serialized_end=2808
  _globals['_MESSAGEDEBUGTIMINGS']._serialized_start=2811
  _globals['_MESSAGEDEBUGTIMINGS']._serialized_end=2995
  _globals['_SENDRESPONSE']._serialized_start=2997
  _globals['_SENDRESPONSE']._serialized_end=3112
  _globals['_SENDMESSAGERETURNFUNCTION']._serialized_start=3114
  _globals['_SENDMESSAGERETURNFUNCTION']._serialized_end=3201
  _globals['_GETGROUPINFORETURNFUNCTION']._serialized_start=3203
  _globals['_GETGROUPINFORETURNFUNCTION']._serialized_end=3285
  _globals['_JOINGROUPWITHLINKRETURNFUNCTION']._serialized_start=3287
  _globals['_JOINGROUPWITHLINKRETURNFUNCTION']._serialized_end=3362
  _globals['_GETGROUPINVITELINKRETURNFUNCTION']._serialized_start=3364
  _globals['_GETGROUPINVITELINKRETURNFUNCTION']._serialized_end=3433
  _globals['_DOWNLOADRETURNFUNCTION']._serialized_start=3435
  _globals['_DOWNLOADRETURNFUNCTION']._serialized_end=3490
  _globals['_UPLOADRETURNFUNCTION']._serialized_start=3492
  _globals['_UPLOADRETURNFUNCTION']._serialized_end=3578
  _globals['_SETGROUPPHOTORETURNFUNCTION']._serialized_start=3580
  _globals['_SETGROUPPHOTORETURNFUNCTION']._serialized_end=3643
  _globals['_ISONWHATSAPPRETURNFUNCTION']._serialized_start=3645
  _globals['_ISONWHATSAPPRETURNFUNCTION']._serialized_end=3749
  _globals['_GETUSERINFOSINGLERETURNFUNCTION']._serialized_start=3751
  _globals['_GETUSERINFOSINGLERETURNFUNCTION']._serialized_end=3848
  _globals['_GETUSERINFORETURNFUNCTION']._serialized_start=3850
  _globals['_GETUSERINFORETURNFUNCTION']._serialized_end=3953
  _globals['_BUILDPOLLVOTERETURNFUNCTION']._serialized_start=3955
  _globals['_BUILDPOLLVOTERETURNFUNCTION']._serialized_end=4036
  _globals['_CREATENEWSLETTERRETURNFUNCTION']._serialized_start=4038
  _globals['_CREATENEWSLETTERRETURNFUNCTION']._serialized_end=4142
  _globals['_GETBLOCKLISTRETURNFUNCTION']._serialized_start=4144
  _globals['_GETBLOCKLISTRETURNFUNCTION']._serialized_end=4226
  _globals['_GETCONTACTQRLINKRETURNFUNCTION']._serialized_start=4228
  _globals['_GETCONTACTQRLINKRETURNFUNCTION']._serialized_end=4289
  _globals['_GETGROUPREQUESTPARTICIPANTSRETURNFUNCTION']._serialized_start=4291
  _globals['_GETGROUPREQUESTPARTICIPANTSRETURNFUNCTION']._serialized_end=4385
  _globals['_GETJOINEDGROUPSRETURNFUNCTION']._serialized_start=4387
  _globals['_GETJOINEDGROUPSRETURNFUNCTION']._serialized_end=4468
  _globals['_REQCREATEGROUP']._serialized_start=4471
  _globals['_REQCREATEGROUP']._serialized_end=4654
  _globals['_JIDARRAY']._serialized_start=4656
  _globals['_JIDARRAY']._serialized_end=4694
  _globals['_ARRAYSTRING']._serialized_start=4696
  _globals['_ARRAYSTRING']._serialized_end=4723
  _globals['_NEWSLETTERMESSAGEMETA']._serialized_start=4725
  _globals['_NEWSLETTERMESSAGEMETA']._serialized_end=4784
  _globals['_MESSAGE']._serialized_start=4787
  _globals['_MESSAGE']._serialized_end=5101
  _globals['_CREATENEWSLETTERPARAMS']._serialized_start=5103
  _globals['_CREATENEWSLETTERPARAMS']._serialized_end=5179
  _globals['_WRAPPEDNEWSLETTERSTATE']._serialized_start=5182
  _globals['_WRAPPEDNEWSLETTERSTATE']._serialized_end=5333
  _globals['_WRAPPEDNEWSLETTERSTATE_NEWSLETTERSTATE']._serialized_start=5271
  _globals['_WRAPPEDNEWSLETTERSTATE_NEWSLETTERSTATE']._serialized_end=5333
  _globals['_NEWSLETTERTEXT']._serialized_start=5335
  _globals['_NEWSLETTERTEXT']._serialized_end=5397
  _globals['_PROFILEPICTUREINFO']._serialized_start=5399
  _globals['_PROFILEPICTUREINFO']._serialized_end=5478
  _globals['_NEWSLETTERREACTIONSETTINGS']._serialized_start=5481
  _globals['_NEWSLETTERREACTIONSETTINGS']._serialized_end=5657
  _globals['_NEWSLETTERREACTIONSETTINGS_NEWSLETTERREACTIONSMODE']._serialized_start=5587
  _globals['_NEWSLETTERREACTIONSETTINGS_NEWSLETTERREACTIONSMODE']._serialized_end=5657
  _globals['_NEWSLETTERSETTING']._serialized_start=5659
  _globals['_NEWSLETTERSETTING']._serialized_end=5738
  _globals['_NEWSLETTERTHREADMETADATA']._serialized_start=5741
  _globals['_NEWSLETTERTHREADMETADATA']._serialized_end=6208
  _globals['_NEWSLETTERTHREADMETADATA_NEWSLETTERVERIFICATIONSTATE']._serialized_start=6149
  _globals['_NEWSLETTERTHREADMETADATA_NEWSLETTERVERIFICATIONSTATE']._serialized_end=6208
  _globals['_NEWSLETTERVIEWERMETADATA']._serialized_start=6211
  _globals['_NEWSLETTERVIEWERMETADATA']._serialized_end=6477
  _globals['_NEWSLETTERVIEWERMETADATA_NEWSLETTERMUTESTATE']._serialized_start=6372
  _globals['_NEWSLETTERVIEWERMETADATA_NEWSLETTERMUTESTATE']._serialized_end=6410
  _globals['_NEWSLETTERVIEWERMETADATA_NEWSLETTERROLE']._serialized_start=6412
  _globals['_NEWSLETTERVIEWERMETADATA_NEWSLETTERROLE']._serialized_end=6477
  _globals['_NEWSLETTERMETADATA']._serialized_start=6480
  _globals['_NEWSLETTERMETADATA']._serialized_end=6684
  _globals['_BLOCKLIST']._serialized_start=6686
  _globals['_BLOCKLIST']._serialized_end=6740
  _globals['_REACTION']._serialized_start=6742
  _globals['_REACTION']._serialized_end=6781
  _globals['_NEWSLETTERMESSAGE']._serialized_start=6784
  _globals['_NEWSLETTERMESSAGE']._serialized_end=6927
  _globals['_GETNEWSLETTERMESSAGEUPDATERETURNFUNCTION']._serialized_start=6929
  _globals['_GETNEWSLETTERMESSAGEUPDATERETURNFUNCTION']._serialized_end=7041
  _globals['_PRIVACYSETTINGS']._serialized_start=7044
  _globals['_PRIVACYSETTINGS']._serialized_end=7593
  _globals['_PRIVACYSETTINGS_PRIVACYSETTING']._serialized_start=7474
  _globals['_PRIVACYSETTINGS_PRIVACYSETTING']._serialized_end=7593
# @@protoc_insertion_point(module_scope)
