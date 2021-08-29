from util.from_type import *


@dataclass
class PluginSecurityInfo:
    """Plugin security info."""
    """Gets or sets a value indicating whether is mb supporter."""
    is_mb_supporter: Optional[bool] = None
    """Gets or sets the supporter key."""
    supporter_key: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PluginSecurityInfo':
        assert isinstance(obj, dict)
        is_mb_supporter = from_union([from_bool, from_none], obj.get("IsMbSupporter"))
        supporter_key = from_union([from_str, from_none], obj.get("SupporterKey"))
        return PluginSecurityInfo(is_mb_supporter, supporter_key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IsMbSupporter"] = from_union([from_bool, from_none], self.is_mb_supporter)
        result["SupporterKey"] = from_union([from_str, from_none], self.supporter_key)
        return result


