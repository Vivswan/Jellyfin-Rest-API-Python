from util.from_type import *


@dataclass
class Items:
    episodes: Optional[int] = None
    movies: Optional[int] = None
    people: Optional[int] = None
    seasons: Optional[int] = None
    shows: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Items':
        assert isinstance(obj, dict)
        episodes = from_union([from_int, from_none], obj.get("episodes"))
        movies = from_union([from_int, from_none], obj.get("movies"))
        people = from_union([from_int, from_none], obj.get("people"))
        seasons = from_union([from_int, from_none], obj.get("seasons"))
        shows = from_union([from_int, from_none], obj.get("shows"))
        return Items(episodes, movies, people, seasons, shows)

    def to_dict(self) -> dict:
        result: dict = {}
        result["episodes"] = from_union([from_int, from_none], self.episodes)
        result["movies"] = from_union([from_int, from_none], self.movies)
        result["people"] = from_union([from_int, from_none], self.people)
        result["seasons"] = from_union([from_int, from_none], self.seasons)
        result["shows"] = from_union([from_int, from_none], self.shows)
        return result


