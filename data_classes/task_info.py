from util.from_type import *
from data_classes.task_result_class import TaskResultClass
from data_classes.task_state_enum import TaskStateEnum
from data_classes.task_trigger_info import TaskTriggerInfo


@dataclass
class TaskInfo:
    """Class TaskInfo."""
    """Gets or sets the category."""
    category: Optional[str] = None
    """Gets or sets the progress."""
    current_progress_percentage: Optional[float] = None
    """Gets or sets the description."""
    description: Optional[str] = None
    """Gets or sets the id."""
    id: Optional[str] = None
    """Gets or sets a value indicating whether this instance is hidden."""
    is_hidden: Optional[bool] = None
    """Gets or sets the key."""
    key: Optional[str] = None
    """Gets or sets the last execution result."""
    last_execution_result: Optional[TaskResultClass] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the state of the task."""
    state: Optional[TaskStateEnum] = None
    """Gets or sets the triggers."""
    triggers: Optional[List[TaskTriggerInfo]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TaskInfo':
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("Category"))
        current_progress_percentage = from_union([from_float, from_none], obj.get("CurrentProgressPercentage"))
        description = from_union([from_str, from_none], obj.get("Description"))
        id = from_union([from_str, from_none], obj.get("Id"))
        is_hidden = from_union([from_bool, from_none], obj.get("IsHidden"))
        key = from_union([from_str, from_none], obj.get("Key"))
        last_execution_result = from_union([TaskResultClass.from_dict, from_none], obj.get("LastExecutionResult"))
        name = from_union([from_str, from_none], obj.get("Name"))
        state = from_union([TaskStateEnum, from_none], obj.get("State"))
        triggers = from_union([lambda x: from_list(TaskTriggerInfo.from_dict, x), from_none], obj.get("Triggers"))
        return TaskInfo(category, current_progress_percentage, description, id, is_hidden, key, last_execution_result, name, state, triggers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Category"] = from_union([from_str, from_none], self.category)
        result["CurrentProgressPercentage"] = from_union([to_float, from_none], self.current_progress_percentage)
        result["Description"] = from_union([from_str, from_none], self.description)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IsHidden"] = from_union([from_bool, from_none], self.is_hidden)
        result["Key"] = from_union([from_str, from_none], self.key)
        result["LastExecutionResult"] = from_union([lambda x: to_class(TaskResultClass, x), from_none], self.last_execution_result)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["State"] = from_union([lambda x: to_enum(TaskStateEnum, x), from_none], self.state)
        result["Triggers"] = from_union([lambda x: from_list(lambda x: to_class(TaskTriggerInfo, x), x), from_none], self.triggers)
        return result


