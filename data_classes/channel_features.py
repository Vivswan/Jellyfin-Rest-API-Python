from data_classes.channel_item_sort_field import ChannelItemSortField
from data_classes.channel_media_content_type import ChannelMediaContentType
from data_classes.channel_media_type_element import ChannelMediaTypeElement
from util.from_type import *


@dataclass
class ChannelFeatures:
    """Gets or sets the automatic refresh levels."""
    auto_refresh_levels: Optional[int] = None
    """Gets or sets a value indicating whether this instance can filter."""
    can_filter: Optional[bool] = None
    """Gets or sets a value indicating whether this instance can search."""
    can_search: Optional[bool] = None
    """Gets or sets the content types."""
    content_types: Optional[List[ChannelMediaContentType]] = None
    """Gets or sets the default sort orders."""
    default_sort_fields: Optional[List[ChannelItemSortField]] = None
    """Gets or sets the identifier."""
    id: Optional[str] = None
    """Represents the maximum number of records the channel allows retrieving at a time."""
    max_page_size: Optional[int] = None
    """Gets or sets the media types."""
    media_types: Optional[List[ChannelMediaTypeElement]] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets a value indicating whether [supports content downloading]."""
    supports_content_downloading: Optional[bool] = None
    """Gets or sets a value indicating whether [supports latest media]."""
    supports_latest_media: Optional[bool] = None
    """Indicates if a sort ascending/descending toggle is supported or not."""
    supports_sort_order_toggle: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelFeatures':
        assert isinstance(obj, dict)
        auto_refresh_levels = from_union([from_int, from_none], obj.get("AutoRefreshLevels"))
        can_filter = from_union([from_bool, from_none], obj.get("CanFilter"))
        can_search = from_union([from_bool, from_none], obj.get("CanSearch"))
        content_types = from_union([lambda x: from_list(ChannelMediaContentType, x), from_none], obj.get("ContentTypes"))
        default_sort_fields = from_union([lambda x: from_list(ChannelItemSortField, x), from_none], obj.get("DefaultSortFields"))
        id = from_union([from_str, from_none], obj.get("Id"))
        max_page_size = from_union([from_int, from_none], obj.get("MaxPageSize"))
        media_types = from_union([lambda x: from_list(ChannelMediaTypeElement, x), from_none], obj.get("MediaTypes"))
        name = from_union([from_str, from_none], obj.get("Name"))
        supports_content_downloading = from_union([from_bool, from_none], obj.get("SupportsContentDownloading"))
        supports_latest_media = from_union([from_bool, from_none], obj.get("SupportsLatestMedia"))
        supports_sort_order_toggle = from_union([from_bool, from_none], obj.get("SupportsSortOrderToggle"))
        return ChannelFeatures(auto_refresh_levels, can_filter, can_search, content_types, default_sort_fields, id, max_page_size, media_types, name, supports_content_downloading, supports_latest_media, supports_sort_order_toggle)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AutoRefreshLevels"] = from_union([from_int, from_none], self.auto_refresh_levels)
        result["CanFilter"] = from_union([from_bool, from_none], self.can_filter)
        result["CanSearch"] = from_union([from_bool, from_none], self.can_search)
        result["ContentTypes"] = from_union([lambda x: from_list(lambda x: to_enum(ChannelMediaContentType, x), x), from_none], self.content_types)
        result["DefaultSortFields"] = from_union([lambda x: from_list(lambda x: to_enum(ChannelItemSortField, x), x), from_none], self.default_sort_fields)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["MaxPageSize"] = from_union([from_int, from_none], self.max_page_size)
        result["MediaTypes"] = from_union([lambda x: from_list(lambda x: to_enum(ChannelMediaTypeElement, x), x), from_none], self.media_types)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["SupportsContentDownloading"] = from_union([from_bool, from_none], self.supports_content_downloading)
        result["SupportsLatestMedia"] = from_union([from_bool, from_none], self.supports_latest_media)
        result["SupportsSortOrderToggle"] = from_union([from_bool, from_none], self.supports_sort_order_toggle)
        return result


