from util.from_type import *
from data_classes.image_option import ImageOption


@dataclass
class TypeOptions:
    image_fetcher_order: Optional[List[str]] = None
    image_fetchers: Optional[List[str]] = None
    image_options: Optional[List[ImageOption]] = None
    metadata_fetcher_order: Optional[List[str]] = None
    metadata_fetchers: Optional[List[str]] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TypeOptions':
        assert isinstance(obj, dict)
        image_fetcher_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ImageFetcherOrder"))
        image_fetchers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ImageFetchers"))
        image_options = from_union([lambda x: from_list(ImageOption.from_dict, x), from_none], obj.get("ImageOptions"))
        metadata_fetcher_order = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MetadataFetcherOrder"))
        metadata_fetchers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MetadataFetchers"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return TypeOptions(image_fetcher_order, image_fetchers, image_options, metadata_fetcher_order, metadata_fetchers, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ImageFetcherOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.image_fetcher_order)
        result["ImageFetchers"] = from_union([lambda x: from_list(from_str, x), from_none], self.image_fetchers)
        result["ImageOptions"] = from_union([lambda x: from_list(lambda x: to_class(ImageOption, x), x), from_none], self.image_options)
        result["MetadataFetcherOrder"] = from_union([lambda x: from_list(from_str, x), from_none], self.metadata_fetcher_order)
        result["MetadataFetchers"] = from_union([lambda x: from_list(from_str, x), from_none], self.metadata_fetchers)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


