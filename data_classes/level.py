from util.from_type import *


class Level(CaseInsensitiveEnum):
    """Gets or sets the notification level.
    
    Gets or sets the maximum unread notification level.
    """
    ERROR = "Error"
    NORMAL = "Normal"
    WARNING = "Warning"
