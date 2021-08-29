from util.from_type import *


@dataclass
class ForgotPasswordPinDto:
    """Forgot Password Pin enter request body DTO."""
    """Gets or sets the entered pin to have the password reset."""
    pin: str

    @staticmethod
    def from_dict(obj: Any) -> 'ForgotPasswordPinDto':
        assert isinstance(obj, dict)
        pin = from_str(obj.get("Pin"))
        return ForgotPasswordPinDto(pin)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Pin"] = from_str(self.pin)
        return result


