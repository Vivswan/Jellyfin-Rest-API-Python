from data_classes.action import Action
from util.from_type import *


@dataclass
class ForgotPasswordResult:
    """Gets or sets the action."""
    action: Optional[Action] = None
    """Gets or sets the pin expiration date."""
    pin_expiration_date: Optional[datetime] = None
    """Gets or sets the pin file."""
    pin_file: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ForgotPasswordResult':
        assert isinstance(obj, dict)
        action = from_union([Action, from_none], obj.get("Action"))
        pin_expiration_date = from_union([from_datetime, from_none], obj.get("PinExpirationDate"))
        pin_file = from_union([from_str, from_none], obj.get("PinFile"))
        return ForgotPasswordResult(action, pin_expiration_date, pin_file)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Action"] = from_union([lambda x: to_enum(Action, x), from_none], self.action)
        result["PinExpirationDate"] = from_union([lambda x: x.isoformat(), from_none], self.pin_expiration_date)
        result["PinFile"] = from_union([from_str, from_none], self.pin_file)
        return result


