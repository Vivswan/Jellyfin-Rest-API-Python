from util.from_type import *


@dataclass
class PingRequestDto:
    """Class PingRequestDto."""
    """Gets or sets the ping time."""
    ping: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PingRequestDto':
        assert isinstance(obj, dict)
        ping = from_union([from_int, from_none], obj.get("Ping"))
        return PingRequestDto(ping)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Ping"] = from_union([from_int, from_none], self.ping)
        return result


