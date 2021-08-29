from util.from_type import *


class RecordingStatusEnum(CaseInsensitiveEnum):
    """Gets or sets the status."""
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"
    CONFLICTED_NOT_OK = "ConflictedNotOk"
    CONFLICTED_OK = "ConflictedOk"
    ERROR = "Error"
    IN_PROGRESS = "InProgress"
    NEW = "New"


