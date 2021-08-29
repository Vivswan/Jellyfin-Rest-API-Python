from data_classes.image_type_element import ImageTypeElement
from data_classes.item_fields import ItemFields
from data_classes.sort_order import SortOrder
from util.from_type import *


@dataclass
class GetProgramsDto:
    """Get programs dto."""
    """Gets or sets the channels to return guide information for."""
    channel_ids: Optional[List[UUID]] = None
    """Gets or sets include image information in output.
    Optional.
    """
    enable_images: Optional[bool] = None
    """Gets or sets the image types to include in the output.
    Optional.
    """
    enable_image_types: Optional[List[ImageTypeElement]] = None
    """Gets or sets a value indicating whether retrieve total record count."""
    enable_total_record_count: Optional[bool] = None
    """Gets or sets include user data.
    Optional.
    """
    enable_user_data: Optional[bool] = None
    """Gets or sets specify additional fields of information to return in the output. This
    allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres,
    HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds,
    PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
    Optional.
    """
    fields: Optional[List[ItemFields]] = None
    """Gets or sets the genre ids to return guide information for."""
    genre_ids: Optional[List[UUID]] = None
    """Gets or sets the genres to return guide information for."""
    genres: Optional[List[str]] = None
    """Gets or sets filter by programs that have completed airing, or not.
    Optional.
    """
    has_aired: Optional[bool] = None
    """Gets or sets the max number of images to return, per image type.
    Optional.
    """
    image_type_limit: Optional[int] = None
    """Gets or sets filter by programs that are currently airing, or not.
    Optional.
    """
    is_airing: Optional[bool] = None
    """Gets or sets filter for kids.
    Optional.
    """
    is_kids: Optional[bool] = None
    """Gets or sets filter for movies.
    Optional.
    """
    is_movie: Optional[bool] = None
    """Gets or sets filter for news.
    Optional.
    """
    is_news: Optional[bool] = None
    """Gets or sets filter for series.
    Optional.
    """
    is_series: Optional[bool] = None
    """Gets or sets filter for sports.
    Optional.
    """
    is_sports: Optional[bool] = None
    """Gets or sets filter by library series id.
    Optional.
    """
    library_series_id: Optional[UUID] = None
    """Gets or sets the maximum number of records to return.
    Optional.
    """
    limit: Optional[int] = None
    """Gets or sets the maximum premiere end date.
    Optional.
    """
    max_end_date: Optional[datetime] = None
    """Gets or sets the maximum premiere start date.
    Optional.
    """
    max_start_date: Optional[datetime] = None
    """Gets or sets the minimum premiere end date.
    Optional.
    """
    min_end_date: Optional[datetime] = None
    """Gets or sets the minimum premiere start date.
    Optional.
    """
    min_start_date: Optional[datetime] = None
    """Gets or sets filter by series timer id.
    Optional.
    """
    series_timer_id: Optional[str] = None
    """Gets or sets specify one or more sort orders, comma delimited. Options: Name, StartDate.
    Optional.
    """
    sort_by: Optional[List[str]] = None
    """Gets or sets sort Order - Ascending,Descending."""
    sort_order: Optional[List[SortOrder]] = None
    """Gets or sets the record index to start at. All items with a lower index will be dropped
    from the results.
    Optional.
    """
    start_index: Optional[int] = None
    """Gets or sets optional. Filter by user id."""
    user_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GetProgramsDto':
        assert isinstance(obj, dict)
        channel_ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("ChannelIds"))
        enable_images = from_union([from_bool, from_none], obj.get("EnableImages"))
        enable_image_types = from_union([lambda x: from_list(ImageTypeElement, x), from_none], obj.get("EnableImageTypes"))
        enable_total_record_count = from_union([from_bool, from_none], obj.get("EnableTotalRecordCount"))
        enable_user_data = from_union([from_bool, from_none], obj.get("EnableUserData"))
        fields = from_union([lambda x: from_list(ItemFields, x), from_none], obj.get("Fields"))
        genre_ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("GenreIds"))
        genres = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Genres"))
        has_aired = from_union([from_bool, from_none], obj.get("HasAired"))
        image_type_limit = from_union([from_int, from_none], obj.get("ImageTypeLimit"))
        is_airing = from_union([from_bool, from_none], obj.get("IsAiring"))
        is_kids = from_union([from_bool, from_none], obj.get("IsKids"))
        is_movie = from_union([from_bool, from_none], obj.get("IsMovie"))
        is_news = from_union([from_bool, from_none], obj.get("IsNews"))
        is_series = from_union([from_bool, from_none], obj.get("IsSeries"))
        is_sports = from_union([from_bool, from_none], obj.get("IsSports"))
        library_series_id = from_union([lambda x: UUID(x), from_none], obj.get("LibrarySeriesId"))
        limit = from_union([from_int, from_none], obj.get("Limit"))
        max_end_date = from_union([from_datetime, from_none], obj.get("MaxEndDate"))
        max_start_date = from_union([from_datetime, from_none], obj.get("MaxStartDate"))
        min_end_date = from_union([from_datetime, from_none], obj.get("MinEndDate"))
        min_start_date = from_union([from_datetime, from_none], obj.get("MinStartDate"))
        series_timer_id = from_union([from_str, from_none], obj.get("SeriesTimerId"))
        sort_by = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SortBy"))
        sort_order = from_union([lambda x: from_list(SortOrder, x), from_none], obj.get("SortOrder"))
        start_index = from_union([from_int, from_none], obj.get("StartIndex"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        return GetProgramsDto(channel_ids, enable_images, enable_image_types, enable_total_record_count, enable_user_data, fields, genre_ids, genres, has_aired, image_type_limit, is_airing, is_kids, is_movie, is_news, is_series, is_sports, library_series_id, limit, max_end_date, max_start_date, min_end_date, min_start_date, series_timer_id, sort_by, sort_order, start_index, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ChannelIds"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.channel_ids)
        result["EnableImages"] = from_union([from_bool, from_none], self.enable_images)
        result["EnableImageTypes"] = from_union([lambda x: from_list(lambda x: to_enum(ImageTypeElement, x), x), from_none], self.enable_image_types)
        result["EnableTotalRecordCount"] = from_union([from_bool, from_none], self.enable_total_record_count)
        result["EnableUserData"] = from_union([from_bool, from_none], self.enable_user_data)
        result["Fields"] = from_union([lambda x: from_list(lambda x: to_enum(ItemFields, x), x), from_none], self.fields)
        result["GenreIds"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.genre_ids)
        result["Genres"] = from_union([lambda x: from_list(from_str, x), from_none], self.genres)
        result["HasAired"] = from_union([from_bool, from_none], self.has_aired)
        result["ImageTypeLimit"] = from_union([from_int, from_none], self.image_type_limit)
        result["IsAiring"] = from_union([from_bool, from_none], self.is_airing)
        result["IsKids"] = from_union([from_bool, from_none], self.is_kids)
        result["IsMovie"] = from_union([from_bool, from_none], self.is_movie)
        result["IsNews"] = from_union([from_bool, from_none], self.is_news)
        result["IsSeries"] = from_union([from_bool, from_none], self.is_series)
        result["IsSports"] = from_union([from_bool, from_none], self.is_sports)
        result["LibrarySeriesId"] = from_union([lambda x: str(x), from_none], self.library_series_id)
        result["Limit"] = from_union([from_int, from_none], self.limit)
        result["MaxEndDate"] = from_union([lambda x: x.isoformat(), from_none], self.max_end_date)
        result["MaxStartDate"] = from_union([lambda x: x.isoformat(), from_none], self.max_start_date)
        result["MinEndDate"] = from_union([lambda x: x.isoformat(), from_none], self.min_end_date)
        result["MinStartDate"] = from_union([lambda x: x.isoformat(), from_none], self.min_start_date)
        result["SeriesTimerId"] = from_union([from_str, from_none], self.series_timer_id)
        result["SortBy"] = from_union([lambda x: from_list(from_str, x), from_none], self.sort_by)
        result["SortOrder"] = from_union([lambda x: from_list(lambda x: to_enum(SortOrder, x), x), from_none], self.sort_order)
        result["StartIndex"] = from_union([from_int, from_none], self.start_index)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        return result


