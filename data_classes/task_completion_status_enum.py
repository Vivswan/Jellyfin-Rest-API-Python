from util.from_type import *


class TaskCompletionStatusEnum(CaseInsensitiveEnum):
    """Enum TaskCompletionStatus.
    
    Gets or sets the status.
    """
    ABORTED = "Aborted"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    FAILED = "Failed"


