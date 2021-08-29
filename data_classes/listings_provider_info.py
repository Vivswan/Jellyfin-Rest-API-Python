from data_classes.name_value_pair import NameValuePair
from util.from_type import *


@dataclass
class ListingsProviderInfo:
    channel_mappings: Optional[List[NameValuePair]] = None
    country: Optional[str] = None
    enable_all_tuners: Optional[bool] = None
    enabled_tuners: Optional[List[str]] = None
    id: Optional[str] = None
    kids_categories: Optional[List[str]] = None
    listings_id: Optional[str] = None
    movie_categories: Optional[List[str]] = None
    movie_prefix: Optional[str] = None
    news_categories: Optional[List[str]] = None
    password: Optional[str] = None
    path: Optional[str] = None
    preferred_language: Optional[str] = None
    sports_categories: Optional[List[str]] = None
    type: Optional[str] = None
    user_agent: Optional[str] = None
    username: Optional[str] = None
    zip_code: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ListingsProviderInfo':
        assert isinstance(obj, dict)
        channel_mappings = from_union([lambda x: from_list(NameValuePair.from_dict, x), from_none], obj.get("ChannelMappings"))
        country = from_union([from_str, from_none], obj.get("Country"))
        enable_all_tuners = from_union([from_bool, from_none], obj.get("EnableAllTuners"))
        enabled_tuners = from_union([lambda x: from_list(from_str, x), from_none], obj.get("EnabledTuners"))
        id = from_union([from_str, from_none], obj.get("Id"))
        kids_categories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("KidsCategories"))
        listings_id = from_union([from_str, from_none], obj.get("ListingsId"))
        movie_categories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MovieCategories"))
        movie_prefix = from_union([from_str, from_none], obj.get("MoviePrefix"))
        news_categories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("NewsCategories"))
        password = from_union([from_str, from_none], obj.get("Password"))
        path = from_union([from_str, from_none], obj.get("Path"))
        preferred_language = from_union([from_str, from_none], obj.get("PreferredLanguage"))
        sports_categories = from_union([lambda x: from_list(from_str, x), from_none], obj.get("SportsCategories"))
        type = from_union([from_str, from_none], obj.get("Type"))
        user_agent = from_union([from_str, from_none], obj.get("UserAgent"))
        username = from_union([from_str, from_none], obj.get("Username"))
        zip_code = from_union([from_str, from_none], obj.get("ZipCode"))
        return ListingsProviderInfo(channel_mappings, country, enable_all_tuners, enabled_tuners, id, kids_categories, listings_id, movie_categories, movie_prefix, news_categories, password, path, preferred_language, sports_categories, type, user_agent, username, zip_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ChannelMappings"] = from_union([lambda x: from_list(lambda x: to_class(NameValuePair, x), x), from_none], self.channel_mappings)
        result["Country"] = from_union([from_str, from_none], self.country)
        result["EnableAllTuners"] = from_union([from_bool, from_none], self.enable_all_tuners)
        result["EnabledTuners"] = from_union([lambda x: from_list(from_str, x), from_none], self.enabled_tuners)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["KidsCategories"] = from_union([lambda x: from_list(from_str, x), from_none], self.kids_categories)
        result["ListingsId"] = from_union([from_str, from_none], self.listings_id)
        result["MovieCategories"] = from_union([lambda x: from_list(from_str, x), from_none], self.movie_categories)
        result["MoviePrefix"] = from_union([from_str, from_none], self.movie_prefix)
        result["NewsCategories"] = from_union([lambda x: from_list(from_str, x), from_none], self.news_categories)
        result["Password"] = from_union([from_str, from_none], self.password)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["PreferredLanguage"] = from_union([from_str, from_none], self.preferred_language)
        result["SportsCategories"] = from_union([lambda x: from_list(from_str, x), from_none], self.sports_categories)
        result["Type"] = from_union([from_str, from_none], self.type)
        result["UserAgent"] = from_union([from_str, from_none], self.user_agent)
        result["Username"] = from_union([from_str, from_none], self.username)
        result["ZipCode"] = from_union([from_str, from_none], self.zip_code)
        return result


