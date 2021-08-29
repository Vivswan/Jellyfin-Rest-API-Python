from util.from_type import *
from data_classes.base_item_dto import BaseItemDto
from data_classes.session_user_info import SessionUserInfo
from data_classes.general_command_type import GeneralCommandType
from data_classes.capabilities import Capabilities
from data_classes.item import Item
from data_classes.queue_item import QueueItem
from data_classes.play import Play
from data_classes.transcoding_info import TranscodingInfo


@dataclass
class SessionInfo:
    """Class SessionInfo."""
    additional_users: Optional[List[SessionUserInfo]] = None
    """Gets or sets the application version."""
    application_version: Optional[str] = None
    capabilities: Optional[Capabilities] = None
    """Gets or sets the type of the client."""
    client: Optional[str] = None
    """Gets or sets the device id."""
    device_id: Optional[str] = None
    """Gets or sets the name of the device."""
    device_name: Optional[str] = None
    """Gets or sets the type of the device."""
    device_type: Optional[str] = None
    """Class BaseItem."""
    full_now_playing_item: Optional[Item] = None
    has_custom_device_name: Optional[bool] = None
    """Gets or sets the id."""
    id: Optional[str] = None
    """Gets a value indicating whether this instance is active."""
    is_active: Optional[bool] = None
    """Gets or sets the last activity date."""
    last_activity_date: Optional[datetime] = None
    """Gets or sets the last playback check in."""
    last_playback_check_in: Optional[datetime] = None
    """Gets or sets the now playing item."""
    now_playing_item: Optional[BaseItemDto] = None
    now_playing_queue: Optional[List[QueueItem]] = None
    """This is strictly used as a data transfer object from the api layer.
    This holds information about a BaseItem in a format that is convenient for the client.
    """
    now_viewing_item: Optional[BaseItemDto] = None
    """Gets or sets the playable media types."""
    playable_media_types: Optional[List[str]] = None
    playlist_item_id: Optional[str] = None
    play_state: Optional[Play] = None
    """Gets or sets the remote end point."""
    remote_end_point: Optional[str] = None
    server_id: Optional[str] = None
    """Gets or sets the supported commands."""
    supported_commands: Optional[List[GeneralCommandType]] = None
    supports_media_control: Optional[bool] = None
    supports_remote_control: Optional[bool] = None
    transcoding_info: Optional[TranscodingInfo] = None
    """Gets or sets the user id."""
    user_id: Optional[UUID] = None
    """Gets or sets the username."""
    user_name: Optional[str] = None
    user_primary_image_tag: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SessionInfo':
        assert isinstance(obj, dict)
        additional_users = from_union([lambda x: from_list(SessionUserInfo.from_dict, x), from_none], obj.get("AdditionalUsers"))
        application_version = from_union([from_str, from_none], obj.get("ApplicationVersion"))
        capabilities = from_union([Capabilities.from_dict, from_none], obj.get("Capabilities"))
        client = from_union([from_str, from_none], obj.get("Client"))
        device_id = from_union([from_str, from_none], obj.get("DeviceId"))
        device_name = from_union([from_str, from_none], obj.get("DeviceName"))
        device_type = from_union([from_str, from_none], obj.get("DeviceType"))
        full_now_playing_item = from_union([Item.from_dict, from_none], obj.get("FullNowPlayingItem"))
        has_custom_device_name = from_union([from_bool, from_none], obj.get("HasCustomDeviceName"))
        id = from_union([from_str, from_none], obj.get("Id"))
        is_active = from_union([from_bool, from_none], obj.get("IsActive"))
        last_activity_date = from_union([from_datetime, from_none], obj.get("LastActivityDate"))
        last_playback_check_in = from_union([from_datetime, from_none], obj.get("LastPlaybackCheckIn"))
        now_playing_item = from_union([BaseItemDto.from_dict, from_none], obj.get("NowPlayingItem"))
        now_playing_queue = from_union([lambda x: from_list(QueueItem.from_dict, x), from_none], obj.get("NowPlayingQueue"))
        now_viewing_item = from_union([BaseItemDto.from_dict, from_none], obj.get("NowViewingItem"))
        playable_media_types = from_union([lambda x: from_list(from_str, x), from_none], obj.get("PlayableMediaTypes"))
        playlist_item_id = from_union([from_str, from_none], obj.get("PlaylistItemId"))
        play_state = from_union([Play.from_dict, from_none], obj.get("PlayState"))
        remote_end_point = from_union([from_str, from_none], obj.get("RemoteEndPoint"))
        server_id = from_union([from_str, from_none], obj.get("ServerId"))
        supported_commands = from_union([lambda x: from_list(GeneralCommandType, x), from_none], obj.get("SupportedCommands"))
        supports_media_control = from_union([from_bool, from_none], obj.get("SupportsMediaControl"))
        supports_remote_control = from_union([from_bool, from_none], obj.get("SupportsRemoteControl"))
        transcoding_info = from_union([TranscodingInfo.from_dict, from_none], obj.get("TranscodingInfo"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        user_name = from_union([from_str, from_none], obj.get("UserName"))
        user_primary_image_tag = from_union([from_str, from_none], obj.get("UserPrimaryImageTag"))
        return SessionInfo(additional_users, application_version, capabilities, client, device_id, device_name, device_type, full_now_playing_item, has_custom_device_name, id, is_active, last_activity_date, last_playback_check_in, now_playing_item, now_playing_queue, now_viewing_item, playable_media_types, playlist_item_id, play_state, remote_end_point, server_id, supported_commands, supports_media_control, supports_remote_control, transcoding_info, user_id, user_name, user_primary_image_tag)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AdditionalUsers"] = from_union([lambda x: from_list(lambda x: to_class(SessionUserInfo, x), x), from_none], self.additional_users)
        result["ApplicationVersion"] = from_union([from_str, from_none], self.application_version)
        result["Capabilities"] = from_union([lambda x: to_class(Capabilities, x), from_none], self.capabilities)
        result["Client"] = from_union([from_str, from_none], self.client)
        result["DeviceId"] = from_union([from_str, from_none], self.device_id)
        result["DeviceName"] = from_union([from_str, from_none], self.device_name)
        result["DeviceType"] = from_union([from_str, from_none], self.device_type)
        result["FullNowPlayingItem"] = from_union([lambda x: to_class(Item, x), from_none], self.full_now_playing_item)
        result["HasCustomDeviceName"] = from_union([from_bool, from_none], self.has_custom_device_name)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IsActive"] = from_union([from_bool, from_none], self.is_active)
        result["LastActivityDate"] = from_union([lambda x: x.isoformat(), from_none], self.last_activity_date)
        result["LastPlaybackCheckIn"] = from_union([lambda x: x.isoformat(), from_none], self.last_playback_check_in)
        result["NowPlayingItem"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.now_playing_item)
        result["NowPlayingQueue"] = from_union([lambda x: from_list(lambda x: to_class(QueueItem, x), x), from_none], self.now_playing_queue)
        result["NowViewingItem"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.now_viewing_item)
        result["PlayableMediaTypes"] = from_union([lambda x: from_list(from_str, x), from_none], self.playable_media_types)
        result["PlaylistItemId"] = from_union([from_str, from_none], self.playlist_item_id)
        result["PlayState"] = from_union([lambda x: to_class(Play, x), from_none], self.play_state)
        result["RemoteEndPoint"] = from_union([from_str, from_none], self.remote_end_point)
        result["ServerId"] = from_union([from_str, from_none], self.server_id)
        result["SupportedCommands"] = from_union([lambda x: from_list(lambda x: to_enum(GeneralCommandType, x), x), from_none], self.supported_commands)
        result["SupportsMediaControl"] = from_union([from_bool, from_none], self.supports_media_control)
        result["SupportsRemoteControl"] = from_union([from_bool, from_none], self.supports_remote_control)
        result["TranscodingInfo"] = from_union([lambda x: to_class(TranscodingInfo, x), from_none], self.transcoding_info)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        result["UserName"] = from_union([from_str, from_none], self.user_name)
        result["UserPrimaryImageTag"] = from_union([from_str, from_none], self.user_primary_image_tag)
        return result


