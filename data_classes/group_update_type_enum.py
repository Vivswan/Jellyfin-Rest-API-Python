from util.from_type import *
class GroupUpdateTypeEnum(CaseInsensitiveEnum):
    """Enum GroupUpdateType.
    
    Gets the update type.
    """
    CREATE_GROUP_DENIED = "CreateGroupDenied"
    GROUP_DOES_NOT_EXIST = "GroupDoesNotExist"
    GROUP_JOINED = "GroupJoined"
    GROUP_LEFT = "GroupLeft"
    JOIN_GROUP_DENIED = "JoinGroupDenied"
    LIBRARY_ACCESS_DENIED = "LibraryAccessDenied"
    NOT_IN_GROUP = "NotInGroup"
    PLAY_QUEUE = "PlayQueue"
    STATE_UPDATE = "StateUpdate"
    USER_JOINED = "UserJoined"
    USER_LEFT = "UserLeft"


