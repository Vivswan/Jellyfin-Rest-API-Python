from typing import List
from typing import Optional

from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.item_fields import ItemFields as ItemFields
from util.BaseRequestClass import BaseRequestClass


class Albums(BaseRequestClass):
    def get_instant_mix_from_album(
            self, 
            id: str, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_images: Optional[bool] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None
    ) -> BaseItemDtoQueryResult:
        """Creates an instant playlist based on a given album.

        Http:
            <get>: /Albums/{id}/InstantMix

        Args:
            id (str): The item id.
            user_id (str): Optional. Filter by user id, and attach user data.
            limit (int): Optional. The maximum number of records to return.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            enable_images (bool): Optional. Include image information in output.
            enable_user_data (bool): Optional. Include user data.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.

        Returns:
            <200> BaseItemDtoQueryResult: Instant playlist returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
            userId=user_id,
            limit=limit,
            fields=fields,
            enableImages=enable_images,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
        )
        return self._get(path='/Albums/{id}/InstantMix', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_similar_albums(
            self, 
            item_id: str, 
            exclude_artist_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets similar items.

        Http:
            <get>: /Albums/{itemId}/Similar

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
        return self._get(path='/Albums/{itemId}/Similar', request_args=request_args, response_type=BaseItemDtoQueryResult)

