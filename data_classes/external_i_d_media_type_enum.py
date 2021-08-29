from util.from_type import *


class ExternalIDMediaTypeEnum(CaseInsensitiveEnum):
    """Gets or sets the specific media type for this id. This is used to distinguish between the
    different
    external id types for providers with multiple ids.
    A null value indicates there is no specific media type associated with the external id,
    or this is the
    default id for the external provider so there is no need to specify a type.
    
    The specific media type of an MediaBrowser.Model.Providers.ExternalIdInfo.
    """
    ALBUM = "Album"
    ALBUM_ARTIST = "AlbumArtist"
    ARTIST = "Artist"
    BOX_SET = "BoxSet"
    EPISODE = "Episode"
    MOVIE = "Movie"
    OTHER_ARTIST = "OtherArtist"
    PERSON = "Person"
    RELEASE_GROUP = "ReleaseGroup"
    SEASON = "Season"
    SERIES = "Series"
    TRACK = "Track"


