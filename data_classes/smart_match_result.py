from util.from_type import *
from data_classes.file_organizer_type_enum import FileOrganizerTypeEnum


@dataclass
class SmartMatchResult:
    display_name: Optional[str] = None
    id: Optional[UUID] = None
    item_name: Optional[str] = None
    match_strings: Optional[List[str]] = None
    organizer_type: Optional[FileOrganizerTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SmartMatchResult':
        assert isinstance(obj, dict)
        display_name = from_union([from_str, from_none], obj.get("DisplayName"))
        id = from_union([lambda x: UUID(x), from_none], obj.get("Id"))
        item_name = from_union([from_str, from_none], obj.get("ItemName"))
        match_strings = from_union([lambda x: from_list(from_str, x), from_none], obj.get("MatchStrings"))
        organizer_type = from_union([FileOrganizerTypeEnum, from_none], obj.get("OrganizerType"))
        return SmartMatchResult(display_name, id, item_name, match_strings, organizer_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DisplayName"] = from_union([from_str, from_none], self.display_name)
        result["Id"] = from_union([lambda x: str(x), from_none], self.id)
        result["ItemName"] = from_union([from_str, from_none], self.item_name)
        result["MatchStrings"] = from_union([lambda x: from_list(from_str, x), from_none], self.match_strings)
        result["OrganizerType"] = from_union([lambda x: to_enum(FileOrganizerTypeEnum, x), from_none], self.organizer_type)
        return result


