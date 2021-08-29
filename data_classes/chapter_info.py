from util.from_type import *


@dataclass
class ChapterInfo:
    """Class ChapterInfo."""
    image_date_modified: Optional[datetime] = None
    """Gets or sets the image path."""
    image_path: Optional[str] = None
    image_tag: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the start position ticks."""
    start_position_ticks: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChapterInfo':
        assert isinstance(obj, dict)
        image_date_modified = from_union([from_datetime, from_none], obj.get("ImageDateModified"))
        image_path = from_union([from_str, from_none], obj.get("ImagePath"))
        image_tag = from_union([from_str, from_none], obj.get("ImageTag"))
        name = from_union([from_str, from_none], obj.get("Name"))
        start_position_ticks = from_union([from_int, from_none], obj.get("StartPositionTicks"))
        return ChapterInfo(image_date_modified, image_path, image_tag, name, start_position_ticks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ImageDateModified"] = from_union([lambda x: x.isoformat(), from_none], self.image_date_modified)
        result["ImagePath"] = from_union([from_str, from_none], self.image_path)
        result["ImageTag"] = from_union([from_str, from_none], self.image_tag)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["StartPositionTicks"] = from_union([from_int, from_none], self.start_position_ticks)
        return result


