from util.from_type import *


class TaskStateEnum(CaseInsensitiveEnum):
    """Gets or sets the state of the task.
    
    Enum TaskState.
    """
    CANCELLING = "Cancelling"
    IDLE = "Idle"
    RUNNING = "Running"


