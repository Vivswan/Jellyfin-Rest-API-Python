from util.from_type import *


@dataclass
class ParentalRating:
    """Class ParentalRating."""
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the value."""
    value: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ParentalRating':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("Name"))
        value = from_union([from_int, from_none], obj.get("Value"))
        return ParentalRating(name, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Value"] = from_union([from_int, from_none], self.value)
        return result


