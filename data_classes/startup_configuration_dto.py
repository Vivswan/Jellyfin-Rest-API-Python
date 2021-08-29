from util.from_type import *


@dataclass
class StartupConfigurationDto:
    """The startup configuration DTO."""
    """Gets or sets the metadata country code."""
    metadata_country_code: Optional[str] = None
    """Gets or sets the preferred language for the metadata."""
    preferred_metadata_language: Optional[str] = None
    """Gets or sets UI language culture."""
    ui_culture: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StartupConfigurationDto':
        assert isinstance(obj, dict)
        metadata_country_code = from_union([from_str, from_none], obj.get("MetadataCountryCode"))
        preferred_metadata_language = from_union([from_str, from_none], obj.get("PreferredMetadataLanguage"))
        ui_culture = from_union([from_str, from_none], obj.get("UICulture"))
        return StartupConfigurationDto(metadata_country_code, preferred_metadata_language, ui_culture)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MetadataCountryCode"] = from_union([from_str, from_none], self.metadata_country_code)
        result["PreferredMetadataLanguage"] = from_union([from_str, from_none], self.preferred_metadata_language)
        result["UICulture"] = from_union([from_str, from_none], self.ui_culture)
        return result


