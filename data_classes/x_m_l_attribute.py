from util.from_type import *


@dataclass
class XMLAttribute:
    """Defines the MediaBrowser.Model.Dlna.XmlAttribute."""
    """Gets or sets the name of the attribute."""
    name: Optional[str] = None
    """Gets or sets the value of the attribute."""
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'XMLAttribute':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        value = from_union([from_str, from_none], obj.get("Value"))
        return XMLAttribute(name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Value"] = from_union([from_str, from_none], self.value)
        return result


