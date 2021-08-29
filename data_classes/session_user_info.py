from util.from_type import *


@dataclass
class SessionUserInfo:
    """Class SessionUserInfo."""
    """Gets or sets the user identifier."""
    user_id: Optional[UUID] = None
    """Gets or sets the name of the user."""
    user_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SessionUserInfo':
        assert isinstance(obj, dict)
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        user_name = from_union([from_str, from_none], obj.get("UserName"))
        return SessionUserInfo(user_id, user_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        result["UserName"] = from_union([from_str, from_none], self.user_name)
        return result


