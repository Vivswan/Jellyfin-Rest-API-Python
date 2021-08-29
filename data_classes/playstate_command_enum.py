from util.from_type import *


class PlaystateCommandEnum(CaseInsensitiveEnum):
    """Enum PlaystateCommand."""
    FAST_FORWARD = "FastForward"
    NEXT_TRACK = "NextTrack"
    PAUSE = "Pause"
    PLAY_PAUSE = "PlayPause"
    PREVIOUS_TRACK = "PreviousTrack"
    REWIND = "Rewind"
    SEEK = "Seek"
    STOP = "Stop"
    UNPAUSE = "Unpause"


