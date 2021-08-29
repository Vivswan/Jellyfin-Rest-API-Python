from util.from_type import *


@dataclass
class IgnoreWaitRequestDto:
    """Class IgnoreWaitRequestDto."""
    """Gets or sets a value indicating whether the client should be ignored."""
    ignore_wait: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IgnoreWaitRequestDto':
        assert isinstance(obj, dict)
        ignore_wait = from_union([from_bool, from_none], obj.get("IgnoreWait"))
        return IgnoreWaitRequestDto(ignore_wait)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IgnoreWait"] = from_union([from_bool, from_none], self.ignore_wait)
        return result


