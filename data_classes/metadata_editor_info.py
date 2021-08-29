from util.from_type import *
from data_classes.name_value_pair import NameValuePair
from data_classes.country_info import CountryInfo
from data_classes.culture_dto import CultureDto
from data_classes.external_i_d_info import ExternalIDInfo
from data_classes.parental_rating import ParentalRating


@dataclass
class MetadataEditorInfo:
    content_type: Optional[str] = None
    content_type_options: Optional[List[NameValuePair]] = None
    countries: Optional[List[CountryInfo]] = None
    cultures: Optional[List[CultureDto]] = None
    external_id_infos: Optional[List[ExternalIDInfo]] = None
    parental_rating_options: Optional[List[ParentalRating]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MetadataEditorInfo':
        assert isinstance(obj, dict)
        content_type = from_union([from_str, from_none], obj.get("ContentType"))
        content_type_options = from_union([lambda x: from_list(NameValuePair.from_dict, x), from_none], obj.get("ContentTypeOptions"))
        countries = from_union([lambda x: from_list(CountryInfo.from_dict, x), from_none], obj.get("Countries"))
        cultures = from_union([lambda x: from_list(CultureDto.from_dict, x), from_none], obj.get("Cultures"))
        external_id_infos = from_union([lambda x: from_list(ExternalIDInfo.from_dict, x), from_none], obj.get("ExternalIdInfos"))
        parental_rating_options = from_union([lambda x: from_list(ParentalRating.from_dict, x), from_none], obj.get("ParentalRatingOptions"))
        return MetadataEditorInfo(content_type, content_type_options, countries, cultures, external_id_infos, parental_rating_options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ContentType"] = from_union([from_str, from_none], self.content_type)
        result["ContentTypeOptions"] = from_union([lambda x: from_list(lambda x: to_class(NameValuePair, x), x), from_none], self.content_type_options)
        result["Countries"] = from_union([lambda x: from_list(lambda x: to_class(CountryInfo, x), x), from_none], self.countries)
        result["Cultures"] = from_union([lambda x: from_list(lambda x: to_class(CultureDto, x), x), from_none], self.cultures)
        result["ExternalIdInfos"] = from_union([lambda x: from_list(lambda x: to_class(ExternalIDInfo, x), x), from_none], self.external_id_infos)
        result["ParentalRatingOptions"] = from_union([lambda x: from_list(lambda x: to_class(ParentalRating, x), x), from_none], self.parental_rating_options)
        return result


