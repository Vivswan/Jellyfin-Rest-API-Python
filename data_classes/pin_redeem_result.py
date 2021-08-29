from util.from_type import *


@dataclass
class PinRedeemResult:
    """Gets or sets a value indicating whether this MediaBrowser.Model.Users.PinRedeemResult is
    success.
    """
    success: Optional[bool] = None
    """Gets or sets the users reset."""
    users_reset: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PinRedeemResult':
        assert isinstance(obj, dict)
        success = from_union([from_bool, from_none], obj.get("Success"))
        users_reset = from_union([lambda x: from_list(from_str, x), from_none], obj.get("UsersReset"))
        return PinRedeemResult(success, users_reset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Success"] = from_union([from_bool, from_none], self.success)
        result["UsersReset"] = from_union([lambda x: from_list(from_str, x), from_none], self.users_reset)
        return result


