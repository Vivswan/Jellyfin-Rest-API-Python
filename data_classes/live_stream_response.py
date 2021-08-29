from data_classes.media_source import MediaSource
from util.from_type import *


@dataclass
class LiveStreamResponse:
    media_source: Optional[MediaSource] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LiveStreamResponse':
        assert isinstance(obj, dict)
        media_source = from_union([MediaSource.from_dict, from_none], obj.get("MediaSource"))
        return LiveStreamResponse(media_source)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MediaSource"] = from_union([lambda x: to_class(MediaSource, x), from_none], self.media_source)
        return result


