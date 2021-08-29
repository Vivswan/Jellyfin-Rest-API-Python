from util.from_type import *


@dataclass
class CreateUserByName:
    """The create user by name request body."""
    """Gets or sets the username."""
    name: Optional[str] = None
    """Gets or sets the password."""
    password: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CreateUserByName':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        password = from_union([from_str, from_none], obj.get("Password"))
        return CreateUserByName(name, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Password"] = from_union([from_str, from_none], self.password)
        return result


