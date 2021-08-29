from data_classes.day_of_week import DayOfWeek
from util.from_type import *


@dataclass
class AccessSchedule:
    """An entity representing a user's access schedule."""
    """Gets or sets the day of week."""
    day_of_week: DayOfWeek
    """Gets or sets the end hour."""
    end_hour: float
    """Gets or sets the id of this instance."""
    id: int
    """Gets or sets the start hour."""
    start_hour: float
    """Gets or sets the id of the associated user."""
    user_id: UUID

    @staticmethod
    def from_dict(obj: Any) -> 'AccessSchedule':
        assert isinstance(obj, dict)
        day_of_week = DayOfWeek(obj.get("DayOfWeek"))
        end_hour = from_float(obj.get("EndHour"))
        id = from_int(obj.get("Id"))
        start_hour = from_float(obj.get("StartHour"))
        user_id = UUID(obj.get("UserId"))
        return AccessSchedule(day_of_week, end_hour, id, start_hour, user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DayOfWeek"] = to_enum(DayOfWeek, self.day_of_week)
        result["EndHour"] = to_float(self.end_hour)
        result["Id"] = from_int(self.id)
        result["StartHour"] = to_float(self.start_hour)
        result["UserId"] = str(self.user_id)
        return result


