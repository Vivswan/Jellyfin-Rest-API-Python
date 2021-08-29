from util.from_type import *


@dataclass
class AuthenticationInfo:
    """Gets or sets the access token."""
    access_token: Optional[str] = None
    """Gets or sets the name of the application."""
    app_name: Optional[str] = None
    """Gets or sets the application version."""
    app_version: Optional[str] = None
    """Gets or sets the date created."""
    date_created: Optional[datetime] = None
    date_last_activity: Optional[datetime] = None
    """Gets or sets the date revoked."""
    date_revoked: Optional[datetime] = None
    """Gets or sets the device identifier."""
    device_id: Optional[str] = None
    """Gets or sets the name of the device."""
    device_name: Optional[str] = None
    """Gets or sets the identifier."""
    id: Optional[int] = None
    """Gets or sets a value indicating whether this instance is active."""
    is_active: Optional[bool] = None
    """Gets or sets the user identifier."""
    user_id: Optional[UUID] = None
    user_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationInfo':
        assert isinstance(obj, dict)
        access_token = from_union([from_str, from_none], obj.get("AccessToken"))
        app_name = from_union([from_str, from_none], obj.get("AppName"))
        app_version = from_union([from_str, from_none], obj.get("AppVersion"))
        date_created = from_union([from_datetime, from_none], obj.get("DateCreated"))
        date_last_activity = from_union([from_datetime, from_none], obj.get("DateLastActivity"))
        date_revoked = from_union([from_datetime, from_none], obj.get("DateRevoked"))
        device_id = from_union([from_str, from_none], obj.get("DeviceId"))
        device_name = from_union([from_str, from_none], obj.get("DeviceName"))
        id = from_union([from_int, from_none], obj.get("Id"))
        is_active = from_union([from_bool, from_none], obj.get("IsActive"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        user_name = from_union([from_str, from_none], obj.get("UserName"))
        return AuthenticationInfo(access_token, app_name, app_version, date_created, date_last_activity, date_revoked, device_id, device_name, id, is_active, user_id, user_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AccessToken"] = from_union([from_str, from_none], self.access_token)
        result["AppName"] = from_union([from_str, from_none], self.app_name)
        result["AppVersion"] = from_union([from_str, from_none], self.app_version)
        result["DateCreated"] = from_union([lambda x: x.isoformat(), from_none], self.date_created)
        result["DateLastActivity"] = from_union([lambda x: x.isoformat(), from_none], self.date_last_activity)
        result["DateRevoked"] = from_union([lambda x: x.isoformat(), from_none], self.date_revoked)
        result["DeviceId"] = from_union([from_str, from_none], self.device_id)
        result["DeviceName"] = from_union([from_str, from_none], self.device_name)
        result["Id"] = from_union([from_int, from_none], self.id)
        result["IsActive"] = from_union([from_bool, from_none], self.is_active)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        result["UserName"] = from_union([from_str, from_none], self.user_name)
        return result


