from util.from_type import *


class SendCommandTypeEnum(CaseInsensitiveEnum):
    """Gets the command.
    
    Enum SendCommandType.
    """
    PAUSE = "Pause"
    SEEK = "Seek"
    STOP = "Stop"
    UNPAUSE = "Unpause"


