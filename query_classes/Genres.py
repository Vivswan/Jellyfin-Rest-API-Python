from typing import List
from typing import Optional

import requests

from data_classes.base_item_dto import BaseItemDto as BaseItemDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.image_format import ImageFormat as ImageFormat
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.item_fields import ItemFields as ItemFields
from util.BaseRequestClass import BaseRequestClass


class Genres(BaseRequestClass):
    def get_genres(
            self, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            search_term: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            include_item_types: Optional[List[str]] = None, 
            is_favorite: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            user_id: Optional[str] = None, 
            name_starts_with_or_greater: Optional[str] = None, 
            name_starts_with: Optional[str] = None, 
            name_less_than: Optional[str] = None, 
            enable_images: Optional[bool] = True, 
            enable_total_record_count: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets all genres from a given item, folder, or the entire library.

        Http:
            <get>: /Genres

        Args:
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            search_term (str): The search term.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            exclude_item_types (List[str]): Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
            include_item_types (List[str]): Optional. If specified, results will be filtered in based on item type. This allows multiple, comma delimited.
            is_favorite (bool): Optional filter by items that are marked as favorite, or not.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            user_id (str): User id.
            name_starts_with_or_greater (str): Optional filter by items whose name is sorted equally or greater than a given input string.
            name_starts_with (str): Optional filter by items whose name is sorted equally than a given input string.
            name_less_than (str): Optional filter by items whose name is equally or lesser than a given input string.
            enable_images (bool = True): Optional, include image information in output.
            enable_total_record_count (bool = True): Optional. Include total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Genres returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            startIndex=start_index,
            limit=limit,
            searchTerm=search_term,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            isFavorite=is_favorite,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            userId=user_id,
            nameStartsWithOrGreater=name_starts_with_or_greater,
            nameStartsWith=name_starts_with,
            nameLessThan=name_less_than,
            enableImages=enable_images,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/Genres', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_genre(
            self, 
            genre_name: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets a genre, by name.

        Http:
            <get>: /Genres/{genreName}

        Args:
            genre_name (str): The genre name.
            user_id (str): The user id.

        Returns:
            <200> BaseItemDto: Genres returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            genreName=genre_name,
            userId=user_id,
        )
        return self._get(path='/Genres/{genreName}', request_args=request_args, response_type=BaseItemDto)

    def get_genre_image(
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
        """Get genre image by name.

        Http:
            <get>: /Genres/{name}/Images/{imageType}

        Args:
            name (str): Genre name.
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
        return self._get(path='/Genres/{name}/Images/{imageType}', request_args=request_args)

    def head_genre_image(
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
        """Get genre image by name.

        Http:
            <head>: /Genres/{name}/Images/{imageType}

        Args:
            name (str): Genre name.
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
        return self._head(path='/Genres/{name}/Images/{imageType}', request_args=request_args)

    def get_genre_image_by_index(
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
        """Get genre image by name.

        Http:
            <get>: /Genres/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Genre name.
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
        return self._get(path='/Genres/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def head_genre_image_by_index(
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
        """Get genre image by name.

        Http:
            <head>: /Genres/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Genre name.
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
        return self._head(path='/Genres/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

