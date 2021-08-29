from util.from_type import *


class SubtitleMode(CaseInsensitiveEnum):
    """An enum representing a subtitle playback mode."""
    ALWAYS = "Always"
    DEFAULT = "Default"
    NONE = "None"
    ONLY_FORCED = "OnlyForced"
    SMART = "Smart"


