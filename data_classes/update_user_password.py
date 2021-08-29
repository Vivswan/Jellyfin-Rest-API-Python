from util.from_type import *


@dataclass
class UpdateUserPassword:
    """The update user password request body."""
    """Gets or sets the current sha1-hashed password."""
    current_password: Optional[str] = None
    """Gets or sets the current plain text password."""
    current_pw: Optional[str] = None
    """Gets or sets the new plain text password."""
    new_pw: Optional[str] = None
    """Gets or sets a value indicating whether to reset the password."""
    reset_password: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateUserPassword':
        assert isinstance(obj, dict)
        current_password = from_union([from_str, from_none], obj.get("CurrentPassword"))
        current_pw = from_union([from_str, from_none], obj.get("CurrentPw"))
        new_pw = from_union([from_str, from_none], obj.get("NewPw"))
        reset_password = from_union([from_bool, from_none], obj.get("ResetPassword"))
        return UpdateUserPassword(current_password, current_pw, new_pw, reset_password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CurrentPassword"] = from_union([from_str, from_none], self.current_password)
        result["CurrentPw"] = from_union([from_str, from_none], self.current_pw)
        result["NewPw"] = from_union([from_str, from_none], self.new_pw)
        result["ResetPassword"] = from_union([from_bool, from_none], self.reset_password)
        return result


