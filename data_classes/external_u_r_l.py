from util.from_type import *


@dataclass
class ExternalURL:
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the type of the item."""
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalURL':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        url = from_union([from_str, from_none], obj.get("Url"))
        return ExternalURL(name, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Url"] = from_union([from_str, from_none], self.url)
        return result


