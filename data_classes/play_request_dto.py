from util.from_type import *


@dataclass
class PlayRequestDto:
    """Class PlayRequestDto."""
    """Gets or sets the position of the playing item in the queue."""
    playing_item_position: Optional[int] = None
    """Gets or sets the playing queue."""
    playing_queue: Optional[List[UUID]] = None
    """Gets or sets the start position ticks."""
    start_position_ticks: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlayRequestDto':
        assert isinstance(obj, dict)
        playing_item_position = from_union([from_int, from_none], obj.get("PlayingItemPosition"))
        playing_queue = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("PlayingQueue"))
        start_position_ticks = from_union([from_int, from_none], obj.get("StartPositionTicks"))
        return PlayRequestDto(playing_item_position, playing_queue, start_position_ticks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlayingItemPosition"] = from_union([from_int, from_none], self.playing_item_position)
        result["PlayingQueue"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.playing_queue)
        result["StartPositionTicks"] = from_union([from_int, from_none], self.start_position_ticks)
        return result


