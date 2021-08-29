from util.from_type import *


@dataclass
class TraktEpisodeIDClass:
    imdb: Optional[str] = None
    slug: Optional[str] = None
    tmdb: Optional[int] = None
    trakt: Optional[int] = None
    tvdb: Optional[int] = None
    tvrage: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktEpisodeIDClass':
        assert isinstance(obj, dict)
        imdb = from_union([from_str, from_none], obj.get("imdb"))
        slug = from_union([from_str, from_none], obj.get("slug"))
        tmdb = from_union([from_int, from_none], obj.get("tmdb"))
        trakt = from_union([from_int, from_none], obj.get("trakt"))
        tvdb = from_union([from_int, from_none], obj.get("tvdb"))
        tvrage = from_union([from_int, from_none], obj.get("tvrage"))
        return TraktEpisodeIDClass(imdb, slug, tmdb, trakt, tvdb, tvrage)

    def to_dict(self) -> dict:
        result: dict = {}
        result["imdb"] = from_union([from_str, from_none], self.imdb)
        result["slug"] = from_union([from_str, from_none], self.slug)
        result["tmdb"] = from_union([from_int, from_none], self.tmdb)
        result["trakt"] = from_union([from_int, from_none], self.trakt)
        result["tvdb"] = from_union([from_int, from_none], self.tvdb)
        result["tvrage"] = from_union([from_int, from_none], self.tvrage)
        return result


