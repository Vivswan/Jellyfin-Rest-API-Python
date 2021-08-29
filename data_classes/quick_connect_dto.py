from util.from_type import *


@dataclass
class QuickConnectDto:
    """The quick connect request body."""
    """Gets or sets the quick connect token."""
    token: str

    @staticmethod
    def from_dict(obj: Any) -> 'QuickConnectDto':
        assert isinstance(obj, dict)
        token = from_str(obj.get("Token"))
        return QuickConnectDto(token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Token"] = from_str(self.token)
        return result


