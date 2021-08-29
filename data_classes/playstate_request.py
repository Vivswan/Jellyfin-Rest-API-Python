from util.from_type import *
from data_classes.playstate_command_enum import PlaystateCommandEnum


@dataclass
class PlaystateRequest:
    """Enum PlaystateCommand."""
    command: Optional[PlaystateCommandEnum] = None
    """Gets or sets the controlling user identifier."""
    controlling_user_id: Optional[str] = None
    seek_position_ticks: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaystateRequest':
        assert isinstance(obj, dict)
        command = from_union([PlaystateCommandEnum, from_none], obj.get("Command"))
        controlling_user_id = from_union([from_str, from_none], obj.get("ControllingUserId"))
        seek_position_ticks = from_union([from_int, from_none], obj.get("SeekPositionTicks"))
        return PlaystateRequest(command, controlling_user_id, seek_position_ticks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Command"] = from_union([lambda x: to_enum(PlaystateCommandEnum, x), from_none], self.command)
        result["ControllingUserId"] = from_union([from_str, from_none], self.controlling_user_id)
        result["SeekPositionTicks"] = from_union([from_int, from_none], self.seek_position_ticks)
        return result


