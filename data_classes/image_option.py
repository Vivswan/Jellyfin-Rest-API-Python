from data_classes.image_type_element import ImageTypeElement
from util.from_type import *


@dataclass
class ImageOption:
    """Gets or sets the limit."""
    limit: Optional[int] = None
    """Gets or sets the minimum width."""
    min_width: Optional[int] = None
    """Gets or sets the type."""
    type: Optional[ImageTypeElement] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ImageOption':
        assert isinstance(obj, dict)
        limit = from_union([from_int, from_none], obj.get("Limit"))
        min_width = from_union([from_int, from_none], obj.get("MinWidth"))
        type = from_union([ImageTypeElement, from_none], obj.get("Type"))
        return ImageOption(limit, min_width, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Limit"] = from_union([from_int, from_none], self.limit)
        result["MinWidth"] = from_union([from_int, from_none], self.min_width)
        result["Type"] = from_union([lambda x: to_enum(ImageTypeElement, x), from_none], self.type)
        return result


