from util.from_type import *


@dataclass
class SeekRequestDto:
    """Class SeekRequestDto."""
    """Gets or sets the position ticks."""
    position_ticks: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SeekRequestDto':
        assert isinstance(obj, dict)
        position_ticks = from_union([from_int, from_none], obj.get("PositionTicks"))
        return SeekRequestDto(position_ticks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PositionTicks"] = from_union([from_int, from_none], self.position_ticks)
        return result


