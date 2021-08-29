from data_classes.image_type_element import ImageTypeElement
from util.from_type import *


@dataclass
class ImageInfo:
    """Class ImageInfo."""
    """Gets or sets the blurhash."""
    blur_hash: Optional[str] = None
    """Gets or sets the height."""
    height: Optional[int] = None
    """Gets or sets the index of the image."""
    image_index: Optional[int] = None
    """Gets or sets the image tag."""
    image_tag: Optional[str] = None
    """Gets or sets the type of the image."""
    image_type: Optional[ImageTypeElement] = None
    """Gets or sets the path."""
    path: Optional[str] = None
    """Gets or sets the size."""
    size: Optional[int] = None
    """Gets or sets the width."""
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageInfo':
        assert isinstance(obj, dict)
        blur_hash = from_union([from_str, from_none], obj.get("BlurHash"))
        height = from_union([from_int, from_none], obj.get("Height"))
        image_index = from_union([from_int, from_none], obj.get("ImageIndex"))
        image_tag = from_union([from_str, from_none], obj.get("ImageTag"))
        image_type = from_union([ImageTypeElement, from_none], obj.get("ImageType"))
        path = from_union([from_str, from_none], obj.get("Path"))
        size = from_union([from_int, from_none], obj.get("Size"))
        width = from_union([from_int, from_none], obj.get("Width"))
        return ImageInfo(blur_hash, height, image_index, image_tag, image_type, path, size, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BlurHash"] = from_union([from_str, from_none], self.blur_hash)
        result["Height"] = from_union([from_int, from_none], self.height)
        result["ImageIndex"] = from_union([from_int, from_none], self.image_index)
        result["ImageTag"] = from_union([from_str, from_none], self.image_tag)
        result["ImageType"] = from_union([lambda x: to_enum(ImageTypeElement, x), from_none], self.image_type)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["Size"] = from_union([from_int, from_none], self.size)
        result["Width"] = from_union([from_int, from_none], self.width)
        return result


