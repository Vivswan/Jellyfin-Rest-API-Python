from util.from_type import *


@dataclass
class CreatePlaylistDto:
    """Create new playlist dto."""
    """Gets or sets item ids to add to the playlist."""
    ids: Optional[List[UUID]] = None
    """Gets or sets the media type."""
    media_type: Optional[str] = None
    """Gets or sets the name of the new playlist."""
    name: Optional[str] = None
    """Gets or sets the user id."""
    user_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreatePlaylistDto':
        assert isinstance(obj, dict)
        ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("Ids"))
        media_type = from_union([from_str, from_none], obj.get("MediaType"))
        name = from_union([from_str, from_none], obj.get("Name"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        return CreatePlaylistDto(ids, media_type, name, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Ids"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.ids)
        result["MediaType"] = from_union([from_str, from_none], self.media_type)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        return result


