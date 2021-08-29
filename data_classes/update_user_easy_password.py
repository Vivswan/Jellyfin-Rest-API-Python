from util.from_type import *


@dataclass
class UpdateUserEasyPassword:
    """The update user easy password request body."""
    """Gets or sets the new sha1-hashed password."""
    new_password: Optional[str] = None
    """Gets or sets the new password."""
    new_pw: Optional[str] = None
    """Gets or sets a value indicating whether to reset the password."""
    reset_password: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UpdateUserEasyPassword':
        assert isinstance(obj, dict)
        new_password = from_union([from_str, from_none], obj.get("NewPassword"))
        new_pw = from_union([from_str, from_none], obj.get("NewPw"))
        reset_password = from_union([from_bool, from_none], obj.get("ResetPassword"))
        return UpdateUserEasyPassword(new_password, new_pw, reset_password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["NewPassword"] = from_union([from_str, from_none], self.new_password)
        result["NewPw"] = from_union([from_str, from_none], self.new_pw)
        result["ResetPassword"] = from_union([from_bool, from_none], self.reset_password)
        return result


