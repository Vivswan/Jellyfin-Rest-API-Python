from util.from_type import *


@dataclass
class SetChannelMappingDto:
    """Set channel mapping dto."""
    """Gets or sets the provider channel id."""
    provider_channel_id: str
    """Gets or sets the provider id."""
    provider_id: str
    """Gets or sets the tuner channel id."""
    tuner_channel_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'SetChannelMappingDto':
        assert isinstance(obj, dict)
        provider_channel_id = from_str(obj.get("ProviderChannelId"))
        provider_id = from_str(obj.get("ProviderId"))
        tuner_channel_id = from_str(obj.get("TunerChannelId"))
        return SetChannelMappingDto(provider_channel_id, provider_id, tuner_channel_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ProviderChannelId"] = from_str(self.provider_channel_id)
        result["ProviderId"] = from_str(self.provider_id)
        result["TunerChannelId"] = from_str(self.tuner_channel_id)
        return result


