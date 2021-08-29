from util.from_type import *
from data_classes.media_source import MediaSource
from data_classes.error_code import ErrorCode


@dataclass
class PlaybackInfoResponse:
    """Class PlaybackInfoResponse."""
    """Gets or sets the error code."""
    error_code: Optional[ErrorCode] = None
    """Gets or sets the media sources."""
    media_sources: Optional[List[MediaSource]] = None
    """Gets or sets the play session identifier."""
    play_session_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PlaybackInfoResponse':
        assert isinstance(obj, dict)
        error_code = from_union([ErrorCode, from_none], obj.get("ErrorCode"))
        media_sources = from_union([lambda x: from_list(MediaSource.from_dict, x), from_none], obj.get("MediaSources"))
        play_session_id = from_union([from_str, from_none], obj.get("PlaySessionId"))
        return PlaybackInfoResponse(error_code, media_sources, play_session_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ErrorCode"] = from_union([lambda x: to_enum(ErrorCode, x), from_none], self.error_code)
        result["MediaSources"] = from_union([lambda x: from_list(lambda x: to_class(MediaSource, x), x), from_none], self.media_sources)
        result["PlaySessionId"] = from_union([from_str, from_none], self.play_session_id)
        return result


