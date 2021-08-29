from data_classes.general_command_type import GeneralCommandType
from util.from_type import *


@dataclass
class GeneralCommand:
    arguments: Optional[Dict[str, str]] = None
    controlling_user_id: Optional[UUID] = None
    """This exists simply to identify a set of known commands."""
    name: Optional[GeneralCommandType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GeneralCommand':
        assert isinstance(obj, dict)
        arguments = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Arguments"))
        controlling_user_id = from_union([lambda x: UUID(x), from_none], obj.get("ControllingUserId"))
        name = from_union([GeneralCommandType, from_none], obj.get("Name"))
        return GeneralCommand(arguments, controlling_user_id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Arguments"] = from_union([lambda x: from_dict(from_str, x), from_none], self.arguments)
        result["ControllingUserId"] = from_union([lambda x: str(x), from_none], self.controlling_user_id)
        result["Name"] = from_union([lambda x: to_enum(GeneralCommandType, x), from_none], self.name)
        return result


