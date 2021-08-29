from util.from_type import *
from data_classes.configuration import Configuration
from data_classes.policy import Policy


@dataclass
class UserDtoClass:
    """Class UserDto."""
    """Gets or sets the configuration."""
    configuration: Optional[Configuration] = None
    """Gets or sets whether async login is enabled or not."""
    enable_auto_login: Optional[bool] = None
    """Gets or sets a value indicating whether this instance has configured easy password."""
    has_configured_easy_password: Optional[bool] = None
    """Gets or sets a value indicating whether this instance has configured password."""
    has_configured_password: Optional[bool] = None
    """Gets or sets a value indicating whether this instance has password."""
    has_password: Optional[bool] = None
    """Gets or sets the id."""
    id: Optional[UUID] = None
    """Gets or sets the last activity date."""
    last_activity_date: Optional[datetime] = None
    """Gets or sets the last login date."""
    last_login_date: Optional[datetime] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the policy."""
    policy: Optional[Policy] = None
    """Gets or sets the primary image aspect ratio."""
    primary_image_aspect_ratio: Optional[float] = None
    """Gets or sets the primary image tag."""
    primary_image_tag: Optional[str] = None
    """Gets or sets the server identifier."""
    server_id: Optional[str] = None
    """Gets or sets the name of the server.
    This is not used by the server and is for client-side usage only.
    """
    server_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserDtoClass':
        assert isinstance(obj, dict)
        configuration = from_union([Configuration.from_dict, from_none], obj.get("Configuration"))
        enable_auto_login = from_union([from_bool, from_none], obj.get("EnableAutoLogin"))
        has_configured_easy_password = from_union([from_bool, from_none], obj.get("HasConfiguredEasyPassword"))
        has_configured_password = from_union([from_bool, from_none], obj.get("HasConfiguredPassword"))
        has_password = from_union([from_bool, from_none], obj.get("HasPassword"))
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        last_activity_date = from_union([from_datetime, from_none], obj.get("LastActivityDate"))
        last_login_date = from_union([from_datetime, from_none], obj.get("LastLoginDate"))
        name = from_union([from_str, from_none], obj.get("Name"))
        policy = from_union([Policy.from_dict, from_none], obj.get("Policy"))
        primary_image_aspect_ratio = from_union([from_float, from_none], obj.get("PrimaryImageAspectRatio"))
        primary_image_tag = from_union([from_str, from_none], obj.get("PrimaryImageTag"))
        server_id = from_union([from_str, from_none], obj.get("ServerId"))
        server_name = from_union([from_str, from_none], obj.get("ServerName"))
        return UserDtoClass(configuration, enable_auto_login, has_configured_easy_password, has_configured_password, has_password, id, last_activity_date, last_login_date, name, policy, primary_image_aspect_ratio, primary_image_tag, server_id, server_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Configuration"] = from_union([lambda x: to_class(Configuration, x), from_none], self.configuration)
        result["EnableAutoLogin"] = from_union([from_bool, from_none], self.enable_auto_login)
        result["HasConfiguredEasyPassword"] = from_union([from_bool, from_none], self.has_configured_easy_password)
        result["HasConfiguredPassword"] = from_union([from_bool, from_none], self.has_configured_password)
        result["HasPassword"] = from_union([from_bool, from_none], self.has_password)
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["LastActivityDate"] = from_union([lambda x: x.isoformat(), from_none], self.last_activity_date)
        result["LastLoginDate"] = from_union([lambda x: x.isoformat(), from_none], self.last_login_date)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Policy"] = from_union([lambda x: to_class(Policy, x), from_none], self.policy)
        result["PrimaryImageAspectRatio"] = from_union([to_float, from_none], self.primary_image_aspect_ratio)
        result["PrimaryImageTag"] = from_union([from_str, from_none], self.primary_image_tag)
        result["ServerId"] = from_union([from_str, from_none], self.server_id)
        result["ServerName"] = from_union([from_str, from_none], self.server_name)
        return result


