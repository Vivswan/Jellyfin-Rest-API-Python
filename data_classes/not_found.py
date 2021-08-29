from util.from_type import *
from data_classes.trakt_episode import TraktEpisode
from data_classes.trakt_movie import TraktMovie
from data_classes.trakt_person import TraktPerson
from data_classes.trakt_season import TraktSeason
from data_classes.trakt_show import TraktShow


@dataclass
class NotFound:
    episodes: Optional[List[TraktEpisode]] = None
    movies: Optional[List[TraktMovie]] = None
    people: Optional[List[TraktPerson]] = None
    seasons: Optional[List[TraktSeason]] = None
    shows: Optional[List[TraktShow]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'NotFound':
        assert isinstance(obj, dict)
        episodes = from_union([lambda x: from_list(TraktEpisode.from_dict, x), from_none], obj.get("episodes"))
        movies = from_union([lambda x: from_list(TraktMovie.from_dict, x), from_none], obj.get("movies"))
        people = from_union([lambda x: from_list(TraktPerson.from_dict, x), from_none], obj.get("people"))
        seasons = from_union([lambda x: from_list(TraktSeason.from_dict, x), from_none], obj.get("seasons"))
        shows = from_union([lambda x: from_list(TraktShow.from_dict, x), from_none], obj.get("shows"))
        return NotFound(episodes, movies, people, seasons, shows)

    def to_dict(self) -> dict:
        result: dict = {}
        result["episodes"] = from_union([lambda x: from_list(lambda x: to_class(TraktEpisode, x), x), from_none], self.episodes)
        result["movies"] = from_union([lambda x: from_list(lambda x: to_class(TraktMovie, x), x), from_none], self.movies)
        result["people"] = from_union([lambda x: from_list(lambda x: to_class(TraktPerson, x), x), from_none], self.people)
        result["seasons"] = from_union([lambda x: from_list(lambda x: to_class(TraktSeason, x), x), from_none], self.seasons)
        result["shows"] = from_union([lambda x: from_list(lambda x: to_class(TraktShow, x), x), from_none], self.shows)
        return result


