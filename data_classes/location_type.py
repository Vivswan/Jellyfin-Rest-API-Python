from util.from_type import *


class LocationType(CaseInsensitiveEnum):
    """Gets or sets the type of the location.
    
    Enum LocationType.
    """
    FILE_SYSTEM = "FileSystem"
    OFFLINE = "Offline"
    REMOTE = "Remote"
    VIRTUAL = "Virtual"


