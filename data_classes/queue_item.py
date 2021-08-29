from util.from_type import *


@dataclass
class QueueItem:
    id: Optional[UUID] = None
    playlist_item_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QueueItem':
        assert isinstance(obj, dict)
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        playlist_item_id = from_union([from_str, from_none], obj.get("PlaylistItemId"))
        return QueueItem(id, playlist_item_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["PlaylistItemId"] = from_union([from_str, from_none], self.playlist_item_id)
        return result


