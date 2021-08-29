from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.sort_order import SortOrder as SortOrder
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.base_item_dto import BaseItemDto as BaseItemDto


class Years(BaseRequestClass):
    def get_years(
            self, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            sort_order: Optional[List[SortOrder]] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            include_item_types: Optional[List[str]] = None, 
            media_types: Optional[List[str]] = None, 
            sort_by: Optional[List[str]] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            user_id: Optional[str] = None, 
            recursive: Optional[bool] = True, 
            enable_images: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Get years.

        Http:
            <get>: /Years

        Args:
            start_index (int): Skips over a given number of items within the results. Use for paging.
            limit (int): Optional. The maximum number of records to return.
            sort_order (List[SortOrder]): Sort Order - Ascending,Descending.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            exclude_item_types (List[str]): Optional. If specified, results will be excluded based on item type. This allows multiple, comma delimited.
            include_item_types (List[str]): Optional. If specified, results will be included based on item type. This allows multiple, comma delimited.
            media_types (List[str]): Optional. Filter by MediaType. Allows multiple, comma delimited.
            sort_by (List[str]): Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
            enable_user_data (bool): Optional. Include user data.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            user_id (str): User Id.
            recursive (bool = True): Search recursively.
            enable_images (bool = True): Optional. Include image information in output.

        Returns:
            <200> BaseItemDtoQueryResult: Year query returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            startIndex=start_index,
            limit=limit,
            sortOrder=sort_order,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            mediaTypes=media_types,
            sortBy=sort_by,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            userId=user_id,
            recursive=recursive,
            enableImages=enable_images,
        )
        return self._get(path='/Years', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_year(
            self, 
            year: int, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets a year.

        Http:
            <get>: /Years/{year}

        Args:
            year (int): The year.
            user_id (str): Optional. Filter by user id, and attach user data.

        Returns:
            <200> BaseItemDto: Year returned.
            <404> requests.Response: Year not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            year=year,
            userId=user_id,
        )
        return self._get(path='/Years/{year}', request_args=request_args, response_type=BaseItemDto)

