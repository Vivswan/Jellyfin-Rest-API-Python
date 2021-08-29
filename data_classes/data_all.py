from data_classes.access_schedule import AccessSchedule
from data_classes.action import Action
from data_classes.activity_log_entry import ActivityLogEntry
from data_classes.activity_log_entry_query_result import ActivityLogEntryQueryResult
from data_classes.add_virtual_folder_dto import AddVirtualFolderDto
from data_classes.admin_notification_dto import AdminNotificationDto
from data_classes.album_info_class import AlbumInfoClass
from data_classes.album_info_remote_search_query import AlbumInfoRemoteSearchQuery
from data_classes.all_theme_media_result import AllThemeMediaResult
from data_classes.architecture import Architecture
from data_classes.artist_info_class import ArtistInfoClass
from data_classes.artist_info_remote_search_query import ArtistInfoRemoteSearchQuery
from data_classes.audio import Audio
from data_classes.authenticate_user_by_name import AuthenticateUserByName
from data_classes.authentication_info import AuthenticationInfo
from data_classes.authentication_info_query_result import AuthenticationInfoQueryResult
from data_classes.authentication_result import AuthenticationResult
from data_classes.base_item_dto import BaseItemDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult
from data_classes.base_item_person import BaseItemPerson
from data_classes.base_plugin_configuration import BasePluginConfiguration
from data_classes.book_info_class import BookInfoClass
from data_classes.book_info_remote_search_query import BookInfoRemoteSearchQuery
from data_classes.box_set_info_class import BoxSetInfoClass
from data_classes.box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery
from data_classes.branding_options import BrandingOptions
from data_classes.buffer_request_dto import BufferRequestDto
from data_classes.capabilities import Capabilities
from data_classes.channel_features import ChannelFeatures
from data_classes.channel_item_sort_field import ChannelItemSortField
from data_classes.channel_mapping_options_dto import ChannelMappingOptionsDto
from data_classes.channel_media_content_type import ChannelMediaContentType
from data_classes.channel_media_type_element import ChannelMediaTypeElement
from data_classes.channel_type import ChannelType
from data_classes.chapter_info import ChapterInfo
from data_classes.client_capabilities_dto import ClientCapabilitiesDto
from data_classes.codec_profile import CodecProfile
from data_classes.codec_type_enum import CodecTypeEnum
from data_classes.collection_creation_result import CollectionCreationResult
from data_classes.collection_type import CollectionType
from data_classes.condition import Condition
from data_classes.configuration import Configuration
from data_classes.configuration_page_info import ConfigurationPageInfo
from data_classes.configuration_page_type import ConfigurationPageType
from data_classes.container_profile import ContainerProfile
from data_classes.context import Context
from data_classes.control_response import ControlResponse
from data_classes.country_info import CountryInfo
from data_classes.create_playlist_dto import CreatePlaylistDto
from data_classes.create_user_by_name import CreateUserByName
from data_classes.culture_dto import CultureDto
from data_classes.custom_query_data import CustomQueryData
from data_classes.day_of_week import DayOfWeek
from data_classes.day_of_week_element import DayOfWeekElement
from data_classes.day_pattern import DayPattern
from data_classes.default_directory_browser_info_dto import DefaultDirectoryBrowserInfoDto
from data_classes.device_info import DeviceInfo
from data_classes.device_info_query_result import DeviceInfoQueryResult
from data_classes.device_options import DeviceOptions
from data_classes.device_profile import DeviceProfile
from data_classes.device_profile_info import DeviceProfileInfo
from data_classes.device_profile_type_enum import DeviceProfileTypeEnum
from data_classes.direct_play_profile import DirectPlayProfile
from data_classes.display_preferences_dto import DisplayPreferencesDto
from data_classes.display_type import DisplayType
from data_classes.end_point_info import EndPointInfo
from data_classes.error_code import ErrorCode
from data_classes.external_i_d_info import ExternalIDInfo
from data_classes.external_i_d_media_type_enum import ExternalIDMediaTypeEnum
from data_classes.external_u_r_l import ExternalURL
from data_classes.field_type import FieldType
from data_classes.file_organization_result import FileOrganizationResult
from data_classes.file_organization_result_query_result import FileOrganizationResultQueryResult
from data_classes.file_organizer_type_enum import FileOrganizerTypeEnum
from data_classes.file_sorting_status_enum import FileSortingStatusEnum
from data_classes.file_system_entry_info import FileSystemEntryInfo
from data_classes.file_system_entry_type_enum import FileSystemEntryTypeEnum
from data_classes.font_file import FontFile
from data_classes.forgot_password_dto import ForgotPasswordDto
from data_classes.forgot_password_pin_dto import ForgotPasswordPinDto
from data_classes.forgot_password_result import ForgotPasswordResult
from data_classes.general_command import GeneralCommand
from data_classes.general_command_type import GeneralCommandType
from data_classes.get_programs_dto import GetProgramsDto
from data_classes.group_info_dto import GroupInfoDto
from data_classes.group_queue_mode_enum import GroupQueueModeEnum
from data_classes.group_repeat_mode_enum import GroupRepeatModeEnum
from data_classes.group_shuffle_mode_enum import GroupShuffleModeEnum
from data_classes.group_state_type_enum import GroupStateTypeEnum
from data_classes.group_update_type_enum import GroupUpdateTypeEnum
from data_classes.guide_info import GuideInfo
from data_classes.h_t_t_p_header_info import HTTPHeaderInfo
from data_classes.header_metadata import HeaderMetadata
from data_classes.i_plugin import IPlugin
from data_classes.i_s_o_type import ISOType
from data_classes.identification import Identification
from data_classes.ignore_wait_request_dto import IgnoreWaitRequestDto
from data_classes.image_by_name_info import ImageByNameInfo
from data_classes.image_format import ImageFormat
from data_classes.image_info import ImageInfo
from data_classes.image_option import ImageOption
from data_classes.image_orientation import ImageOrientation
from data_classes.image_provider_info import ImageProviderInfo
from data_classes.image_saving_convention import ImageSavingConvention
from data_classes.image_type_element import ImageTypeElement
from data_classes.installation_info import InstallationInfo
from data_classes.item import Item
from data_classes.item_counts import ItemCounts
from data_classes.item_fields import ItemFields
from data_classes.item_filter import ItemFilter
from data_classes.item_view_type import ItemViewType
from data_classes.items import Items
from data_classes.join_group_request_dto import JoinGroupRequestDto
from data_classes.keep_until import KeepUntil
from data_classes.level import Level
from data_classes.library_option_info_dto import LibraryOptionInfoDto
from data_classes.library_options import LibraryOptions
from data_classes.library_options_result_dto import LibraryOptionsResultDto
from data_classes.library_type_options_dto import LibraryTypeOptionsDto
from data_classes.library_update_info import LibraryUpdateInfo
from data_classes.listings_provider_info import ListingsProviderInfo
from data_classes.live_stream_response import LiveStreamResponse
from data_classes.live_tv_info import LiveTvInfo
from data_classes.live_tv_service_info import LiveTvServiceInfo
from data_classes.live_tv_service_status_enum import LiveTvServiceStatusEnum
from data_classes.localization_option import LocalizationOption
from data_classes.location import Location
from data_classes.location_type import LocationType
from data_classes.log_file import LogFile
from data_classes.match import Match
from data_classes.media_attachment import MediaAttachment
from data_classes.media_encoder_path_dto import MediaEncoderPathDto
from data_classes.media_path_dto import MediaPathDto
from data_classes.media_source import MediaSource
from data_classes.media_source_type_enum import MediaSourceTypeEnum
from data_classes.media_stream import MediaStream
from data_classes.media_stream_type_enum import MediaStreamTypeEnum
from data_classes.media_u_r_l import MediaURL
from data_classes.media_update_info_dto import MediaUpdateInfoDto
from data_classes.media_update_info_path_dto import MediaUpdateInfoPathDto
from data_classes.message_command import MessageCommand
from data_classes.metadata_editor_info import MetadataEditorInfo
from data_classes.metadata_field import MetadataField
from data_classes.metadata_options import MetadataOptions
from data_classes.metadata_refresh_mode import MetadataRefreshMode
from data_classes.method import Method
from data_classes.move_playlist_item_request_dto import MovePlaylistItemRequestDto
from data_classes.movie_info_class import MovieInfoClass
from data_classes.movie_info_remote_search_query import MovieInfoRemoteSearchQuery
from data_classes.music_video_info_class import MusicVideoInfoClass
from data_classes.music_video_info_remote_search_query import MusicVideoInfoRemoteSearchQuery
from data_classes.name_g_u_i_d_pair import NameGUIDPair
from data_classes.name_i_d_pair import NameIDPair
from data_classes.name_value_pair import NameValuePair
from data_classes.new_group_request_dto import NewGroupRequestDto
from data_classes.next_item_request_dto import NextItemRequestDto
from data_classes.not_found import NotFound
from data_classes.notification_dto import NotificationDto
from data_classes.notification_result_dto import NotificationResultDto
from data_classes.notification_type_info import NotificationTypeInfo
from data_classes.notifications_summary_dto import NotificationsSummaryDto
from data_classes.object_group_update import ObjectGroupUpdate
from data_classes.open_live_stream_dto import OpenLiveStreamDto
from data_classes.package_info import PackageInfo
from data_classes.parental_rating import ParentalRating
from data_classes.path_info import PathInfo
from data_classes.path_substitution import PathSubstitution
from data_classes.person_lookup_info_class import PersonLookupInfoClass
from data_classes.person_lookup_info_remote_search_query import PersonLookupInfoRemoteSearchQuery
from data_classes.pin_redeem_result import PinRedeemResult
from data_classes.ping_request_dto import PingRequestDto
from data_classes.play import Play
from data_classes.play_access import PlayAccess
from data_classes.play_command import PlayCommand
from data_classes.play_method import PlayMethod
from data_classes.play_request import PlayRequest
from data_classes.play_request_dto import PlayRequestDto
from data_classes.playback_info_dto import PlaybackInfoDto
from data_classes.playback_info_response import PlaybackInfoResponse
from data_classes.playback_progress_info import PlaybackProgressInfo
from data_classes.playback_start_info import PlaybackStartInfo
from data_classes.playback_stop_info import PlaybackStopInfo
from data_classes.playlist_creation_result import PlaylistCreationResult
from data_classes.playstate_command_enum import PlaystateCommandEnum
from data_classes.playstate_request import PlaystateRequest
from data_classes.plugin_info import PluginInfo
from data_classes.plugin_security_info import PluginSecurityInfo
from data_classes.plugin_status_enum import PluginStatusEnum
from data_classes.policy import Policy
from data_classes.previous_item_request_dto import PreviousItemRequestDto
from data_classes.pro import Pro
from data_classes.problem_details import ProblemDetails
from data_classes.profile_condition import ProfileCondition
from data_classes.protocol import Protocol
from data_classes.public_system_info import PublicSystemInfo
from data_classes.query_filters import QueryFilters
from data_classes.query_filters_legacy import QueryFiltersLegacy
from data_classes.queue_item import QueueItem
from data_classes.queue_request_dto import QueueRequestDto
from data_classes.quick_connect_dto import QuickConnectDto
from data_classes.quick_connect_result import QuickConnectResult
from data_classes.quick_connect_state import QuickConnectState
from data_classes.rating_type import RatingType
from data_classes.ready_request_dto import ReadyRequestDto
from data_classes.recommendation_dto import RecommendationDto
from data_classes.recommendation_type import RecommendationType
from data_classes.recording_status_enum import RecordingStatusEnum
from data_classes.remote_image_info import RemoteImageInfo
from data_classes.remote_image_result import RemoteImageResult
from data_classes.remote_search_result import RemoteSearchResult
from data_classes.remote_subtitle_info import RemoteSubtitleInfo
from data_classes.remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto
from data_classes.report_export_type import ReportExportType
from data_classes.report_group import ReportGroup
from data_classes.report_header import ReportHeader
from data_classes.report_item import ReportItem
from data_classes.report_result import ReportResult
from data_classes.report_row import ReportRow
from data_classes.repository_info import RepositoryInfo
from data_classes.response_profile import ResponseProfile
from data_classes.row_type import RowType
from data_classes.scroll_direction import ScrollDirection
from data_classes.search_hint import SearchHint
from data_classes.search_hint_result import SearchHintResult
from data_classes.seek_request_dto import SeekRequestDto
from data_classes.send_command import SendCommand
from data_classes.send_command_type_enum import SendCommandTypeEnum
from data_classes.series_info_class import SeriesInfoClass
from data_classes.series_info_remote_search_query import SeriesInfoRemoteSearchQuery
from data_classes.series_status import SeriesStatus
from data_classes.series_timer_info_dto import SeriesTimerInfoDto
from data_classes.series_timer_info_dto_query_result import SeriesTimerInfoDtoQueryResult
from data_classes.server_configuration import ServerConfiguration
from data_classes.server_discovery_info import ServerDiscoveryInfo
from data_classes.session_info import SessionInfo
from data_classes.session_message_type import SessionMessageType
from data_classes.session_user_info import SessionUserInfo
from data_classes.set_channel_mapping_dto import SetChannelMappingDto
from data_classes.set_playlist_item_request_dto import SetPlaylistItemRequestDto
from data_classes.set_repeat_mode_request_dto import SetRepeatModeRequestDto
from data_classes.set_shuffle_mode_request_dto import SetShuffleModeRequestDto
from data_classes.severity import Severity
from data_classes.smart_match_result import SmartMatchResult
from data_classes.smart_match_result_query_result import SmartMatchResultQueryResult
from data_classes.song_info import SongInfo
from data_classes.sort_order import SortOrder
from data_classes.special_view_option_dto import SpecialViewOptionDto
from data_classes.startup_configuration_dto import StartupConfigurationDto
from data_classes.startup_remote_access_dto import StartupRemoteAccessDto
from data_classes.startup_user_dto import StartupUserDto
from data_classes.subtitle_mode import SubtitleMode
from data_classes.subtitle_profile import SubtitleProfile
from data_classes.sync_play import SyncPlay
from data_classes.system_info import SystemInfo
from data_classes.task_completion_status_enum import TaskCompletionStatusEnum
from data_classes.task_info import TaskInfo
from data_classes.task_result_class import TaskResultClass
from data_classes.task_state_enum import TaskStateEnum
from data_classes.task_trigger_info import TaskTriggerInfo
from data_classes.theme_media_result_class import ThemeMediaResultClass
from data_classes.timer_event_info import TimerEventInfo
from data_classes.timer_info_dto import TimerInfoDto
from data_classes.timer_info_dto_query_result import TimerInfoDtoQueryResult
from data_classes.timestamp import Timestamp
from data_classes.trailer_info_class import TrailerInfoClass
from data_classes.trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery
from data_classes.trakt_episode import TraktEpisode
from data_classes.trakt_episode_i_d_class import TraktEpisodeIDClass
from data_classes.trakt_movie import TraktMovie
from data_classes.trakt_movie_i_d_class import TraktMovieIDClass
from data_classes.trakt_person import TraktPerson
from data_classes.trakt_person_i_d_class import TraktPersonIDClass
from data_classes.trakt_season import TraktSeason
from data_classes.trakt_season_i_d_class import TraktSeasonIDClass
from data_classes.trakt_show import TraktShow
from data_classes.trakt_show_i_d_class import TraktShowIDClass
from data_classes.trakt_sync_response import TraktSyncResponse
from data_classes.transcode_reason import TranscodeReason
from data_classes.transcode_seek_info import TranscodeSeekInfo
from data_classes.transcoding_info import TranscodingInfo
from data_classes.transcoding_profile import TranscodingProfile
from data_classes.tuner_channel_mapping import TunerChannelMapping
from data_classes.tuner_host_info import TunerHostInfo
from data_classes.type_options import TypeOptions
from data_classes.u_t_c_time_response import UTCTimeResponse
from data_classes.unrated_item import UnratedItem
from data_classes.update_library_options_dto import UpdateLibraryOptionsDto
from data_classes.update_media_path_request_dto import UpdateMediaPathRequestDto
from data_classes.update_user_easy_password import UpdateUserEasyPassword
from data_classes.update_user_password import UpdateUserPassword
from data_classes.upload_subtitle_dto import UploadSubtitleDto
from data_classes.user import User
from data_classes.user_dto_class import UserDtoClass
from data_classes.validate_path_dto import ValidatePathDto
from data_classes.version_info import VersionInfo
from data_classes.version_number import VersionNumber
from data_classes.video3_d_format import Video3DFormat
from data_classes.video_type import VideoType
from data_classes.virtual_folder_info import VirtualFolderInfo
from data_classes.wake_on_l_a_n_info import WakeOnLANInfo
from data_classes.x_m_l_attribute import XMLAttribute
from util.from_type import *


@dataclass
class DataAll:
    access_schedule: Optional[AccessSchedule] = None
    activity_log_entry: Optional[ActivityLogEntry] = None
    activity_log_entry_query_result: Optional[ActivityLogEntryQueryResult] = None
    add_virtual_folder_dto: Optional[AddVirtualFolderDto] = None
    admin_notification_dto: Optional[AdminNotificationDto] = None
    album_info: Optional[AlbumInfoClass] = None
    album_info_remote_search_query: Optional[AlbumInfoRemoteSearchQuery] = None
    all_theme_media_result: Optional[AllThemeMediaResult] = None
    architecture: Optional[Architecture] = None
    artist_info: Optional[ArtistInfoClass] = None
    artist_info_remote_search_query: Optional[ArtistInfoRemoteSearchQuery] = None
    authenticate_user_by_name: Optional[AuthenticateUserByName] = None
    authentication_info: Optional[AuthenticationInfo] = None
    authentication_info_query_result: Optional[AuthenticationInfoQueryResult] = None
    authentication_result: Optional[AuthenticationResult] = None
    base_item: Optional[Item] = None
    base_item_dto: Optional[BaseItemDto] = None
    base_item_dto_query_result: Optional[BaseItemDtoQueryResult] = None
    base_item_person: Optional[BaseItemPerson] = None
    base_plugin_configuration: Optional[BasePluginConfiguration] = None
    book_info: Optional[BookInfoClass] = None
    book_info_remote_search_query: Optional[BookInfoRemoteSearchQuery] = None
    box_set_info: Optional[BoxSetInfoClass] = None
    box_set_info_remote_search_query: Optional[BoxSetInfoRemoteSearchQuery] = None
    branding_options: Optional[BrandingOptions] = None
    buffer_request_dto: Optional[BufferRequestDto] = None
    channel_features: Optional[ChannelFeatures] = None
    channel_item_sort_field: Optional[ChannelItemSortField] = None
    channel_mapping_options_dto: Optional[ChannelMappingOptionsDto] = None
    channel_media_content_type: Optional[ChannelMediaContentType] = None
    channel_media_type: Optional[ChannelMediaTypeElement] = None
    channel_type: Optional[ChannelType] = None
    chapter_info: Optional[ChapterInfo] = None
    client_capabilities: Optional[Capabilities] = None
    client_capabilities_dto: Optional[ClientCapabilitiesDto] = None
    codec_profile: Optional[CodecProfile] = None
    codec_type: Optional[CodecTypeEnum] = None
    collection_creation_result: Optional[CollectionCreationResult] = None
    collection_type_options: Optional[CollectionType] = None
    configuration_page_info: Optional[ConfigurationPageInfo] = None
    configuration_page_type: Optional[ConfigurationPageType] = None
    container_profile: Optional[ContainerProfile] = None
    control_response: Optional[ControlResponse] = None
    country_info: Optional[CountryInfo] = None
    create_playlist_dto: Optional[CreatePlaylistDto] = None
    create_user_by_name: Optional[CreateUserByName] = None
    culture_dto: Optional[CultureDto] = None
    custom_query_data: Optional[CustomQueryData] = None
    day_of_week: Optional[DayOfWeekElement] = None
    day_pattern: Optional[DayPattern] = None
    default_directory_browser_info_dto: Optional[DefaultDirectoryBrowserInfoDto] = None
    device_identification: Optional[Identification] = None
    device_info: Optional[DeviceInfo] = None
    device_info_query_result: Optional[DeviceInfoQueryResult] = None
    device_options: Optional[DeviceOptions] = None
    device_profile: Optional[DeviceProfile] = None
    device_profile_info: Optional[DeviceProfileInfo] = None
    device_profile_type: Optional[DeviceProfileTypeEnum] = None
    direct_play_profile: Optional[DirectPlayProfile] = None
    display_preferences_dto: Optional[DisplayPreferencesDto] = None
    dlna_profile_type: Optional[ChannelMediaTypeElement] = None
    dynamic_day_of_week: Optional[DayOfWeek] = None
    encoding_context: Optional[Context] = None
    end_point_info: Optional[EndPointInfo] = None
    external_id_info: Optional[ExternalIDInfo] = None
    external_id_media_type: Optional[ExternalIDMediaTypeEnum] = None
    external_url: Optional[ExternalURL] = None
    f_fmpeg_location: Optional[Location] = None
    file_organization_result: Optional[FileOrganizationResult] = None
    file_organization_result_query_result: Optional[FileOrganizationResultQueryResult] = None
    file_organizer_type: Optional[FileOrganizerTypeEnum] = None
    file_sorting_status: Optional[FileSortingStatusEnum] = None
    file_system_entry_info: Optional[FileSystemEntryInfo] = None
    file_system_entry_type: Optional[FileSystemEntryTypeEnum] = None
    font_file: Optional[FontFile] = None
    forgot_password_action: Optional[Action] = None
    forgot_password_dto: Optional[ForgotPasswordDto] = None
    forgot_password_pin_dto: Optional[ForgotPasswordPinDto] = None
    forgot_password_result: Optional[ForgotPasswordResult] = None
    general_command: Optional[GeneralCommand] = None
    general_command_type: Optional[GeneralCommandType] = None
    get_programs_dto: Optional[GetProgramsDto] = None
    group_info_dto: Optional[GroupInfoDto] = None
    group_queue_mode: Optional[GroupQueueModeEnum] = None
    group_repeat_mode: Optional[GroupRepeatModeEnum] = None
    group_shuffle_mode: Optional[GroupShuffleModeEnum] = None
    group_state_type: Optional[GroupStateTypeEnum] = None
    group_update_type: Optional[GroupUpdateTypeEnum] = None
    guide_info: Optional[GuideInfo] = None
    header_match_type: Optional[Match] = None
    header_metadata: Optional[HeaderMetadata] = None
    http_header_info: Optional[HTTPHeaderInfo] = None
    ignore_wait_request_dto: Optional[IgnoreWaitRequestDto] = None
    image_by_name_info: Optional[ImageByNameInfo] = None
    image_format: Optional[ImageFormat] = None
    image_info: Optional[ImageInfo] = None
    image_option: Optional[ImageOption] = None
    image_orientation: Optional[ImageOrientation] = None
    image_provider_info: Optional[ImageProviderInfo] = None
    image_saving_convention: Optional[ImageSavingConvention] = None
    image_type: Optional[ImageTypeElement] = None
    installation_info: Optional[InstallationInfo] = None
    i_plugin: Optional[IPlugin] = None
    iso_type: Optional[ISOType] = None
    item_counts: Optional[ItemCounts] = None
    item_fields: Optional[ItemFields] = None
    item_filter: Optional[ItemFilter] = None
    items: Optional[Items] = None
    item_view_type: Optional[ItemViewType] = None
    join_group_request_dto: Optional[JoinGroupRequestDto] = None
    keep_until: Optional[KeepUntil] = None
    library_option_info_dto: Optional[LibraryOptionInfoDto] = None
    library_options: Optional[LibraryOptions] = None
    library_options_result_dto: Optional[LibraryOptionsResultDto] = None
    library_type_options_dto: Optional[LibraryTypeOptionsDto] = None
    library_update_info: Optional[LibraryUpdateInfo] = None
    listings_provider_info: Optional[ListingsProviderInfo] = None
    live_stream_response: Optional[LiveStreamResponse] = None
    live_tv_info: Optional[LiveTvInfo] = None
    live_tv_service_info: Optional[LiveTvServiceInfo] = None
    live_tv_service_status: Optional[LiveTvServiceStatusEnum] = None
    localization_option: Optional[LocalizationOption] = None
    location_type: Optional[LocationType] = None
    log_file: Optional[LogFile] = None
    log_level: Optional[Severity] = None
    media_attachment: Optional[MediaAttachment] = None
    media_encoder_path_dto: Optional[MediaEncoderPathDto] = None
    media_path_dto: Optional[MediaPathDto] = None
    media_path_info: Optional[PathInfo] = None
    media_protocol: Optional[Protocol] = None
    media_source_info: Optional[MediaSource] = None
    media_source_type: Optional[MediaSourceTypeEnum] = None
    media_stream: Optional[MediaStream] = None
    media_stream_type: Optional[MediaStreamTypeEnum] = None
    media_update_info_dto: Optional[MediaUpdateInfoDto] = None
    media_update_info_path_dto: Optional[MediaUpdateInfoPathDto] = None
    media_url: Optional[MediaURL] = None
    message_command: Optional[MessageCommand] = None
    metadata_editor_info: Optional[MetadataEditorInfo] = None
    metadata_field: Optional[MetadataField] = None
    metadata_options: Optional[MetadataOptions] = None
    metadata_refresh_mode: Optional[MetadataRefreshMode] = None
    move_playlist_item_request_dto: Optional[MovePlaylistItemRequestDto] = None
    movie_info: Optional[MovieInfoClass] = None
    movie_info_remote_search_query: Optional[MovieInfoRemoteSearchQuery] = None
    music_video_info: Optional[MusicVideoInfoClass] = None
    music_video_info_remote_search_query: Optional[MusicVideoInfoRemoteSearchQuery] = None
    name_guid_pair: Optional[NameGUIDPair] = None
    name_id_pair: Optional[NameIDPair] = None
    name_value_pair: Optional[NameValuePair] = None
    new_group_request_dto: Optional[NewGroupRequestDto] = None
    next_item_request_dto: Optional[NextItemRequestDto] = None
    not_found_objects: Optional[NotFound] = None
    notification_dto: Optional[NotificationDto] = None
    notification_level: Optional[Level] = None
    notification_result_dto: Optional[NotificationResultDto] = None
    notifications_summary_dto: Optional[NotificationsSummaryDto] = None
    notification_type_info: Optional[NotificationTypeInfo] = None
    object_group_update: Optional[ObjectGroupUpdate] = None
    open_live_stream_dto: Optional[OpenLiveStreamDto] = None
    package_info: Optional[PackageInfo] = None
    parental_rating: Optional[ParentalRating] = None
    path_substitution: Optional[PathSubstitution] = None
    person_lookup_info: Optional[PersonLookupInfoClass] = None
    person_lookup_info_remote_search_query: Optional[PersonLookupInfoRemoteSearchQuery] = None
    ping_request_dto: Optional[PingRequestDto] = None
    pin_redeem_result: Optional[PinRedeemResult] = None
    play_access: Optional[PlayAccess] = None
    playback_error_code: Optional[ErrorCode] = None
    playback_info_dto: Optional[PlaybackInfoDto] = None
    playback_info_response: Optional[PlaybackInfoResponse] = None
    playback_progress_info: Optional[PlaybackProgressInfo] = None
    playback_start_info: Optional[PlaybackStartInfo] = None
    playback_stop_info: Optional[PlaybackStopInfo] = None
    play_command: Optional[PlayCommand] = None
    player_state_info: Optional[Play] = None
    playlist_creation_result: Optional[PlaylistCreationResult] = None
    play_method: Optional[PlayMethod] = None
    play_request: Optional[PlayRequest] = None
    play_request_dto: Optional[PlayRequestDto] = None
    playstate_command: Optional[PlaystateCommandEnum] = None
    playstate_request: Optional[PlaystateRequest] = None
    plugin_info: Optional[PluginInfo] = None
    plugin_security_info: Optional[PluginSecurityInfo] = None
    plugin_status: Optional[PluginStatusEnum] = None
    previous_item_request_dto: Optional[PreviousItemRequestDto] = None
    problem_details: Optional[ProblemDetails] = None
    profile_condition: Optional[ProfileCondition] = None
    profile_condition_type: Optional[Condition] = None
    profile_condition_value: Optional[Pro] = None
    program_audio: Optional[Audio] = None
    public_system_info: Optional[PublicSystemInfo] = None
    query_filters: Optional[QueryFilters] = None
    query_filters_legacy: Optional[QueryFiltersLegacy] = None
    queue_item: Optional[QueueItem] = None
    queue_request_dto: Optional[QueueRequestDto] = None
    quick_connect_dto: Optional[QuickConnectDto] = None
    quick_connect_result: Optional[QuickConnectResult] = None
    quick_connect_state: Optional[QuickConnectState] = None
    rating_type: Optional[RatingType] = None
    ready_request_dto: Optional[ReadyRequestDto] = None
    recommendation_dto: Optional[RecommendationDto] = None
    recommendation_type: Optional[RecommendationType] = None
    recording_status: Optional[RecordingStatusEnum] = None
    remote_image_info: Optional[RemoteImageInfo] = None
    remote_image_result: Optional[RemoteImageResult] = None
    remote_search_result: Optional[RemoteSearchResult] = None
    remote_subtitle_info: Optional[RemoteSubtitleInfo] = None
    remove_from_playlist_request_dto: Optional[RemoveFromPlaylistRequestDto] = None
    repeat_mode: Optional[GroupRepeatModeEnum] = None
    report_display_type: Optional[DisplayType] = None
    report_export_type: Optional[ReportExportType] = None
    report_field_type: Optional[FieldType] = None
    report_group: Optional[ReportGroup] = None
    report_header: Optional[ReportHeader] = None
    report_include_item_types: Optional[RowType] = None
    report_item: Optional[ReportItem] = None
    report_result: Optional[ReportResult] = None
    report_row: Optional[ReportRow] = None
    repository_info: Optional[RepositoryInfo] = None
    response_profile: Optional[ResponseProfile] = None
    scroll_direction: Optional[ScrollDirection] = None
    search_hint: Optional[SearchHint] = None
    search_hint_result: Optional[SearchHintResult] = None
    seek_request_dto: Optional[SeekRequestDto] = None
    send_command: Optional[SendCommand] = None
    send_command_type: Optional[SendCommandTypeEnum] = None
    series_info: Optional[SeriesInfoClass] = None
    series_info_remote_search_query: Optional[SeriesInfoRemoteSearchQuery] = None
    series_status: Optional[SeriesStatus] = None
    series_timer_info_dto: Optional[SeriesTimerInfoDto] = None
    series_timer_info_dto_query_result: Optional[SeriesTimerInfoDtoQueryResult] = None
    server_configuration: Optional[ServerConfiguration] = None
    server_discovery_info: Optional[ServerDiscoveryInfo] = None
    session_info: Optional[SessionInfo] = None
    session_message_type: Optional[SessionMessageType] = None
    session_user_info: Optional[SessionUserInfo] = None
    set_channel_mapping_dto: Optional[SetChannelMappingDto] = None
    set_playlist_item_request_dto: Optional[SetPlaylistItemRequestDto] = None
    set_repeat_mode_request_dto: Optional[SetRepeatModeRequestDto] = None
    set_shuffle_mode_request_dto: Optional[SetShuffleModeRequestDto] = None
    smart_match_result: Optional[SmartMatchResult] = None
    smart_match_result_query_result: Optional[SmartMatchResultQueryResult] = None
    song_info: Optional[SongInfo] = None
    sort_order: Optional[SortOrder] = None
    special_view_option_dto: Optional[SpecialViewOptionDto] = None
    startup_configuration_dto: Optional[StartupConfigurationDto] = None
    startup_remote_access_dto: Optional[StartupRemoteAccessDto] = None
    startup_user_dto: Optional[StartupUserDto] = None
    subtitle_delivery_method: Optional[Method] = None
    subtitle_playback_mode: Optional[SubtitleMode] = None
    subtitle_profile: Optional[SubtitleProfile] = None
    sync_play_user_access_type: Optional[SyncPlay] = None
    system_info: Optional[SystemInfo] = None
    task_completion_status: Optional[TaskCompletionStatusEnum] = None
    task_info: Optional[TaskInfo] = None
    task_result: Optional[TaskResultClass] = None
    task_state: Optional[TaskStateEnum] = None
    task_trigger_info: Optional[TaskTriggerInfo] = None
    theme_media_result: Optional[ThemeMediaResultClass] = None
    timer_event_info: Optional[TimerEventInfo] = None
    timer_info_dto: Optional[TimerInfoDto] = None
    timer_info_dto_query_result: Optional[TimerInfoDtoQueryResult] = None
    trailer_info: Optional[TrailerInfoClass] = None
    trailer_info_remote_search_query: Optional[TrailerInfoRemoteSearchQuery] = None
    trakt_episode: Optional[TraktEpisode] = None
    trakt_episode_id: Optional[TraktEpisodeIDClass] = None
    trakt_movie: Optional[TraktMovie] = None
    trakt_movie_id: Optional[TraktMovieIDClass] = None
    trakt_person: Optional[TraktPerson] = None
    trakt_person_id: Optional[TraktPersonIDClass] = None
    trakt_season: Optional[TraktSeason] = None
    trakt_season_id: Optional[TraktSeasonIDClass] = None
    trakt_show: Optional[TraktShow] = None
    trakt_show_id: Optional[TraktShowIDClass] = None
    trakt_sync_response: Optional[TraktSyncResponse] = None
    transcode_reason: Optional[TranscodeReason] = None
    transcode_seek_info: Optional[TranscodeSeekInfo] = None
    transcoding_info: Optional[TranscodingInfo] = None
    transcoding_profile: Optional[TranscodingProfile] = None
    transport_stream_timestamp: Optional[Timestamp] = None
    tuner_channel_mapping: Optional[TunerChannelMapping] = None
    tuner_host_info: Optional[TunerHostInfo] = None
    type_options: Optional[TypeOptions] = None
    unrated_item: Optional[UnratedItem] = None
    update_library_options_dto: Optional[UpdateLibraryOptionsDto] = None
    update_media_path_request_dto: Optional[UpdateMediaPathRequestDto] = None
    update_user_easy_password: Optional[UpdateUserEasyPassword] = None
    update_user_password: Optional[UpdateUserPassword] = None
    upload_subtitle_dto: Optional[UploadSubtitleDto] = None
    user_configuration: Optional[Configuration] = None
    user_dto: Optional[UserDtoClass] = None
    user_item_data_dto: Optional[User] = None
    user_policy: Optional[Policy] = None
    utc_time_response: Optional[UTCTimeResponse] = None
    validate_path_dto: Optional[ValidatePathDto] = None
    version: Optional[VersionNumber] = None
    version_info: Optional[VersionInfo] = None
    video3_d_format: Optional[Video3DFormat] = None
    video_type: Optional[VideoType] = None
    virtual_folder_info: Optional[VirtualFolderInfo] = None
    wake_on_lan_info: Optional[WakeOnLANInfo] = None
    xml_attribute: Optional[XMLAttribute] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataAll':
        assert isinstance(obj, dict)
        access_schedule = from_union([AccessSchedule.from_dict, from_none], obj.get("AccessSchedule"))
        activity_log_entry = from_union([ActivityLogEntry.from_dict, from_none], obj.get("ActivityLogEntry"))
        activity_log_entry_query_result = from_union([ActivityLogEntryQueryResult.from_dict, from_none], obj.get("ActivityLogEntryQueryResult"))
        add_virtual_folder_dto = from_union([AddVirtualFolderDto.from_dict, from_none], obj.get("AddVirtualFolderDto"))
        admin_notification_dto = from_union([AdminNotificationDto.from_dict, from_none], obj.get("AdminNotificationDto"))
        album_info = from_union([AlbumInfoClass.from_dict, from_none], obj.get("AlbumInfo"))
        album_info_remote_search_query = from_union([AlbumInfoRemoteSearchQuery.from_dict, from_none], obj.get("AlbumInfoRemoteSearchQuery"))
        all_theme_media_result = from_union([AllThemeMediaResult.from_dict, from_none], obj.get("AllThemeMediaResult"))
        architecture = from_union([Architecture, from_none], obj.get("Architecture"))
        artist_info = from_union([ArtistInfoClass.from_dict, from_none], obj.get("ArtistInfo"))
        artist_info_remote_search_query = from_union([ArtistInfoRemoteSearchQuery.from_dict, from_none], obj.get("ArtistInfoRemoteSearchQuery"))
        authenticate_user_by_name = from_union([AuthenticateUserByName.from_dict, from_none], obj.get("AuthenticateUserByName"))
        authentication_info = from_union([AuthenticationInfo.from_dict, from_none], obj.get("AuthenticationInfo"))
        authentication_info_query_result = from_union([AuthenticationInfoQueryResult.from_dict, from_none], obj.get("AuthenticationInfoQueryResult"))
        authentication_result = from_union([AuthenticationResult.from_dict, from_none], obj.get("AuthenticationResult"))
        base_item = from_union([Item.from_dict, from_none], obj.get("BaseItem"))
        base_item_dto = from_union([BaseItemDto.from_dict, from_none], obj.get("BaseItemDto"))
        base_item_dto_query_result = from_union([BaseItemDtoQueryResult.from_dict, from_none], obj.get("BaseItemDtoQueryResult"))
        base_item_person = from_union([BaseItemPerson.from_dict, from_none], obj.get("BaseItemPerson"))
        base_plugin_configuration = from_union([BasePluginConfiguration.from_dict, from_none], obj.get("BasePluginConfiguration"))
        book_info = from_union([BookInfoClass.from_dict, from_none], obj.get("BookInfo"))
        book_info_remote_search_query = from_union([BookInfoRemoteSearchQuery.from_dict, from_none], obj.get("BookInfoRemoteSearchQuery"))
        box_set_info = from_union([BoxSetInfoClass.from_dict, from_none], obj.get("BoxSetInfo"))
        box_set_info_remote_search_query = from_union([BoxSetInfoRemoteSearchQuery.from_dict, from_none], obj.get("BoxSetInfoRemoteSearchQuery"))
        branding_options = from_union([BrandingOptions.from_dict, from_none], obj.get("BrandingOptions"))
        buffer_request_dto = from_union([BufferRequestDto.from_dict, from_none], obj.get("BufferRequestDto"))
        channel_features = from_union([ChannelFeatures.from_dict, from_none], obj.get("ChannelFeatures"))
        channel_item_sort_field = from_union([ChannelItemSortField, from_none], obj.get("ChannelItemSortField"))
        channel_mapping_options_dto = from_union([ChannelMappingOptionsDto.from_dict, from_none], obj.get("ChannelMappingOptionsDto"))
        channel_media_content_type = from_union([ChannelMediaContentType, from_none], obj.get("ChannelMediaContentType"))
        channel_media_type = from_union([ChannelMediaTypeElement, from_none], obj.get("ChannelMediaType"))
        channel_type = from_union([ChannelType, from_none], obj.get("ChannelType"))
        chapter_info = from_union([ChapterInfo.from_dict, from_none], obj.get("ChapterInfo"))
        client_capabilities = from_union([Capabilities.from_dict, from_none], obj.get("ClientCapabilities"))
        client_capabilities_dto = from_union([ClientCapabilitiesDto.from_dict, from_none], obj.get("ClientCapabilitiesDto"))
        codec_profile = from_union([CodecProfile.from_dict, from_none], obj.get("CodecProfile"))
        codec_type = from_union([CodecTypeEnum, from_none], obj.get("CodecType"))
        collection_creation_result = from_union([CollectionCreationResult.from_dict, from_none], obj.get("CollectionCreationResult"))
        collection_type_options = from_union([CollectionType, from_none], obj.get("CollectionTypeOptions"))
        configuration_page_info = from_union([ConfigurationPageInfo.from_dict, from_none], obj.get("ConfigurationPageInfo"))
        configuration_page_type = from_union([ConfigurationPageType, from_none], obj.get("ConfigurationPageType"))
        container_profile = from_union([ContainerProfile.from_dict, from_none], obj.get("ContainerProfile"))
        control_response = from_union([ControlResponse.from_dict, from_none], obj.get("ControlResponse"))
        country_info = from_union([CountryInfo.from_dict, from_none], obj.get("CountryInfo"))
        create_playlist_dto = from_union([CreatePlaylistDto.from_dict, from_none], obj.get("CreatePlaylistDto"))
        create_user_by_name = from_union([CreateUserByName.from_dict, from_none], obj.get("CreateUserByName"))
        culture_dto = from_union([CultureDto.from_dict, from_none], obj.get("CultureDto"))
        custom_query_data = from_union([CustomQueryData.from_dict, from_none], obj.get("CustomQueryData"))
        day_of_week = from_union([DayOfWeekElement, from_none], obj.get("DayOfWeek"))
        day_pattern = from_union([DayPattern, from_none], obj.get("DayPattern"))
        default_directory_browser_info_dto = from_union([DefaultDirectoryBrowserInfoDto.from_dict, from_none], obj.get("DefaultDirectoryBrowserInfoDto"))
        device_identification = from_union([Identification.from_dict, from_none], obj.get("DeviceIdentification"))
        device_info = from_union([DeviceInfo.from_dict, from_none], obj.get("DeviceInfo"))
        device_info_query_result = from_union([DeviceInfoQueryResult.from_dict, from_none], obj.get("DeviceInfoQueryResult"))
        device_options = from_union([DeviceOptions.from_dict, from_none], obj.get("DeviceOptions"))
        device_profile = from_union([DeviceProfile.from_dict, from_none], obj.get("DeviceProfile"))
        device_profile_info = from_union([DeviceProfileInfo.from_dict, from_none], obj.get("DeviceProfileInfo"))
        device_profile_type = from_union([DeviceProfileTypeEnum, from_none], obj.get("DeviceProfileType"))
        direct_play_profile = from_union([DirectPlayProfile.from_dict, from_none], obj.get("DirectPlayProfile"))
        display_preferences_dto = from_union([DisplayPreferencesDto.from_dict, from_none], obj.get("DisplayPreferencesDto"))
        dlna_profile_type = from_union([ChannelMediaTypeElement, from_none], obj.get("DlnaProfileType"))
        dynamic_day_of_week = from_union([DayOfWeek, from_none], obj.get("DynamicDayOfWeek"))
        encoding_context = from_union([Context, from_none], obj.get("EncodingContext"))
        end_point_info = from_union([EndPointInfo.from_dict, from_none], obj.get("EndPointInfo"))
        external_id_info = from_union([ExternalIDInfo.from_dict, from_none], obj.get("ExternalIdInfo"))
        external_id_media_type = from_union([ExternalIDMediaTypeEnum, from_none], obj.get("ExternalIdMediaType"))
        external_url = from_union([ExternalURL.from_dict, from_none], obj.get("ExternalUrl"))
        f_fmpeg_location = from_union([Location, from_none], obj.get("FFmpegLocation"))
        file_organization_result = from_union([FileOrganizationResult.from_dict, from_none], obj.get("FileOrganizationResult"))
        file_organization_result_query_result = from_union([FileOrganizationResultQueryResult.from_dict, from_none], obj.get("FileOrganizationResultQueryResult"))
        file_organizer_type = from_union([FileOrganizerTypeEnum, from_none], obj.get("FileOrganizerType"))
        file_sorting_status = from_union([FileSortingStatusEnum, from_none], obj.get("FileSortingStatus"))
        file_system_entry_info = from_union([FileSystemEntryInfo.from_dict, from_none], obj.get("FileSystemEntryInfo"))
        file_system_entry_type = from_union([FileSystemEntryTypeEnum, from_none], obj.get("FileSystemEntryType"))
        font_file = from_union([FontFile.from_dict, from_none], obj.get("FontFile"))
        forgot_password_action = from_union([Action, from_none], obj.get("ForgotPasswordAction"))
        forgot_password_dto = from_union([ForgotPasswordDto.from_dict, from_none], obj.get("ForgotPasswordDto"))
        forgot_password_pin_dto = from_union([ForgotPasswordPinDto.from_dict, from_none], obj.get("ForgotPasswordPinDto"))
        forgot_password_result = from_union([ForgotPasswordResult.from_dict, from_none], obj.get("ForgotPasswordResult"))
        general_command = from_union([GeneralCommand.from_dict, from_none], obj.get("GeneralCommand"))
        general_command_type = from_union([GeneralCommandType, from_none], obj.get("GeneralCommandType"))
        get_programs_dto = from_union([GetProgramsDto.from_dict, from_none], obj.get("GetProgramsDto"))
        group_info_dto = from_union([GroupInfoDto.from_dict, from_none], obj.get("GroupInfoDto"))
        group_queue_mode = from_union([GroupQueueModeEnum, from_none], obj.get("GroupQueueMode"))
        group_repeat_mode = from_union([GroupRepeatModeEnum, from_none], obj.get("GroupRepeatMode"))
        group_shuffle_mode = from_union([GroupShuffleModeEnum, from_none], obj.get("GroupShuffleMode"))
        group_state_type = from_union([GroupStateTypeEnum, from_none], obj.get("GroupStateType"))
        group_update_type = from_union([GroupUpdateTypeEnum, from_none], obj.get("GroupUpdateType"))
        guide_info = from_union([GuideInfo.from_dict, from_none], obj.get("GuideInfo"))
        header_match_type = from_union([Match, from_none], obj.get("HeaderMatchType"))
        header_metadata = from_union([HeaderMetadata, from_none], obj.get("HeaderMetadata"))
        http_header_info = from_union([HTTPHeaderInfo.from_dict, from_none], obj.get("HttpHeaderInfo"))
        ignore_wait_request_dto = from_union([IgnoreWaitRequestDto.from_dict, from_none], obj.get("IgnoreWaitRequestDto"))
        image_by_name_info = from_union([ImageByNameInfo.from_dict, from_none], obj.get("ImageByNameInfo"))
        image_format = from_union([ImageFormat, from_none], obj.get("ImageFormat"))
        image_info = from_union([ImageInfo.from_dict, from_none], obj.get("ImageInfo"))
        image_option = from_union([ImageOption.from_dict, from_none], obj.get("ImageOption"))
        image_orientation = from_union([ImageOrientation, from_none], obj.get("ImageOrientation"))
        image_provider_info = from_union([ImageProviderInfo.from_dict, from_none], obj.get("ImageProviderInfo"))
        image_saving_convention = from_union([ImageSavingConvention, from_none], obj.get("ImageSavingConvention"))
        image_type = from_union([ImageTypeElement, from_none], obj.get("ImageType"))
        installation_info = from_union([InstallationInfo.from_dict, from_none], obj.get("InstallationInfo"))
        i_plugin = from_union([IPlugin.from_dict, from_none], obj.get("IPlugin"))
        iso_type = from_union([ISOType, from_none], obj.get("IsoType"))
        item_counts = from_union([ItemCounts.from_dict, from_none], obj.get("ItemCounts"))
        item_fields = from_union([ItemFields, from_none], obj.get("ItemFields"))
        item_filter = from_union([ItemFilter, from_none], obj.get("ItemFilter"))
        items = from_union([Items.from_dict, from_none], obj.get("Items"))
        item_view_type = from_union([ItemViewType, from_none], obj.get("ItemViewType"))
        join_group_request_dto = from_union([JoinGroupRequestDto.from_dict, from_none], obj.get("JoinGroupRequestDto"))
        keep_until = from_union([KeepUntil, from_none], obj.get("KeepUntil"))
        library_option_info_dto = from_union([LibraryOptionInfoDto.from_dict, from_none], obj.get("LibraryOptionInfoDto"))
        library_options = from_union([LibraryOptions.from_dict, from_none], obj.get("LibraryOptions"))
        library_options_result_dto = from_union([LibraryOptionsResultDto.from_dict, from_none], obj.get("LibraryOptionsResultDto"))
        library_type_options_dto = from_union([LibraryTypeOptionsDto.from_dict, from_none], obj.get("LibraryTypeOptionsDto"))
        library_update_info = from_union([LibraryUpdateInfo.from_dict, from_none], obj.get("LibraryUpdateInfo"))
        listings_provider_info = from_union([ListingsProviderInfo.from_dict, from_none], obj.get("ListingsProviderInfo"))
        live_stream_response = from_union([LiveStreamResponse.from_dict, from_none], obj.get("LiveStreamResponse"))
        live_tv_info = from_union([LiveTvInfo.from_dict, from_none], obj.get("LiveTvInfo"))
        live_tv_service_info = from_union([LiveTvServiceInfo.from_dict, from_none], obj.get("LiveTvServiceInfo"))
        live_tv_service_status = from_union([LiveTvServiceStatusEnum, from_none], obj.get("LiveTvServiceStatus"))
        localization_option = from_union([LocalizationOption.from_dict, from_none], obj.get("LocalizationOption"))
        location_type = from_union([LocationType, from_none], obj.get("LocationType"))
        log_file = from_union([LogFile.from_dict, from_none], obj.get("LogFile"))
        log_level = from_union([Severity, from_none], obj.get("LogLevel"))
        media_attachment = from_union([MediaAttachment.from_dict, from_none], obj.get("MediaAttachment"))
        media_encoder_path_dto = from_union([MediaEncoderPathDto.from_dict, from_none], obj.get("MediaEncoderPathDto"))
        media_path_dto = from_union([MediaPathDto.from_dict, from_none], obj.get("MediaPathDto"))
        media_path_info = from_union([PathInfo.from_dict, from_none], obj.get("MediaPathInfo"))
        media_protocol = from_union([Protocol, from_none], obj.get("MediaProtocol"))
        media_source_info = from_union([MediaSource.from_dict, from_none], obj.get("MediaSourceInfo"))
        media_source_type = from_union([MediaSourceTypeEnum, from_none], obj.get("MediaSourceType"))
        media_stream = from_union([MediaStream.from_dict, from_none], obj.get("MediaStream"))
        media_stream_type = from_union([MediaStreamTypeEnum, from_none], obj.get("MediaStreamType"))
        media_update_info_dto = from_union([MediaUpdateInfoDto.from_dict, from_none], obj.get("MediaUpdateInfoDto"))
        media_update_info_path_dto = from_union([MediaUpdateInfoPathDto.from_dict, from_none], obj.get("MediaUpdateInfoPathDto"))
        media_url = from_union([MediaURL.from_dict, from_none], obj.get("MediaUrl"))
        message_command = from_union([MessageCommand.from_dict, from_none], obj.get("MessageCommand"))
        metadata_editor_info = from_union([MetadataEditorInfo.from_dict, from_none], obj.get("MetadataEditorInfo"))
        metadata_field = from_union([MetadataField, from_none], obj.get("MetadataField"))
        metadata_options = from_union([MetadataOptions.from_dict, from_none], obj.get("MetadataOptions"))
        metadata_refresh_mode = from_union([MetadataRefreshMode, from_none], obj.get("MetadataRefreshMode"))
        move_playlist_item_request_dto = from_union([MovePlaylistItemRequestDto.from_dict, from_none], obj.get("MovePlaylistItemRequestDto"))
        movie_info = from_union([MovieInfoClass.from_dict, from_none], obj.get("MovieInfo"))
        movie_info_remote_search_query = from_union([MovieInfoRemoteSearchQuery.from_dict, from_none], obj.get("MovieInfoRemoteSearchQuery"))
        music_video_info = from_union([MusicVideoInfoClass.from_dict, from_none], obj.get("MusicVideoInfo"))
        music_video_info_remote_search_query = from_union([MusicVideoInfoRemoteSearchQuery.from_dict, from_none], obj.get("MusicVideoInfoRemoteSearchQuery"))
        name_guid_pair = from_union([NameGUIDPair.from_dict, from_none], obj.get("NameGuidPair"))
        name_id_pair = from_union([NameIDPair.from_dict, from_none], obj.get("NameIdPair"))
        name_value_pair = from_union([NameValuePair.from_dict, from_none], obj.get("NameValuePair"))
        new_group_request_dto = from_union([NewGroupRequestDto.from_dict, from_none], obj.get("NewGroupRequestDto"))
        next_item_request_dto = from_union([NextItemRequestDto.from_dict, from_none], obj.get("NextItemRequestDto"))
        not_found_objects = from_union([NotFound.from_dict, from_none], obj.get("NotFoundObjects"))
        notification_dto = from_union([NotificationDto.from_dict, from_none], obj.get("NotificationDto"))
        notification_level = from_union([Level, from_none], obj.get("NotificationLevel"))
        notification_result_dto = from_union([NotificationResultDto.from_dict, from_none], obj.get("NotificationResultDto"))
        notifications_summary_dto = from_union([NotificationsSummaryDto.from_dict, from_none], obj.get("NotificationsSummaryDto"))
        notification_type_info = from_union([NotificationTypeInfo.from_dict, from_none], obj.get("NotificationTypeInfo"))
        object_group_update = from_union([ObjectGroupUpdate.from_dict, from_none], obj.get("ObjectGroupUpdate"))
        open_live_stream_dto = from_union([OpenLiveStreamDto.from_dict, from_none], obj.get("OpenLiveStreamDto"))
        package_info = from_union([PackageInfo.from_dict, from_none], obj.get("PackageInfo"))
        parental_rating = from_union([ParentalRating.from_dict, from_none], obj.get("ParentalRating"))
        path_substitution = from_union([PathSubstitution.from_dict, from_none], obj.get("PathSubstitution"))
        person_lookup_info = from_union([PersonLookupInfoClass.from_dict, from_none], obj.get("PersonLookupInfo"))
        person_lookup_info_remote_search_query = from_union([PersonLookupInfoRemoteSearchQuery.from_dict, from_none], obj.get("PersonLookupInfoRemoteSearchQuery"))
        ping_request_dto = from_union([PingRequestDto.from_dict, from_none], obj.get("PingRequestDto"))
        pin_redeem_result = from_union([PinRedeemResult.from_dict, from_none], obj.get("PinRedeemResult"))
        play_access = from_union([PlayAccess, from_none], obj.get("PlayAccess"))
        playback_error_code = from_union([ErrorCode, from_none], obj.get("PlaybackErrorCode"))
        playback_info_dto = from_union([PlaybackInfoDto.from_dict, from_none], obj.get("PlaybackInfoDto"))
        playback_info_response = from_union([PlaybackInfoResponse.from_dict, from_none], obj.get("PlaybackInfoResponse"))
        playback_progress_info = from_union([PlaybackProgressInfo.from_dict, from_none], obj.get("PlaybackProgressInfo"))
        playback_start_info = from_union([PlaybackStartInfo.from_dict, from_none], obj.get("PlaybackStartInfo"))
        playback_stop_info = from_union([PlaybackStopInfo.from_dict, from_none], obj.get("PlaybackStopInfo"))
        play_command = from_union([PlayCommand, from_none], obj.get("PlayCommand"))
        player_state_info = from_union([Play.from_dict, from_none], obj.get("PlayerStateInfo"))
        playlist_creation_result = from_union([PlaylistCreationResult.from_dict, from_none], obj.get("PlaylistCreationResult"))
        play_method = from_union([PlayMethod, from_none], obj.get("PlayMethod"))
        play_request = from_union([PlayRequest.from_dict, from_none], obj.get("PlayRequest"))
        play_request_dto = from_union([PlayRequestDto.from_dict, from_none], obj.get("PlayRequestDto"))
        playstate_command = from_union([PlaystateCommandEnum, from_none], obj.get("PlaystateCommand"))
        playstate_request = from_union([PlaystateRequest.from_dict, from_none], obj.get("PlaystateRequest"))
        plugin_info = from_union([PluginInfo.from_dict, from_none], obj.get("PluginInfo"))
        plugin_security_info = from_union([PluginSecurityInfo.from_dict, from_none], obj.get("PluginSecurityInfo"))
        plugin_status = from_union([PluginStatusEnum, from_none], obj.get("PluginStatus"))
        previous_item_request_dto = from_union([PreviousItemRequestDto.from_dict, from_none], obj.get("PreviousItemRequestDto"))
        problem_details = from_union([ProblemDetails.from_dict, from_none], obj.get("ProblemDetails"))
        profile_condition = from_union([ProfileCondition.from_dict, from_none], obj.get("ProfileCondition"))
        profile_condition_type = from_union([Condition, from_none], obj.get("ProfileConditionType"))
        profile_condition_value = from_union([Pro, from_none], obj.get("ProfileConditionValue"))
        program_audio = from_union([Audio, from_none], obj.get("ProgramAudio"))
        public_system_info = from_union([PublicSystemInfo.from_dict, from_none], obj.get("PublicSystemInfo"))
        query_filters = from_union([QueryFilters.from_dict, from_none], obj.get("QueryFilters"))
        query_filters_legacy = from_union([QueryFiltersLegacy.from_dict, from_none], obj.get("QueryFiltersLegacy"))
        queue_item = from_union([QueueItem.from_dict, from_none], obj.get("QueueItem"))
        queue_request_dto = from_union([QueueRequestDto.from_dict, from_none], obj.get("QueueRequestDto"))
        quick_connect_dto = from_union([QuickConnectDto.from_dict, from_none], obj.get("QuickConnectDto"))
        quick_connect_result = from_union([QuickConnectResult.from_dict, from_none], obj.get("QuickConnectResult"))
        quick_connect_state = from_union([QuickConnectState, from_none], obj.get("QuickConnectState"))
        rating_type = from_union([RatingType, from_none], obj.get("RatingType"))
        ready_request_dto = from_union([ReadyRequestDto.from_dict, from_none], obj.get("ReadyRequestDto"))
        recommendation_dto = from_union([RecommendationDto.from_dict, from_none], obj.get("RecommendationDto"))
        recommendation_type = from_union([RecommendationType, from_none], obj.get("RecommendationType"))
        recording_status = from_union([RecordingStatusEnum, from_none], obj.get("RecordingStatus"))
        remote_image_info = from_union([RemoteImageInfo.from_dict, from_none], obj.get("RemoteImageInfo"))
        remote_image_result = from_union([RemoteImageResult.from_dict, from_none], obj.get("RemoteImageResult"))
        remote_search_result = from_union([RemoteSearchResult.from_dict, from_none], obj.get("RemoteSearchResult"))
        remote_subtitle_info = from_union([RemoteSubtitleInfo.from_dict, from_none], obj.get("RemoteSubtitleInfo"))
        remove_from_playlist_request_dto = from_union([RemoveFromPlaylistRequestDto.from_dict, from_none], obj.get("RemoveFromPlaylistRequestDto"))
        repeat_mode = from_union([GroupRepeatModeEnum, from_none], obj.get("RepeatMode"))
        report_display_type = from_union([DisplayType, from_none], obj.get("ReportDisplayType"))
        report_export_type = from_union([ReportExportType, from_none], obj.get("ReportExportType"))
        report_field_type = from_union([FieldType, from_none], obj.get("ReportFieldType"))
        report_group = from_union([ReportGroup.from_dict, from_none], obj.get("ReportGroup"))
        report_header = from_union([ReportHeader.from_dict, from_none], obj.get("ReportHeader"))
        report_include_item_types = from_union([RowType, from_none], obj.get("ReportIncludeItemTypes"))
        report_item = from_union([ReportItem.from_dict, from_none], obj.get("ReportItem"))
        report_result = from_union([ReportResult.from_dict, from_none], obj.get("ReportResult"))
        report_row = from_union([ReportRow.from_dict, from_none], obj.get("ReportRow"))
        repository_info = from_union([RepositoryInfo.from_dict, from_none], obj.get("RepositoryInfo"))
        response_profile = from_union([ResponseProfile.from_dict, from_none], obj.get("ResponseProfile"))
        scroll_direction = from_union([ScrollDirection, from_none], obj.get("ScrollDirection"))
        search_hint = from_union([SearchHint.from_dict, from_none], obj.get("SearchHint"))
        search_hint_result = from_union([SearchHintResult.from_dict, from_none], obj.get("SearchHintResult"))
        seek_request_dto = from_union([SeekRequestDto.from_dict, from_none], obj.get("SeekRequestDto"))
        send_command = from_union([SendCommand.from_dict, from_none], obj.get("SendCommand"))
        send_command_type = from_union([SendCommandTypeEnum, from_none], obj.get("SendCommandType"))
        series_info = from_union([SeriesInfoClass.from_dict, from_none], obj.get("SeriesInfo"))
        series_info_remote_search_query = from_union([SeriesInfoRemoteSearchQuery.from_dict, from_none], obj.get("SeriesInfoRemoteSearchQuery"))
        series_status = from_union([SeriesStatus, from_none], obj.get("SeriesStatus"))
        series_timer_info_dto = from_union([SeriesTimerInfoDto.from_dict, from_none], obj.get("SeriesTimerInfoDto"))
        series_timer_info_dto_query_result = from_union([SeriesTimerInfoDtoQueryResult.from_dict, from_none], obj.get("SeriesTimerInfoDtoQueryResult"))
        server_configuration = from_union([ServerConfiguration.from_dict, from_none], obj.get("ServerConfiguration"))
        server_discovery_info = from_union([ServerDiscoveryInfo.from_dict, from_none], obj.get("ServerDiscoveryInfo"))
        session_info = from_union([SessionInfo.from_dict, from_none], obj.get("SessionInfo"))
        session_message_type = from_union([SessionMessageType, from_none], obj.get("SessionMessageType"))
        session_user_info = from_union([SessionUserInfo.from_dict, from_none], obj.get("SessionUserInfo"))
        set_channel_mapping_dto = from_union([SetChannelMappingDto.from_dict, from_none], obj.get("SetChannelMappingDto"))
        set_playlist_item_request_dto = from_union([SetPlaylistItemRequestDto.from_dict, from_none], obj.get("SetPlaylistItemRequestDto"))
        set_repeat_mode_request_dto = from_union([SetRepeatModeRequestDto.from_dict, from_none], obj.get("SetRepeatModeRequestDto"))
        set_shuffle_mode_request_dto = from_union([SetShuffleModeRequestDto.from_dict, from_none], obj.get("SetShuffleModeRequestDto"))
        smart_match_result = from_union([SmartMatchResult.from_dict, from_none], obj.get("SmartMatchResult"))
        smart_match_result_query_result = from_union([SmartMatchResultQueryResult.from_dict, from_none], obj.get("SmartMatchResultQueryResult"))
        song_info = from_union([SongInfo.from_dict, from_none], obj.get("SongInfo"))
        sort_order = from_union([SortOrder, from_none], obj.get("SortOrder"))
        special_view_option_dto = from_union([SpecialViewOptionDto.from_dict, from_none], obj.get("SpecialViewOptionDto"))
        startup_configuration_dto = from_union([StartupConfigurationDto.from_dict, from_none], obj.get("StartupConfigurationDto"))
        startup_remote_access_dto = from_union([StartupRemoteAccessDto.from_dict, from_none], obj.get("StartupRemoteAccessDto"))
        startup_user_dto = from_union([StartupUserDto.from_dict, from_none], obj.get("StartupUserDto"))
        subtitle_delivery_method = from_union([Method, from_none], obj.get("SubtitleDeliveryMethod"))
        subtitle_playback_mode = from_union([SubtitleMode, from_none], obj.get("SubtitlePlaybackMode"))
        subtitle_profile = from_union([SubtitleProfile.from_dict, from_none], obj.get("SubtitleProfile"))
        sync_play_user_access_type = from_union([SyncPlay, from_none], obj.get("SyncPlayUserAccessType"))
        system_info = from_union([SystemInfo.from_dict, from_none], obj.get("SystemInfo"))
        task_completion_status = from_union([TaskCompletionStatusEnum, from_none], obj.get("TaskCompletionStatus"))
        task_info = from_union([TaskInfo.from_dict, from_none], obj.get("TaskInfo"))
        task_result = from_union([TaskResultClass.from_dict, from_none], obj.get("TaskResult"))
        task_state = from_union([TaskStateEnum, from_none], obj.get("TaskState"))
        task_trigger_info = from_union([TaskTriggerInfo.from_dict, from_none], obj.get("TaskTriggerInfo"))
        theme_media_result = from_union([ThemeMediaResultClass.from_dict, from_none], obj.get("ThemeMediaResult"))
        timer_event_info = from_union([TimerEventInfo.from_dict, from_none], obj.get("TimerEventInfo"))
        timer_info_dto = from_union([TimerInfoDto.from_dict, from_none], obj.get("TimerInfoDto"))
        timer_info_dto_query_result = from_union([TimerInfoDtoQueryResult.from_dict, from_none], obj.get("TimerInfoDtoQueryResult"))
        trailer_info = from_union([TrailerInfoClass.from_dict, from_none], obj.get("TrailerInfo"))
        trailer_info_remote_search_query = from_union([TrailerInfoRemoteSearchQuery.from_dict, from_none], obj.get("TrailerInfoRemoteSearchQuery"))
        trakt_episode = from_union([TraktEpisode.from_dict, from_none], obj.get("TraktEpisode"))
        trakt_episode_id = from_union([TraktEpisodeIDClass.from_dict, from_none], obj.get("TraktEpisodeId"))
        trakt_movie = from_union([TraktMovie.from_dict, from_none], obj.get("TraktMovie"))
        trakt_movie_id = from_union([TraktMovieIDClass.from_dict, from_none], obj.get("TraktMovieId"))
        trakt_person = from_union([TraktPerson.from_dict, from_none], obj.get("TraktPerson"))
        trakt_person_id = from_union([TraktPersonIDClass.from_dict, from_none], obj.get("TraktPersonId"))
        trakt_season = from_union([TraktSeason.from_dict, from_none], obj.get("TraktSeason"))
        trakt_season_id = from_union([TraktSeasonIDClass.from_dict, from_none], obj.get("TraktSeasonId"))
        trakt_show = from_union([TraktShow.from_dict, from_none], obj.get("TraktShow"))
        trakt_show_id = from_union([TraktShowIDClass.from_dict, from_none], obj.get("TraktShowId"))
        trakt_sync_response = from_union([TraktSyncResponse.from_dict, from_none], obj.get("TraktSyncResponse"))
        transcode_reason = from_union([TranscodeReason, from_none], obj.get("TranscodeReason"))
        transcode_seek_info = from_union([TranscodeSeekInfo, from_none], obj.get("TranscodeSeekInfo"))
        transcoding_info = from_union([TranscodingInfo.from_dict, from_none], obj.get("TranscodingInfo"))
        transcoding_profile = from_union([TranscodingProfile.from_dict, from_none], obj.get("TranscodingProfile"))
        transport_stream_timestamp = from_union([Timestamp, from_none], obj.get("TransportStreamTimestamp"))
        tuner_channel_mapping = from_union([TunerChannelMapping.from_dict, from_none], obj.get("TunerChannelMapping"))
        tuner_host_info = from_union([TunerHostInfo.from_dict, from_none], obj.get("TunerHostInfo"))
        type_options = from_union([TypeOptions.from_dict, from_none], obj.get("TypeOptions"))
        unrated_item = from_union([UnratedItem, from_none], obj.get("UnratedItem"))
        update_library_options_dto = from_union([UpdateLibraryOptionsDto.from_dict, from_none], obj.get("UpdateLibraryOptionsDto"))
        update_media_path_request_dto = from_union([UpdateMediaPathRequestDto.from_dict, from_none], obj.get("UpdateMediaPathRequestDto"))
        update_user_easy_password = from_union([UpdateUserEasyPassword.from_dict, from_none], obj.get("UpdateUserEasyPassword"))
        update_user_password = from_union([UpdateUserPassword.from_dict, from_none], obj.get("UpdateUserPassword"))
        upload_subtitle_dto = from_union([UploadSubtitleDto.from_dict, from_none], obj.get("UploadSubtitleDto"))
        user_configuration = from_union([Configuration.from_dict, from_none], obj.get("UserConfiguration"))
        user_dto = from_union([UserDtoClass.from_dict, from_none], obj.get("UserDto"))
        user_item_data_dto = from_union([User.from_dict, from_none], obj.get("UserItemDataDto"))
        user_policy = from_union([Policy.from_dict, from_none], obj.get("UserPolicy"))
        utc_time_response = from_union([UTCTimeResponse.from_dict, from_none], obj.get("UtcTimeResponse"))
        validate_path_dto = from_union([ValidatePathDto.from_dict, from_none], obj.get("ValidatePathDto"))
        version = from_union([VersionNumber.from_dict, from_none], obj.get("Version"))
        version_info = from_union([VersionInfo.from_dict, from_none], obj.get("VersionInfo"))
        video3_d_format = from_union([Video3DFormat, from_none], obj.get("Video3DFormat"))
        video_type = from_union([VideoType, from_none], obj.get("VideoType"))
        virtual_folder_info = from_union([VirtualFolderInfo.from_dict, from_none], obj.get("VirtualFolderInfo"))
        wake_on_lan_info = from_union([WakeOnLANInfo.from_dict, from_none], obj.get("WakeOnLanInfo"))
        xml_attribute = from_union([XMLAttribute.from_dict, from_none], obj.get("XmlAttribute"))
        return DataAll(access_schedule, activity_log_entry, activity_log_entry_query_result, add_virtual_folder_dto, admin_notification_dto, album_info, album_info_remote_search_query, all_theme_media_result, architecture, artist_info, artist_info_remote_search_query, authenticate_user_by_name, authentication_info, authentication_info_query_result, authentication_result, base_item, base_item_dto, base_item_dto_query_result, base_item_person, base_plugin_configuration, book_info, book_info_remote_search_query, box_set_info, box_set_info_remote_search_query, branding_options, buffer_request_dto, channel_features, channel_item_sort_field, channel_mapping_options_dto, channel_media_content_type, channel_media_type, channel_type, chapter_info, client_capabilities, client_capabilities_dto, codec_profile, codec_type, collection_creation_result, collection_type_options, configuration_page_info, configuration_page_type, container_profile, control_response, country_info, create_playlist_dto, create_user_by_name, culture_dto, custom_query_data, day_of_week, day_pattern, default_directory_browser_info_dto, device_identification, device_info, device_info_query_result, device_options, device_profile, device_profile_info, device_profile_type, direct_play_profile, display_preferences_dto, dlna_profile_type, dynamic_day_of_week, encoding_context, end_point_info, external_id_info, external_id_media_type, external_url, f_fmpeg_location, file_organization_result, file_organization_result_query_result, file_organizer_type, file_sorting_status, file_system_entry_info, file_system_entry_type, font_file, forgot_password_action, forgot_password_dto, forgot_password_pin_dto, forgot_password_result, general_command, general_command_type, get_programs_dto, group_info_dto, group_queue_mode, group_repeat_mode, group_shuffle_mode, group_state_type, group_update_type, guide_info, header_match_type, header_metadata, http_header_info, ignore_wait_request_dto, image_by_name_info, image_format, image_info, image_option, image_orientation, image_provider_info, image_saving_convention, image_type, installation_info, i_plugin, iso_type, item_counts, item_fields, item_filter, items, item_view_type, join_group_request_dto, keep_until, library_option_info_dto, library_options, library_options_result_dto, library_type_options_dto, library_update_info, listings_provider_info, live_stream_response, live_tv_info, live_tv_service_info, live_tv_service_status, localization_option, location_type, log_file, log_level, media_attachment, media_encoder_path_dto, media_path_dto, media_path_info, media_protocol, media_source_info, media_source_type, media_stream, media_stream_type, media_update_info_dto, media_update_info_path_dto, media_url, message_command, metadata_editor_info, metadata_field, metadata_options, metadata_refresh_mode, move_playlist_item_request_dto, movie_info, movie_info_remote_search_query, music_video_info, music_video_info_remote_search_query, name_guid_pair, name_id_pair, name_value_pair, new_group_request_dto, next_item_request_dto, not_found_objects, notification_dto, notification_level, notification_result_dto, notifications_summary_dto, notification_type_info, object_group_update, open_live_stream_dto, package_info, parental_rating, path_substitution, person_lookup_info, person_lookup_info_remote_search_query, ping_request_dto, pin_redeem_result, play_access, playback_error_code, playback_info_dto, playback_info_response, playback_progress_info, playback_start_info, playback_stop_info, play_command, player_state_info, playlist_creation_result, play_method, play_request, play_request_dto, playstate_command, playstate_request, plugin_info, plugin_security_info, plugin_status, previous_item_request_dto, problem_details, profile_condition, profile_condition_type, profile_condition_value, program_audio, public_system_info, query_filters, query_filters_legacy, queue_item, queue_request_dto, quick_connect_dto, quick_connect_result, quick_connect_state, rating_type, ready_request_dto, recommendation_dto, recommendation_type, recording_status, remote_image_info, remote_image_result, remote_search_result, remote_subtitle_info, remove_from_playlist_request_dto, repeat_mode, report_display_type, report_export_type, report_field_type, report_group, report_header, report_include_item_types, report_item, report_result, report_row, repository_info, response_profile, scroll_direction, search_hint, search_hint_result, seek_request_dto, send_command, send_command_type, series_info, series_info_remote_search_query, series_status, series_timer_info_dto, series_timer_info_dto_query_result, server_configuration, server_discovery_info, session_info, session_message_type, session_user_info, set_channel_mapping_dto, set_playlist_item_request_dto, set_repeat_mode_request_dto, set_shuffle_mode_request_dto, smart_match_result, smart_match_result_query_result, song_info, sort_order, special_view_option_dto, startup_configuration_dto, startup_remote_access_dto, startup_user_dto, subtitle_delivery_method, subtitle_playback_mode, subtitle_profile, sync_play_user_access_type, system_info, task_completion_status, task_info, task_result, task_state, task_trigger_info, theme_media_result, timer_event_info, timer_info_dto, timer_info_dto_query_result, trailer_info, trailer_info_remote_search_query, trakt_episode, trakt_episode_id, trakt_movie, trakt_movie_id, trakt_person, trakt_person_id, trakt_season, trakt_season_id, trakt_show, trakt_show_id, trakt_sync_response, transcode_reason, transcode_seek_info, transcoding_info, transcoding_profile, transport_stream_timestamp, tuner_channel_mapping, tuner_host_info, type_options, unrated_item, update_library_options_dto, update_media_path_request_dto, update_user_easy_password, update_user_password, upload_subtitle_dto, user_configuration, user_dto, user_item_data_dto, user_policy, utc_time_response, validate_path_dto, version, version_info, video3_d_format, video_type, virtual_folder_info, wake_on_lan_info, xml_attribute)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AccessSchedule"] = from_union([lambda x: to_class(AccessSchedule, x), from_none], self.access_schedule)
        result["ActivityLogEntry"] = from_union([lambda x: to_class(ActivityLogEntry, x), from_none], self.activity_log_entry)
        result["ActivityLogEntryQueryResult"] = from_union([lambda x: to_class(ActivityLogEntryQueryResult, x), from_none], self.activity_log_entry_query_result)
        result["AddVirtualFolderDto"] = from_union([lambda x: to_class(AddVirtualFolderDto, x), from_none], self.add_virtual_folder_dto)
        result["AdminNotificationDto"] = from_union([lambda x: to_class(AdminNotificationDto, x), from_none], self.admin_notification_dto)
        result["AlbumInfo"] = from_union([lambda x: to_class(AlbumInfoClass, x), from_none], self.album_info)
        result["AlbumInfoRemoteSearchQuery"] = from_union([lambda x: to_class(AlbumInfoRemoteSearchQuery, x), from_none], self.album_info_remote_search_query)
        result["AllThemeMediaResult"] = from_union([lambda x: to_class(AllThemeMediaResult, x), from_none], self.all_theme_media_result)
        result["Architecture"] = from_union([lambda x: to_enum(Architecture, x), from_none], self.architecture)
        result["ArtistInfo"] = from_union([lambda x: to_class(ArtistInfoClass, x), from_none], self.artist_info)
        result["ArtistInfoRemoteSearchQuery"] = from_union([lambda x: to_class(ArtistInfoRemoteSearchQuery, x), from_none], self.artist_info_remote_search_query)
        result["AuthenticateUserByName"] = from_union([lambda x: to_class(AuthenticateUserByName, x), from_none], self.authenticate_user_by_name)
        result["AuthenticationInfo"] = from_union([lambda x: to_class(AuthenticationInfo, x), from_none], self.authentication_info)
        result["AuthenticationInfoQueryResult"] = from_union([lambda x: to_class(AuthenticationInfoQueryResult, x), from_none], self.authentication_info_query_result)
        result["AuthenticationResult"] = from_union([lambda x: to_class(AuthenticationResult, x), from_none], self.authentication_result)
        result["BaseItem"] = from_union([lambda x: to_class(Item, x), from_none], self.base_item)
        result["BaseItemDto"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.base_item_dto)
        result["BaseItemDtoQueryResult"] = from_union([lambda x: to_class(BaseItemDtoQueryResult, x), from_none], self.base_item_dto_query_result)
        result["BaseItemPerson"] = from_union([lambda x: to_class(BaseItemPerson, x), from_none], self.base_item_person)
        result["BasePluginConfiguration"] = from_union([lambda x: to_class(BasePluginConfiguration, x), from_none], self.base_plugin_configuration)
        result["BookInfo"] = from_union([lambda x: to_class(BookInfoClass, x), from_none], self.book_info)
        result["BookInfoRemoteSearchQuery"] = from_union([lambda x: to_class(BookInfoRemoteSearchQuery, x), from_none], self.book_info_remote_search_query)
        result["BoxSetInfo"] = from_union([lambda x: to_class(BoxSetInfoClass, x), from_none], self.box_set_info)
        result["BoxSetInfoRemoteSearchQuery"] = from_union([lambda x: to_class(BoxSetInfoRemoteSearchQuery, x), from_none], self.box_set_info_remote_search_query)
        result["BrandingOptions"] = from_union([lambda x: to_class(BrandingOptions, x), from_none], self.branding_options)
        result["BufferRequestDto"] = from_union([lambda x: to_class(BufferRequestDto, x), from_none], self.buffer_request_dto)
        result["ChannelFeatures"] = from_union([lambda x: to_class(ChannelFeatures, x), from_none], self.channel_features)
        result["ChannelItemSortField"] = from_union([lambda x: to_enum(ChannelItemSortField, x), from_none], self.channel_item_sort_field)
        result["ChannelMappingOptionsDto"] = from_union([lambda x: to_class(ChannelMappingOptionsDto, x), from_none], self.channel_mapping_options_dto)
        result["ChannelMediaContentType"] = from_union([lambda x: to_enum(ChannelMediaContentType, x), from_none], self.channel_media_content_type)
        result["ChannelMediaType"] = from_union([lambda x: to_enum(ChannelMediaTypeElement, x), from_none], self.channel_media_type)
        result["ChannelType"] = from_union([lambda x: to_enum(ChannelType, x), from_none], self.channel_type)
        result["ChapterInfo"] = from_union([lambda x: to_class(ChapterInfo, x), from_none], self.chapter_info)
        result["ClientCapabilities"] = from_union([lambda x: to_class(Capabilities, x), from_none], self.client_capabilities)
        result["ClientCapabilitiesDto"] = from_union([lambda x: to_class(ClientCapabilitiesDto, x), from_none], self.client_capabilities_dto)
        result["CodecProfile"] = from_union([lambda x: to_class(CodecProfile, x), from_none], self.codec_profile)
        result["CodecType"] = from_union([lambda x: to_enum(CodecTypeEnum, x), from_none], self.codec_type)
        result["CollectionCreationResult"] = from_union([lambda x: to_class(CollectionCreationResult, x), from_none], self.collection_creation_result)
        result["CollectionTypeOptions"] = from_union([lambda x: to_enum(CollectionType, x), from_none], self.collection_type_options)
        result["ConfigurationPageInfo"] = from_union([lambda x: to_class(ConfigurationPageInfo, x), from_none], self.configuration_page_info)
        result["ConfigurationPageType"] = from_union([lambda x: to_enum(ConfigurationPageType, x), from_none], self.configuration_page_type)
        result["ContainerProfile"] = from_union([lambda x: to_class(ContainerProfile, x), from_none], self.container_profile)
        result["ControlResponse"] = from_union([lambda x: to_class(ControlResponse, x), from_none], self.control_response)
        result["CountryInfo"] = from_union([lambda x: to_class(CountryInfo, x), from_none], self.country_info)
        result["CreatePlaylistDto"] = from_union([lambda x: to_class(CreatePlaylistDto, x), from_none], self.create_playlist_dto)
        result["CreateUserByName"] = from_union([lambda x: to_class(CreateUserByName, x), from_none], self.create_user_by_name)
        result["CultureDto"] = from_union([lambda x: to_class(CultureDto, x), from_none], self.culture_dto)
        result["CustomQueryData"] = from_union([lambda x: to_class(CustomQueryData, x), from_none], self.custom_query_data)
        result["DayOfWeek"] = from_union([lambda x: to_enum(DayOfWeekElement, x), from_none], self.day_of_week)
        result["DayPattern"] = from_union([lambda x: to_enum(DayPattern, x), from_none], self.day_pattern)
        result["DefaultDirectoryBrowserInfoDto"] = from_union([lambda x: to_class(DefaultDirectoryBrowserInfoDto, x), from_none], self.default_directory_browser_info_dto)
        result["DeviceIdentification"] = from_union([lambda x: to_class(Identification, x), from_none], self.device_identification)
        result["DeviceInfo"] = from_union([lambda x: to_class(DeviceInfo, x), from_none], self.device_info)
        result["DeviceInfoQueryResult"] = from_union([lambda x: to_class(DeviceInfoQueryResult, x), from_none], self.device_info_query_result)
        result["DeviceOptions"] = from_union([lambda x: to_class(DeviceOptions, x), from_none], self.device_options)
        result["DeviceProfile"] = from_union([lambda x: to_class(DeviceProfile, x), from_none], self.device_profile)
        result["DeviceProfileInfo"] = from_union([lambda x: to_class(DeviceProfileInfo, x), from_none], self.device_profile_info)
        result["DeviceProfileType"] = from_union([lambda x: to_enum(DeviceProfileTypeEnum, x), from_none], self.device_profile_type)
        result["DirectPlayProfile"] = from_union([lambda x: to_class(DirectPlayProfile, x), from_none], self.direct_play_profile)
        result["DisplayPreferencesDto"] = from_union([lambda x: to_class(DisplayPreferencesDto, x), from_none], self.display_preferences_dto)
        result["DlnaProfileType"] = from_union([lambda x: to_enum(ChannelMediaTypeElement, x), from_none], self.dlna_profile_type)
        result["DynamicDayOfWeek"] = from_union([lambda x: to_enum(DayOfWeek, x), from_none], self.dynamic_day_of_week)
        result["EncodingContext"] = from_union([lambda x: to_enum(Context, x), from_none], self.encoding_context)
        result["EndPointInfo"] = from_union([lambda x: to_class(EndPointInfo, x), from_none], self.end_point_info)
        result["ExternalIdInfo"] = from_union([lambda x: to_class(ExternalIDInfo, x), from_none], self.external_id_info)
        result["ExternalIdMediaType"] = from_union([lambda x: to_enum(ExternalIDMediaTypeEnum, x), from_none], self.external_id_media_type)
        result["ExternalUrl"] = from_union([lambda x: to_class(ExternalURL, x), from_none], self.external_url)
        result["FFmpegLocation"] = from_union([lambda x: to_enum(Location, x), from_none], self.f_fmpeg_location)
        result["FileOrganizationResult"] = from_union([lambda x: to_class(FileOrganizationResult, x), from_none], self.file_organization_result)
        result["FileOrganizationResultQueryResult"] = from_union([lambda x: to_class(FileOrganizationResultQueryResult, x), from_none], self.file_organization_result_query_result)
        result["FileOrganizerType"] = from_union([lambda x: to_enum(FileOrganizerTypeEnum, x), from_none], self.file_organizer_type)
        result["FileSortingStatus"] = from_union([lambda x: to_enum(FileSortingStatusEnum, x), from_none], self.file_sorting_status)
        result["FileSystemEntryInfo"] = from_union([lambda x: to_class(FileSystemEntryInfo, x), from_none], self.file_system_entry_info)
        result["FileSystemEntryType"] = from_union([lambda x: to_enum(FileSystemEntryTypeEnum, x), from_none], self.file_system_entry_type)
        result["FontFile"] = from_union([lambda x: to_class(FontFile, x), from_none], self.font_file)
        result["ForgotPasswordAction"] = from_union([lambda x: to_enum(Action, x), from_none], self.forgot_password_action)
        result["ForgotPasswordDto"] = from_union([lambda x: to_class(ForgotPasswordDto, x), from_none], self.forgot_password_dto)
        result["ForgotPasswordPinDto"] = from_union([lambda x: to_class(ForgotPasswordPinDto, x), from_none], self.forgot_password_pin_dto)
        result["ForgotPasswordResult"] = from_union([lambda x: to_class(ForgotPasswordResult, x), from_none], self.forgot_password_result)
        result["GeneralCommand"] = from_union([lambda x: to_class(GeneralCommand, x), from_none], self.general_command)
        result["GeneralCommandType"] = from_union([lambda x: to_enum(GeneralCommandType, x), from_none], self.general_command_type)
        result["GetProgramsDto"] = from_union([lambda x: to_class(GetProgramsDto, x), from_none], self.get_programs_dto)
        result["GroupInfoDto"] = from_union([lambda x: to_class(GroupInfoDto, x), from_none], self.group_info_dto)
        result["GroupQueueMode"] = from_union([lambda x: to_enum(GroupQueueModeEnum, x), from_none], self.group_queue_mode)
        result["GroupRepeatMode"] = from_union([lambda x: to_enum(GroupRepeatModeEnum, x), from_none], self.group_repeat_mode)
        result["GroupShuffleMode"] = from_union([lambda x: to_enum(GroupShuffleModeEnum, x), from_none], self.group_shuffle_mode)
        result["GroupStateType"] = from_union([lambda x: to_enum(GroupStateTypeEnum, x), from_none], self.group_state_type)
        result["GroupUpdateType"] = from_union([lambda x: to_enum(GroupUpdateTypeEnum, x), from_none], self.group_update_type)
        result["GuideInfo"] = from_union([lambda x: to_class(GuideInfo, x), from_none], self.guide_info)
        result["HeaderMatchType"] = from_union([lambda x: to_enum(Match, x), from_none], self.header_match_type)
        result["HeaderMetadata"] = from_union([lambda x: to_enum(HeaderMetadata, x), from_none], self.header_metadata)
        result["HttpHeaderInfo"] = from_union([lambda x: to_class(HTTPHeaderInfo, x), from_none], self.http_header_info)
        result["IgnoreWaitRequestDto"] = from_union([lambda x: to_class(IgnoreWaitRequestDto, x), from_none], self.ignore_wait_request_dto)
        result["ImageByNameInfo"] = from_union([lambda x: to_class(ImageByNameInfo, x), from_none], self.image_by_name_info)
        result["ImageFormat"] = from_union([lambda x: to_enum(ImageFormat, x), from_none], self.image_format)
        result["ImageInfo"] = from_union([lambda x: to_class(ImageInfo, x), from_none], self.image_info)
        result["ImageOption"] = from_union([lambda x: to_class(ImageOption, x), from_none], self.image_option)
        result["ImageOrientation"] = from_union([lambda x: to_enum(ImageOrientation, x), from_none], self.image_orientation)
        result["ImageProviderInfo"] = from_union([lambda x: to_class(ImageProviderInfo, x), from_none], self.image_provider_info)
        result["ImageSavingConvention"] = from_union([lambda x: to_enum(ImageSavingConvention, x), from_none], self.image_saving_convention)
        result["ImageType"] = from_union([lambda x: to_enum(ImageTypeElement, x), from_none], self.image_type)
        result["InstallationInfo"] = from_union([lambda x: to_class(InstallationInfo, x), from_none], self.installation_info)
        result["IPlugin"] = from_union([lambda x: to_class(IPlugin, x), from_none], self.i_plugin)
        result["IsoType"] = from_union([lambda x: to_enum(ISOType, x), from_none], self.iso_type)
        result["ItemCounts"] = from_union([lambda x: to_class(ItemCounts, x), from_none], self.item_counts)
        result["ItemFields"] = from_union([lambda x: to_enum(ItemFields, x), from_none], self.item_fields)
        result["ItemFilter"] = from_union([lambda x: to_enum(ItemFilter, x), from_none], self.item_filter)
        result["Items"] = from_union([lambda x: to_class(Items, x), from_none], self.items)
        result["ItemViewType"] = from_union([lambda x: to_enum(ItemViewType, x), from_none], self.item_view_type)
        result["JoinGroupRequestDto"] = from_union([lambda x: to_class(JoinGroupRequestDto, x), from_none], self.join_group_request_dto)
        result["KeepUntil"] = from_union([lambda x: to_enum(KeepUntil, x), from_none], self.keep_until)
        result["LibraryOptionInfoDto"] = from_union([lambda x: to_class(LibraryOptionInfoDto, x), from_none], self.library_option_info_dto)
        result["LibraryOptions"] = from_union([lambda x: to_class(LibraryOptions, x), from_none], self.library_options)
        result["LibraryOptionsResultDto"] = from_union([lambda x: to_class(LibraryOptionsResultDto, x), from_none], self.library_options_result_dto)
        result["LibraryTypeOptionsDto"] = from_union([lambda x: to_class(LibraryTypeOptionsDto, x), from_none], self.library_type_options_dto)
        result["LibraryUpdateInfo"] = from_union([lambda x: to_class(LibraryUpdateInfo, x), from_none], self.library_update_info)
        result["ListingsProviderInfo"] = from_union([lambda x: to_class(ListingsProviderInfo, x), from_none], self.listings_provider_info)
        result["LiveStreamResponse"] = from_union([lambda x: to_class(LiveStreamResponse, x), from_none], self.live_stream_response)
        result["LiveTvInfo"] = from_union([lambda x: to_class(LiveTvInfo, x), from_none], self.live_tv_info)
        result["LiveTvServiceInfo"] = from_union([lambda x: to_class(LiveTvServiceInfo, x), from_none], self.live_tv_service_info)
        result["LiveTvServiceStatus"] = from_union([lambda x: to_enum(LiveTvServiceStatusEnum, x), from_none], self.live_tv_service_status)
        result["LocalizationOption"] = from_union([lambda x: to_class(LocalizationOption, x), from_none], self.localization_option)
        result["LocationType"] = from_union([lambda x: to_enum(LocationType, x), from_none], self.location_type)
        result["LogFile"] = from_union([lambda x: to_class(LogFile, x), from_none], self.log_file)
        result["LogLevel"] = from_union([lambda x: to_enum(Severity, x), from_none], self.log_level)
        result["MediaAttachment"] = from_union([lambda x: to_class(MediaAttachment, x), from_none], self.media_attachment)
        result["MediaEncoderPathDto"] = from_union([lambda x: to_class(MediaEncoderPathDto, x), from_none], self.media_encoder_path_dto)
        result["MediaPathDto"] = from_union([lambda x: to_class(MediaPathDto, x), from_none], self.media_path_dto)
        result["MediaPathInfo"] = from_union([lambda x: to_class(PathInfo, x), from_none], self.media_path_info)
        result["MediaProtocol"] = from_union([lambda x: to_enum(Protocol, x), from_none], self.media_protocol)
        result["MediaSourceInfo"] = from_union([lambda x: to_class(MediaSource, x), from_none], self.media_source_info)
        result["MediaSourceType"] = from_union([lambda x: to_enum(MediaSourceTypeEnum, x), from_none], self.media_source_type)
        result["MediaStream"] = from_union([lambda x: to_class(MediaStream, x), from_none], self.media_stream)
        result["MediaStreamType"] = from_union([lambda x: to_enum(MediaStreamTypeEnum, x), from_none], self.media_stream_type)
        result["MediaUpdateInfoDto"] = from_union([lambda x: to_class(MediaUpdateInfoDto, x), from_none], self.media_update_info_dto)
        result["MediaUpdateInfoPathDto"] = from_union([lambda x: to_class(MediaUpdateInfoPathDto, x), from_none], self.media_update_info_path_dto)
        result["MediaUrl"] = from_union([lambda x: to_class(MediaURL, x), from_none], self.media_url)
        result["MessageCommand"] = from_union([lambda x: to_class(MessageCommand, x), from_none], self.message_command)
        result["MetadataEditorInfo"] = from_union([lambda x: to_class(MetadataEditorInfo, x), from_none], self.metadata_editor_info)
        result["MetadataField"] = from_union([lambda x: to_enum(MetadataField, x), from_none], self.metadata_field)
        result["MetadataOptions"] = from_union([lambda x: to_class(MetadataOptions, x), from_none], self.metadata_options)
        result["MetadataRefreshMode"] = from_union([lambda x: to_enum(MetadataRefreshMode, x), from_none], self.metadata_refresh_mode)
        result["MovePlaylistItemRequestDto"] = from_union([lambda x: to_class(MovePlaylistItemRequestDto, x), from_none], self.move_playlist_item_request_dto)
        result["MovieInfo"] = from_union([lambda x: to_class(MovieInfoClass, x), from_none], self.movie_info)
        result["MovieInfoRemoteSearchQuery"] = from_union([lambda x: to_class(MovieInfoRemoteSearchQuery, x), from_none], self.movie_info_remote_search_query)
        result["MusicVideoInfo"] = from_union([lambda x: to_class(MusicVideoInfoClass, x), from_none], self.music_video_info)
        result["MusicVideoInfoRemoteSearchQuery"] = from_union([lambda x: to_class(MusicVideoInfoRemoteSearchQuery, x), from_none], self.music_video_info_remote_search_query)
        result["NameGuidPair"] = from_union([lambda x: to_class(NameGUIDPair, x), from_none], self.name_guid_pair)
        result["NameIdPair"] = from_union([lambda x: to_class(NameIDPair, x), from_none], self.name_id_pair)
        result["NameValuePair"] = from_union([lambda x: to_class(NameValuePair, x), from_none], self.name_value_pair)
        result["NewGroupRequestDto"] = from_union([lambda x: to_class(NewGroupRequestDto, x), from_none], self.new_group_request_dto)
        result["NextItemRequestDto"] = from_union([lambda x: to_class(NextItemRequestDto, x), from_none], self.next_item_request_dto)
        result["NotFoundObjects"] = from_union([lambda x: to_class(NotFound, x), from_none], self.not_found_objects)
        result["NotificationDto"] = from_union([lambda x: to_class(NotificationDto, x), from_none], self.notification_dto)
        result["NotificationLevel"] = from_union([lambda x: to_enum(Level, x), from_none], self.notification_level)
        result["NotificationResultDto"] = from_union([lambda x: to_class(NotificationResultDto, x), from_none], self.notification_result_dto)
        result["NotificationsSummaryDto"] = from_union([lambda x: to_class(NotificationsSummaryDto, x), from_none], self.notifications_summary_dto)
        result["NotificationTypeInfo"] = from_union([lambda x: to_class(NotificationTypeInfo, x), from_none], self.notification_type_info)
        result["ObjectGroupUpdate"] = from_union([lambda x: to_class(ObjectGroupUpdate, x), from_none], self.object_group_update)
        result["OpenLiveStreamDto"] = from_union([lambda x: to_class(OpenLiveStreamDto, x), from_none], self.open_live_stream_dto)
        result["PackageInfo"] = from_union([lambda x: to_class(PackageInfo, x), from_none], self.package_info)
        result["ParentalRating"] = from_union([lambda x: to_class(ParentalRating, x), from_none], self.parental_rating)
        result["PathSubstitution"] = from_union([lambda x: to_class(PathSubstitution, x), from_none], self.path_substitution)
        result["PersonLookupInfo"] = from_union([lambda x: to_class(PersonLookupInfoClass, x), from_none], self.person_lookup_info)
        result["PersonLookupInfoRemoteSearchQuery"] = from_union([lambda x: to_class(PersonLookupInfoRemoteSearchQuery, x), from_none], self.person_lookup_info_remote_search_query)
        result["PingRequestDto"] = from_union([lambda x: to_class(PingRequestDto, x), from_none], self.ping_request_dto)
        result["PinRedeemResult"] = from_union([lambda x: to_class(PinRedeemResult, x), from_none], self.pin_redeem_result)
        result["PlayAccess"] = from_union([lambda x: to_enum(PlayAccess, x), from_none], self.play_access)
        result["PlaybackErrorCode"] = from_union([lambda x: to_enum(ErrorCode, x), from_none], self.playback_error_code)
        result["PlaybackInfoDto"] = from_union([lambda x: to_class(PlaybackInfoDto, x), from_none], self.playback_info_dto)
        result["PlaybackInfoResponse"] = from_union([lambda x: to_class(PlaybackInfoResponse, x), from_none], self.playback_info_response)
        result["PlaybackProgressInfo"] = from_union([lambda x: to_class(PlaybackProgressInfo, x), from_none], self.playback_progress_info)
        result["PlaybackStartInfo"] = from_union([lambda x: to_class(PlaybackStartInfo, x), from_none], self.playback_start_info)
        result["PlaybackStopInfo"] = from_union([lambda x: to_class(PlaybackStopInfo, x), from_none], self.playback_stop_info)
        result["PlayCommand"] = from_union([lambda x: to_enum(PlayCommand, x), from_none], self.play_command)
        result["PlayerStateInfo"] = from_union([lambda x: to_class(Play, x), from_none], self.player_state_info)
        result["PlaylistCreationResult"] = from_union([lambda x: to_class(PlaylistCreationResult, x), from_none], self.playlist_creation_result)
        result["PlayMethod"] = from_union([lambda x: to_enum(PlayMethod, x), from_none], self.play_method)
        result["PlayRequest"] = from_union([lambda x: to_class(PlayRequest, x), from_none], self.play_request)
        result["PlayRequestDto"] = from_union([lambda x: to_class(PlayRequestDto, x), from_none], self.play_request_dto)
        result["PlaystateCommand"] = from_union([lambda x: to_enum(PlaystateCommandEnum, x), from_none], self.playstate_command)
        result["PlaystateRequest"] = from_union([lambda x: to_class(PlaystateRequest, x), from_none], self.playstate_request)
        result["PluginInfo"] = from_union([lambda x: to_class(PluginInfo, x), from_none], self.plugin_info)
        result["PluginSecurityInfo"] = from_union([lambda x: to_class(PluginSecurityInfo, x), from_none], self.plugin_security_info)
        result["PluginStatus"] = from_union([lambda x: to_enum(PluginStatusEnum, x), from_none], self.plugin_status)
        result["PreviousItemRequestDto"] = from_union([lambda x: to_class(PreviousItemRequestDto, x), from_none], self.previous_item_request_dto)
        result["ProblemDetails"] = from_union([lambda x: to_class(ProblemDetails, x), from_none], self.problem_details)
        result["ProfileCondition"] = from_union([lambda x: to_class(ProfileCondition, x), from_none], self.profile_condition)
        result["ProfileConditionType"] = from_union([lambda x: to_enum(Condition, x), from_none], self.profile_condition_type)
        result["ProfileConditionValue"] = from_union([lambda x: to_enum(Pro, x), from_none], self.profile_condition_value)
        result["ProgramAudio"] = from_union([lambda x: to_enum(Audio, x), from_none], self.program_audio)
        result["PublicSystemInfo"] = from_union([lambda x: to_class(PublicSystemInfo, x), from_none], self.public_system_info)
        result["QueryFilters"] = from_union([lambda x: to_class(QueryFilters, x), from_none], self.query_filters)
        result["QueryFiltersLegacy"] = from_union([lambda x: to_class(QueryFiltersLegacy, x), from_none], self.query_filters_legacy)
        result["QueueItem"] = from_union([lambda x: to_class(QueueItem, x), from_none], self.queue_item)
        result["QueueRequestDto"] = from_union([lambda x: to_class(QueueRequestDto, x), from_none], self.queue_request_dto)
        result["QuickConnectDto"] = from_union([lambda x: to_class(QuickConnectDto, x), from_none], self.quick_connect_dto)
        result["QuickConnectResult"] = from_union([lambda x: to_class(QuickConnectResult, x), from_none], self.quick_connect_result)
        result["QuickConnectState"] = from_union([lambda x: to_enum(QuickConnectState, x), from_none], self.quick_connect_state)
        result["RatingType"] = from_union([lambda x: to_enum(RatingType, x), from_none], self.rating_type)
        result["ReadyRequestDto"] = from_union([lambda x: to_class(ReadyRequestDto, x), from_none], self.ready_request_dto)
        result["RecommendationDto"] = from_union([lambda x: to_class(RecommendationDto, x), from_none], self.recommendation_dto)
        result["RecommendationType"] = from_union([lambda x: to_enum(RecommendationType, x), from_none], self.recommendation_type)
        result["RecordingStatus"] = from_union([lambda x: to_enum(RecordingStatusEnum, x), from_none], self.recording_status)
        result["RemoteImageInfo"] = from_union([lambda x: to_class(RemoteImageInfo, x), from_none], self.remote_image_info)
        result["RemoteImageResult"] = from_union([lambda x: to_class(RemoteImageResult, x), from_none], self.remote_image_result)
        result["RemoteSearchResult"] = from_union([lambda x: to_class(RemoteSearchResult, x), from_none], self.remote_search_result)
        result["RemoteSubtitleInfo"] = from_union([lambda x: to_class(RemoteSubtitleInfo, x), from_none], self.remote_subtitle_info)
        result["RemoveFromPlaylistRequestDto"] = from_union([lambda x: to_class(RemoveFromPlaylistRequestDto, x), from_none], self.remove_from_playlist_request_dto)
        result["RepeatMode"] = from_union([lambda x: to_enum(GroupRepeatModeEnum, x), from_none], self.repeat_mode)
        result["ReportDisplayType"] = from_union([lambda x: to_enum(DisplayType, x), from_none], self.report_display_type)
        result["ReportExportType"] = from_union([lambda x: to_enum(ReportExportType, x), from_none], self.report_export_type)
        result["ReportFieldType"] = from_union([lambda x: to_enum(FieldType, x), from_none], self.report_field_type)
        result["ReportGroup"] = from_union([lambda x: to_class(ReportGroup, x), from_none], self.report_group)
        result["ReportHeader"] = from_union([lambda x: to_class(ReportHeader, x), from_none], self.report_header)
        result["ReportIncludeItemTypes"] = from_union([lambda x: to_enum(RowType, x), from_none], self.report_include_item_types)
        result["ReportItem"] = from_union([lambda x: to_class(ReportItem, x), from_none], self.report_item)
        result["ReportResult"] = from_union([lambda x: to_class(ReportResult, x), from_none], self.report_result)
        result["ReportRow"] = from_union([lambda x: to_class(ReportRow, x), from_none], self.report_row)
        result["RepositoryInfo"] = from_union([lambda x: to_class(RepositoryInfo, x), from_none], self.repository_info)
        result["ResponseProfile"] = from_union([lambda x: to_class(ResponseProfile, x), from_none], self.response_profile)
        result["ScrollDirection"] = from_union([lambda x: to_enum(ScrollDirection, x), from_none], self.scroll_direction)
        result["SearchHint"] = from_union([lambda x: to_class(SearchHint, x), from_none], self.search_hint)
        result["SearchHintResult"] = from_union([lambda x: to_class(SearchHintResult, x), from_none], self.search_hint_result)
        result["SeekRequestDto"] = from_union([lambda x: to_class(SeekRequestDto, x), from_none], self.seek_request_dto)
        result["SendCommand"] = from_union([lambda x: to_class(SendCommand, x), from_none], self.send_command)
        result["SendCommandType"] = from_union([lambda x: to_enum(SendCommandTypeEnum, x), from_none], self.send_command_type)
        result["SeriesInfo"] = from_union([lambda x: to_class(SeriesInfoClass, x), from_none], self.series_info)
        result["SeriesInfoRemoteSearchQuery"] = from_union([lambda x: to_class(SeriesInfoRemoteSearchQuery, x), from_none], self.series_info_remote_search_query)
        result["SeriesStatus"] = from_union([lambda x: to_enum(SeriesStatus, x), from_none], self.series_status)
        result["SeriesTimerInfoDto"] = from_union([lambda x: to_class(SeriesTimerInfoDto, x), from_none], self.series_timer_info_dto)
        result["SeriesTimerInfoDtoQueryResult"] = from_union([lambda x: to_class(SeriesTimerInfoDtoQueryResult, x), from_none], self.series_timer_info_dto_query_result)
        result["ServerConfiguration"] = from_union([lambda x: to_class(ServerConfiguration, x), from_none], self.server_configuration)
        result["ServerDiscoveryInfo"] = from_union([lambda x: to_class(ServerDiscoveryInfo, x), from_none], self.server_discovery_info)
        result["SessionInfo"] = from_union([lambda x: to_class(SessionInfo, x), from_none], self.session_info)
        result["SessionMessageType"] = from_union([lambda x: to_enum(SessionMessageType, x), from_none], self.session_message_type)
        result["SessionUserInfo"] = from_union([lambda x: to_class(SessionUserInfo, x), from_none], self.session_user_info)
        result["SetChannelMappingDto"] = from_union([lambda x: to_class(SetChannelMappingDto, x), from_none], self.set_channel_mapping_dto)
        result["SetPlaylistItemRequestDto"] = from_union([lambda x: to_class(SetPlaylistItemRequestDto, x), from_none], self.set_playlist_item_request_dto)
        result["SetRepeatModeRequestDto"] = from_union([lambda x: to_class(SetRepeatModeRequestDto, x), from_none], self.set_repeat_mode_request_dto)
        result["SetShuffleModeRequestDto"] = from_union([lambda x: to_class(SetShuffleModeRequestDto, x), from_none], self.set_shuffle_mode_request_dto)
        result["SmartMatchResult"] = from_union([lambda x: to_class(SmartMatchResult, x), from_none], self.smart_match_result)
        result["SmartMatchResultQueryResult"] = from_union([lambda x: to_class(SmartMatchResultQueryResult, x), from_none], self.smart_match_result_query_result)
        result["SongInfo"] = from_union([lambda x: to_class(SongInfo, x), from_none], self.song_info)
        result["SortOrder"] = from_union([lambda x: to_enum(SortOrder, x), from_none], self.sort_order)
        result["SpecialViewOptionDto"] = from_union([lambda x: to_class(SpecialViewOptionDto, x), from_none], self.special_view_option_dto)
        result["StartupConfigurationDto"] = from_union([lambda x: to_class(StartupConfigurationDto, x), from_none], self.startup_configuration_dto)
        result["StartupRemoteAccessDto"] = from_union([lambda x: to_class(StartupRemoteAccessDto, x), from_none], self.startup_remote_access_dto)
        result["StartupUserDto"] = from_union([lambda x: to_class(StartupUserDto, x), from_none], self.startup_user_dto)
        result["SubtitleDeliveryMethod"] = from_union([lambda x: to_enum(Method, x), from_none], self.subtitle_delivery_method)
        result["SubtitlePlaybackMode"] = from_union([lambda x: to_enum(SubtitleMode, x), from_none], self.subtitle_playback_mode)
        result["SubtitleProfile"] = from_union([lambda x: to_class(SubtitleProfile, x), from_none], self.subtitle_profile)
        result["SyncPlayUserAccessType"] = from_union([lambda x: to_enum(SyncPlay, x), from_none], self.sync_play_user_access_type)
        result["SystemInfo"] = from_union([lambda x: to_class(SystemInfo, x), from_none], self.system_info)
        result["TaskCompletionStatus"] = from_union([lambda x: to_enum(TaskCompletionStatusEnum, x), from_none], self.task_completion_status)
        result["TaskInfo"] = from_union([lambda x: to_class(TaskInfo, x), from_none], self.task_info)
        result["TaskResult"] = from_union([lambda x: to_class(TaskResultClass, x), from_none], self.task_result)
        result["TaskState"] = from_union([lambda x: to_enum(TaskStateEnum, x), from_none], self.task_state)
        result["TaskTriggerInfo"] = from_union([lambda x: to_class(TaskTriggerInfo, x), from_none], self.task_trigger_info)
        result["ThemeMediaResult"] = from_union([lambda x: to_class(ThemeMediaResultClass, x), from_none], self.theme_media_result)
        result["TimerEventInfo"] = from_union([lambda x: to_class(TimerEventInfo, x), from_none], self.timer_event_info)
        result["TimerInfoDto"] = from_union([lambda x: to_class(TimerInfoDto, x), from_none], self.timer_info_dto)
        result["TimerInfoDtoQueryResult"] = from_union([lambda x: to_class(TimerInfoDtoQueryResult, x), from_none], self.timer_info_dto_query_result)
        result["TrailerInfo"] = from_union([lambda x: to_class(TrailerInfoClass, x), from_none], self.trailer_info)
        result["TrailerInfoRemoteSearchQuery"] = from_union([lambda x: to_class(TrailerInfoRemoteSearchQuery, x), from_none], self.trailer_info_remote_search_query)
        result["TraktEpisode"] = from_union([lambda x: to_class(TraktEpisode, x), from_none], self.trakt_episode)
        result["TraktEpisodeId"] = from_union([lambda x: to_class(TraktEpisodeIDClass, x), from_none], self.trakt_episode_id)
        result["TraktMovie"] = from_union([lambda x: to_class(TraktMovie, x), from_none], self.trakt_movie)
        result["TraktMovieId"] = from_union([lambda x: to_class(TraktMovieIDClass, x), from_none], self.trakt_movie_id)
        result["TraktPerson"] = from_union([lambda x: to_class(TraktPerson, x), from_none], self.trakt_person)
        result["TraktPersonId"] = from_union([lambda x: to_class(TraktPersonIDClass, x), from_none], self.trakt_person_id)
        result["TraktSeason"] = from_union([lambda x: to_class(TraktSeason, x), from_none], self.trakt_season)
        result["TraktSeasonId"] = from_union([lambda x: to_class(TraktSeasonIDClass, x), from_none], self.trakt_season_id)
        result["TraktShow"] = from_union([lambda x: to_class(TraktShow, x), from_none], self.trakt_show)
        result["TraktShowId"] = from_union([lambda x: to_class(TraktShowIDClass, x), from_none], self.trakt_show_id)
        result["TraktSyncResponse"] = from_union([lambda x: to_class(TraktSyncResponse, x), from_none], self.trakt_sync_response)
        result["TranscodeReason"] = from_union([lambda x: to_enum(TranscodeReason, x), from_none], self.transcode_reason)
        result["TranscodeSeekInfo"] = from_union([lambda x: to_enum(TranscodeSeekInfo, x), from_none], self.transcode_seek_info)
        result["TranscodingInfo"] = from_union([lambda x: to_class(TranscodingInfo, x), from_none], self.transcoding_info)
        result["TranscodingProfile"] = from_union([lambda x: to_class(TranscodingProfile, x), from_none], self.transcoding_profile)
        result["TransportStreamTimestamp"] = from_union([lambda x: to_enum(Timestamp, x), from_none], self.transport_stream_timestamp)
        result["TunerChannelMapping"] = from_union([lambda x: to_class(TunerChannelMapping, x), from_none], self.tuner_channel_mapping)
        result["TunerHostInfo"] = from_union([lambda x: to_class(TunerHostInfo, x), from_none], self.tuner_host_info)
        result["TypeOptions"] = from_union([lambda x: to_class(TypeOptions, x), from_none], self.type_options)
        result["UnratedItem"] = from_union([lambda x: to_enum(UnratedItem, x), from_none], self.unrated_item)
        result["UpdateLibraryOptionsDto"] = from_union([lambda x: to_class(UpdateLibraryOptionsDto, x), from_none], self.update_library_options_dto)
        result["UpdateMediaPathRequestDto"] = from_union([lambda x: to_class(UpdateMediaPathRequestDto, x), from_none], self.update_media_path_request_dto)
        result["UpdateUserEasyPassword"] = from_union([lambda x: to_class(UpdateUserEasyPassword, x), from_none], self.update_user_easy_password)
        result["UpdateUserPassword"] = from_union([lambda x: to_class(UpdateUserPassword, x), from_none], self.update_user_password)
        result["UploadSubtitleDto"] = from_union([lambda x: to_class(UploadSubtitleDto, x), from_none], self.upload_subtitle_dto)
        result["UserConfiguration"] = from_union([lambda x: to_class(Configuration, x), from_none], self.user_configuration)
        result["UserDto"] = from_union([lambda x: to_class(UserDtoClass, x), from_none], self.user_dto)
        result["UserItemDataDto"] = from_union([lambda x: to_class(User, x), from_none], self.user_item_data_dto)
        result["UserPolicy"] = from_union([lambda x: to_class(Policy, x), from_none], self.user_policy)
        result["UtcTimeResponse"] = from_union([lambda x: to_class(UTCTimeResponse, x), from_none], self.utc_time_response)
        result["ValidatePathDto"] = from_union([lambda x: to_class(ValidatePathDto, x), from_none], self.validate_path_dto)
        result["Version"] = from_union([lambda x: to_class(VersionNumber, x), from_none], self.version)
        result["VersionInfo"] = from_union([lambda x: to_class(VersionInfo, x), from_none], self.version_info)
        result["Video3DFormat"] = from_union([lambda x: to_enum(Video3DFormat, x), from_none], self.video3_d_format)
        result["VideoType"] = from_union([lambda x: to_enum(VideoType, x), from_none], self.video_type)
        result["VirtualFolderInfo"] = from_union([lambda x: to_class(VirtualFolderInfo, x), from_none], self.virtual_folder_info)
        result["WakeOnLanInfo"] = from_union([lambda x: to_class(WakeOnLANInfo, x), from_none], self.wake_on_lan_info)
        result["XmlAttribute"] = from_union([lambda x: to_class(XMLAttribute, x), from_none], self.xml_attribute)
        return result


def data_all_from_dict(s: Any) -> DataAll:
    return DataAll.from_dict(s)


def data_all_to_dict(x: DataAll) -> Any:
    return to_class(DataAll, x)
