from util.from_type import *


@dataclass
class AuthenticateUserByName:
    """The authenticate user by name request body."""
    """Gets or sets the sha1-hashed password."""
    password: Optional[str] = None
    """Gets or sets the plain text password."""
    pw: Optional[str] = None
    """Gets or sets the username."""
    username: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticateUserByName':
        assert isinstance(obj, dict)
        password = from_union([from_str, from_none], obj.get("Password"))
        pw = from_union([from_str, from_none], obj.get("Pw"))
        username = from_union([from_str, from_none], obj.get("Username"))
        return AuthenticateUserByName(password, pw, username)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Password"] = from_union([from_str, from_none], self.password)
        result["Pw"] = from_union([from_str, from_none], self.pw)
        result["Username"] = from_union([from_str, from_none], self.username)
        return result


