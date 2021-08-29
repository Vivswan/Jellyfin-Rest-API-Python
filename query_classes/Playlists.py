import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.playlist_creation_result import PlaylistCreationResult as PlaylistCreationResult
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.create_playlist_dto import CreatePlaylistDto as CreatePlaylistDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult


class Playlists(BaseRequestClass):
    def get_instant_mix_from_playlist(
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
        """Creates an instant playlist based on a given playlist.

        Http:
            <get>: /Playlists/{id}/InstantMix

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
        return self._get(path='/Playlists/{id}/InstantMix', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def create_playlist(
            self, 
            name: Optional[str] = None, 
            ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            media_type: Optional[str] = None, 
            request_body: Optional[CreatePlaylistDto] = None
    ) -> PlaylistCreationResult:
        """Creates a new playlist.

        Http:
            <post>: /Playlists

        Args:
            name (str): The playlist name.
            ids (List[str]): The item ids.
            user_id (str): The user id.
            media_type (str): The media type.
            request_body (CreatePlaylistDto): The create playlist payload.

        Returns:
            <200> PlaylistCreationResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            ids=ids,
            userId=user_id,
            mediaType=media_type,
            requestBody=request_body,
        )
        return self._post(path='/Playlists', request_args=request_args, response_type=PlaylistCreationResult)

    def add_to_playlist(
            self, 
            playlist_id: str, 
            ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None
    ) -> requests.Response:
        """Adds items to a playlist.

        Http:
            <post>: /Playlists/{playlistId}/Items

        Args:
            playlist_id (str): The playlist id.
            ids (List[str]): Item id, comma delimited.
            user_id (str): The userId.

        Returns:
            <204> requests.Response: Items added to playlist.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            playlistId=playlist_id,
            ids=ids,
            userId=user_id,
        )
        return self._post(path='/Playlists/{playlistId}/Items', request_args=request_args)

    def remove_from_playlist(
            self, 
            playlist_id: str, 
            entry_ids: Optional[List[str]] = None
    ) -> requests.Response:
        """Removes items from a playlist.

        Http:
            <delete>: /Playlists/{playlistId}/Items

        Args:
            playlist_id (str): The playlist id.
            entry_ids (List[str]): The item ids, comma delimited.

        Returns:
            <204> requests.Response: Items removed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            playlistId=playlist_id,
            entryIds=entry_ids,
        )
        return self._delete(path='/Playlists/{playlistId}/Items', request_args=request_args)

    def get_playlist_items(
            self, 
            playlist_id: str, 
            user_id: str, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_images: Optional[bool] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets the original items of a playlist.

        Http:
            <get>: /Playlists/{playlistId}/Items

        Args:
            playlist_id (str): The playlist id.
            user_id (str): User id.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            enable_images (bool): Optional. Include image information in output.
            enable_user_data (bool): Optional. Include user data.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.

        Returns:
            <200> BaseItemDtoQueryResult: Original playlist returned.
            <404> requests.Response: Playlist not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            playlistId=playlist_id,
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            fields=fields,
            enableImages=enable_images,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
        )
        return self._get(path='/Playlists/{playlistId}/Items', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def move_item(
            self, 
            playlist_id: str, 
            item_id: str, 
            new_index: int
    ) -> requests.Response:
        """Moves a playlist item.

        Http:
            <post>: /Playlists/{playlistId}/Items/{itemId}/Move/{newIndex}

        Args:
            playlist_id (str): The playlist id.
            item_id (str): The item id.
            new_index (int): The new index.

        Returns:
            <204> requests.Response: Item moved to new index.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            playlistId=playlist_id,
            itemId=item_id,
            newIndex=new_index,
        )
        return self._post(path='/Playlists/{playlistId}/Items/{itemId}/Move/{newIndex}', request_args=request_args)

