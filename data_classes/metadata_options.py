from util.from_type import *


@dataclass
class MetadataOptions:
    """Class MetadataOptions."""
    disabled_image_fetchers: Optional[List[str]] = None
    disabled_metadata_fetchers: Optional[List[str]] = None
    disabled_metadata_savers: Optional[List[str]] = None
    image_fetcher_order: Optional[List[str]] = None
    item_type: Optional[str] = None
    local_metadata_reader_order: Optional[List[str]] = None
    metadata_fetcher_order: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MetadataOptions':
        assert isinstance(obj, dict)
        disabled_image_fetchers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("DisabledImageFetchers"))
        disabled_metadata_fetchers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("DisabledMetadataFetchers"))
        disabled_metadata_savers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("DisabledMetadataSavers"))
        image_fetcher_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ImageFetcherOrder"))
        item_type = from_union([from_str, from_none], obj.get("ItemType"))
        local_metadata_reader_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("LocalMetadataReaderOrder"))
        metadata_fetcher_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MetadataFetcherOrder"))
        return MetadataOptions(disabled_image_fetchers, disabled_metadata_fetchers, disabled_metadata_savers, image_fetcher_order, item_type, local_metadata_reader_order, metadata_fetcher_order)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DisabledImageFetchers"] = from_union([lambda x: from_list(from_str, x), from_none], self.disabled_image_fetchers)
        result["DisabledMetadataFetchers"] = from_union([lambda x: from_list(from_str, x), from_none], self.disabled_metadata_fetchers)
        result["DisabledMetadataSavers"] = from_union([lambda x: from_list(from_str, x), from_none], self.disabled_metadata_savers)
        result["ImageFetcherOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.image_fetcher_order)
        result["ItemType"] = from_union([from_str, from_none], self.item_type)
        result["LocalMetadataReaderOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.local_metadata_reader_order)
        result["MetadataFetcherOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.metadata_fetcher_order)
        return result


