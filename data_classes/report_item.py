
from util.from_type import *


@dataclass
class ReportItem:
    custom_tag: Optional[str] = None
    id: Optional[str] = None
    image: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReportItem':
        assert isinstance(obj, dict)
        custom_tag = from_union([from_str, from_none], obj.get("CustomTag"))
        id = from_union([from_str, from_none], obj.get("Id"))
        image = from_union([from_str, from_none], obj.get("Image"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return ReportItem(custom_tag, id, image, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CustomTag"] = from_union([from_str, from_none], self.custom_tag)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Image"] = from_union([from_str, from_none], self.image)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


