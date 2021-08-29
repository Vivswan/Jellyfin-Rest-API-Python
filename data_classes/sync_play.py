from util.from_type import *


class SyncPlay(CaseInsensitiveEnum):
    """Gets or sets a value indicating what SyncPlay features the user can access.
    
    Enum SyncPlayUserAccessType.
    """
    CREATE_AND_JOIN_GROUPS = "CreateAndJoinGroups"
    JOIN_GROUPS = "JoinGroups"
    NONE = "None"


