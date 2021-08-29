from util.from_type import *


@dataclass
class QueryFiltersLegacy:
    genres: Optional[List[str]] = None
    official_ratings: Optional[List[str]] = None
    tags: Optional[List[str]] = None
    years: Optional[List[int]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QueryFiltersLegacy':
        assert isinstance(obj, dict)
        genres = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Genres"))
        official_ratings = from_union([lambda x: from_list(from_str, x), from_none], obj.get("OfficialRatings"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Tags"))
        years = from_union([lambda x: from_list(from_int, x), from_none], obj.get("Years"))
        return QueryFiltersLegacy(genres, official_ratings, tags, years)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Genres"] = from_union([lambda x: from_list(from_str, x), from_none], self.genres)
        result["OfficialRatings"] = from_union([lambda x: from_list(from_str, x), from_none], self.official_ratings)
        result["Tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        result["Years"] = from_union([lambda x: from_list(from_int, x), from_none], self.years)
        return result


