from data_classes.name_i_d_pair import NameIDPair
from data_classes.name_value_pair import NameValuePair
from data_classes.tuner_channel_mapping import TunerChannelMapping
from util.from_type import *


@dataclass
class ChannelMappingOptionsDto:
    """Channel mapping options dto."""
    """Gets or sets list of mappings."""
    mappings: Optional[List[NameValuePair]] = None
    """Gets or sets list of provider channels."""
    provider_channels: Optional[List[NameIDPair]] = None
    """Gets or sets provider name."""
    provider_name: Optional[str] = None
    """Gets or sets list of tuner channels."""
    tuner_channels: Optional[List[TunerChannelMapping]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelMappingOptionsDto':
        assert isinstance(obj, dict)
        mappings = from_union([lambda x: from_list(NameValuePair.from_dict, x), from_none], obj.get("Mappings"))
        provider_channels = from_union([lambda x: from_list(NameIDPair.from_dict, x), from_none], obj.get("ProviderChannels"))
        provider_name = from_union([from_str, from_none], obj.get("ProviderName"))
        tuner_channels = from_union([lambda x: from_list(TunerChannelMapping.from_dict, x), from_none], obj.get("TunerChannels"))
        return ChannelMappingOptionsDto(mappings, provider_channels, provider_name, tuner_channels)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Mappings"] = from_union([lambda x: from_list(lambda x: to_class(NameValuePair, x), x), from_none], self.mappings)
        result["ProviderChannels"] = from_union([lambda x: from_list(lambda x: to_class(NameIDPair, x), x), from_none], self.provider_channels)
        result["ProviderName"] = from_union([from_str, from_none], self.provider_name)
        result["TunerChannels"] = from_union([lambda x: from_list(lambda x: to_class(TunerChannelMapping, x), x), from_none], self.tuner_channels)
        return result


