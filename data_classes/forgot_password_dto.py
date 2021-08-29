from util.from_type import *


@dataclass
class ForgotPasswordDto:
    """Forgot Password request body DTO."""
    """Gets or sets the entered username to have its password reset."""
    entered_username: str

    @staticmethod
    def from_dict(obj: Any) -> 'ForgotPasswordDto':
        assert isinstance(obj, dict)
        entered_username = from_str(obj.get("EnteredUsername"))
        return ForgotPasswordDto(entered_username)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EnteredUsername"] = from_str(self.entered_username)
        return result


