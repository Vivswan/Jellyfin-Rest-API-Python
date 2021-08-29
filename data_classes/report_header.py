from util.from_type import *
from data_classes.header_metadata import HeaderMetadata
from data_classes.item_view_type import ItemViewType
from data_classes.display_type import DisplayType
from data_classes.field_type import FieldType


@dataclass
class ReportHeader:
    can_group: Optional[bool] = None
    display_type: Optional[DisplayType] = None
    field_name: Optional[HeaderMetadata] = None
    header_field_type: Optional[FieldType] = None
    item_view_type: Optional[ItemViewType] = None
    name: Optional[str] = None
    show_header_label: Optional[bool] = None
    sort_field: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReportHeader':
        assert isinstance(obj, dict)
        can_group = from_union([from_bool, from_none], obj.get("CanGroup"))
        display_type = from_union([DisplayType, from_none], obj.get("DisplayType"))
        field_name = from_union([HeaderMetadata, from_none], obj.get("FieldName"))
        header_field_type = from_union([FieldType, from_none], obj.get("HeaderFieldType"))
        item_view_type = from_union([ItemViewType, from_none], obj.get("ItemViewType"))
        name = from_union([from_str, from_none], obj.get("Name"))
        show_header_label = from_union([from_bool, from_none], obj.get("ShowHeaderLabel"))
        sort_field = from_union([from_str, from_none], obj.get("SortField"))
        type = from_union([from_str, from_none], obj.get("Type"))
        visible = from_union([from_bool, from_none], obj.get("Visible"))
        return ReportHeader(can_group, display_type, field_name, header_field_type, item_view_type, name, show_header_label, sort_field, type, visible)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CanGroup"] = from_union([from_bool, from_none], self.can_group)
        result["DisplayType"] = from_union([lambda x: to_enum(DisplayType, x), from_none], self.display_type)
        result["FieldName"] = from_union([lambda x: to_enum(HeaderMetadata, x), from_none], self.field_name)
        result["HeaderFieldType"] = from_union([lambda x: to_enum(FieldType, x), from_none], self.header_field_type)
        result["ItemViewType"] = from_union([lambda x: to_enum(ItemViewType, x), from_none], self.item_view_type)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ShowHeaderLabel"] = from_union([from_bool, from_none], self.show_header_label)
        result["SortField"] = from_union([from_str, from_none], self.sort_field)
        result["Type"] = from_union([from_str, from_none], self.type)
        result["Visible"] = from_union([from_bool, from_none], self.visible)
        return result


