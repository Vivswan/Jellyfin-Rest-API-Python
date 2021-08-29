from util.from_type import *


class Severity(CaseInsensitiveEnum):
    """Gets or sets the log severity."""
    CRITICAL = "Critical"
    DEBUG = "Debug"
    ERROR = "Error"
    INFORMATION = "Information"
    NONE = "None"
    TRACE = "Trace"
    WARNING = "Warning"


