from util.from_type import *
from data_classes.send_command_type_enum import SendCommandTypeEnum


@dataclass
class SendCommand:
    """Class SendCommand."""
    """Gets the command."""
    command: Optional[SendCommandTypeEnum] = None
    """Gets the UTC time when this command has been emitted."""
    emitted_at: Optional[datetime] = None
    """Gets the group identifier."""
    group_id: Optional[UUID] = None
    """Gets the playlist identifier of the playing item."""
    playlist_item_id: Optional[UUID] = None
    """Gets the position ticks."""
    position_ticks: Optional[int] = None
    """Gets or sets the UTC time when to execute the command."""
    when: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SendCommand':
        assert isinstance(obj, dict)
        command = from_union([SendCommandTypeEnum, from_none], obj.get("Command"))
        emitted_at = from_union([from_datetime, from_none], obj.get("EmittedAt"))
        group_id = from_union([lambda x: UUID(x), from_none], obj.get("GroupId"))
        playlist_item_id = from_union([lambda x: UUID(x), from_none], obj.get("PlaylistItemId"))
        position_ticks = from_union([from_int, from_none], obj.get("PositionTicks"))
        when = from_union([from_datetime, from_none], obj.get("When"))
        return SendCommand(command, emitted_at, group_id, playlist_item_id, position_ticks, when)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Command"] = from_union([lambda x: to_enum(SendCommandTypeEnum, x), from_none], self.command)
        result["EmittedAt"] = from_union([lambda x: x.isoformat(), from_none], self.emitted_at)
        result["GroupId"] = from_union([lambda x: str(x), from_none], self.group_id)
        result["PlaylistItemId"] = from_union([lambda x: str(x), from_none], self.playlist_item_id)
        result["PositionTicks"] = from_union([from_int, from_none], self.position_ticks)
        result["When"] = from_union([lambda x: x.isoformat(), from_none], self.when)
        return result


