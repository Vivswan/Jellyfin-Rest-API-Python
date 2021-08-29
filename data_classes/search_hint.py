from util.from_type import *


@dataclass
class SearchHint:
    """Class SearchHintResult."""
    """Gets or sets the album."""
    album: Optional[str] = None
    """Gets or sets the album artist."""
    album_artist: Optional[str] = None
    album_id: Optional[UUID] = None
    """Gets or sets the artists."""
    artists: Optional[List[str]] = None
    """Gets or sets the backdrop image item identifier."""
    backdrop_image_item_id: Optional[str] = None
    """Gets or sets the backdrop image tag."""
    backdrop_image_tag: Optional[str] = None
    """Gets or sets the channel identifier."""
    channel_id: Optional[UUID] = None
    """Gets or sets the name of the channel."""
    channel_name: Optional[str] = None
    end_date: Optional[datetime] = None
    """Gets or sets the episode count."""
    episode_count: Optional[int] = None
    id: Optional[UUID] = None
    """Gets or sets the index number."""
    index_number: Optional[int] = None
    is_folder: Optional[bool] = None
    """Gets or sets the item id."""
    item_id: Optional[UUID] = None
    """Gets or sets the matched term."""
    matched_term: Optional[str] = None
    """Gets or sets the type of the media."""
    media_type: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the parent index number."""
    parent_index_number: Optional[int] = None
    """Gets or sets the primary image aspect ratio."""
    primary_image_aspect_ratio: Optional[float] = None
    """Gets or sets the image tag."""
    primary_image_tag: Optional[str] = None
    """Gets or sets the production year."""
    production_year: Optional[int] = None
    """Gets or sets the run time ticks."""
    run_time_ticks: Optional[int] = None
    """Gets or sets the series."""
    series: Optional[str] = None
    """Gets or sets the song count."""
    song_count: Optional[int] = None
    start_date: Optional[datetime] = None
    status: Optional[str] = None
    """Gets or sets the thumb image item identifier."""
    thumb_image_item_id: Optional[str] = None
    """Gets or sets the thumb image tag."""
    thumb_image_tag: Optional[str] = None
    """Gets or sets the type."""
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchHint':
        assert isinstance(obj, dict)
        album = from_union([from_str, from_none], obj.get("Album"))
        album_artist = from_union([from_str, from_none], obj.get("AlbumArtist"))
        album_id = from_union([lambda x: UUID(x), from_none], obj.get("AlbumId"))
        artists = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Artists"))
        backdrop_image_item_id = from_union([from_str, from_none], obj.get("BackdropImageItemId"))
        backdrop_image_tag = from_union([from_str, from_none], obj.get("BackdropImageTag"))
        channel_id = from_union([lambda x: UUID(x), from_none], obj.get("ChannelId"))
        channel_name = from_union([from_str, from_none], obj.get("ChannelName"))
        end_date = from_union([from_datetime, from_none], obj.get("EndDate"))
        episode_count = from_union([from_int, from_none], obj.get("EpisodeCount"))
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        index_number = from_union([from_int, from_none], obj.get("IndexNumber"))
        is_folder = from_union([from_bool, from_none], obj.get("IsFolder"))
        item_id = from_union([lambda x: UUID(x), from_none], obj.get("ItemId"))
        matched_term = from_union([from_str, from_none], obj.get("MatchedTerm"))
        media_type = from_union([from_str, from_none], obj.get("MediaType"))
        name = from_union([from_str, from_none], obj.get("Name"))
        parent_index_number = from_union([from_int, from_none], obj.get("ParentIndexNumber"))
        primary_image_aspect_ratio = from_union([from_float, from_none], obj.get("PrimaryImageAspectRatio"))
        primary_image_tag = from_union([from_str, from_none], obj.get("PrimaryImageTag"))
        production_year = from_union([from_int, from_none], obj.get("ProductionYear"))
        run_time_ticks = from_union([from_int, from_none], obj.get("RunTimeTicks"))
        series = from_union([from_str, from_none], obj.get("Series"))
        song_count = from_union([from_int, from_none], obj.get("SongCount"))
        start_date = from_union([from_datetime, from_none], obj.get("StartDate"))
        status = from_union([from_str, from_none], obj.get("Status"))
        thumb_image_item_id = from_union([from_str, from_none], obj.get("ThumbImageItemId"))
        thumb_image_tag = from_union([from_str, from_none], obj.get("ThumbImageTag"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return SearchHint(album, album_artist, album_id, artists, backdrop_image_item_id, backdrop_image_tag, channel_id, channel_name, end_date, episode_count, id, index_number, is_folder, item_id, matched_term, media_type, name, parent_index_number, primary_image_aspect_ratio, primary_image_tag, production_year, run_time_ticks, series, song_count, start_date, status, thumb_image_item_id, thumb_image_tag, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Album"] = from_union([from_str, from_none], self.album)
        result["AlbumArtist"] = from_union([from_str, from_none], self.album_artist)
        result["AlbumId"] = from_union([lambda x: str(x), from_none], self.album_id)
        result["Artists"] = from_union([lambda x: from_list(from_str, x), from_none], self.artists)
        result["BackdropImageItemId"] = from_union([from_str, from_none], self.backdrop_image_item_id)
        result["BackdropImageTag"] = from_union([from_str, from_none], self.backdrop_image_tag)
        result["ChannelId"] = from_union([lambda x: str(x), from_none], self.channel_id)
        result["ChannelName"] = from_union([from_str, from_none], self.channel_name)
        result["EndDate"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
        result["EpisodeCount"] = from_union([from_int, from_none], self.episode_count)
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["IndexNumber"] = from_union([from_int, from_none], self.index_number)
        result["IsFolder"] = from_union([from_bool, from_none], self.is_folder)
        result["ItemId"] = from_union([lambda x: str(x), from_none], self.item_id)
        result["MatchedTerm"] = from_union([from_str, from_none], self.matched_term)
        result["MediaType"] = from_union([from_str, from_none], self.media_type)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ParentIndexNumber"] = from_union([from_int, from_none], self.parent_index_number)
        result["PrimaryImageAspectRatio"] = from_union([to_float, from_none], self.primary_image_aspect_ratio)
        result["PrimaryImageTag"] = from_union([from_str, from_none], self.primary_image_tag)
        result["ProductionYear"] = from_union([from_int, from_none], self.production_year)
        result["RunTimeTicks"] = from_union([from_int, from_none], self.run_time_ticks)
        result["Series"] = from_union([from_str, from_none], self.series)
        result["SongCount"] = from_union([from_int, from_none], self.song_count)
        result["StartDate"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        result["Status"] = from_union([from_str, from_none], self.status)
        result["ThumbImageItemId"] = from_union([from_str, from_none], self.thumb_image_item_id)
        result["ThumbImageTag"] = from_union([from_str, from_none], self.thumb_image_tag)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


