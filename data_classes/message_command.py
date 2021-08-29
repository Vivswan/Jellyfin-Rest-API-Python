from util.from_type import *


@dataclass
class MessageCommand:
    text: str
    header: Optional[str] = None
    timeout_ms: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageCommand':
        assert isinstance(obj, dict)
        text = from_str(obj.get("Text"))
        header = from_union([from_str, from_none], obj.get("Header"))
        timeout_ms = from_union([from_int, from_none], obj.get("TimeoutMs"))
        return MessageCommand(text, header, timeout_ms)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Text"] = from_str(self.text)
        result["Header"] = from_union([from_str, from_none], self.header)
        result["TimeoutMs"] = from_union([from_int, from_none], self.timeout_ms)
        return result


