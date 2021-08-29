from util.from_type import *
from data_classes.group_shuffle_mode_enum import GroupShuffleModeEnum


@dataclass
class SetShuffleModeRequestDto:
    """Class SetShuffleModeRequestDto."""
    """Gets or sets the shuffle mode."""
    mode: Optional[GroupShuffleModeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SetShuffleModeRequestDto':
        assert isinstance(obj, dict)
        mode = from_union([GroupShuffleModeEnum, from_none], obj.get("Mode"))
        return SetShuffleModeRequestDto(mode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Mode"] = from_union([lambda x: to_enum(GroupShuffleModeEnum, x), from_none], self.mode)
        return result


