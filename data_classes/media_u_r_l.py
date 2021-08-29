from util.from_type import *


@dataclass
class MediaURL:
    name: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaURL':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        url = from_union([from_str, from_none], obj.get("Url"))
        return MediaURL(name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Url"] = from_union([from_str, from_none], self.url)
        return result


