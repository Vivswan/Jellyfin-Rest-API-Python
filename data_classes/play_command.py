from util.from_type import *


class PlayCommand(CaseInsensitiveEnum):
    """Enum PlayCommand.
    
    Gets or sets the play command.
    """
    PLAY_INSTANT_MIX = "PlayInstantMix"
    PLAY_LAST = "PlayLast"
    PLAY_NEXT = "PlayNext"
    PLAY_NOW = "PlayNow"
    PLAY_SHUFFLE = "PlayShuffle"


