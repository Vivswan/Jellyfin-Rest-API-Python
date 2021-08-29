from util.from_type import *
from data_classes.trakt_person_i_d_class import TraktPersonIDClass


@dataclass
class TraktPerson:
    ids: Optional[TraktPersonIDClass] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktPerson':
        assert isinstance(obj, dict)
        ids = from_union([TraktPersonIDClass.from_dict, from_none], obj.get("ids"))
        name = from_union([from_str, from_none], obj.get("name"))
        return TraktPerson(ids, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ids"] = from_union([lambda x: to_class(TraktPersonIDClass, x), from_none], self.ids)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


