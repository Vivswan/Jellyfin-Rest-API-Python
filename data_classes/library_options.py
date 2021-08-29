from data_classes.path_info import PathInfo
from data_classes.type_options import TypeOptions
from util.from_type import *


@dataclass
class LibraryOptions:
    """Gets or sets library options."""
    automatic_refresh_interval_days: Optional[int] = None
    disabled_local_metadata_readers: Optional[List[str]] = None
    disabled_subtitle_fetchers: Optional[List[str]] = None
    enable_automatic_series_grouping: Optional[bool] = None
    enable_chapter_image_extraction: Optional[bool] = None
    enable_embedded_episode_infos: Optional[bool] = None
    enable_embedded_titles: Optional[bool] = None
    enable_internet_providers: Optional[bool] = None
    enable_photos: Optional[bool] = None
    enable_realtime_monitor: Optional[bool] = None
    extract_chapter_images_during_library_scan: Optional[bool] = None
    local_metadata_reader_order: Optional[List[str]] = None
    """Gets or sets the metadata country code."""
    metadata_country_code: Optional[str] = None
    metadata_savers: Optional[List[str]] = None
    path_infos: Optional[List[PathInfo]] = None
    """Gets or sets the preferred metadata language."""
    preferred_metadata_language: Optional[str] = None
    require_perfect_subtitle_match: Optional[bool] = None
    save_local_metadata: Optional[bool] = None
    save_subtitles_with_media: Optional[bool] = None
    season_zero_display_name: Optional[str] = None
    skip_subtitles_if_audio_track_matches: Optional[bool] = None
    skip_subtitles_if_embedded_subtitles_present: Optional[bool] = None
    subtitle_download_languages: Optional[List[str]] = None
    subtitle_fetcher_order: Optional[List[str]] = None
    type_options: Optional[List[TypeOptions]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LibraryOptions':
        assert isinstance(obj, dict)
        automatic_refresh_interval_days = from_union([from_int, from_none], obj.get("AutomaticRefreshIntervalDays"))
        disabled_local_metadata_readers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("DisabledLocalMetadataReaders"))
        disabled_subtitle_fetchers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("DisabledSubtitleFetchers"))
        enable_automatic_series_grouping = from_union([from_bool, from_none], obj.get("EnableAutomaticSeriesGrouping"))
        enable_chapter_image_extraction = from_union([from_bool, from_none], obj.get("EnableChapterImageExtraction"))
        enable_embedded_episode_infos = from_union([from_bool, from_none], obj.get("EnableEmbeddedEpisodeInfos"))
        enable_embedded_titles = from_union([from_bool, from_none], obj.get("EnableEmbeddedTitles"))
        enable_internet_providers = from_union([from_bool, from_none], obj.get("EnableInternetProviders"))
        enable_photos = from_union([from_bool, from_none], obj.get("EnablePhotos"))
        enable_realtime_monitor = from_union([from_bool, from_none], obj.get("EnableRealtimeMonitor"))
        extract_chapter_images_during_library_scan = from_union([from_bool, from_none], obj.get("ExtractChapterImagesDuringLibraryScan"))
        local_metadata_reader_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("LocalMetadataReaderOrder"))
        metadata_country_code = from_union([from_str, from_none], obj.get("MetadataCountryCode"))
        metadata_savers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MetadataSavers"))
        path_infos = from_union([lambda x: from_list(PathInfo.from_dict, x), from_none], obj.get("PathInfos"))
        preferred_metadata_language = from_union([from_str, from_none], obj.get("PreferredMetadataLanguage"))
        require_perfect_subtitle_match = from_union([from_bool, from_none], obj.get("RequirePerfectSubtitleMatch"))
        save_local_metadata = from_union([from_bool, from_none], obj.get("SaveLocalMetadata"))
        save_subtitles_with_media = from_union([from_bool, from_none], obj.get("SaveSubtitlesWithMedia"))
        season_zero_display_name = from_union([from_str, from_none], obj.get("SeasonZeroDisplayName"))
        skip_subtitles_if_audio_track_matches = from_union([from_bool, from_none], obj.get("SkipSubtitlesIfAudioTrackMatches"))
        skip_subtitles_if_embedded_subtitles_present = from_union([from_bool, from_none], obj.get("SkipSubtitlesIfEmbeddedSubtitlesPresent"))
        subtitle_download_languages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SubtitleDownloadLanguages"))
        subtitle_fetcher_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SubtitleFetcherOrder"))
        type_options = from_union([lambda x: from_list(TypeOptions.from_dict, x), from_none], obj.get("TypeOptions"))
        return LibraryOptions(automatic_refresh_interval_days, disabled_local_metadata_readers, disabled_subtitle_fetchers, enable_automatic_series_grouping, enable_chapter_image_extraction, enable_embedded_episode_infos, enable_embedded_titles, enable_internet_providers, enable_photos, enable_realtime_monitor, extract_chapter_images_during_library_scan, local_metadata_reader_order, metadata_country_code, metadata_savers, path_infos, preferred_metadata_language, require_perfect_subtitle_match, save_local_metadata, save_subtitles_with_media, season_zero_display_name, skip_subtitles_if_audio_track_matches, skip_subtitles_if_embedded_subtitles_present, subtitle_download_languages, subtitle_fetcher_order, type_options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AutomaticRefreshIntervalDays"] = from_union([from_int, from_none], self.automatic_refresh_interval_days)
        result["DisabledLocalMetadataReaders"] = from_union([lambda x: from_list(from_str, x), from_none], self.disabled_local_metadata_readers)
        result["DisabledSubtitleFetchers"] = from_union([lambda x: from_list(from_str, x), from_none], self.disabled_subtitle_fetchers)
        result["EnableAutomaticSeriesGrouping"] = from_union([from_bool, from_none], self.enable_automatic_series_grouping)
        result["EnableChapterImageExtraction"] = from_union([from_bool, from_none], self.enable_chapter_image_extraction)
        result["EnableEmbeddedEpisodeInfos"] = from_union([from_bool, from_none], self.enable_embedded_episode_infos)
        result["EnableEmbeddedTitles"] = from_union([from_bool, from_none], self.enable_embedded_titles)
        result["EnableInternetProviders"] = from_union([from_bool, from_none], self.enable_internet_providers)
        result["EnablePhotos"] = from_union([from_bool, from_none], self.enable_photos)
        result["EnableRealtimeMonitor"] = from_union([from_bool, from_none], self.enable_realtime_monitor)
        result["ExtractChapterImagesDuringLibraryScan"] = from_union([from_bool, from_none], self.extract_chapter_images_during_library_scan)
        result["LocalMetadataReaderOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.local_metadata_reader_order)
        result["MetadataCountryCode"] = from_union([from_str, from_none], self.metadata_country_code)
        result["MetadataSavers"] = from_union([lambda x: from_list(from_str, x), from_none], self.metadata_savers)
        result["PathInfos"] = from_union([lambda x: from_list(lambda x: to_class(PathInfo, x), x), from_none], self.path_infos)
        result["PreferredMetadataLanguage"] = from_union([from_str, from_none], self.preferred_metadata_language)
        result["RequirePerfectSubtitleMatch"] = from_union([from_bool, from_none], self.require_perfect_subtitle_match)
        result["SaveLocalMetadata"] = from_union([from_bool, from_none], self.save_local_metadata)
        result["SaveSubtitlesWithMedia"] = from_union([from_bool, from_none], self.save_subtitles_with_media)
        result["SeasonZeroDisplayName"] = from_union([from_str, from_none], self.season_zero_display_name)
        result["SkipSubtitlesIfAudioTrackMatches"] = from_union([from_bool, from_none], self.skip_subtitles_if_audio_track_matches)
        result["SkipSubtitlesIfEmbeddedSubtitlesPresent"] = from_union([from_bool, from_none], self.skip_subtitles_if_embedded_subtitles_present)
        result["SubtitleDownloadLanguages"] = from_union([lambda x: from_list(from_str, x), from_none], self.subtitle_download_languages)
        result["SubtitleFetcherOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.subtitle_fetcher_order)
        result["TypeOptions"] = from_union([lambda x: from_list(lambda x: to_class(TypeOptions, x), x), from_none], self.type_options)
        return result


