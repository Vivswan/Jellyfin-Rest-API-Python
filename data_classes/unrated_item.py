from util.from_type import *


class UnratedItem(CaseInsensitiveEnum):
    """An enum representing an unrated item."""
    BOOK = "Book"
    CHANNEL_CONTENT = "ChannelContent"
    LIVE_TV_CHANNEL = "LiveTvChannel"
    LIVE_TV_PROGRAM = "LiveTvProgram"
    MOVIE = "Movie"
    MUSIC = "Music"
    OTHER = "Other"
    SERIES = "Series"
    TRAILER = "Trailer"


