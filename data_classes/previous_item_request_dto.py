from util.from_type import *


@dataclass
class PreviousItemRequestDto:
    """Class PreviousItemRequestDto."""
    """Gets or sets the playing item identifier."""
    playlist_item_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PreviousItemRequestDto':
        assert isinstance(obj, dict)
        playlist_item_id = from_union([lambda x: UUID(x), from_none], obj.get("PlaylistItemId"))
        return PreviousItemRequestDto(playlist_item_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["PlaylistItemId"] = from_union([lambda x: str(x), from_none], self.playlist_item_id)
        return result


