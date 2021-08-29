from util.from_type import *
from data_classes.trakt_episode_i_d_class import TraktEpisodeIDClass


@dataclass
class TraktEpisode:
    ids: Optional[TraktEpisodeIDClass] = None
    number: Optional[int] = None
    season: Optional[int] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktEpisode':
        assert isinstance(obj, dict)
        ids = from_union([TraktEpisodeIDClass.from_dict, from_none], obj.get("ids"))
        number = from_union([from_int, from_none], obj.get("number"))
        season = from_union([from_int, from_none], obj.get("season"))
        title = from_union([from_str, from_none], obj.get("title"))
        return TraktEpisode(ids, number, season, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ids"] = from_union([lambda x: to_class(TraktEpisodeIDClass, x), from_none], self.ids)
        result["number"] = from_union([from_int, from_none], self.number)
        result["season"] = from_union([from_int, from_none], self.season)
        result["title"] = from_union([from_str, from_none], self.title)
        return result


