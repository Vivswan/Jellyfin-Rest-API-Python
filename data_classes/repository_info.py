from util.from_type import *


@dataclass
class RepositoryInfo:
    """Class RepositoryInfo."""
    """Gets or sets a value indicating whether the repository is enabled."""
    enabled: Optional[bool] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the URL."""
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RepositoryInfo':
        assert isinstance(obj, dict)
        enabled = from_union([from_bool, from_none], obj.get("Enabled"))
        name = from_union([from_str, from_none], obj.get("Name"))
        url = from_union([from_str, from_none], obj.get("Url"))
        return RepositoryInfo(enabled, name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Enabled"] = from_union([from_bool, from_none], self.enabled)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Url"] = from_union([from_str, from_none], self.url)
        return result


