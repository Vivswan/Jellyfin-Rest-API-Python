from util.from_type import *
from data_classes.trakt_show_i_d_class import TraktShowIDClass


@dataclass
class TraktShow:
    ids: Optional[TraktShowIDClass] = None
    title: Optional[str] = None
    year: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktShow':
        assert isinstance(obj, dict)
        ids = from_union([TraktShowIDClass.from_dict, from_none], obj.get("ids"))
        title = from_union([from_str, from_none], obj.get("title"))
        year = from_union([from_int, from_none], obj.get("year"))
        return TraktShow(ids, title, year)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ids"] = from_union([lambda x: to_class(TraktShowIDClass, x), from_none], self.ids)
        result["title"] = from_union([from_str, from_none], self.title)
        result["year"] = from_union([from_int, from_none], self.year)
        return result


