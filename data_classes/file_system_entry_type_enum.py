from util.from_type import *


class FileSystemEntryTypeEnum(CaseInsensitiveEnum):
    """Gets the type.
    
    Enum FileSystemEntryType.
    """
    DIRECTORY = "Directory"
    FILE = "File"
    NETWORK_COMPUTER = "NetworkComputer"
    NETWORK_SHARE = "NetworkShare"


