from util.from_type import *
from data_classes.day_of_week_element import DayOfWeekElement


@dataclass
class TaskTriggerInfo:
    """Class TaskTriggerInfo."""
    """Gets or sets the day of week."""
    day_of_week: Optional[DayOfWeekElement] = None
    """Gets or sets the interval."""
    interval_ticks: Optional[int] = None
    """Gets or sets the maximum runtime ticks."""
    max_runtime_ticks: Optional[int] = None
    """Gets or sets the time of day."""
    time_of_day_ticks: Optional[int] = None
    """Gets or sets the type."""
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TaskTriggerInfo':
        assert isinstance(obj, dict)
        day_of_week = from_union([DayOfWeekElement, from_none], obj.get("DayOfWeek"))
        interval_ticks = from_union([from_int, from_none], obj.get("IntervalTicks"))
        max_runtime_ticks = from_union([from_int, from_none], obj.get("MaxRuntimeTicks"))
        time_of_day_ticks = from_union([from_int, from_none], obj.get("TimeOfDayTicks"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return TaskTriggerInfo(day_of_week, interval_ticks, max_runtime_ticks, time_of_day_ticks, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DayOfWeek"] = from_union([lambda x: to_enum(DayOfWeekElement, x), from_none], self.day_of_week)
        result["IntervalTicks"] = from_union([from_int, from_none], self.interval_ticks)
        result["MaxRuntimeTicks"] = from_union([from_int, from_none], self.max_runtime_ticks)
        result["TimeOfDayTicks"] = from_union([from_int, from_none], self.time_of_day_ticks)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


