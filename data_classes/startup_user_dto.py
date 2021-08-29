from util.from_type import *


@dataclass
class StartupUserDto:
    """The startup user DTO."""
    """Gets or sets the username."""
    name: Optional[str] = None
    """Gets or sets the user's password."""
    password: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StartupUserDto':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        password = from_union([from_str, from_none], obj.get("Password"))
        return StartupUserDto(name, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Password"] = from_union([from_str, from_none], self.password)
        return result


