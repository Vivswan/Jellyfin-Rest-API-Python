from util.from_type import *
class ItemFilter(CaseInsensitiveEnum):
    """Enum ItemFilter."""
    DISLIKES = "Dislikes"
    IS_FAVORITE = "IsFavorite"
    IS_FAVORITE_OR_LIKES = "IsFavoriteOrLikes"
    IS_FOLDER = "IsFolder"
    IS_NOT_FOLDER = "IsNotFolder"
    IS_PLAYED = "IsPlayed"
    IS_RESUMABLE = "IsResumable"
    IS_UNPLAYED = "IsUnplayed"
    LIKES = "Likes"


