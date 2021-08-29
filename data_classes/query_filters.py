from util.from_type import *
from data_classes.name_g_u_i_d_pair import NameGUIDPair


@dataclass
class QueryFilters:
    genres: Optional[List[NameGUIDPair]] = None
    tags: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'QueryFilters':
        assert isinstance(obj, dict)
        genres = from_union([lambda x: from_list(NameGUIDPair.from_dict, x), from_none], obj.get("Genres"))
        tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("Tags"))
        return QueryFilters(genres, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Genres"] = from_union([lambda x: from_list(lambda x: to_class(NameGUIDPair, x), x), from_none], self.genres)
        result["Tags"] = from_union([lambda x: from_list(from_str, x), from_none], self.tags)
        return result


