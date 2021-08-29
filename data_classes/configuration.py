from data_classes.subtitle_mode import SubtitleMode
from util.from_type import *


@dataclass
class Configuration:
    """Gets or sets the configuration.
    
    Class UserConfiguration.
    """
    """Gets or sets the audio language preference."""
    audio_language_preference: Optional[str] = None
    display_collections_view: Optional[bool] = None
    display_missing_episodes: Optional[bool] = None
    enable_local_password: Optional[bool] = None
    enable_next_episode_auto_play: Optional[bool] = None
    grouped_folders: Optional[List[str]] = None
    hide_played_in_latest: Optional[bool] = None
    latest_items_excludes: Optional[List[str]] = None
    my_media_excludes: Optional[List[str]] = None
    ordered_views: Optional[List[str]] = None
    """Gets or sets a value indicating whether [play default audio track]."""
    play_default_audio_track: Optional[bool] = None
    remember_audio_selections: Optional[bool] = None
    remember_subtitle_selections: Optional[bool] = None
    """Gets or sets the subtitle language preference."""
    subtitle_language_preference: Optional[str] = None
    """An enum representing a subtitle playback mode."""
    subtitle_mode: Optional[SubtitleMode] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Configuration':
        assert isinstance(obj, dict)
        audio_language_preference = from_union([from_str, from_none], obj.get("AudioLanguagePreference"))
        display_collections_view = from_union([from_bool, from_none], obj.get("DisplayCollectionsView"))
        display_missing_episodes = from_union([from_bool, from_none], obj.get("DisplayMissingEpisodes"))
        enable_local_password = from_union([from_bool, from_none], obj.get("EnableLocalPassword"))
        enable_next_episode_auto_play = from_union([from_bool, from_none], obj.get("EnableNextEpisodeAutoPlay"))
        grouped_folders = from_union([lambda x: from_list(from_str, x), from_none], obj.get("GroupedFolders"))
        hide_played_in_latest = from_union([from_bool, from_none], obj.get("HidePlayedInLatest"))
        latest_items_excludes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("LatestItemsExcludes"))
        my_media_excludes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MyMediaExcludes"))
        ordered_views = from_union([lambda x: from_list(from_str, x), from_none], obj.get("OrderedViews"))
        play_default_audio_track = from_union([from_bool, from_none], obj.get("PlayDefaultAudioTrack"))
        remember_audio_selections = from_union([from_bool, from_none], obj.get("RememberAudioSelections"))
        remember_subtitle_selections = from_union([from_bool, from_none], obj.get("RememberSubtitleSelections"))
        subtitle_language_preference = from_union([from_str, from_none], obj.get("SubtitleLanguagePreference"))
        subtitle_mode = from_union([SubtitleMode, from_none], obj.get("SubtitleMode"))
        return Configuration(audio_language_preference, display_collections_view, display_missing_episodes, enable_local_password, enable_next_episode_auto_play, grouped_folders, hide_played_in_latest, latest_items_excludes, my_media_excludes, ordered_views, play_default_audio_track, remember_audio_selections, remember_subtitle_selections, subtitle_language_preference, subtitle_mode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AudioLanguagePreference"] = from_union([from_str, from_none], self.audio_language_preference)
        result["DisplayCollectionsView"] = from_union([from_bool, from_none], self.display_collections_view)
        result["DisplayMissingEpisodes"] = from_union([from_bool, from_none], self.display_missing_episodes)
        result["EnableLocalPassword"] = from_union([from_bool, from_none], self.enable_local_password)
        result["EnableNextEpisodeAutoPlay"] = from_union([from_bool, from_none], self.enable_next_episode_auto_play)
        result["GroupedFolders"] = from_union([lambda x: from_list(from_str, x), from_none], self.grouped_folders)
        result["HidePlayedInLatest"] = from_union([from_bool, from_none], self.hide_played_in_latest)
        result["LatestItemsExcludes"] = from_union([lambda x: from_list(from_str, x), from_none], self.latest_items_excludes)
        result["MyMediaExcludes"] = from_union([lambda x: from_list(from_str, x), from_none], self.my_media_excludes)
        result["OrderedViews"] = from_union([lambda x: from_list(from_str, x), from_none], self.ordered_views)
        result["PlayDefaultAudioTrack"] = from_union([from_bool, from_none], self.play_default_audio_track)
        result["RememberAudioSelections"] = from_union([from_bool, from_none], self.remember_audio_selections)
        result["RememberSubtitleSelections"] = from_union([from_bool, from_none], self.remember_subtitle_selections)
        result["SubtitleLanguagePreference"] = from_union([from_str, from_none], self.subtitle_language_preference)
        result["SubtitleMode"] = from_union([lambda x: to_enum(SubtitleMode, x), from_none], self.subtitle_mode)
        return result


