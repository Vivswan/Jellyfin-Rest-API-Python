from util.from_type import *
from data_classes.items import Items
from data_classes.not_found import NotFound


@dataclass
class TraktSyncResponse:
    added: Optional[Items] = None
    deleted: Optional[Items] = None
    existing: Optional[Items] = None
    not_found: Optional[NotFound] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TraktSyncResponse':
        assert isinstance(obj, dict)
        added = from_union([Items.from_dict, from_none], obj.get("added"))
        deleted = from_union([Items.from_dict, from_none], obj.get("deleted"))
        existing = from_union([Items.from_dict, from_none], obj.get("existing"))
        not_found = from_union([NotFound.from_dict, from_none], obj.get("not_found"))
        return TraktSyncResponse(added, deleted, existing, not_found)

    def to_dict(self) -> dict:
        result: dict = {}
        result["added"] = from_union([lambda x: to_class(Items, x), from_none], self.added)
        result["deleted"] = from_union([lambda x: to_class(Items, x), from_none], self.deleted)
        result["existing"] = from_union([lambda x: to_class(Items, x), from_none], self.existing)
        result["not_found"] = from_union([lambda x: to_class(NotFound, x), from_none], self.not_found)
        return result


