# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0eresponse.proto\x12\x05manga"P\n\x06\x42\x61nner\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\'\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x17.manga.TransitionAction\x12\n\n\x02id\x18\x03 \x01(\r"B\n\nBannerList\x12\x14\n\x0c\x62\x61nner_title\x18\x01 \x01(\t\x12\x1e\n\x07\x62\x61nners\x18\x02 \x03(\x0b\x32\r.manga.Banner"/\n\x10TransitionAction\x12\x0e\n\x06method\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t"\xc9\x01\n\x07\x43hapter\x12\x10\n\x08title_id\x18\x01 \x01(\r\x12\x12\n\nchapter_id\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\tsub_title\x18\x04 \x01(\t\x12\x15\n\rthumbnail_url\x18\x05 \x01(\t\x12\x17\n\x0fstart_timestamp\x18\x06 \x01(\r\x12\x15\n\rend_timestamp\x18\x07 \x01(\r\x12\x16\n\x0e\x61lready_viewed\x18\x08 \x01(\x08\x12\x18\n\x10is_vertical_only\x18\t \x01(\x08"\xaf\x01\n\x07\x43omment\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05index\x18\x02 \x01(\r\x12\x11\n\tuser_name\x18\x03 \x01(\t\x12\x10\n\x08icon_url\x18\x04 \x01(\t\x12\x15\n\ris_my_comment\x18\x06 \x01(\x08\x12\x15\n\ralready_liked\x18\x07 \x01(\x08\x12\x17\n\x0fnumber_of_likes\x18\t \x01(\r\x12\x0c\n\x04\x62ody\x18\n \x01(\t\x12\x0f\n\x07\x63reated\x18\x0b \x01(\r"\xfa\x03\n\rAdNetworkList\x12\x33\n\x0b\x61\x64_networks\x18\x01 \x01(\x0b\x32\x1e.manga.AdNetworkList.AdNetwork\x1a\xb3\x03\n\tAdNetwork\x12\x39\n\x08\x66\x61\x63\x65\x62ook\x18\x01 \x01(\x0b\x32\'.manga.AdNetworkList.AdNetwork.Facebook\x12\x33\n\x05\x61\x64mob\x18\x02 \x01(\x0b\x32$.manga.AdNetworkList.AdNetwork.Admob\x12\x33\n\x05mopub\x18\x03 \x01(\x0b\x32$.manga.AdNetworkList.AdNetwork.Mopub\x12\x37\n\x07\x61\x64sense\x18\x04 \x01(\x0b\x32&.manga.AdNetworkList.AdNetwork.Adsense\x12\x39\n\x08\x61pplovin\x18\x05 \x01(\x0b\x32\'.manga.AdNetworkList.AdNetwork.Applovin\x1a \n\x08\x46\x61\x63\x65\x62ook\x12\x14\n\x0cplacement_id\x18\x01 \x01(\t\x1a\x18\n\x05\x41\x64mob\x12\x0f\n\x07unit_id\x18\x01 \x01(\t\x1a\x18\n\x05Mopub\x12\x0f\n\x07unit_id\x18\x01 \x01(\t\x1a\x1a\n\x07\x41\x64sense\x12\x0f\n\x07unit_id\x18\x01 \x01(\t\x1a\x1b\n\x08\x41pplovin\x12\x0f\n\x07unit_id\x18\x01 \x01(\t"\xb8\x04\n\x05Popup\x12*\n\nos_default\x18\x01 \x01(\x0b\x32\x16.manga.Popup.OSDefault\x12,\n\x0b\x61pp_default\x18\x02 \x01(\x0b\x32\x17.manga.Popup.AppDefault\x12.\n\x0cmovie_reward\x18\x03 \x01(\x0b\x32\x18.manga.Popup.MovieReward\x1a?\n\x06\x42utton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\'\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x17.manga.TransitionAction\x1a\xab\x01\n\tOSDefault\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12&\n\tok_button\x18\x03 \x01(\x0b\x32\x13.manga.Popup.Button\x12+\n\x0eneutral_button\x18\x04 \x01(\x0b\x32\x13.manga.Popup.Button\x12*\n\rcancel_button\x18\x05 \x01(\x0b\x32\x13.manga.Popup.Button\x1ag\n\nAppDefault\x12\x0f\n\x07subject\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\t\x12\'\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32\x17.manga.TransitionAction\x12\x11\n\timage_url\x18\x04 \x01(\t\x1aM\n\x0bMovieReward\x12\x11\n\timage_url\x18\x01 \x01(\t\x12+\n\radvertisement\x18\x02 \x01(\x0b\x32\x14.manga.AdNetworkList"\x95\x02\n\x08LastPage\x12\'\n\x0f\x63urrent_chapter\x18\x01 \x01(\x0b\x32\x0e.manga.Chapter\x12$\n\x0cnext_chapter\x18\x02 \x01(\x0b\x32\x0e.manga.Chapter\x12$\n\x0ctop_comments\x18\x03 \x03(\x0b\x32\x0e.manga.Comment\x12\x15\n\ris_subscribed\x18\x04 \x01(\x08\x12\x16\n\x0enext_timestamp\x18\x05 \x01(\r\x12\x14\n\x0c\x63hapter_type\x18\x06 \x01(\x05\x12+\n\radvertisement\x18\x07 \x01(\x0b\x32\x14.manga.AdNetworkList\x12"\n\x0cmovie_reward\x18\x08 \x01(\x0b\x32\x0c.manga.Popup"c\n\tMangaPage\x12\x11\n\timage_url\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\x16\n\x0e\x65ncryption_key\x18\x05 \x01(\t"\xa5\x01\n\x04Page\x12$\n\nmanga_page\x18\x01 \x01(\x0b\x32\x10.manga.MangaPage\x12&\n\x0b\x62\x61nner_list\x18\x02 \x01(\x0b\x32\x11.manga.BannerList\x12"\n\tlast_page\x18\x03 \x01(\x0b\x32\x0f.manga.LastPage\x12+\n\radvertisement\x18\x04 \x01(\x0b\x32\x14.manga.AdNetworkList" \n\x03Sns\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t"\x84\x02\n\x0bMangaViewer\x12\x1a\n\x05pages\x18\x01 \x03(\x0b\x32\x0b.manga.Page\x12\x12\n\nchapter_id\x18\x02 \x01(\r\x12 \n\x08\x63hapters\x18\x03 \x03(\x0b\x32\x0e.manga.Chapter\x12\x17\n\x03sns\x18\x04 \x01(\x0b\x32\n.manga.Sns\x12\x12\n\ntitle_name\x18\x05 \x01(\t\x12\x14\n\x0c\x63hapter_name\x18\x06 \x01(\t\x12\x1a\n\x12number_of_comments\x18\x07 \x01(\r\x12\x18\n\x10is_vertical_only\x18\x08 \x01(\x08\x12\x10\n\x08title_id\x18\t \x01(\r\x12\x18\n\x10start_from_right\x18\n \x01(\x08"\x96\x01\n\x05Title\x12\x10\n\x08title_id\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x1a\n\x12portrait_image_url\x18\x04 \x01(\t\x12\x1b\n\x13landscape_image_url\x18\x05 \x01(\t\x12\x12\n\nview_count\x18\x06 \x01(\r\x12\x10\n\x08language\x18\x07 \x01(\x05"\x93\x01\n\x10\x43hapterListGroup\x12*\n\x12\x66irst_chapter_list\x18\x02 \x03(\x0b\x32\x0e.manga.Chapter\x12(\n\x10mid_chapter_list\x18\x03 \x03(\x0b\x32\x0e.manga.Chapter\x12)\n\x11last_chapter_list\x18\x04 \x03(\x0b\x32\x0e.manga.Chapter"\xd2\x04\n\x0fTitleDetailView\x12\x1b\n\x05title\x18\x01 \x01(\x0b\x32\x0c.manga.Title\x12\x17\n\x0ftitle_image_url\x18\x02 \x01(\t\x12\x10\n\x08overview\x18\x03 \x01(\t\x12\x1c\n\x14\x62\x61\x63kground_image_url\x18\x04 \x01(\t\x12\x16\n\x0enext_timestamp\x18\x05 \x01(\r\x12\x15\n\rupdate_timing\x18\x06 \x01(\x05\x12"\n\x1aviewing_period_description\x18\x07 \x01(\t\x12\x1b\n\x13non_appearance_info\x18\x08 \x01(\t\x12*\n\x12\x66irst_chapter_list\x18\t \x03(\x0b\x32\x0e.manga.Chapter\x12)\n\x11last_chapter_list\x18\n \x03(\x0b\x32\x0e.manga.Chapter\x12\x1e\n\x07\x62\x61nners\x18\x0b \x03(\x0b\x32\r.manga.Banner\x12,\n\x16recommended_title_list\x18\x0c \x03(\x0b\x32\x0c.manga.Title\x12\x17\n\x03sns\x18\r \x01(\x0b\x32\n.manga.Sns\x12\x19\n\x11is_simul_released\x18\x0e \x01(\x08\x12\x15\n\ris_subscribed\x18\x0f \x01(\x08\x12\x0e\n\x06rating\x18\x10 \x01(\x05\x12\x1b\n\x13\x63hapters_descending\x18\x11 \x01(\x08\x12\x17\n\x0fnumber_of_views\x18\x12 \x01(\r\x12\x33\n\x12\x63hapter_list_group\x18\x1c \x01(\x0b\x32\x17.manga.ChapterListGroup"l\n\rSuccessResult\x12\x31\n\x11title_detail_view\x18\x08 \x01(\x0b\x32\x16.manga.TitleDetailView\x12(\n\x0cmanga_viewer\x18\n \x01(\x0b\x32\x12.manga.MangaViewer"1\n\x08Response\x12%\n\x07success\x18\x01 \x01(\x0b\x32\x14.manga.SuccessResultb\x06proto3'
)


_BANNER = DESCRIPTOR.message_types_by_name["Banner"]
_BANNERLIST = DESCRIPTOR.message_types_by_name["BannerList"]
_TRANSITIONACTION = DESCRIPTOR.message_types_by_name["TransitionAction"]
_CHAPTER = DESCRIPTOR.message_types_by_name["Chapter"]
_COMMENT = DESCRIPTOR.message_types_by_name["Comment"]
_ADNETWORKLIST = DESCRIPTOR.message_types_by_name["AdNetworkList"]
_ADNETWORKLIST_ADNETWORK = _ADNETWORKLIST.nested_types_by_name["AdNetwork"]
_ADNETWORKLIST_ADNETWORK_FACEBOOK = (
    _ADNETWORKLIST_ADNETWORK.nested_types_by_name["Facebook"]
)
_ADNETWORKLIST_ADNETWORK_ADMOB = _ADNETWORKLIST_ADNETWORK.nested_types_by_name[
    "Admob"
]
_ADNETWORKLIST_ADNETWORK_MOPUB = _ADNETWORKLIST_ADNETWORK.nested_types_by_name[
    "Mopub"
]
_ADNETWORKLIST_ADNETWORK_ADSENSE = (
    _ADNETWORKLIST_ADNETWORK.nested_types_by_name["Adsense"]
)
_ADNETWORKLIST_ADNETWORK_APPLOVIN = (
    _ADNETWORKLIST_ADNETWORK.nested_types_by_name["Applovin"]
)
_POPUP = DESCRIPTOR.message_types_by_name["Popup"]
_POPUP_BUTTON = _POPUP.nested_types_by_name["Button"]
_POPUP_OSDEFAULT = _POPUP.nested_types_by_name["OSDefault"]
_POPUP_APPDEFAULT = _POPUP.nested_types_by_name["AppDefault"]
_POPUP_MOVIEREWARD = _POPUP.nested_types_by_name["MovieReward"]
_LASTPAGE = DESCRIPTOR.message_types_by_name["LastPage"]
_MANGAPAGE = DESCRIPTOR.message_types_by_name["MangaPage"]
_PAGE = DESCRIPTOR.message_types_by_name["Page"]
_SNS = DESCRIPTOR.message_types_by_name["Sns"]
_MANGAVIEWER = DESCRIPTOR.message_types_by_name["MangaViewer"]
_TITLE = DESCRIPTOR.message_types_by_name["Title"]
_CHAPTERLISTGROUP = DESCRIPTOR.message_types_by_name["ChapterListGroup"]
_TITLEDETAILVIEW = DESCRIPTOR.message_types_by_name["TitleDetailView"]
_SUCCESSRESULT = DESCRIPTOR.message_types_by_name["SuccessResult"]
_RESPONSE = DESCRIPTOR.message_types_by_name["Response"]
Banner = _reflection.GeneratedProtocolMessageType(
    "Banner",
    (_message.Message,),
    {
        "DESCRIPTOR": _BANNER,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Banner)
    },
)
_sym_db.RegisterMessage(Banner)

BannerList = _reflection.GeneratedProtocolMessageType(
    "BannerList",
    (_message.Message,),
    {
        "DESCRIPTOR": _BANNERLIST,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.BannerList)
    },
)
_sym_db.RegisterMessage(BannerList)

TransitionAction = _reflection.GeneratedProtocolMessageType(
    "TransitionAction",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSITIONACTION,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.TransitionAction)
    },
)
_sym_db.RegisterMessage(TransitionAction)

Chapter = _reflection.GeneratedProtocolMessageType(
    "Chapter",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHAPTER,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Chapter)
    },
)
_sym_db.RegisterMessage(Chapter)

Comment = _reflection.GeneratedProtocolMessageType(
    "Comment",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMMENT,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Comment)
    },
)
_sym_db.RegisterMessage(Comment)

AdNetworkList = _reflection.GeneratedProtocolMessageType(
    "AdNetworkList",
    (_message.Message,),
    {
        "AdNetwork": _reflection.GeneratedProtocolMessageType(
            "AdNetwork",
            (_message.Message,),
            {
                "Facebook": _reflection.GeneratedProtocolMessageType(
                    "Facebook",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ADNETWORKLIST_ADNETWORK_FACEBOOK,
                        "__module__": "response_pb2"
                        # @@protoc_insertion_point(class_scope:manga.AdNetworkList.AdNetwork.Facebook)
                    },
                ),
                "Admob": _reflection.GeneratedProtocolMessageType(
                    "Admob",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ADNETWORKLIST_ADNETWORK_ADMOB,
                        "__module__": "response_pb2"
                        # @@protoc_insertion_point(class_scope:manga.AdNetworkList.AdNetwork.Admob)
                    },
                ),
                "Mopub": _reflection.GeneratedProtocolMessageType(
                    "Mopub",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ADNETWORKLIST_ADNETWORK_MOPUB,
                        "__module__": "response_pb2"
                        # @@protoc_insertion_point(class_scope:manga.AdNetworkList.AdNetwork.Mopub)
                    },
                ),
                "Adsense": _reflection.GeneratedProtocolMessageType(
                    "Adsense",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ADNETWORKLIST_ADNETWORK_ADSENSE,
                        "__module__": "response_pb2"
                        # @@protoc_insertion_point(class_scope:manga.AdNetworkList.AdNetwork.Adsense)
                    },
                ),
                "Applovin": _reflection.GeneratedProtocolMessageType(
                    "Applovin",
                    (_message.Message,),
                    {
                        "DESCRIPTOR": _ADNETWORKLIST_ADNETWORK_APPLOVIN,
                        "__module__": "response_pb2"
                        # @@protoc_insertion_point(class_scope:manga.AdNetworkList.AdNetwork.Applovin)
                    },
                ),
                "DESCRIPTOR": _ADNETWORKLIST_ADNETWORK,
                "__module__": "response_pb2"
                # @@protoc_insertion_point(class_scope:manga.AdNetworkList.AdNetwork)
            },
        ),
        "DESCRIPTOR": _ADNETWORKLIST,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.AdNetworkList)
    },
)
_sym_db.RegisterMessage(AdNetworkList)
_sym_db.RegisterMessage(AdNetworkList.AdNetwork)
_sym_db.RegisterMessage(AdNetworkList.AdNetwork.Facebook)
_sym_db.RegisterMessage(AdNetworkList.AdNetwork.Admob)
_sym_db.RegisterMessage(AdNetworkList.AdNetwork.Mopub)
_sym_db.RegisterMessage(AdNetworkList.AdNetwork.Adsense)
_sym_db.RegisterMessage(AdNetworkList.AdNetwork.Applovin)

Popup = _reflection.GeneratedProtocolMessageType(
    "Popup",
    (_message.Message,),
    {
        "Button": _reflection.GeneratedProtocolMessageType(
            "Button",
            (_message.Message,),
            {
                "DESCRIPTOR": _POPUP_BUTTON,
                "__module__": "response_pb2"
                # @@protoc_insertion_point(class_scope:manga.Popup.Button)
            },
        ),
        "OSDefault": _reflection.GeneratedProtocolMessageType(
            "OSDefault",
            (_message.Message,),
            {
                "DESCRIPTOR": _POPUP_OSDEFAULT,
                "__module__": "response_pb2"
                # @@protoc_insertion_point(class_scope:manga.Popup.OSDefault)
            },
        ),
        "AppDefault": _reflection.GeneratedProtocolMessageType(
            "AppDefault",
            (_message.Message,),
            {
                "DESCRIPTOR": _POPUP_APPDEFAULT,
                "__module__": "response_pb2"
                # @@protoc_insertion_point(class_scope:manga.Popup.AppDefault)
            },
        ),
        "MovieReward": _reflection.GeneratedProtocolMessageType(
            "MovieReward",
            (_message.Message,),
            {
                "DESCRIPTOR": _POPUP_MOVIEREWARD,
                "__module__": "response_pb2"
                # @@protoc_insertion_point(class_scope:manga.Popup.MovieReward)
            },
        ),
        "DESCRIPTOR": _POPUP,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Popup)
    },
)
_sym_db.RegisterMessage(Popup)
_sym_db.RegisterMessage(Popup.Button)
_sym_db.RegisterMessage(Popup.OSDefault)
_sym_db.RegisterMessage(Popup.AppDefault)
_sym_db.RegisterMessage(Popup.MovieReward)

LastPage = _reflection.GeneratedProtocolMessageType(
    "LastPage",
    (_message.Message,),
    {
        "DESCRIPTOR": _LASTPAGE,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.LastPage)
    },
)
_sym_db.RegisterMessage(LastPage)

MangaPage = _reflection.GeneratedProtocolMessageType(
    "MangaPage",
    (_message.Message,),
    {
        "DESCRIPTOR": _MANGAPAGE,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.MangaPage)
    },
)
_sym_db.RegisterMessage(MangaPage)

Page = _reflection.GeneratedProtocolMessageType(
    "Page",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAGE,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Page)
    },
)
_sym_db.RegisterMessage(Page)

Sns = _reflection.GeneratedProtocolMessageType(
    "Sns",
    (_message.Message,),
    {
        "DESCRIPTOR": _SNS,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Sns)
    },
)
_sym_db.RegisterMessage(Sns)

MangaViewer = _reflection.GeneratedProtocolMessageType(
    "MangaViewer",
    (_message.Message,),
    {
        "DESCRIPTOR": _MANGAVIEWER,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.MangaViewer)
    },
)
_sym_db.RegisterMessage(MangaViewer)

Title = _reflection.GeneratedProtocolMessageType(
    "Title",
    (_message.Message,),
    {
        "DESCRIPTOR": _TITLE,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Title)
    },
)
_sym_db.RegisterMessage(Title)

ChapterListGroup = _reflection.GeneratedProtocolMessageType(
    "ChapterListGroup",
    (_message.Message,),
    {
        "DESCRIPTOR": _CHAPTERLISTGROUP,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.ChapterListGroup)
    },
)
_sym_db.RegisterMessage(ChapterListGroup)

TitleDetailView = _reflection.GeneratedProtocolMessageType(
    "TitleDetailView",
    (_message.Message,),
    {
        "DESCRIPTOR": _TITLEDETAILVIEW,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.TitleDetailView)
    },
)
_sym_db.RegisterMessage(TitleDetailView)

SuccessResult = _reflection.GeneratedProtocolMessageType(
    "SuccessResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _SUCCESSRESULT,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.SuccessResult)
    },
)
_sym_db.RegisterMessage(SuccessResult)

Response = _reflection.GeneratedProtocolMessageType(
    "Response",
    (_message.Message,),
    {
        "DESCRIPTOR": _RESPONSE,
        "__module__": "response_pb2"
        # @@protoc_insertion_point(class_scope:manga.Response)
    },
)
_sym_db.RegisterMessage(Response)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _BANNER._serialized_start = 25
    _BANNER._serialized_end = 105
    _BANNERLIST._serialized_start = 107
    _BANNERLIST._serialized_end = 173
    _TRANSITIONACTION._serialized_start = 175
    _TRANSITIONACTION._serialized_end = 222
    _CHAPTER._serialized_start = 225
    _CHAPTER._serialized_end = 426
    _COMMENT._serialized_start = 429
    _COMMENT._serialized_end = 604
    _ADNETWORKLIST._serialized_start = 607
    _ADNETWORKLIST._serialized_end = 1113
    _ADNETWORKLIST_ADNETWORK._serialized_start = 678
    _ADNETWORKLIST_ADNETWORK._serialized_end = 1113
    _ADNETWORKLIST_ADNETWORK_FACEBOOK._serialized_start = 972
    _ADNETWORKLIST_ADNETWORK_FACEBOOK._serialized_end = 1004
    _ADNETWORKLIST_ADNETWORK_ADMOB._serialized_start = 1006
    _ADNETWORKLIST_ADNETWORK_ADMOB._serialized_end = 1030
    _ADNETWORKLIST_ADNETWORK_MOPUB._serialized_start = 1032
    _ADNETWORKLIST_ADNETWORK_MOPUB._serialized_end = 1056
    _ADNETWORKLIST_ADNETWORK_ADSENSE._serialized_start = 1058
    _ADNETWORKLIST_ADNETWORK_ADSENSE._serialized_end = 1084
    _ADNETWORKLIST_ADNETWORK_APPLOVIN._serialized_start = 1086
    _ADNETWORKLIST_ADNETWORK_APPLOVIN._serialized_end = 1113
    _POPUP._serialized_start = 1116
    _POPUP._serialized_end = 1684
    _POPUP_BUTTON._serialized_start = 1263
    _POPUP_BUTTON._serialized_end = 1326
    _POPUP_OSDEFAULT._serialized_start = 1329
    _POPUP_OSDEFAULT._serialized_end = 1500
    _POPUP_APPDEFAULT._serialized_start = 1502
    _POPUP_APPDEFAULT._serialized_end = 1605
    _POPUP_MOVIEREWARD._serialized_start = 1607
    _POPUP_MOVIEREWARD._serialized_end = 1684
    _LASTPAGE._serialized_start = 1687
    _LASTPAGE._serialized_end = 1964
    _MANGAPAGE._serialized_start = 1966
    _MANGAPAGE._serialized_end = 2065
    _PAGE._serialized_start = 2068
    _PAGE._serialized_end = 2233
    _SNS._serialized_start = 2235
    _SNS._serialized_end = 2267
    _MANGAVIEWER._serialized_start = 2270
    _MANGAVIEWER._serialized_end = 2530
    _TITLE._serialized_start = 2533
    _TITLE._serialized_end = 2683
    _CHAPTERLISTGROUP._serialized_start = 2686
    _CHAPTERLISTGROUP._serialized_end = 2833
    _TITLEDETAILVIEW._serialized_start = 2836
    _TITLEDETAILVIEW._serialized_end = 3430
    _SUCCESSRESULT._serialized_start = 3432
    _SUCCESSRESULT._serialized_end = 3540
    _RESPONSE._serialized_start = 3542
    _RESPONSE._serialized_end = 3591
# @@protoc_insertion_point(module_scope)
