from util.from_type import *


@dataclass
class CountryInfo:
    """Class CountryInfo."""
    """Gets or sets the display name."""
    display_name: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the name of the three letter ISO region."""
    three_letter_iso_region_name: Optional[str] = None
    """Gets or sets the name of the two letter ISO region."""
    two_letter_iso_region_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CountryInfo':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("DisplayName"))
        name = from_union([from_str, from_none], obj.get("Name"))
        three_letter_iso_region_name = from_union([from_str, from_none], obj.get("ThreeLetterISORegionName"))
        two_letter_iso_region_name = from_union([from_str, from_none], obj.get("TwoLetterISORegionName"))
        return CountryInfo(display_name, name, three_letter_iso_region_name, two_letter_iso_region_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DisplayName"] = from_union([from_str, from_none], self.display_name)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ThreeLetterISORegionName"] = from_union([from_str, from_none], self.three_letter_iso_region_name)
        result["TwoLetterISORegionName"] = from_union([from_str, from_none], self.two_letter_iso_region_name)
        return result


