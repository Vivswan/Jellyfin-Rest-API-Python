from util.from_type import *
from data_classes.media_update_info_path_dto import MediaUpdateInfoPathDto


@dataclass
class MediaUpdateInfoDto:
    """Media Update Info Dto."""
    """Gets or sets the list of updates."""
    updates: Optional[List[MediaUpdateInfoPathDto]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaUpdateInfoDto':
        assert isinstance(obj, dict)
        updates = from_union([lambda x: from_list(MediaUpdateInfoPathDto.from_dict, x), from_none], obj.get("Updates"))
        return MediaUpdateInfoDto(updates)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Updates"] = from_union([lambda x: from_list(lambda x: to_class(MediaUpdateInfoPathDto, x), x), from_none], self.updates)
        return result


