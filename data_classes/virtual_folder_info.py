from util.from_type import *
from data_classes.library_options import LibraryOptions
from data_classes.collection_type import CollectionType


@dataclass
class VirtualFolderInfo:
    """Used to hold information about a user's list of configured virtual folders."""
    """Gets or sets the type of the collection."""
    collection_type: Optional[CollectionType] = None
    """Gets or sets the item identifier."""
    item_id: Optional[str] = None
    library_options: Optional[LibraryOptions] = None
    """Gets or sets the locations."""
    locations: Optional[List[str]] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the primary image item identifier."""
    primary_image_item_id: Optional[str] = None
    refresh_progress: Optional[float] = None
    refresh_status: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VirtualFolderInfo':
        assert isinstance(obj, dict)
        collection_type = from_union([CollectionType, from_none], obj.get("CollectionType"))
        item_id = from_union([from_str, from_none], obj.get("ItemId"))
        library_options = from_union([LibraryOptions.from_dict, from_none], obj.get("LibraryOptions"))
        locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Locations"))
        name = from_union([from_str, from_none], obj.get("Name"))
        primary_image_item_id = from_union([from_str, from_none], obj.get("PrimaryImageItemId"))
        refresh_progress = from_union([from_float, from_none], obj.get("RefreshProgress"))
        refresh_status = from_union([from_str, from_none], obj.get("RefreshStatus"))
        return VirtualFolderInfo(collection_type, item_id, library_options, locations, name, primary_image_item_id, refresh_progress, refresh_status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CollectionType"] = from_union([lambda x: to_enum(CollectionType, x), from_none], self.collection_type)
        result["ItemId"] = from_union([from_str, from_none], self.item_id)
        result["LibraryOptions"] = from_union([lambda x: to_class(LibraryOptions, x), from_none], self.library_options)
        result["Locations"] = from_union([lambda x: from_list(from_str, x), from_none], self.locations)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["PrimaryImageItemId"] = from_union([from_str, from_none], self.primary_image_item_id)
        result["RefreshProgress"] = from_union([to_float, from_none], self.refresh_progress)
        result["RefreshStatus"] = from_union([from_str, from_none], self.refresh_status)
        return result


