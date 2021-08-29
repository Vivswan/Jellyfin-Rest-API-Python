from util.from_type import *
from data_classes.access_schedule import AccessSchedule
from data_classes.unrated_item import UnratedItem
from data_classes.sync_play import SyncPlay


@dataclass
class Policy:
    """Gets or sets the policy."""
    access_schedules: Optional[List[AccessSchedule]] = None
    authentication_provider_id: Optional[str] = None
    blocked_channels: Optional[List[UUID]] = None
    blocked_media_folders: Optional[List[UUID]] = None
    blocked_tags: Optional[List[str]] = None
    block_unrated_items: Optional[List[UnratedItem]] = None
    enable_all_channels: Optional[bool] = None
    enable_all_devices: Optional[bool] = None
    enable_all_folders: Optional[bool] = None
    enable_audio_playback_transcoding: Optional[bool] = None
    enable_content_deletion: Optional[bool] = None
    enable_content_deletion_from_folders: Optional[List[str]] = None
    enable_content_downloading: Optional[bool] = None
    enabled_channels: Optional[List[UUID]] = None
    enabled_devices: Optional[List[str]] = None
    enabled_folders: Optional[List[UUID]] = None
    enable_live_tv_access: Optional[bool] = None
    enable_live_tv_management: Optional[bool] = None
    enable_media_conversion: Optional[bool] = None
    enable_media_playback: Optional[bool] = None
    enable_playback_remuxing: Optional[bool] = None
    enable_public_sharing: Optional[bool] = None
    enable_remote_access: Optional[bool] = None
    enable_remote_control_of_other_users: Optional[bool] = None
    enable_shared_device_control: Optional[bool] = None
    """Gets or sets a value indicating whether [enable synchronize]."""
    enable_sync_transcoding: Optional[bool] = None
    enable_user_preference_access: Optional[bool] = None
    enable_video_playback_transcoding: Optional[bool] = None
    force_remote_source_transcoding: Optional[bool] = None
    invalid_login_attempt_count: Optional[int] = None
    """Gets or sets a value indicating whether this instance is administrator."""
    is_administrator: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is disabled."""
    is_disabled: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is hidden."""
    is_hidden: Optional[bool] = None
    login_attempts_before_lockout: Optional[int] = None
    max_active_sessions: Optional[int] = None
    """Gets or sets the max parental rating."""
    max_parental_rating: Optional[int] = None
    password_reset_provider_id: Optional[str] = None
    remote_client_bitrate_limit: Optional[int] = None
    """Gets or sets a value indicating what SyncPlay features the user can access."""
    sync_play_access: Optional[SyncPlay] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Policy':
        assert isinstance(obj, dict)
        access_schedules = from_union([lambda x: from_list(AccessSchedule.from_dict, x), from_none], obj.get("AccessSchedules"))
        authentication_provider_id = from_union([from_str, from_none], obj.get("AuthenticationProviderId"))
        blocked_channels = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("BlockedChannels"))
        blocked_media_folders = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("BlockedMediaFolders"))
        blocked_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("BlockedTags"))
        block_unrated_items = from_union([lambda x: from_list(UnratedItem, x), from_none], obj.get("BlockUnratedItems"))
        enable_all_channels = from_union([from_bool, from_none], obj.get("EnableAllChannels"))
        enable_all_devices = from_union([from_bool, from_none], obj.get("EnableAllDevices"))
        enable_all_folders = from_union([from_bool, from_none], obj.get("EnableAllFolders"))
        enable_audio_playback_transcoding = from_union([from_bool, from_none], obj.get("EnableAudioPlaybackTranscoding"))
        enable_content_deletion = from_union([from_bool, from_none], obj.get("EnableContentDeletion"))
        enable_content_deletion_from_folders = from_union([lambda x: from_list(from_str, x), from_none], obj.get("EnableContentDeletionFromFolders"))
        enable_content_downloading = from_union([from_bool, from_none], obj.get("EnableContentDownloading"))
        enabled_channels = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("EnabledChannels"))
        enabled_devices = from_union([lambda x: from_list(from_str, x), from_none], obj.get("EnabledDevices"))
        enabled_folders = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("EnabledFolders"))
        enable_live_tv_access = from_union([from_bool, from_none], obj.get("EnableLiveTvAccess"))
        enable_live_tv_management = from_union([from_bool, from_none], obj.get("EnableLiveTvManagement"))
        enable_media_conversion = from_union([from_bool, from_none], obj.get("EnableMediaConversion"))
        enable_media_playback = from_union([from_bool, from_none], obj.get("EnableMediaPlayback"))
        enable_playback_remuxing = from_union([from_bool, from_none], obj.get("EnablePlaybackRemuxing"))
        enable_public_sharing = from_union([from_bool, from_none], obj.get("EnablePublicSharing"))
        enable_remote_access = from_union([from_bool, from_none], obj.get("EnableRemoteAccess"))
        enable_remote_control_of_other_users = from_union([from_bool, from_none], obj.get("EnableRemoteControlOfOtherUsers"))
        enable_shared_device_control = from_union([from_bool, from_none], obj.get("EnableSharedDeviceControl"))
        enable_sync_transcoding = from_union([from_bool, from_none], obj.get("EnableSyncTranscoding"))
        enable_user_preference_access = from_union([from_bool, from_none], obj.get("EnableUserPreferenceAccess"))
        enable_video_playback_transcoding = from_union([from_bool, from_none], obj.get("EnableVideoPlaybackTranscoding"))
        force_remote_source_transcoding = from_union([from_bool, from_none], obj.get("ForceRemoteSourceTranscoding"))
        invalid_login_attempt_count = from_union([from_int, from_none], obj.get("InvalidLoginAttemptCount"))
        is_administrator = from_union([from_bool, from_none], obj.get("IsAdministrator"))
        is_disabled = from_union([from_bool, from_none], obj.get("IsDisabled"))
        is_hidden = from_union([from_bool, from_none], obj.get("IsHidden"))
        login_attempts_before_lockout = from_union([from_int, from_none], obj.get("LoginAttemptsBeforeLockout"))
        max_active_sessions = from_union([from_int, from_none], obj.get("MaxActiveSessions"))
        max_parental_rating = from_union([from_int, from_none], obj.get("MaxParentalRating"))
        password_reset_provider_id = from_union([from_str, from_none], obj.get("PasswordResetProviderId"))
        remote_client_bitrate_limit = from_union([from_int, from_none], obj.get("RemoteClientBitrateLimit"))
        sync_play_access = from_union([SyncPlay, from_none], obj.get("SyncPlayAccess"))
        return Policy(access_schedules, authentication_provider_id, blocked_channels, blocked_media_folders, blocked_tags, block_unrated_items, enable_all_channels, enable_all_devices, enable_all_folders, enable_audio_playback_transcoding, enable_content_deletion, enable_content_deletion_from_folders, enable_content_downloading, enabled_channels, enabled_devices, enabled_folders, enable_live_tv_access, enable_live_tv_management, enable_media_conversion, enable_media_playback, enable_playback_remuxing, enable_public_sharing, enable_remote_access, enable_remote_control_of_other_users, enable_shared_device_control, enable_sync_transcoding, enable_user_preference_access, enable_video_playback_transcoding, force_remote_source_transcoding, invalid_login_attempt_count, is_administrator, is_disabled, is_hidden, login_attempts_before_lockout, max_active_sessions, max_parental_rating, password_reset_provider_id, remote_client_bitrate_limit, sync_play_access)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AccessSchedules"] = from_union([lambda x: from_list(lambda x: to_class(AccessSchedule, x), x), from_none], self.access_schedules)
        result["AuthenticationProviderId"] = from_union([from_str, from_none], self.authentication_provider_id)
        result["BlockedChannels"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.blocked_channels)
        result["BlockedMediaFolders"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.blocked_media_folders)
        result["BlockedTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.blocked_tags)
        result["BlockUnratedItems"] = from_union([lambda x: from_list(lambda x: to_enum(UnratedItem, x), x), from_none], self.block_unrated_items)
        result["EnableAllChannels"] = from_union([from_bool, from_none], self.enable_all_channels)
        result["EnableAllDevices"] = from_union([from_bool, from_none], self.enable_all_devices)
        result["EnableAllFolders"] = from_union([from_bool, from_none], self.enable_all_folders)
        result["EnableAudioPlaybackTranscoding"] = from_union([from_bool, from_none], self.enable_audio_playback_transcoding)
        result["EnableContentDeletion"] = from_union([from_bool, from_none], self.enable_content_deletion)
        result["EnableContentDeletionFromFolders"] = from_union([lambda x: from_list(from_str, x), from_none], self.enable_content_deletion_from_folders)
        result["EnableContentDownloading"] = from_union([from_bool, from_none], self.enable_content_downloading)
        result["EnabledChannels"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.enabled_channels)
        result["EnabledDevices"] = from_union([lambda x: from_list(from_str, x), from_none], self.enabled_devices)
        result["EnabledFolders"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.enabled_folders)
        result["EnableLiveTvAccess"] = from_union([from_bool, from_none], self.enable_live_tv_access)
        result["EnableLiveTvManagement"] = from_union([from_bool, from_none], self.enable_live_tv_management)
        result["EnableMediaConversion"] = from_union([from_bool, from_none], self.enable_media_conversion)
        result["EnableMediaPlayback"] = from_union([from_bool, from_none], self.enable_media_playback)
        result["EnablePlaybackRemuxing"] = from_union([from_bool, from_none], self.enable_playback_remuxing)
        result["EnablePublicSharing"] = from_union([from_bool, from_none], self.enable_public_sharing)
        result["EnableRemoteAccess"] = from_union([from_bool, from_none], self.enable_remote_access)
        result["EnableRemoteControlOfOtherUsers"] = from_union([from_bool, from_none], self.enable_remote_control_of_other_users)
        result["EnableSharedDeviceControl"] = from_union([from_bool, from_none], self.enable_shared_device_control)
        result["EnableSyncTranscoding"] = from_union([from_bool, from_none], self.enable_sync_transcoding)
        result["EnableUserPreferenceAccess"] = from_union([from_bool, from_none], self.enable_user_preference_access)
        result["EnableVideoPlaybackTranscoding"] = from_union([from_bool, from_none], self.enable_video_playback_transcoding)
        result["ForceRemoteSourceTranscoding"] = from_union([from_bool, from_none], self.force_remote_source_transcoding)
        result["InvalidLoginAttemptCount"] = from_union([from_int, from_none], self.invalid_login_attempt_count)
        result["IsAdministrator"] = from_union([from_bool, from_none], self.is_administrator)
        result["IsDisabled"] = from_union([from_bool, from_none], self.is_disabled)
        result["IsHidden"] = from_union([from_bool, from_none], self.is_hidden)
        result["LoginAttemptsBeforeLockout"] = from_union([from_int, from_none], self.login_attempts_before_lockout)
        result["MaxActiveSessions"] = from_union([from_int, from_none], self.max_active_sessions)
        result["MaxParentalRating"] = from_union([from_int, from_none], self.max_parental_rating)
        result["PasswordResetProviderId"] = from_union([from_str, from_none], self.password_reset_provider_id)
        result["RemoteClientBitrateLimit"] = from_union([from_int, from_none], self.remote_client_bitrate_limit)
        result["SyncPlayAccess"] = from_union([lambda x: to_enum(SyncPlay, x), from_none], self.sync_play_access)
        return result


