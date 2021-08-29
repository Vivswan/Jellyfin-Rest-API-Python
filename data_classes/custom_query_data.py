from util.from_type import *


@dataclass
class CustomQueryData:
    custom_query_string: Optional[str] = None
    replace_user_id: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CustomQueryData':
        assert isinstance(obj, dict)
        custom_query_string = from_union([from_str, from_none], obj.get("CustomQueryString"))
        replace_user_id = from_union([from_bool, from_none], obj.get("ReplaceUserId"))
        return CustomQueryData(custom_query_string, replace_user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CustomQueryString"] = from_union([from_str, from_none], self.custom_query_string)
        result["ReplaceUserId"] = from_union([from_bool, from_none], self.replace_user_id)
        return result


