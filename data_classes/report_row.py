from util.from_type import *
from data_classes.report_item import ReportItem
from data_classes.row_type import RowType


@dataclass
class ReportRow:
    columns: Optional[List[ReportItem]] = None
    has_embedded_image: Optional[bool] = None
    has_image_tags_backdrop: Optional[bool] = None
    has_image_tags_logo: Optional[bool] = None
    has_image_tags_primary: Optional[bool] = None
    has_local_trailer: Optional[bool] = None
    has_lock_data: Optional[bool] = None
    has_specials: Optional[bool] = None
    has_subtitles: Optional[bool] = None
    id: Optional[str] = None
    row_type: Optional[RowType] = None
    user_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReportRow':
        assert isinstance(obj, dict)
        columns = from_union([lambda x: from_list(ReportItem.from_dict, x), from_none], obj.get("Columns"))
        has_embedded_image = from_union([from_bool, from_none], obj.get("HasEmbeddedImage"))
        has_image_tags_backdrop = from_union([from_bool, from_none], obj.get("HasImageTagsBackdrop"))
        has_image_tags_logo = from_union([from_bool, from_none], obj.get("HasImageTagsLogo"))
        has_image_tags_primary = from_union([from_bool, from_none], obj.get("HasImageTagsPrimary"))
        has_local_trailer = from_union([from_bool, from_none], obj.get("HasLocalTrailer"))
        has_lock_data = from_union([from_bool, from_none], obj.get("HasLockData"))
        has_specials = from_union([from_bool, from_none], obj.get("HasSpecials"))
        has_subtitles = from_union([from_bool, from_none], obj.get("HasSubtitles"))
        id = from_union([from_str, from_none], obj.get("Id"))
        row_type = from_union([RowType, from_none], obj.get("RowType"))
        user_id = from_union([lambda x: UUID(x), from_none], obj.get("UserId"))
        return ReportRow(columns, has_embedded_image, has_image_tags_backdrop, has_image_tags_logo, has_image_tags_primary, has_local_trailer, has_lock_data, has_specials, has_subtitles, id, row_type, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Columns"] = from_union([lambda x: from_list(lambda x: to_class(ReportItem, x), x), from_none], self.columns)
        result["HasEmbeddedImage"] = from_union([from_bool, from_none], self.has_embedded_image)
        result["HasImageTagsBackdrop"] = from_union([from_bool, from_none], self.has_image_tags_backdrop)
        result["HasImageTagsLogo"] = from_union([from_bool, from_none], self.has_image_tags_logo)
        result["HasImageTagsPrimary"] = from_union([from_bool, from_none], self.has_image_tags_primary)
        result["HasLocalTrailer"] = from_union([from_bool, from_none], self.has_local_trailer)
        result["HasLockData"] = from_union([from_bool, from_none], self.has_lock_data)
        result["HasSpecials"] = from_union([from_bool, from_none], self.has_specials)
        result["HasSubtitles"] = from_union([from_bool, from_none], self.has_subtitles)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["RowType"] = from_union([lambda x: to_enum(RowType, x), from_none], self.row_type)
        result["UserId"] = from_union([lambda x: str(x), from_none], self.user_id)
        return result


