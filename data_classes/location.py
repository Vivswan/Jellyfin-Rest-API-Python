from util.from_type import *


class Location(CaseInsensitiveEnum):
    """Enum describing the location of the FFmpeg tool."""
    CUSTOM = "Custom"
    NOT_FOUND = "NotFound"
    SET_BY_ARGUMENT = "SetByArgument"
    SYSTEM = "System"


