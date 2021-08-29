from util.from_type import *


@dataclass
class UploadSubtitleDto:
    """Upload subtitles dto."""
    """Gets or sets the subtitle data."""
    data: str
    """Gets or sets the subtitle format."""
    format: str
    """Gets or sets a value indicating whether the subtitle is forced."""
    is_forced: bool
    """Gets or sets the subtitle language."""
    language: str

    @staticmethod
    def from_dict(obj: Any) -> 'UploadSubtitleDto':
        assert isinstance(obj, dict)
        data = from_str(obj.get("Data"))
        format = from_str(obj.get("Format"))
        is_forced = from_bool(obj.get("IsForced"))
        language = from_str(obj.get("Language"))
        return UploadSubtitleDto(data, format, is_forced, language)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Data"] = from_str(self.data)
        result["Format"] = from_str(self.format)
        result["IsForced"] = from_bool(self.is_forced)
        result["Language"] = from_str(self.language)
        return result


