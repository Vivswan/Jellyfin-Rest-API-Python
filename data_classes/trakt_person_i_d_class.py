from util.from_type import *


@dataclass
class TraktPersonIDClass:
    imdb: Optional[str] = None
    slug: Optional[str] = None
    tmdb: Optional[int] = None
    trakt: Optional[int] = None
    tvrage: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktPersonIDClass':
        assert isinstance(obj, dict)
        imdb = from_union([from_str, from_none], obj.get("imdb"))
        slug = from_union([from_str, from_none], obj.get("slug"))
        tmdb = from_union([from_int, from_none], obj.get("tmdb"))
        trakt = from_union([from_int, from_none], obj.get("trakt"))
        tvrage = from_union([from_int, from_none], obj.get("tvrage"))
        return TraktPersonIDClass(imdb, slug, tmdb, trakt, tvrage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["imdb"] = from_union([from_str, from_none], self.imdb)
        result["slug"] = from_union([from_str, from_none], self.slug)
        result["tmdb"] = from_union([from_int, from_none], self.tmdb)
        result["trakt"] = from_union([from_int, from_none], self.trakt)
        result["tvrage"] = from_union([from_int, from_none], self.tvrage)
        return result


