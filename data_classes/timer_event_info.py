from util.from_type import *


@dataclass
class TimerEventInfo:
    id: Optional[str] = None
    program_id: Optional[UUID] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TimerEventInfo':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        program_id = from_union([lambda x: UUID(x), from_none], obj.get("ProgramId"))
        return TimerEventInfo(id, program_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["ProgramId"] = from_union([lambda x: str(x), from_none], self.program_id)
        return result


