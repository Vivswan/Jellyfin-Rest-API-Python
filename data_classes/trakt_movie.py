from util.from_type import *
from data_classes.trakt_movie_i_d_class import TraktMovieIDClass


@dataclass
class TraktMovie:
    ids: Optional[TraktMovieIDClass] = None
    title: Optional[str] = None
    year: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktMovie':
        assert isinstance(obj, dict)
        ids = from_union([TraktMovieIDClass.from_dict, from_none], obj.get("ids"))
        title = from_union([from_str, from_none], obj.get("title"))
        year = from_union([from_int, from_none], obj.get("year"))
        return TraktMovie(ids, title, year)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ids"] = from_union([lambda x: to_class(TraktMovieIDClass, x), from_none], self.ids)
        result["title"] = from_union([from_str, from_none], self.title)
        result["year"] = from_union([from_int, from_none], self.year)
        return result


