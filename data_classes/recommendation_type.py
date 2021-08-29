from util.from_type import *


class RecommendationType(CaseInsensitiveEnum):
    HAS_ACTOR_FROM_RECENTLY_PLAYED = "HasActorFromRecentlyPlayed"
    HAS_DIRECTOR_FROM_RECENTLY_PLAYED = "HasDirectorFromRecentlyPlayed"
    HAS_LIKED_ACTOR = "HasLikedActor"
    HAS_LIKED_DIRECTOR = "HasLikedDirector"
    SIMILAR_TO_LIKED_ITEM = "SimilarToLikedItem"
    SIMILAR_TO_RECENTLY_PLAYED = "SimilarToRecentlyPlayed"


