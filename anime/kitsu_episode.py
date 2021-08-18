# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = kitsu_episode_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast

T = TypeVar("T")


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return int(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


@dataclass
class Meta:
    dimensions: Optional[Dict[str, Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        dimensions = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("dimensions"))
        return Meta(dimensions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dimensions"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.dimensions)
        return result


@dataclass
class Thumbnail:
    meta: Optional[Meta] = None
    original: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Thumbnail':
        assert isinstance(obj, dict)
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        original = from_union([from_str, from_none], obj.get("original"))
        return Thumbnail(meta, original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        result["original"] = from_union([from_str, from_none], self.original)
        return result


@dataclass
class Titles:
    en_jp: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Titles':
        assert isinstance(obj, dict)
        en_jp = from_union([from_str, from_none], obj.get("en_jp"))
        return Titles(en_jp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["en_jp"] = from_union([from_str, from_none], self.en_jp)
        return result


@dataclass
class KitsuEpisode:
    airdate: Optional[str] = None
    canonical_title: Optional[str] = None
    created_at: Optional[str] = None
    id: Optional[str] = None
    length: Optional[str] = None
    number: Optional[float] = None
    season_number: Optional[float] = None
    synopsis: Optional[str] = None
    thumbnail: Optional[Thumbnail] = None
    titles: Optional[Titles] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'KitsuEpisode':
        assert isinstance(obj, dict)
        airdate = from_union([from_str, from_none], obj.get("airdate"))
        canonical_title = from_union([from_str, from_none], obj.get("canonicalTitle"))
        created_at = from_union([from_str, from_none], obj.get("createdAt"))
        id = from_union([from_str, from_none], obj.get("id"))
        length = from_union([from_int, from_none], obj.get("length"))
        number = from_union([from_int, from_none], obj.get("number"))
        season_number = from_union([from_int, from_none], obj.get("seasonNumber"))
        synopsis = from_union([from_str, from_none], obj.get("synopsis"))
        thumbnail = from_union([Thumbnail.from_dict, from_none], obj.get("thumbnail"))
        titles = from_union([Titles.from_dict, from_none], obj.get("titles"))
        type = from_union([from_str, from_none], obj.get("type"))
        updated_at = from_union([from_str, from_none], obj.get("updatedAt"))
        return KitsuEpisode(airdate, canonical_title, created_at, id, length, number, season_number, synopsis,
                            thumbnail, titles, type, updated_at)

    def to_dict(self) -> dict:
        result: dict = {}
        result["airdate"] = from_union([from_str, from_none], self.airdate)
        result["canonicalTitle"] = from_union([from_str, from_none], self.canonical_title)
        result["createdAt"] = from_union([from_str, from_none], self.created_at)
        result["id"] = from_union([from_str, from_none], self.id)
        result["length"] = from_union([from_none, from_str], self.length)
        result["number"] = from_union([to_float, from_none], self.number)
        result["seasonNumber"] = from_union([to_float, from_none], self.season_number)
        result["synopsis"] = from_union([from_str, from_none], self.synopsis)
        result["thumbnail"] = from_union([lambda x: to_class(Thumbnail, x), from_none], self.thumbnail)
        result["titles"] = from_union([lambda x: to_class(Titles, x), from_none], self.titles)
        result["type"] = from_union([from_str, from_none], self.type)
        result["updatedAt"] = from_union([from_str, from_none], self.updated_at)
        return result
