from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult


class Shows(BaseRequestClass):
    def get_similar_shows(
            self, 
            item_id: str, 
            exclude_artist_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets similar items.

        Http:
            <get>: /Shows/{itemId}/Similar

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
        return self._get(path='/Shows/{itemId}/Similar', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_episodes(
            self, 
            series_id: str, 
            user_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            season: Optional[int] = None, 
            season_id: Optional[str] = None, 
            is_missing: Optional[bool] = None, 
            adjacent_to: Optional[str] = None, 
            start_item_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            enable_user_data: Optional[bool] = None, 
            sort_by: Optional[str] = None
    ) -> BaseItemDtoQueryResult:
        """Gets episodes for a tv season.

        Http:
            <get>: /Shows/{seriesId}/Episodes

        Args:
            series_id (str): The series id.
            user_id (str): The user id.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
            season (int): Optional filter by season number.
            season_id (str): Optional. Filter by season id.
            is_missing (bool): Optional. Filter by items that are missing episodes or not.
            adjacent_to (str): Optional. Return items that are siblings of a supplied item.
            start_item_id (str): Optional. Skip through the list until a given item is found.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            enable_images (bool): Optional, include image information in output.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            enable_user_data (bool): Optional. Include user data.
            sort_by (str): Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.

        Returns:
            <200> BaseItemDtoQueryResult: Success
            <404> requests.Response: Not Found
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            seriesId=series_id,
            userId=user_id,
            fields=fields,
            season=season,
            seasonId=season_id,
            isMissing=is_missing,
            adjacentTo=adjacent_to,
            startItemId=start_item_id,
            startIndex=start_index,
            limit=limit,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            enableUserData=enable_user_data,
            sortBy=sort_by,
        )
        return self._get(path='/Shows/{seriesId}/Episodes', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_seasons(
            self, 
            series_id: str, 
            user_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            is_special_season: Optional[bool] = None, 
            is_missing: Optional[bool] = None, 
            adjacent_to: Optional[str] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            enable_user_data: Optional[bool] = None
    ) -> BaseItemDtoQueryResult:
        """Gets seasons for a tv series.

        Http:
            <get>: /Shows/{seriesId}/Seasons

        Args:
            series_id (str): The series id.
            user_id (str): The user id.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines, TrailerUrls.
            is_special_season (bool): Optional. Filter by special season.
            is_missing (bool): Optional. Filter by items that are missing episodes or not.
            adjacent_to (str): Optional. Return items that are siblings of a supplied item.
            enable_images (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            enable_user_data (bool): Optional. Include user data.

        Returns:
            <200> BaseItemDtoQueryResult: Success
            <404> requests.Response: Not Found
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            seriesId=series_id,
            userId=user_id,
            fields=fields,
            isSpecialSeason=is_special_season,
            isMissing=is_missing,
            adjacentTo=adjacent_to,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            enableUserData=enable_user_data,
        )
        return self._get(path='/Shows/{seriesId}/Seasons', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_next_up(
            self, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None, 
            series_id: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            enable_imges: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            enable_user_data: Optional[bool] = None, 
            enable_total_record_count: Optional[bool] = True, 
            disable_first_episode: Optional[bool] = False
    ) -> BaseItemDtoQueryResult:
        """Gets a list of next up episodes.

        Http:
            <get>: /Shows/NextUp

        Args:
            user_id (str): The user id of the user to get the next up episodes for.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            series_id (str): Optional. Filter by series id.
            parent_id (str): Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
            enable_imges (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            enable_user_data (bool): Optional. Include user data.
            enable_total_record_count (bool = True): Whether to enable the total records count. Defaults to true.
            disable_first_episode (bool = False): Whether to disable sending the first episode in a series as next up.

        Returns:
            <200> BaseItemDtoQueryResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            fields=fields,
            seriesId=series_id,
            parentId=parent_id,
            enableImges=enable_imges,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            enableUserData=enable_user_data,
            enableTotalRecordCount=enable_total_record_count,
            disableFirstEpisode=disable_first_episode,
        )
        return self._get(path='/Shows/NextUp', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_upcoming_episodes(
            self, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None, 
            parent_id: Optional[str] = None, 
            enable_imges: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            enable_user_data: Optional[bool] = None
    ) -> BaseItemDtoQueryResult:
        """Gets a list of upcoming episodes.

        Http:
            <get>: /Shows/Upcoming

        Args:
            user_id (str): The user id of the user to get the upcoming episodes for.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            parent_id (str): Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
            enable_imges (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            enable_user_data (bool): Optional. Include user data.

        Returns:
            <200> BaseItemDtoQueryResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            fields=fields,
            parentId=parent_id,
            enableImges=enable_imges,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            enableUserData=enable_user_data,
        )
        return self._get(path='/Shows/Upcoming', request_args=request_args, response_type=BaseItemDtoQueryResult)

