from data_classes.audio import Audio
from data_classes.base_item_dto_image_blur_hashes import BaseItemDtoImageBlurHashes
from data_classes.base_item_person import BaseItemPerson
from data_classes.channel_type import ChannelType
from data_classes.chapter_info import ChapterInfo
from data_classes.day_of_week_element import DayOfWeekElement
from data_classes.external_u_r_l import ExternalURL
from data_classes.i_s_o_type import ISOType
from data_classes.image_orientation import ImageOrientation
from data_classes.location_type import LocationType
from data_classes.media_source import MediaSource
from data_classes.media_stream import MediaStream
from data_classes.media_u_r_l import MediaURL
from data_classes.metadata_field import MetadataField
from data_classes.name_g_u_i_d_pair import NameGUIDPair
from data_classes.play_access import PlayAccess
from data_classes.user import User
from data_classes.video3_d_format import Video3DFormat
from data_classes.video_type import VideoType
from util.from_type import *


@dataclass
class BaseItemDto:
    """This is strictly used as a data transfer object from the api layer.
    This holds information about a BaseItem in a format that is convenient for the client.
    
    Gets or sets the current program.
    
    Gets or sets the now playing item.
    
    Gets or sets the item.
    
    Gets or sets the program information.
    """
    """Gets or sets the air days."""
    air_days: Optional[List[DayOfWeekElement]] = None
    airs_after_season_number: Optional[int] = None
    airs_before_episode_number: Optional[int] = None
    airs_before_season_number: Optional[int] = None
    """Gets or sets the air time."""
    air_time: Optional[str] = None
    """Gets or sets the album."""
    album: Optional[str] = None
    """Gets or sets the album artist."""
    album_artist: Optional[str] = None
    """Gets or sets the album artists."""
    album_artists: Optional[List[NameGUIDPair]] = None
    """Gets or sets the album count."""
    album_count: Optional[int] = None
    """Gets or sets the album id."""
    album_id: Optional[UUID] = None
    """Gets or sets the album image tag."""
    album_primary_image_tag: Optional[str] = None
    altitude: Optional[float] = None
    aperture: Optional[float] = None
    artist_count: Optional[int] = None
    """Gets or sets the artist items."""
    artist_items: Optional[List[NameGUIDPair]] = None
    """Gets or sets the artists."""
    artists: Optional[List[str]] = None
    """Gets or sets the aspect ratio."""
    aspect_ratio: Optional[str] = None
    """Gets or sets the audio."""
    audio: Optional[Audio] = None
    """Gets or sets the backdrop image tags."""
    backdrop_image_tags: Optional[List[str]] = None
    camera_make: Optional[str] = None
    camera_model: Optional[str] = None
    can_delete: Optional[bool] = None
    can_download: Optional[bool] = None
    """Gets or sets the channel identifier."""
    channel_id: Optional[UUID] = None
    channel_name: Optional[str] = None
    channel_number: Optional[str] = None
    """Gets or sets the channel primary image tag."""
    channel_primary_image_tag: Optional[str] = None
    """Gets or sets the type of the channel."""
    channel_type: Optional[ChannelType] = None
    """Gets or sets the chapters."""
    chapters: Optional[List[ChapterInfo]] = None
    """Gets or sets the child count."""
    child_count: Optional[int] = None
    """Gets or sets the type of the collection."""
    collection_type: Optional[str] = None
    """Gets or sets the community rating."""
    community_rating: Optional[float] = None
    """Gets or sets the completion percentage."""
    completion_percentage: Optional[float] = None
    container: Optional[str] = None
    """Gets or sets the critic rating."""
    critic_rating: Optional[float] = None
    """Gets or sets the cumulative run time ticks."""
    cumulative_run_time_ticks: Optional[int] = None
    """Gets or sets the current program."""
    current_program: Optional['BaseItemDto'] = None
    """Gets or sets the custom rating."""
    custom_rating: Optional[str] = None
    """Gets or sets the date created."""
    date_created: Optional[datetime] = None
    date_last_media_added: Optional[datetime] = None
    """Gets or sets the display order."""
    display_order: Optional[str] = None
    """Gets or sets the display preferences id."""
    display_preferences_id: Optional[str] = None
    enable_media_source_display: Optional[bool] = None
    """Gets or sets the end date."""
    end_date: Optional[datetime] = None
    """Gets or sets the episode count."""
    episode_count: Optional[int] = None
    """Gets or sets the episode title."""
    episode_title: Optional[str] = None
    """Gets or sets the etag."""
    etag: Optional[str] = None
    exposure_time: Optional[float] = None
    """Gets or sets the external urls."""
    external_urls: Optional[List[ExternalURL]] = None
    extra_type: Optional[str] = None
    focal_length: Optional[float] = None
    forced_sort_name: Optional[str] = None
    genre_items: Optional[List[NameGUIDPair]] = None
    """Gets or sets the genres."""
    genres: Optional[List[str]] = None
    has_subtitles: Optional[bool] = None
    height: Optional[int] = None
    """Gets or sets the id."""
    id: Optional[UUID] = None
    """Gets or sets the blurhashes for the image tags.
    Maps image type to dictionary mapping image tag to blurhash value.
    """
    image_blur_hashes: Optional[BaseItemDtoImageBlurHashes] = None
    image_orientation: Optional[ImageOrientation] = None
    """Gets or sets the image tags."""
    image_tags: Optional[Dict[str, str]] = None
    """Gets or sets the index number."""
    index_number: Optional[int] = None
    """Gets or sets the index number end."""
    index_number_end: Optional[int] = None
    """Gets or sets a value indicating whether this instance is folder."""
    is_folder: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is HD."""
    is_hd: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is kids."""
    is_kids: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is live."""
    is_live: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is movie."""
    is_movie: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is news."""
    is_news: Optional[bool] = None
    iso_speed_rating: Optional[int] = None
    """Gets or sets the type of the iso."""
    iso_type: Optional[ISOType] = None
    """Gets or sets a value indicating whether this instance is place holder."""
    is_place_holder: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is premiere."""
    is_premiere: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is repeat."""
    is_repeat: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is series."""
    is_series: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is sports."""
    is_sports: Optional[bool] = None
    latitude: Optional[float] = None
    """Gets or sets the local trailer count."""
    local_trailer_count: Optional[int] = None
    """Gets or sets the type of the location."""
    location_type: Optional[LocationType] = None
    """Gets or sets a value indicating whether [enable internet providers]."""
    lock_data: Optional[bool] = None
    """Gets or sets the locked fields."""
    locked_fields: Optional[List[MetadataField]] = None
    longitude: Optional[float] = None
    media_source_count: Optional[int] = None
    """Gets or sets the media versions."""
    media_sources: Optional[List[MediaSource]] = None
    """Gets or sets the media streams."""
    media_streams: Optional[List[MediaStream]] = None
    """Gets or sets the type of the media."""
    media_type: Optional[str] = None
    """Gets or sets the movie count."""
    movie_count: Optional[int] = None
    """Gets or sets the music video count."""
    music_video_count: Optional[int] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the number."""
    number: Optional[str] = None
    """Gets or sets the official rating."""
    official_rating: Optional[str] = None
    original_title: Optional[str] = None
    """Gets or sets the overview."""
    overview: Optional[str] = None
    """Gets or sets the parent art image tag."""
    parent_art_image_tag: Optional[str] = None
    """If the item does not have a art, this will hold the Id of the Parent that has one."""
    parent_art_item_id: Optional[str] = None
    """Gets or sets the parent backdrop image tags."""
    parent_backdrop_image_tags: Optional[List[str]] = None
    """If the item does not have any backdrops, this will hold the Id of the Parent that has one."""
    parent_backdrop_item_id: Optional[str] = None
    """Gets or sets the parent id."""
    parent_id: Optional[UUID] = None
    """Gets or sets the parent index number."""
    parent_index_number: Optional[int] = None
    """Gets or sets the parent logo image tag."""
    parent_logo_image_tag: Optional[str] = None
    """If the item does not have a logo, this will hold the Id of the Parent that has one."""
    parent_logo_item_id: Optional[str] = None
    """Gets or sets the parent primary image item identifier."""
    parent_primary_image_item_id: Optional[str] = None
    """Gets or sets the parent primary image tag."""
    parent_primary_image_tag: Optional[str] = None
    """Gets or sets the parent thumb image tag."""
    parent_thumb_image_tag: Optional[str] = None
    """Gets or sets the parent thumb item id."""
    parent_thumb_item_id: Optional[str] = None
    """Gets or sets the part count."""
    part_count: Optional[int] = None
    """Gets or sets the path."""
    path: Optional[str] = None
    """Gets or sets the people."""
    people: Optional[List[BaseItemPerson]] = None
    """Gets or sets the play access."""
    play_access: Optional[PlayAccess] = None
    """Gets or sets the playlist item identifier."""
    playlist_item_id: Optional[str] = None
    preferred_metadata_country_code: Optional[str] = None
    preferred_metadata_language: Optional[str] = None
    """Gets or sets the premiere date."""
    premiere_date: Optional[datetime] = None
    """Gets or sets the primary image aspect ratio, after image enhancements."""
    primary_image_aspect_ratio: Optional[float] = None
    production_locations: Optional[List[str]] = None
    """Gets or sets the production year."""
    production_year: Optional[int] = None
    program_count: Optional[int] = None
    """Gets or sets the program identifier."""
    program_id: Optional[str] = None
    """Gets or sets the provider ids."""
    provider_ids: Optional[Dict[str, str]] = None
    """Gets or sets the recursive item count."""
    recursive_item_count: Optional[int] = None
    """Gets or sets the trailer urls."""
    remote_trailers: Optional[List[MediaURL]] = None
    """Gets or sets the run time ticks."""
    run_time_ticks: Optional[int] = None
    """Gets or sets the screenshot image tags."""
    screenshot_image_tags: Optional[List[str]] = None
    """Gets or sets the season identifier."""
    season_id: Optional[UUID] = None
    """Gets or sets the name of the season."""
    season_name: Optional[str] = None
    """Gets or sets the series count."""
    series_count: Optional[int] = None
    """Gets or sets the series id."""
    series_id: Optional[UUID] = None
    """Gets or sets the name of the series."""
    series_name: Optional[str] = None
    """Gets or sets the series primary image tag."""
    series_primary_image_tag: Optional[str] = None
    """Gets or sets the series studio."""
    series_studio: Optional[str] = None
    """Gets or sets the series thumb image tag."""
    series_thumb_image_tag: Optional[str] = None
    """Gets or sets the series timer identifier."""
    series_timer_id: Optional[str] = None
    """Gets or sets the server identifier."""
    server_id: Optional[str] = None
    shutter_speed: Optional[float] = None
    software: Optional[str] = None
    """Gets or sets the song count."""
    song_count: Optional[int] = None
    """Gets or sets the name of the sort."""
    sort_name: Optional[str] = None
    """Gets or sets the type of the source."""
    source_type: Optional[str] = None
    """Gets or sets the special feature count."""
    special_feature_count: Optional[int] = None
    """The start date of the recording, in UTC."""
    start_date: Optional[datetime] = None
    """Gets or sets the status."""
    status: Optional[str] = None
    """Gets or sets the studios."""
    studios: Optional[List[NameGUIDPair]] = None
    """Gets or sets a value indicating whether [supports synchronize]."""
    supports_sync: Optional[bool] = None
    """Gets or sets the taglines."""
    taglines: Optional[List[str]] = None
    """Gets or sets the tags."""
    tags: Optional[List[str]] = None
    """Gets or sets the timer identifier."""
    timer_id: Optional[str] = None
    """Gets or sets the trailer count."""
    trailer_count: Optional[int] = None
    """Gets or sets the type."""
    type: Optional[str] = None
    """User data for this item based on the user it's being requested for."""
    user_data: Optional[User] = None
    """Gets or sets the video3 D format."""
    video3_d_format: Optional[Video3DFormat] = None
    """Gets or sets the type of the video."""
    video_type: Optional[VideoType] = None
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BaseItemDto':
        assert isinstance(obj, dict)
        air_days = from_union([lambda x: from_list(DayOfWeekElement, x), from_none], obj.get("AirDays"))
        airs_after_season_number = from_union([from_int, from_none], obj.get("AirsAfterSeasonNumber"))
        airs_before_episode_number = from_union([from_int, from_none], obj.get("AirsBeforeEpisodeNumber"))
        airs_before_season_number = from_union([from_int, from_none], obj.get("AirsBeforeSeasonNumber"))
        air_time = from_union([from_str, from_none], obj.get("AirTime"))
        album = from_union([from_str, from_none], obj.get("Album"))
        album_artist = from_union([from_str, from_none], obj.get("AlbumArtist"))
        album_artists = from_union([lambda x: from_list(NameGUIDPair.from_dict, x), from_none], obj.get("AlbumArtists"))
        album_count = from_union([from_int, from_none], obj.get("AlbumCount"))
        album_id = from_union([lambda x: UUID(x), from_none], obj.get("AlbumId"))
        album_primary_image_tag = from_union([from_str, from_none], obj.get("AlbumPrimaryImageTag"))
        altitude = from_union([from_float, from_none], obj.get("Altitude"))
        aperture = from_union([from_float, from_none], obj.get("Aperture"))
        artist_count = from_union([from_int, from_none], obj.get("ArtistCount"))
        artist_items = from_union([lambda x: from_list(NameGUIDPair.from_dict, x), from_none], obj.get("ArtistItems"))
        artists = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Artists"))
        aspect_ratio = from_union([from_str, from_none], obj.get("AspectRatio"))
        audio = from_union([Audio, from_none], obj.get("Audio"))
        backdrop_image_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("BackdropImageTags"))
        camera_make = from_union([from_str, from_none], obj.get("CameraMake"))
        camera_model = from_union([from_str, from_none], obj.get("CameraModel"))
        can_delete = from_union([from_bool, from_none], obj.get("CanDelete"))
        can_download = from_union([from_bool, from_none], obj.get("CanDownload"))
        channel_id = from_union([lambda x: UUID(x), from_none], obj.get("ChannelId"))
        channel_name = from_union([from_str, from_none], obj.get("ChannelName"))
        channel_number = from_union([from_str, from_none], obj.get("ChannelNumber"))
        channel_primary_image_tag = from_union([from_str, from_none], obj.get("ChannelPrimaryImageTag"))
        channel_type = from_union([ChannelType, from_none], obj.get("ChannelType"))
        chapters = from_union([lambda x: from_list(ChapterInfo.from_dict, x), from_none], obj.get("Chapters"))
        child_count = from_union([from_int, from_none], obj.get("ChildCount"))
        collection_type = from_union([from_str, from_none], obj.get("CollectionType"))
        community_rating = from_union([from_float, from_none], obj.get("CommunityRating"))
        completion_percentage = from_union([from_float, from_none], obj.get("CompletionPercentage"))
        container = from_union([from_str, from_none], obj.get("Container"))
        critic_rating = from_union([from_float, from_none], obj.get("CriticRating"))
        cumulative_run_time_ticks = from_union([from_int, from_none], obj.get("CumulativeRunTimeTicks"))
        current_program = from_union([BaseItemDto.from_dict, from_none], obj.get("CurrentProgram"))
        custom_rating = from_union([from_str, from_none], obj.get("CustomRating"))
        date_created = from_union([from_datetime, from_none], obj.get("DateCreated"))
        date_last_media_added = from_union([from_datetime, from_none], obj.get("DateLastMediaAdded"))
        display_order = from_union([from_str, from_none], obj.get("DisplayOrder"))
        display_preferences_id = from_union([from_str, from_none], obj.get("DisplayPreferencesId"))
        enable_media_source_display = from_union([from_bool, from_none], obj.get("EnableMediaSourceDisplay"))
        end_date = from_union([from_datetime, from_none], obj.get("EndDate"))
        episode_count = from_union([from_int, from_none], obj.get("EpisodeCount"))
        episode_title = from_union([from_str, from_none], obj.get("EpisodeTitle"))
        etag = from_union([from_str, from_none], obj.get("Etag"))
        exposure_time = from_union([from_float, from_none], obj.get("ExposureTime"))
        external_urls = from_union([lambda x: from_list(ExternalURL.from_dict, x), from_none], obj.get("ExternalUrls"))
        extra_type = from_union([from_str, from_none], obj.get("ExtraType"))
        focal_length = from_union([from_float, from_none], obj.get("FocalLength"))
        forced_sort_name = from_union([from_str, from_none], obj.get("ForcedSortName"))
        genre_items = from_union([lambda x: from_list(NameGUIDPair.from_dict, x), from_none], obj.get("GenreItems"))
        genres = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Genres"))
        has_subtitles = from_union([from_bool, from_none], obj.get("HasSubtitles"))
        height = from_union([from_int, from_none], obj.get("Height"))
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        image_blur_hashes = from_union([BaseItemDtoImageBlurHashes.from_dict, from_none], obj.get("ImageBlurHashes"))
        image_orientation = from_union([ImageOrientation, from_none], obj.get("ImageOrientation"))
        image_tags = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ImageTags"))
        index_number = from_union([from_int, from_none], obj.get("IndexNumber"))
        index_number_end = from_union([from_int, from_none], obj.get("IndexNumberEnd"))
        is_folder = from_union([from_bool, from_none], obj.get("IsFolder"))
        is_hd = from_union([from_bool, from_none], obj.get("IsHD"))
        is_kids = from_union([from_bool, from_none], obj.get("IsKids"))
        is_live = from_union([from_bool, from_none], obj.get("IsLive"))
        is_movie = from_union([from_bool, from_none], obj.get("IsMovie"))
        is_news = from_union([from_bool, from_none], obj.get("IsNews"))
        iso_speed_rating = from_union([from_int, from_none], obj.get("IsoSpeedRating"))
        iso_type = from_union([ISOType, from_none], obj.get("IsoType"))
        is_place_holder = from_union([from_bool, from_none], obj.get("IsPlaceHolder"))
        is_premiere = from_union([from_bool, from_none], obj.get("IsPremiere"))
        is_repeat = from_union([from_bool, from_none], obj.get("IsRepeat"))
        is_series = from_union([from_bool, from_none], obj.get("IsSeries"))
        is_sports = from_union([from_bool, from_none], obj.get("IsSports"))
        latitude = from_union([from_float, from_none], obj.get("Latitude"))
        local_trailer_count = from_union([from_int, from_none], obj.get("LocalTrailerCount"))
        location_type = from_union([LocationType, from_none], obj.get("LocationType"))
        lock_data = from_union([from_bool, from_none], obj.get("LockData"))
        locked_fields = from_union([lambda x: from_list(MetadataField, x), from_none], obj.get("LockedFields"))
        longitude = from_union([from_float, from_none], obj.get("Longitude"))
        media_source_count = from_union([from_int, from_none], obj.get("MediaSourceCount"))
        media_sources = from_union([lambda x: from_list(MediaSource.from_dict, x), from_none], obj.get("MediaSources"))
        media_streams = from_union([lambda x: from_list(MediaStream.from_dict, x), from_none], obj.get("MediaStreams"))
        media_type = from_union([from_str, from_none], obj.get("MediaType"))
        movie_count = from_union([from_int, from_none], obj.get("MovieCount"))
        music_video_count = from_union([from_int, from_none], obj.get("MusicVideoCount"))
        name = from_union([from_str, from_none], obj.get("Name"))
        number = from_union([from_str, from_none], obj.get("Number"))
        official_rating = from_union([from_str, from_none], obj.get("OfficialRating"))
        original_title = from_union([from_str, from_none], obj.get("OriginalTitle"))
        overview = from_union([from_str, from_none], obj.get("Overview"))
        parent_art_image_tag = from_union([from_str, from_none], obj.get("ParentArtImageTag"))
        parent_art_item_id = from_union([from_str, from_none], obj.get("ParentArtItemId"))
        parent_backdrop_image_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ParentBackdropImageTags"))
        parent_backdrop_item_id = from_union([from_str, from_none], obj.get("ParentBackdropItemId"))
        parent_id = from_union([lambda x: UUID(x), from_none], obj.get("ParentId"))
        parent_index_number = from_union([from_int, from_none], obj.get("ParentIndexNumber"))
        parent_logo_image_tag = from_union([from_str, from_none], obj.get("ParentLogoImageTag"))
        parent_logo_item_id = from_union([from_str, from_none], obj.get("ParentLogoItemId"))
        parent_primary_image_item_id = from_union([from_str, from_none], obj.get("ParentPrimaryImageItemId"))
        parent_primary_image_tag = from_union([from_str, from_none], obj.get("ParentPrimaryImageTag"))
        parent_thumb_image_tag = from_union([from_str, from_none], obj.get("ParentThumbImageTag"))
        parent_thumb_item_id = from_union([from_str, from_none], obj.get("ParentThumbItemId"))
        part_count = from_union([from_int, from_none], obj.get("PartCount"))
        path = from_union([from_str, from_none], obj.get("Path"))
        people = from_union([lambda x: from_list(BaseItemPerson.from_dict, x), from_none], obj.get("People"))
        play_access = from_union([PlayAccess, from_none], obj.get("PlayAccess"))
        playlist_item_id = from_union([from_str, from_none], obj.get("PlaylistItemId"))
        preferred_metadata_country_code = from_union([from_str, from_none], obj.get("PreferredMetadataCountryCode"))
        preferred_metadata_language = from_union([from_str, from_none], obj.get("PreferredMetadataLanguage"))
        premiere_date = from_union([from_datetime, from_none], obj.get("PremiereDate"))
        primary_image_aspect_ratio = from_union([from_float, from_none], obj.get("PrimaryImageAspectRatio"))
        production_locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ProductionLocations"))
        production_year = from_union([from_int, from_none], obj.get("ProductionYear"))
        program_count = from_union([from_int, from_none], obj.get("ProgramCount"))
        program_id = from_union([from_str, from_none], obj.get("ProgramId"))
        provider_ids = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ProviderIds"))
        recursive_item_count = from_union([from_int, from_none], obj.get("RecursiveItemCount"))
        remote_trailers = from_union([lambda x: from_list(MediaURL.from_dict, x), from_none], obj.get("RemoteTrailers"))
        run_time_ticks = from_union([from_int, from_none], obj.get("RunTimeTicks"))
        screenshot_image_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ScreenshotImageTags"))
        season_id = from_union([lambda x: UUID(x), from_none], obj.get("SeasonId"))
        season_name = from_union([from_str, from_none], obj.get("SeasonName"))
        series_count = from_union([from_int, from_none], obj.get("SeriesCount"))
        series_id = from_union([lambda x: UUID(x), from_none], obj.get("SeriesId"))
        series_name = from_union([from_str, from_none], obj.get("SeriesName"))
        series_primary_image_tag = from_union([from_str, from_none], obj.get("SeriesPrimaryImageTag"))
        series_studio = from_union([from_str, from_none], obj.get("SeriesStudio"))
        series_thumb_image_tag = from_union([from_str, from_none], obj.get("SeriesThumbImageTag"))
        series_timer_id = from_union([from_str, from_none], obj.get("SeriesTimerId"))
        server_id = from_union([from_str, from_none], obj.get("ServerId"))
        shutter_speed = from_union([from_float, from_none], obj.get("ShutterSpeed"))
        software = from_union([from_str, from_none], obj.get("Software"))
        song_count = from_union([from_int, from_none], obj.get("SongCount"))
        sort_name = from_union([from_str, from_none], obj.get("SortName"))
        source_type = from_union([from_str, from_none], obj.get("SourceType"))
        special_feature_count = from_union([from_int, from_none], obj.get("SpecialFeatureCount"))
        start_date = from_union([from_datetime, from_none], obj.get("StartDate"))
        status = from_union([from_str, from_none], obj.get("Status"))
        studios = from_union([lambda x: from_list(NameGUIDPair.from_dict, x), from_none], obj.get("Studios"))
        supports_sync = from_union([from_bool, from_none], obj.get("SupportsSync"))
        taglines = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Taglines"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Tags"))
        timer_id = from_union([from_str, from_none], obj.get("TimerId"))
        trailer_count = from_union([from_int, from_none], obj.get("TrailerCount"))
        type = from_union([from_str, from_none], obj.get("Type"))
        user_data = from_union([User.from_dict, from_none], obj.get("UserData"))
        video3_d_format = from_union([Video3DFormat, from_none], obj.get("Video3DFormat"))
        video_type = from_union([VideoType, from_none], obj.get("VideoType"))
        width = from_union([from_int, from_none], obj.get("Width"))
        return BaseItemDto(air_days, airs_after_season_number, airs_before_episode_number, airs_before_season_number, air_time, album, album_artist, album_artists, album_count, album_id, album_primary_image_tag, altitude, aperture, artist_count, artist_items, artists, aspect_ratio, audio, backdrop_image_tags, camera_make, camera_model, can_delete, can_download, channel_id, channel_name, channel_number, channel_primary_image_tag, channel_type, chapters, child_count, collection_type, community_rating, completion_percentage, container, critic_rating, cumulative_run_time_ticks, current_program, custom_rating, date_created, date_last_media_added, display_order, display_preferences_id, enable_media_source_display, end_date, episode_count, episode_title, etag, exposure_time, external_urls, extra_type, focal_length, forced_sort_name, genre_items, genres, has_subtitles, height, id, image_blur_hashes, image_orientation, image_tags, index_number, index_number_end, is_folder, is_hd, is_kids, is_live, is_movie, is_news, iso_speed_rating, iso_type, is_place_holder, is_premiere, is_repeat, is_series, is_sports, latitude, local_trailer_count, location_type, lock_data, locked_fields, longitude, media_source_count, media_sources, media_streams, media_type, movie_count, music_video_count, name, number, official_rating, original_title, overview, parent_art_image_tag, parent_art_item_id, parent_backdrop_image_tags, parent_backdrop_item_id, parent_id, parent_index_number, parent_logo_image_tag, parent_logo_item_id, parent_primary_image_item_id, parent_primary_image_tag, parent_thumb_image_tag, parent_thumb_item_id, part_count, path, people, play_access, playlist_item_id, preferred_metadata_country_code, preferred_metadata_language, premiere_date, primary_image_aspect_ratio, production_locations, production_year, program_count, program_id, provider_ids, recursive_item_count, remote_trailers, run_time_ticks, screenshot_image_tags, season_id, season_name, series_count, series_id, series_name, series_primary_image_tag, series_studio, series_thumb_image_tag, series_timer_id, server_id, shutter_speed, software, song_count, sort_name, source_type, special_feature_count, start_date, status, studios, supports_sync, taglines, tags, timer_id, trailer_count, type, user_data, video3_d_format, video_type, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AirDays"] = from_union([lambda x: from_list(lambda x: to_enum(DayOfWeekElement, x), x), from_none], self.air_days)
        result["AirsAfterSeasonNumber"] = from_union([from_int, from_none], self.airs_after_season_number)
        result["AirsBeforeEpisodeNumber"] = from_union([from_int, from_none], self.airs_before_episode_number)
        result["AirsBeforeSeasonNumber"] = from_union([from_int, from_none], self.airs_before_season_number)
        result["AirTime"] = from_union([from_str, from_none], self.air_time)
        result["Album"] = from_union([from_str, from_none], self.album)
        result["AlbumArtist"] = from_union([from_str, from_none], self.album_artist)
        result["AlbumArtists"] = from_union([lambda x: from_list(lambda x: to_class(NameGUIDPair, x), x), from_none], self.album_artists)
        result["AlbumCount"] = from_union([from_int, from_none], self.album_count)
        result["AlbumId"] = from_union([lambda x: str(x), from_none], self.album_id)
        result["AlbumPrimaryImageTag"] = from_union([from_str, from_none], self.album_primary_image_tag)
        result["Altitude"] = from_union([to_float, from_none], self.altitude)
        result["Aperture"] = from_union([to_float, from_none], self.aperture)
        result["ArtistCount"] = from_union([from_int, from_none], self.artist_count)
        result["ArtistItems"] = from_union([lambda x: from_list(lambda x: to_class(NameGUIDPair, x), x), from_none], self.artist_items)
        result["Artists"] = from_union([lambda x: from_list(from_str, x), from_none], self.artists)
        result["AspectRatio"] = from_union([from_str, from_none], self.aspect_ratio)
        result["Audio"] = from_union([lambda x: to_enum(Audio, x), from_none], self.audio)
        result["BackdropImageTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.backdrop_image_tags)
        result["CameraMake"] = from_union([from_str, from_none], self.camera_make)
        result["CameraModel"] = from_union([from_str, from_none], self.camera_model)
        result["CanDelete"] = from_union([from_bool, from_none], self.can_delete)
        result["CanDownload"] = from_union([from_bool, from_none], self.can_download)
        result["ChannelId"] = from_union([lambda x: str(x), from_none], self.channel_id)
        result["ChannelName"] = from_union([from_str, from_none], self.channel_name)
        result["ChannelNumber"] = from_union([from_str, from_none], self.channel_number)
        result["ChannelPrimaryImageTag"] = from_union([from_str, from_none], self.channel_primary_image_tag)
        result["ChannelType"] = from_union([lambda x: to_enum(ChannelType, x), from_none], self.channel_type)
        result["Chapters"] = from_union([lambda x: from_list(lambda x: to_class(ChapterInfo, x), x), from_none], self.chapters)
        result["ChildCount"] = from_union([from_int, from_none], self.child_count)
        result["CollectionType"] = from_union([from_str, from_none], self.collection_type)
        result["CommunityRating"] = from_union([to_float, from_none], self.community_rating)
        result["CompletionPercentage"] = from_union([to_float, from_none], self.completion_percentage)
        result["Container"] = from_union([from_str, from_none], self.container)
        result["CriticRating"] = from_union([to_float, from_none], self.critic_rating)
        result["CumulativeRunTimeTicks"] = from_union([from_int, from_none], self.cumulative_run_time_ticks)
        result["CurrentProgram"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.current_program)
        result["CustomRating"] = from_union([from_str, from_none], self.custom_rating)
        result["DateCreated"] = from_union([lambda x: x.isoformat(), from_none], self.date_created)
        result["DateLastMediaAdded"] = from_union([lambda x: x.isoformat(), from_none], self.date_last_media_added)
        result["DisplayOrder"] = from_union([from_str, from_none], self.display_order)
        result["DisplayPreferencesId"] = from_union([from_str, from_none], self.display_preferences_id)
        result["EnableMediaSourceDisplay"] = from_union([from_bool, from_none], self.enable_media_source_display)
        result["EndDate"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
        result["EpisodeCount"] = from_union([from_int, from_none], self.episode_count)
        result["EpisodeTitle"] = from_union([from_str, from_none], self.episode_title)
        result["Etag"] = from_union([from_str, from_none], self.etag)
        result["ExposureTime"] = from_union([to_float, from_none], self.exposure_time)
        result["ExternalUrls"] = from_union([lambda x: from_list(lambda x: to_class(ExternalURL, x), x), from_none], self.external_urls)
        result["ExtraType"] = from_union([from_str, from_none], self.extra_type)
        result["FocalLength"] = from_union([to_float, from_none], self.focal_length)
        result["ForcedSortName"] = from_union([from_str, from_none], self.forced_sort_name)
        result["GenreItems"] = from_union([lambda x: from_list(lambda x: to_class(NameGUIDPair, x), x), from_none], self.genre_items)
        result["Genres"] = from_union([lambda x: from_list(from_str, x), from_none], self.genres)
        result["HasSubtitles"] = from_union([from_bool, from_none], self.has_subtitles)
        result["Height"] = from_union([from_int, from_none], self.height)
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["ImageBlurHashes"] = from_union([lambda x: to_class(BaseItemDtoImageBlurHashes, x), from_none], self.image_blur_hashes)
        result["ImageOrientation"] = from_union([lambda x: to_enum(ImageOrientation, x), from_none], self.image_orientation)
        result["ImageTags"] = from_union([lambda x: from_dict(from_str, x), from_none], self.image_tags)
        result["IndexNumber"] = from_union([from_int, from_none], self.index_number)
        result["IndexNumberEnd"] = from_union([from_int, from_none], self.index_number_end)
        result["IsFolder"] = from_union([from_bool, from_none], self.is_folder)
        result["IsHD"] = from_union([from_bool, from_none], self.is_hd)
        result["IsKids"] = from_union([from_bool, from_none], self.is_kids)
        result["IsLive"] = from_union([from_bool, from_none], self.is_live)
        result["IsMovie"] = from_union([from_bool, from_none], self.is_movie)
        result["IsNews"] = from_union([from_bool, from_none], self.is_news)
        result["IsoSpeedRating"] = from_union([from_int, from_none], self.iso_speed_rating)
        result["IsoType"] = from_union([lambda x: to_enum(ISOType, x), from_none], self.iso_type)
        result["IsPlaceHolder"] = from_union([from_bool, from_none], self.is_place_holder)
        result["IsPremiere"] = from_union([from_bool, from_none], self.is_premiere)
        result["IsRepeat"] = from_union([from_bool, from_none], self.is_repeat)
        result["IsSeries"] = from_union([from_bool, from_none], self.is_series)
        result["IsSports"] = from_union([from_bool, from_none], self.is_sports)
        result["Latitude"] = from_union([to_float, from_none], self.latitude)
        result["LocalTrailerCount"] = from_union([from_int, from_none], self.local_trailer_count)
        result["LocationType"] = from_union([lambda x: to_enum(LocationType, x), from_none], self.location_type)
        result["LockData"] = from_union([from_bool, from_none], self.lock_data)
        result["LockedFields"] = from_union([lambda x: from_list(lambda x: to_enum(MetadataField, x), x), from_none], self.locked_fields)
        result["Longitude"] = from_union([to_float, from_none], self.longitude)
        result["MediaSourceCount"] = from_union([from_int, from_none], self.media_source_count)
        result["MediaSources"] = from_union([lambda x: from_list(lambda x: to_class(MediaSource, x), x), from_none], self.media_sources)
        result["MediaStreams"] = from_union([lambda x: from_list(lambda x: to_class(MediaStream, x), x), from_none], self.media_streams)
        result["MediaType"] = from_union([from_str, from_none], self.media_type)
        result["MovieCount"] = from_union([from_int, from_none], self.movie_count)
        result["MusicVideoCount"] = from_union([from_int, from_none], self.music_video_count)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Number"] = from_union([from_str, from_none], self.number)
        result["OfficialRating"] = from_union([from_str, from_none], self.official_rating)
        result["OriginalTitle"] = from_union([from_str, from_none], self.original_title)
        result["Overview"] = from_union([from_str, from_none], self.overview)
        result["ParentArtImageTag"] = from_union([from_str, from_none], self.parent_art_image_tag)
        result["ParentArtItemId"] = from_union([from_str, from_none], self.parent_art_item_id)
        result["ParentBackdropImageTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.parent_backdrop_image_tags)
        result["ParentBackdropItemId"] = from_union([from_str, from_none], self.parent_backdrop_item_id)
        result["ParentId"] = from_union([lambda x: str(x), from_none], self.parent_id)
        result["ParentIndexNumber"] = from_union([from_int, from_none], self.parent_index_number)
        result["ParentLogoImageTag"] = from_union([from_str, from_none], self.parent_logo_image_tag)
        result["ParentLogoItemId"] = from_union([from_str, from_none], self.parent_logo_item_id)
        result["ParentPrimaryImageItemId"] = from_union([from_str, from_none], self.parent_primary_image_item_id)
        result["ParentPrimaryImageTag"] = from_union([from_str, from_none], self.parent_primary_image_tag)
        result["ParentThumbImageTag"] = from_union([from_str, from_none], self.parent_thumb_image_tag)
        result["ParentThumbItemId"] = from_union([from_str, from_none], self.parent_thumb_item_id)
        result["PartCount"] = from_union([from_int, from_none], self.part_count)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["People"] = from_union([lambda x: from_list(lambda x: to_class(BaseItemPerson, x), x), from_none], self.people)
        result["PlayAccess"] = from_union([lambda x: to_enum(PlayAccess, x), from_none], self.play_access)
        result["PlaylistItemId"] = from_union([from_str, from_none], self.playlist_item_id)
        result["PreferredMetadataCountryCode"] = from_union([from_str, from_none], self.preferred_metadata_country_code)
        result["PreferredMetadataLanguage"] = from_union([from_str, from_none], self.preferred_metadata_language)
        result["PremiereDate"] = from_union([lambda x: x.isoformat(), from_none], self.premiere_date)
        result["PrimaryImageAspectRatio"] = from_union([to_float, from_none], self.primary_image_aspect_ratio)
        result["ProductionLocations"] = from_union([lambda x: from_list(from_str, x), from_none], self.production_locations)
        result["ProductionYear"] = from_union([from_int, from_none], self.production_year)
        result["ProgramCount"] = from_union([from_int, from_none], self.program_count)
        result["ProgramId"] = from_union([from_str, from_none], self.program_id)
        result["ProviderIds"] = from_union([lambda x: from_dict(from_str, x), from_none], self.provider_ids)
        result["RecursiveItemCount"] = from_union([from_int, from_none], self.recursive_item_count)
        result["RemoteTrailers"] = from_union([lambda x: from_list(lambda x: to_class(MediaURL, x), x), from_none], self.remote_trailers)
        result["RunTimeTicks"] = from_union([from_int, from_none], self.run_time_ticks)
        result["ScreenshotImageTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.screenshot_image_tags)
        result["SeasonId"] = from_union([lambda x: str(x), from_none], self.season_id)
        result["SeasonName"] = from_union([from_str, from_none], self.season_name)
        result["SeriesCount"] = from_union([from_int, from_none], self.series_count)
        result["SeriesId"] = from_union([lambda x: str(x), from_none], self.series_id)
        result["SeriesName"] = from_union([from_str, from_none], self.series_name)
        result["SeriesPrimaryImageTag"] = from_union([from_str, from_none], self.series_primary_image_tag)
        result["SeriesStudio"] = from_union([from_str, from_none], self.series_studio)
        result["SeriesThumbImageTag"] = from_union([from_str, from_none], self.series_thumb_image_tag)
        result["SeriesTimerId"] = from_union([from_str, from_none], self.series_timer_id)
        result["ServerId"] = from_union([from_str, from_none], self.server_id)
        result["ShutterSpeed"] = from_union([to_float, from_none], self.shutter_speed)
        result["Software"] = from_union([from_str, from_none], self.software)
        result["SongCount"] = from_union([from_int, from_none], self.song_count)
        result["SortName"] = from_union([from_str, from_none], self.sort_name)
        result["SourceType"] = from_union([from_str, from_none], self.source_type)
        result["SpecialFeatureCount"] = from_union([from_int, from_none], self.special_feature_count)
        result["StartDate"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        result["Status"] = from_union([from_str, from_none], self.status)
        result["Studios"] = from_union([lambda x: from_list(lambda x: to_class(NameGUIDPair, x), x), from_none], self.studios)
        result["SupportsSync"] = from_union([from_bool, from_none], self.supports_sync)
        result["Taglines"] = from_union([lambda x: from_list(from_str, x), from_none], self.taglines)
        result["Tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        result["TimerId"] = from_union([from_str, from_none], self.timer_id)
        result["TrailerCount"] = from_union([from_int, from_none], self.trailer_count)
        result["Type"] = from_union([from_str, from_none], self.type)
        result["UserData"] = from_union([lambda x: to_class(User, x), from_none], self.user_data)
        result["Video3DFormat"] = from_union([lambda x: to_enum(Video3DFormat, x), from_none], self.video3_d_format)
        result["VideoType"] = from_union([lambda x: to_enum(VideoType, x), from_none], self.video_type)
        result["Width"] = from_union([from_int, from_none], self.width)
        return result


