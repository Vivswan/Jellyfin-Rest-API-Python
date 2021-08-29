import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.image_format import ImageFormat as ImageFormat
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.base_item_dto import BaseItemDto as BaseItemDto


class MusicGenres(BaseRequestClass):
    def get_music_genre_image(
            self, 
            name: str, 
            image_type: ImageType, 
            tag: Optional[str] = None, 
            format: Optional[ImageFormat] = None, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            crop_whitespace: Optional[bool] = None, 
            add_played_indicator: Optional[bool] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None, 
            image_index: Optional[int] = None
    ) -> requests.Response:
        """Get music genre image by name.

        Http:
            <get>: /MusicGenres/{name}/Images/{imageType}

        Args:
            name (str): Music genre name.
            image_type (ImageType): Image type.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            format (ImageFormat): Determines the output format of the image - original,gif,jpg,png.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            add_played_indicator (bool): Optional. Add a played indicator.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.
            image_index (int): Image index.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            name=name,
            imageType=image_type,
            tag=tag,
            format=format,
            maxWidth=max_width,
            maxHeight=max_height,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            cropWhitespace=crop_whitespace,
            addPlayedIndicator=add_played_indicator,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
            imageIndex=image_index,
        )
        return self._get(path='/MusicGenres/{name}/Images/{imageType}', request_args=request_args)

    def head_music_genre_image(
            self, 
            name: str, 
            image_type: ImageType, 
            tag: Optional[str] = None, 
            format: Optional[ImageFormat] = None, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            crop_whitespace: Optional[bool] = None, 
            add_played_indicator: Optional[bool] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None, 
            image_index: Optional[int] = None
    ) -> requests.Response:
        """Get music genre image by name.

        Http:
            <head>: /MusicGenres/{name}/Images/{imageType}

        Args:
            name (str): Music genre name.
            image_type (ImageType): Image type.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            format (ImageFormat): Determines the output format of the image - original,gif,jpg,png.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            add_played_indicator (bool): Optional. Add a played indicator.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.
            image_index (int): Image index.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            name=name,
            imageType=image_type,
            tag=tag,
            format=format,
            maxWidth=max_width,
            maxHeight=max_height,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            cropWhitespace=crop_whitespace,
            addPlayedIndicator=add_played_indicator,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
            imageIndex=image_index,
        )
        return self._head(path='/MusicGenres/{name}/Images/{imageType}', request_args=request_args)

    def get_music_genre_image_by_index(
            self, 
            name: str, 
            image_type: ImageType, 
            image_index: int, 
            tag: Optional[str] = None, 
            format: Optional[ImageFormat] = None, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            crop_whitespace: Optional[bool] = None, 
            add_played_indicator: Optional[bool] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None
    ) -> requests.Response:
        """Get music genre image by name.

        Http:
            <get>: /MusicGenres/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Music genre name.
            image_type (ImageType): Image type.
            image_index (int): Image index.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            format (ImageFormat): Determines the output format of the image - original,gif,jpg,png.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            add_played_indicator (bool): Optional. Add a played indicator.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            name=name,
            imageType=image_type,
            imageIndex=image_index,
            tag=tag,
            format=format,
            maxWidth=max_width,
            maxHeight=max_height,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            cropWhitespace=crop_whitespace,
            addPlayedIndicator=add_played_indicator,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
        )
        return self._get(path='/MusicGenres/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def head_music_genre_image_by_index(
            self, 
            name: str, 
            image_type: ImageType, 
            image_index: int, 
            tag: Optional[str] = None, 
            format: Optional[ImageFormat] = None, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            crop_whitespace: Optional[bool] = None, 
            add_played_indicator: Optional[bool] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None
    ) -> requests.Response:
        """Get music genre image by name.

        Http:
            <head>: /MusicGenres/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Music genre name.
            image_type (ImageType): Image type.
            image_index (int): Image index.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            format (ImageFormat): Determines the output format of the image - original,gif,jpg,png.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            add_played_indicator (bool): Optional. Add a played indicator.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            name=name,
            imageType=image_type,
            imageIndex=image_index,
            tag=tag,
            format=format,
            maxWidth=max_width,
            maxHeight=max_height,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            cropWhitespace=crop_whitespace,
            addPlayedIndicator=add_played_indicator,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
        )
        return self._head(path='/MusicGenres/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def get_instant_mix_from_music_genre_by_id(
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
        """Creates an instant playlist based on a given genre.

        Http:
            <get>: /MusicGenres/{id}/InstantMix

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
        return self._get(path='/MusicGenres/{id}/InstantMix', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_instant_mix_from_music_genre_by_name(
            self, 
            name: str, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_images: Optional[bool] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None
    ) -> BaseItemDtoQueryResult:
        """Creates an instant playlist based on a given genre.

        Http:
            <get>: /MusicGenres/{name}/InstantMix

        Args:
            name (str): The genre name.
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
            name=name,
            userId=user_id,
            limit=limit,
            fields=fields,
            enableImages=enable_images,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
        )
        return self._get(path='/MusicGenres/{name}/InstantMix', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_music_genre(
            self, 
            genre_name: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets a music genre, by name.

        Http:
            <get>: /MusicGenres/{genreName}

        Args:
            genre_name (str): The genre name.
            user_id (str): Optional. Filter by user id, and attach user data.

        Returns:
            <200> BaseItemDto: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            genreName=genre_name,
            userId=user_id,
        )
        return self._get(path='/MusicGenres/{genreName}', request_args=request_args, response_type=BaseItemDto)

