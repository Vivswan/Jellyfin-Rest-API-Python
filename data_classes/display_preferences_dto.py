from data_classes.scroll_direction import ScrollDirection
from data_classes.sort_order import SortOrder
from util.from_type import *


@dataclass
class DisplayPreferencesDto:
    """Defines the display preferences for any item that supports them (usually Folders)."""
    """Gets or sets the client."""
    client: Optional[str] = None
    """Gets or sets the custom prefs."""
    custom_prefs: Optional[Dict[str, str]] = None
    """Gets or sets the user id."""
    id: Optional[str] = None
    """Gets or sets the index by."""
    index_by: Optional[str] = None
    """Gets or sets the height of the primary image."""
    primary_image_height: Optional[int] = None
    """Gets or sets the width of the primary image."""
    primary_image_width: Optional[int] = None
    """Gets or sets a value indicating whether [remember indexing]."""
    remember_indexing: Optional[bool] = None
    """Gets or sets a value indicating whether [remember sorting]."""
    remember_sorting: Optional[bool] = None
    """Gets or sets the scroll direction."""
    scroll_direction: Optional[ScrollDirection] = None
    """Gets or sets a value indicating whether to show backdrops on this item."""
    show_backdrop: Optional[bool] = None
    """Gets or sets a value indicating whether [show sidebar]."""
    show_sidebar: Optional[bool] = None
    """Gets or sets the sort by."""
    sort_by: Optional[str] = None
    """Gets or sets the sort order."""
    sort_order: Optional[SortOrder] = None
    """Gets or sets the type of the view."""
    view_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DisplayPreferencesDto':
        assert isinstance(obj, dict)
        client = from_union([from_str, from_none], obj.get("Client"))
        custom_prefs = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("CustomPrefs"))
        id = from_union([from_str, from_none], obj.get("Id"))
        index_by = from_union([from_str, from_none], obj.get("IndexBy"))
        primary_image_height = from_union([from_int, from_none], obj.get("PrimaryImageHeight"))
        primary_image_width = from_union([from_int, from_none], obj.get("PrimaryImageWidth"))
        remember_indexing = from_union([from_bool, from_none], obj.get("RememberIndexing"))
        remember_sorting = from_union([from_bool, from_none], obj.get("RememberSorting"))
        scroll_direction = from_union([ScrollDirection, from_none], obj.get("ScrollDirection"))
        show_backdrop = from_union([from_bool, from_none], obj.get("ShowBackdrop"))
        show_sidebar = from_union([from_bool, from_none], obj.get("ShowSidebar"))
        sort_by = from_union([from_str, from_none], obj.get("SortBy"))
        sort_order = from_union([SortOrder, from_none], obj.get("SortOrder"))
        view_type = from_union([from_str, from_none], obj.get("ViewType"))
        return DisplayPreferencesDto(client, custom_prefs, id, index_by, primary_image_height, primary_image_width, remember_indexing, remember_sorting, scroll_direction, show_backdrop, show_sidebar, sort_by, sort_order, view_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Client"] = from_union([from_str, from_none], self.client)
        result["CustomPrefs"] = from_union([lambda x: from_dict(from_str, x), from_none], self.custom_prefs)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IndexBy"] = from_union([from_str, from_none], self.index_by)
        result["PrimaryImageHeight"] = from_union([from_int, from_none], self.primary_image_height)
        result["PrimaryImageWidth"] = from_union([from_int, from_none], self.primary_image_width)
        result["RememberIndexing"] = from_union([from_bool, from_none], self.remember_indexing)
        result["RememberSorting"] = from_union([from_bool, from_none], self.remember_sorting)
        result["ScrollDirection"] = from_union([lambda x: to_enum(ScrollDirection, x), from_none], self.scroll_direction)
        result["ShowBackdrop"] = from_union([from_bool, from_none], self.show_backdrop)
        result["ShowSidebar"] = from_union([from_bool, from_none], self.show_sidebar)
        result["SortBy"] = from_union([from_str, from_none], self.sort_by)
        result["SortOrder"] = from_union([lambda x: to_enum(SortOrder, x), from_none], self.sort_order)
        result["ViewType"] = from_union([from_str, from_none], self.view_type)
        return result


