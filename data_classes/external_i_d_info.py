from data_classes.external_i_d_media_type_enum import ExternalIDMediaTypeEnum
from util.from_type import *


@dataclass
class ExternalIDInfo:
    """Represents the external id information for serialization to the client."""
    """Gets or sets the unique key for this id. This key should be unique across all providers."""
    key: Optional[str] = None
    """Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz, etc)."""
    name: Optional[str] = None
    """Gets or sets the specific media type for this id. This is used to distinguish between the
    different
    external id types for providers with multiple ids.
    A null value indicates there is no specific media type associated with the external id,
    or this is the
    default id for the external provider so there is no need to specify a type.
    """
    type: Optional[ExternalIDMediaTypeEnum] = None
    """Gets or sets the URL format string."""
    url_format_string: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalIDInfo':
        assert isinstance(obj, dict)
        key = from_union([from_str, from_none], obj.get("Key"))
        name = from_union([from_str, from_none], obj.get("Name"))
        type = from_union([ExternalIDMediaTypeEnum, from_none], obj.get("Type"))
        url_format_string = from_union([from_str, from_none], obj.get("UrlFormatString"))
        return ExternalIDInfo(key, name, type, url_format_string)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Key"] = from_union([from_str, from_none], self.key)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Type"] = from_union([lambda x: to_enum(ExternalIDMediaTypeEnum, x), from_none], self.type)
        result["UrlFormatString"] = from_union([from_str, from_none], self.url_format_string)
        return result


