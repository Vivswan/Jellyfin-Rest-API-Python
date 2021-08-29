from util.from_type import *


@dataclass
class PathSubstitution:
    """Defines the MediaBrowser.Model.Configuration.PathSubstitution."""
    """Gets or sets the value to substitute."""
    path_substitution_from: Optional[str] = None
    """Gets or sets the value to substitution with."""
    to: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PathSubstitution':
        assert isinstance(obj, dict)
        path_substitution_from = from_union([from_str, from_none], obj.get("From"))
        to = from_union([from_str, from_none], obj.get("To"))
        return PathSubstitution(path_substitution_from, to)

    def to_dict(self) -> dict:
        result: dict = {}
        result["From"] = from_union([from_str, from_none], self.path_substitution_from)
        result["To"] = from_union([from_str, from_none], self.to)
        return result


