from data_classes.album_info_class import AlbumInfoClass
from util.from_type import *


@dataclass
class AlbumInfoRemoteSearchQuery:
    """Gets or sets a value indicating whether disabled providers should be included."""
    include_disabled_providers: Optional[bool] = None
    item_id: Optional[UUID] = None
    search_info: Optional[AlbumInfoClass] = None
    """Will only search within the given provider when set."""
    search_provider_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AlbumInfoRemoteSearchQuery':
        assert isinstance(obj, dict)
        include_disabled_providers = from_union([from_bool, from_none], obj.get("IncludeDisabledProviders"))
        item_id = from_union([lambda x: UUID(x), from_none], obj.get("ItemId"))
        search_info = from_union([AlbumInfoClass.from_dict, from_none], obj.get("SearchInfo"))
        search_provider_name = from_union([from_str, from_none], obj.get("SearchProviderName"))
        return AlbumInfoRemoteSearchQuery(include_disabled_providers, item_id, search_info, search_provider_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IncludeDisabledProviders"] = from_union([from_bool, from_none], self.include_disabled_providers)
        result["ItemId"] = from_union([lambda x: str(x), from_none], self.item_id)
        result["SearchInfo"] = from_union([lambda x: to_class(AlbumInfoClass, x), from_none], self.search_info)
        result["SearchProviderName"] = from_union([from_str, from_none], self.search_provider_name)
        return result


