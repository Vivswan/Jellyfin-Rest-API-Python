from util.from_type import *
from data_classes.method import Method


@dataclass
class SubtitleProfile:
    container: Optional[str] = None
    didl_mode: Optional[str] = None
    format: Optional[str] = None
    language: Optional[str] = None
    method: Optional[Method] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubtitleProfile':
        assert isinstance(obj, dict)
        container = from_union([from_str, from_none], obj.get("Container"))
        didl_mode = from_union([from_str, from_none], obj.get("DidlMode"))
        format = from_union([from_str, from_none], obj.get("Format"))
        language = from_union([from_str, from_none], obj.get("Language"))
        method = from_union([Method, from_none], obj.get("Method"))
        return SubtitleProfile(container, didl_mode, format, language, method)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Container"] = from_union([from_str, from_none], self.container)
        result["DidlMode"] = from_union([from_str, from_none], self.didl_mode)
        result["Format"] = from_union([from_str, from_none], self.format)
        result["Language"] = from_union([from_str, from_none], self.language)
        result["Method"] = from_union([lambda x: to_enum(Method, x), from_none], self.method)
        return result


