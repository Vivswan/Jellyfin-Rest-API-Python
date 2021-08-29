from util.from_type import *
from data_classes.image_type_element import ImageTypeElement
from data_classes.rating_type import RatingType


@dataclass
class RemoteImageInfo:
    """Class RemoteImageInfo."""
    """Gets or sets the community rating."""
    community_rating: Optional[float] = None
    """Gets or sets the height."""
    height: Optional[int] = None
    """Gets or sets the language."""
    language: Optional[str] = None
    """Gets or sets the name of the provider."""
    provider_name: Optional[str] = None
    """Gets or sets the type of the rating."""
    rating_type: Optional[RatingType] = None
    """Gets a url used for previewing a smaller version."""
    thumbnail_url: Optional[str] = None
    """Gets or sets the type."""
    type: Optional[ImageTypeElement] = None
    """Gets or sets the URL."""
    url: Optional[str] = None
    """Gets or sets the vote count."""
    vote_count: Optional[int] = None
    """Gets or sets the width."""
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoteImageInfo':
        assert isinstance(obj, dict)
        community_rating = from_union([from_float, from_none], obj.get("CommunityRating"))
        height = from_union([from_int, from_none], obj.get("Height"))
        language = from_union([from_str, from_none], obj.get("Language"))
        provider_name = from_union([from_str, from_none], obj.get("ProviderName"))
        rating_type = from_union([RatingType, from_none], obj.get("RatingType"))
        thumbnail_url = from_union([from_str, from_none], obj.get("ThumbnailUrl"))
        type = from_union([ImageTypeElement, from_none], obj.get("Type"))
        url = from_union([from_str, from_none], obj.get("Url"))
        vote_count = from_union([from_int, from_none], obj.get("VoteCount"))
        width = from_union([from_int, from_none], obj.get("Width"))
        return RemoteImageInfo(community_rating, height, language, provider_name, rating_type, thumbnail_url, type, url, vote_count, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CommunityRating"] = from_union([to_float, from_none], self.community_rating)
        result["Height"] = from_union([from_int, from_none], self.height)
        result["Language"] = from_union([from_str, from_none], self.language)
        result["ProviderName"] = from_union([from_str, from_none], self.provider_name)
        result["RatingType"] = from_union([lambda x: to_enum(RatingType, x), from_none], self.rating_type)
        result["ThumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        result["Type"] = from_union([lambda x: to_enum(ImageTypeElement, x), from_none], self.type)
        result["Url"] = from_union([from_str, from_none], self.url)
        result["VoteCount"] = from_union([from_int, from_none], self.vote_count)
        result["Width"] = from_union([from_int, from_none], self.width)
        return result


