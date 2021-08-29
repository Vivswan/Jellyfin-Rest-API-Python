from util.from_type import *


@dataclass
class QuickConnectResult:
    """Stores the result of an incoming quick connect request."""
    """Gets a value indicating whether this request is authorized."""
    authenticated: Optional[bool] = None
    """Gets or sets the private access token."""
    authentication: Optional[str] = None
    """Gets or sets the user facing code used so the user can quickly differentiate this request
    from others.
    """
    code: Optional[str] = None
    """Gets or sets the DateTime that this request was created."""
    date_added: Optional[datetime] = None
    """Gets or sets an error message."""
    error: Optional[str] = None
    """Gets or sets the secret value used to uniquely identify this request. Can be used to
    retrieve authentication information.
    """
    secret: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QuickConnectResult':
        assert isinstance(obj, dict)
        authenticated = from_union([from_bool, from_none], obj.get("Authenticated"))
        authentication = from_union([from_str, from_none], obj.get("Authentication"))
        code = from_union([from_str, from_none], obj.get("Code"))
        date_added = from_union([from_datetime, from_none], obj.get("DateAdded"))
        error = from_union([from_str, from_none], obj.get("Error"))
        secret = from_union([from_str, from_none], obj.get("Secret"))
        return QuickConnectResult(authenticated, authentication, code, date_added, error, secret)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Authenticated"] = from_union([from_bool, from_none], self.authenticated)
        result["Authentication"] = from_union([from_str, from_none], self.authentication)
        result["Code"] = from_union([from_str, from_none], self.code)
        result["DateAdded"] = from_union([lambda x: x.isoformat(), from_none], self.date_added)
        result["Error"] = from_union([from_str, from_none], self.error)
        result["Secret"] = from_union([from_str, from_none], self.secret)
        return result


