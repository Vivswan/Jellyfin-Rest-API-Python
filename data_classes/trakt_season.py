from util.from_type import *
from data_classes.trakt_season_i_d_class import TraktSeasonIDClass


@dataclass
class TraktSeason:
    ids: Optional[TraktSeasonIDClass] = None
    number: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktSeason':
        assert isinstance(obj, dict)
        ids = from_union([TraktSeasonIDClass.from_dict, from_none], obj.get("ids"))
        number = from_union([from_int, from_none], obj.get("number"))
        return TraktSeason(ids, number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ids"] = from_union([lambda x: to_class(TraktSeasonIDClass, x), from_none], self.ids)
        result["number"] = from_union([from_int, from_none], self.number)
        return result


