from data_classes.image_type_element import ImageTypeElement
from util.from_type import *


@dataclass
class ImageProviderInfo:
    """Class ImageProviderInfo."""
    """Gets the name."""
    name: Optional[str] = None
    """Gets the supported image types."""
    supported_images: Optional[List[ImageTypeElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageProviderInfo':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        supported_images = from_union([lambda x: from_list(ImageTypeElement, x), from_none], obj.get("SupportedImages"))
        return ImageProviderInfo(name, supported_images)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["SupportedImages"] = from_union([lambda x: from_list(lambda x: to_enum(ImageTypeElement, x), x), from_none], self.supported_images)
        return result


