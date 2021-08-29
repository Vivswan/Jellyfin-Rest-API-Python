from util.from_type import *


@dataclass
class LibraryUpdateInfo:
    """Class LibraryUpdateInfo."""
    collection_folders: Optional[List[str]] = None
    """Gets or sets the folders added to."""
    folders_added_to: Optional[List[str]] = None
    """Gets or sets the folders removed from."""
    folders_removed_from: Optional[List[str]] = None
    is_empty: Optional[bool] = None
    """Gets or sets the items added."""
    items_added: Optional[List[str]] = None
    """Gets or sets the items removed."""
    items_removed: Optional[List[str]] = None
    """Gets or sets the items updated."""
    items_updated: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LibraryUpdateInfo':
        assert isinstance(obj, dict)
        collection_folders = from_union([lambda x: from_list(from_str, x), from_none], obj.get("CollectionFolders"))
        folders_added_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("FoldersAddedTo"))
        folders_removed_from = from_union([lambda x: from_list(from_str, x), from_none], obj.get("FoldersRemovedFrom"))
        is_empty = from_union([from_bool, from_none], obj.get("IsEmpty"))
        items_added = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ItemsAdded"))
        items_removed = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ItemsRemoved"))
        items_updated = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ItemsUpdated"))
        return LibraryUpdateInfo(collection_folders, folders_added_to, folders_removed_from, is_empty, items_added, items_removed, items_updated)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CollectionFolders"] = from_union([lambda x: from_list(from_str, x), from_none], self.collection_folders)
        result["FoldersAddedTo"] = from_union([lambda x: from_list(from_str, x), from_none], self.folders_added_to)
        result["FoldersRemovedFrom"] = from_union([lambda x: from_list(from_str, x), from_none], self.folders_removed_from)
        result["IsEmpty"] = from_union([from_bool, from_none], self.is_empty)
        result["ItemsAdded"] = from_union([lambda x: from_list(from_str, x), from_none], self.items_added)
        result["ItemsRemoved"] = from_union([lambda x: from_list(from_str, x), from_none], self.items_removed)
        result["ItemsUpdated"] = from_union([lambda x: from_list(from_str, x), from_none], self.items_updated)
        return result


