from data_classes.device_profile import DeviceProfile
from data_classes.general_command_type import GeneralCommandType
from util.from_type import *


@dataclass
class ClientCapabilitiesDto:
    """Client capabilities dto."""
    """Gets or sets the app store url."""
    app_store_url: Optional[str] = None
    """Gets or sets the device profile."""
    device_profile: Optional[DeviceProfile] = None
    """Gets or sets the icon url."""
    icon_url: Optional[str] = None
    """Gets or sets the message callback url."""
    message_callback_url: Optional[str] = None
    """Gets or sets the list of playable media types."""
    playable_media_types: Optional[List[str]] = None
    """Gets or sets the list of supported commands."""
    supported_commands: Optional[List[GeneralCommandType]] = None
    """Gets or sets a value indicating whether session supports content uploading."""
    supports_content_uploading: Optional[bool] = None
    """Gets or sets a value indicating whether session supports media control."""
    supports_media_control: Optional[bool] = None
    """Gets or sets a value indicating whether session supports a persistent identifier."""
    supports_persistent_identifier: Optional[bool] = None
    """Gets or sets a value indicating whether session supports sync."""
    supports_sync: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ClientCapabilitiesDto':
        assert isinstance(obj, dict)
        app_store_url = from_union([from_str, from_none], obj.get("AppStoreUrl"))
        device_profile = from_union([DeviceProfile.from_dict, from_none], obj.get("DeviceProfile"))
        icon_url = from_union([from_str, from_none], obj.get("IconUrl"))
        message_callback_url = from_union([from_str, from_none], obj.get("MessageCallbackUrl"))
        playable_media_types = from_union([lambda x: from_list(from_str, x), from_none], obj.get("PlayableMediaTypes"))
        supported_commands = from_union([lambda x: from_list(GeneralCommandType, x), from_none], obj.get("SupportedCommands"))
        supports_content_uploading = from_union([from_bool, from_none], obj.get("SupportsContentUploading"))
        supports_media_control = from_union([from_bool, from_none], obj.get("SupportsMediaControl"))
        supports_persistent_identifier = from_union([from_bool, from_none], obj.get("SupportsPersistentIdentifier"))
        supports_sync = from_union([from_bool, from_none], obj.get("SupportsSync"))
        return ClientCapabilitiesDto(app_store_url, device_profile, icon_url, message_callback_url, playable_media_types, supported_commands, supports_content_uploading, supports_media_control, supports_persistent_identifier, supports_sync)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AppStoreUrl"] = from_union([from_str, from_none], self.app_store_url)
        result["DeviceProfile"] = from_union([lambda x: to_class(DeviceProfile, x), from_none], self.device_profile)
        result["IconUrl"] = from_union([from_str, from_none], self.icon_url)
        result["MessageCallbackUrl"] = from_union([from_str, from_none], self.message_callback_url)
        result["PlayableMediaTypes"] = from_union([lambda x: from_list(from_str, x), from_none], self.playable_media_types)
        result["SupportedCommands"] = from_union([lambda x: from_list(lambda x: to_enum(GeneralCommandType, x), x), from_none], self.supported_commands)
        result["SupportsContentUploading"] = from_union([from_bool, from_none], self.supports_content_uploading)
        result["SupportsMediaControl"] = from_union([from_bool, from_none], self.supports_media_control)
        result["SupportsPersistentIdentifier"] = from_union([from_bool, from_none], self.supports_persistent_identifier)
        result["SupportsSync"] = from_union([from_bool, from_none], self.supports_sync)
        return result


