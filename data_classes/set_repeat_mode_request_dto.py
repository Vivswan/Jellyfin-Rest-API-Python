from util.from_type import *
from data_classes.group_repeat_mode_enum import GroupRepeatModeEnum


@dataclass
class SetRepeatModeRequestDto:
    """Class SetRepeatModeRequestDto."""
    """Gets or sets the repeat mode."""
    mode: Optional[GroupRepeatModeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SetRepeatModeRequestDto':
        assert isinstance(obj, dict)
        mode = from_union([GroupRepeatModeEnum, from_none], obj.get("Mode"))
        return SetRepeatModeRequestDto(mode)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Mode"] = from_union([lambda x: to_enum(GroupRepeatModeEnum, x), from_none], self.mode)
        return result


