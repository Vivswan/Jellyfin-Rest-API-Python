from util.from_type import *


@dataclass
class TunerHostInfo:
    allow_hw_transcoding: Optional[bool] = None
    device_id: Optional[str] = None
    enable_stream_looping: Optional[bool] = None
    friendly_name: Optional[str] = None
    id: Optional[str] = None
    import_favorites_only: Optional[bool] = None
    source: Optional[str] = None
    tuner_count: Optional[int] = None
    type: Optional[str] = None
    url: Optional[str] = None
    user_agent: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TunerHostInfo':
        assert isinstance(obj, dict)
        allow_hw_transcoding = from_union([from_bool, from_none], obj.get("AllowHWTranscoding"))
        device_id = from_union([from_str, from_none], obj.get("DeviceId"))
        enable_stream_looping = from_union([from_bool, from_none], obj.get("EnableStreamLooping"))
        friendly_name = from_union([from_str, from_none], obj.get("FriendlyName"))
        id = from_union([from_str, from_none], obj.get("Id"))
        import_favorites_only = from_union([from_bool, from_none], obj.get("ImportFavoritesOnly"))
        source = from_union([from_str, from_none], obj.get("Source"))
        tuner_count = from_union([from_int, from_none], obj.get("TunerCount"))
        type = from_union([from_str, from_none], obj.get("Type"))
        url = from_union([from_str, from_none], obj.get("Url"))
        user_agent = from_union([from_str, from_none], obj.get("UserAgent"))
        return TunerHostInfo(allow_hw_transcoding, device_id, enable_stream_looping, friendly_name, id, import_favorites_only, source, tuner_count, type, url, user_agent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AllowHWTranscoding"] = from_union([from_bool, from_none], self.allow_hw_transcoding)
        result["DeviceId"] = from_union([from_str, from_none], self.device_id)
        result["EnableStreamLooping"] = from_union([from_bool, from_none], self.enable_stream_looping)
        result["FriendlyName"] = from_union([from_str, from_none], self.friendly_name)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["ImportFavoritesOnly"] = from_union([from_bool, from_none], self.import_favorites_only)
        result["Source"] = from_union([from_str, from_none], self.source)
        result["TunerCount"] = from_union([from_int, from_none], self.tuner_count)
        result["Type"] = from_union([from_str, from_none], self.type)
        result["Url"] = from_union([from_str, from_none], self.url)
        result["UserAgent"] = from_union([from_str, from_none], self.user_agent)
        return result


