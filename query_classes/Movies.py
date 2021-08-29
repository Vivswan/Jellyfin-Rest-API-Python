from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.recommendation_dto import RecommendationDto as RecommendationDto
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult


class Movies(BaseRequestClass):
    def get_similar_movies(
            self, 
            item_id: str, 
            exclude_artist_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets similar items.

        Http:
            <get>: /Movies/{itemId}/Similar

        Args:
            item_id (str): The item id.
            exclude_artist_ids (List[str]): Exclude artist ids.
            user_id (str): Optional. Filter by user id, and attach user data.
            limit (int): Optional. The maximum number of records to return.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.

        Returns:
            <200> BaseItemDtoQueryResult: Similar items returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            excludeArtistIds=exclude_artist_ids,
            userId=user_id,
            limit=limit,
            fields=fields,
        )
        return self._get(path='/Movies/{itemId}/Similar', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_movie_recommendations(
            self, 
            user_id: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            category_limit: Optional[int] = 5, 
            item_limit: Optional[int] = 8
    ) -> List[RecommendationDto]:
        """Gets movie recommendations.

        Http:
            <get>: /Movies/Recommendations

        Args:
            user_id (str): Optional. Filter by user id, and attach user data.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. The fields to return.
            category_limit (int = 5): The max number of categories to return.
            item_limit (int = 8): The max number of items to return per category.

        Returns:
            <200> List[RecommendationDto]: Movie recommendations returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            parentId=parent_id,
            fields=fields,
            categoryLimit=category_limit,
            itemLimit=item_limit,
        )
        return self._get(path='/Movies/Recommendations', request_args=request_args, response_type=List[RecommendationDto])

