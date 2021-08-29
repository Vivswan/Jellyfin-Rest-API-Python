from data_classes.session_info import SessionInfo
from data_classes.user_dto_class import UserDtoClass
from util.from_type import *


@dataclass
class AuthenticationResult:
    access_token: Optional[str] = None
    server_id: Optional[str] = None
    """Class SessionInfo."""
    session_info: Optional[SessionInfo] = None
    """Class UserDto."""
    user: Optional[UserDtoClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationResult':
        assert isinstance(obj, dict)
        access_token = from_union([from_str, from_none], obj.get("AccessToken"))
        server_id = from_union([from_str, from_none], obj.get("ServerId"))
        session_info = from_union([SessionInfo.from_dict, from_none], obj.get("SessionInfo"))
        user = from_union([UserDtoClass.from_dict, from_none], obj.get("User"))
        return AuthenticationResult(access_token, server_id, session_info, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AccessToken"] = from_union([from_str, from_none], self.access_token)
        result["ServerId"] = from_union([from_str, from_none], self.server_id)
        result["SessionInfo"] = from_union([lambda x: to_class(SessionInfo, x), from_none], self.session_info)
        result["User"] = from_union([lambda x: to_class(UserDtoClass, x), from_none], self.user)
        return result


