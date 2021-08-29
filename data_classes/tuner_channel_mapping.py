from util.from_type import *


@dataclass
class TunerChannelMapping:
    id: Optional[str] = None
    name: Optional[str] = None
    provider_channel_id: Optional[str] = None
    provider_channel_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TunerChannelMapping':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        provider_channel_id = from_union([from_str, from_none], obj.get("ProviderChannelId"))
        provider_channel_name = from_union([from_str, from_none], obj.get("ProviderChannelName"))
        return TunerChannelMapping(id, name, provider_channel_id, provider_channel_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ProviderChannelId"] = from_union([from_str, from_none], self.provider_channel_id)
        result["ProviderChannelName"] = from_union([from_str, from_none], self.provider_channel_name)
        return result


