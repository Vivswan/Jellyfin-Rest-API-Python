from util.from_type import *
from data_classes.remote_image_info import RemoteImageInfo


@dataclass
class RemoteImageResult:
    """Class RemoteImageResult."""
    """Gets or sets the images."""
    images: Optional[List[RemoteImageInfo]] = None
    """Gets or sets the providers."""
    providers: Optional[List[str]] = None
    """Gets or sets the total record count."""
    total_record_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoteImageResult':
        assert isinstance(obj, dict)
        images = from_union([lambda x: from_list(RemoteImageInfo.from_dict, x), from_none], obj.get("Images"))
        providers = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Providers"))
        total_record_count = from_union([from_int, from_none], obj.get("TotalRecordCount"))
        return RemoteImageResult(images, providers, total_record_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Images"] = from_union([lambda x: from_list(lambda x: to_class(RemoteImageInfo, x), x), from_none], self.images)
        result["Providers"] = from_union([lambda x: from_list(from_str, x), from_none], self.providers)
        result["TotalRecordCount"] = from_union([from_int, from_none], self.total_record_count)
        return result


