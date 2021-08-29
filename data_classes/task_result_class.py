from util.from_type import *
from data_classes.task_completion_status_enum import TaskCompletionStatusEnum


@dataclass
class TaskResultClass:
    """Gets or sets the last execution result.
    
    Class TaskExecutionInfo.
    """
    """Gets or sets the end time UTC."""
    end_time_utc: Optional[datetime] = None
    """Gets or sets the error message."""
    error_message: Optional[str] = None
    """Gets or sets the id."""
    id: Optional[str] = None
    """Gets or sets the key."""
    key: Optional[str] = None
    """Gets or sets the long error message."""
    long_error_message: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the start time UTC."""
    start_time_utc: Optional[datetime] = None
    """Gets or sets the status."""
    status: Optional[TaskCompletionStatusEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TaskResultClass':
        assert isinstance(obj, dict)
        end_time_utc = from_union([from_datetime, from_none], obj.get("EndTimeUtc"))
        error_message = from_union([from_str, from_none], obj.get("ErrorMessage"))
        id = from_union([from_str, from_none], obj.get("Id"))
        key = from_union([from_str, from_none], obj.get("Key"))
        long_error_message = from_union([from_str, from_none], obj.get("LongErrorMessage"))
        name = from_union([from_str, from_none], obj.get("Name"))
        start_time_utc = from_union([from_datetime, from_none], obj.get("StartTimeUtc"))
        status = from_union([TaskCompletionStatusEnum, from_none], obj.get("Status"))
        return TaskResultClass(end_time_utc, error_message, id, key, long_error_message, name, start_time_utc, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EndTimeUtc"] = from_union([lambda x: x.isoformat(), from_none], self.end_time_utc)
        result["ErrorMessage"] = from_union([from_str, from_none], self.error_message)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Key"] = from_union([from_str, from_none], self.key)
        result["LongErrorMessage"] = from_union([from_str, from_none], self.long_error_message)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["StartTimeUtc"] = from_union([lambda x: x.isoformat(), from_none], self.start_time_utc)
        result["Status"] = from_union([lambda x: to_enum(TaskCompletionStatusEnum, x), from_none], self.status)
        return result


