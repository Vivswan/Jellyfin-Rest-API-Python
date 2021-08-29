from util.from_type import *


@dataclass
class CultureDto:
    """Class CultureDto."""
    """Gets or sets the display name."""
    display_name: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the name of the three letter ISO language."""
    three_letter_iso_language_name: Optional[str] = None
    three_letter_iso_language_names: Optional[List[str]] = None
    """Gets or sets the name of the two letter ISO language."""
    two_letter_iso_language_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CultureDto':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("DisplayName"))
        name = from_union([from_str, from_none], obj.get("Name"))
        three_letter_iso_language_name = from_union([from_str, from_none], obj.get("ThreeLetterISOLanguageName"))
        three_letter_iso_language_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ThreeLetterISOLanguageNames"))
        two_letter_iso_language_name = from_union([from_str, from_none], obj.get("TwoLetterISOLanguageName"))
        return CultureDto(display_name, name, three_letter_iso_language_name, three_letter_iso_language_names, two_letter_iso_language_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DisplayName"] = from_union([from_str, from_none], self.display_name)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ThreeLetterISOLanguageName"] = from_union([from_str, from_none], self.three_letter_iso_language_name)
        result["ThreeLetterISOLanguageNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.three_letter_iso_language_names)
        result["TwoLetterISOLanguageName"] = from_union([from_str, from_none], self.two_letter_iso_language_name)
        return result


