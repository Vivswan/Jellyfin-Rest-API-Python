from data_classes.media_u_r_l import MediaURL
from util.from_type import *


@dataclass
class Item:
    """Class BaseItem."""
    container: Optional[str] = None
    date_last_saved: Optional[datetime] = None
    extra_ids: Optional[List[UUID]] = None
    height: Optional[int] = None
    is_hd: Optional[bool] = None
    is_shortcut: Optional[bool] = None
    """Gets or sets the remote trailers."""
    remote_trailers: Optional[List[MediaURL]] = None
    shortcut_path: Optional[str] = None
    size: Optional[int] = None
    supports_external_transfer: Optional[bool] = None
    width: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        container = from_union([from_str, from_none], obj.get("Container"))
        date_last_saved = from_union([from_datetime, from_none], obj.get("DateLastSaved"))
        extra_ids = from_union([lambda x: from_list(lambda x: UUID(x), x), from_none], obj.get("ExtraIds"))
        height = from_union([from_int, from_none], obj.get("Height"))
        is_hd = from_union([from_bool, from_none], obj.get("IsHD"))
        is_shortcut = from_union([from_bool, from_none], obj.get("IsShortcut"))
        remote_trailers = from_union([lambda x: from_list(MediaURL.from_dict, x), from_none], obj.get("RemoteTrailers"))
        shortcut_path = from_union([from_str, from_none], obj.get("ShortcutPath"))
        size = from_union([from_int, from_none], obj.get("Size"))
        supports_external_transfer = from_union([from_bool, from_none], obj.get("SupportsExternalTransfer"))
        width = from_union([from_int, from_none], obj.get("Width"))
        return Item(container, date_last_saved, extra_ids, height, is_hd, is_shortcut, remote_trailers, shortcut_path, size, supports_external_transfer, width)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Container"] = from_union([from_str, from_none], self.container)
        result["DateLastSaved"] = from_union([lambda x: x.isoformat(), from_none], self.date_last_saved)
        result["ExtraIds"] = from_union([lambda x: from_list(lambda x: str(x), x), from_none], self.extra_ids)
        result["Height"] = from_union([from_int, from_none], self.height)
        result["IsHD"] = from_union([from_bool, from_none], self.is_hd)
        result["IsShortcut"] = from_union([from_bool, from_none], self.is_shortcut)
        result["RemoteTrailers"] = from_union([lambda x: from_list(lambda x: to_class(MediaURL, x), x), from_none], self.remote_trailers)
        result["ShortcutPath"] = from_union([from_str, from_none], self.shortcut_path)
        result["Size"] = from_union([from_int, from_none], self.size)
        result["SupportsExternalTransfer"] = from_union([from_bool, from_none], self.supports_external_transfer)
        result["Width"] = from_union([from_int, from_none], self.width)
        return result


