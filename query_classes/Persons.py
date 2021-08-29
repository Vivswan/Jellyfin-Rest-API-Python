import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.item_filter import ItemFilter as ItemFilter
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.image_format import ImageFormat as ImageFormat
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.base_item_dto import BaseItemDto as BaseItemDto


class Persons(BaseRequestClass):
    def get_person_image(
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
        """Get person image by name.

        Http:
            <get>: /Persons/{name}/Images/{imageType}

        Args:
            name (str): Person name.
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
        return self._get(path='/Persons/{name}/Images/{imageType}', request_args=request_args)

    def head_person_image(
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
        """Get person image by name.

        Http:
            <head>: /Persons/{name}/Images/{imageType}

        Args:
            name (str): Person name.
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
        return self._head(path='/Persons/{name}/Images/{imageType}', request_args=request_args)

    def get_person_image_by_index(
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
        """Get person image by name.

        Http:
            <get>: /Persons/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Person name.
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
        return self._get(path='/Persons/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def head_person_image_by_index(
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
        """Get person image by name.

        Http:
            <head>: /Persons/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Person name.
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
        return self._head(path='/Persons/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def get_persons(
            self, 
            limit: Optional[int] = None, 
            search_term: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            filters: Optional[List[ItemFilter]] = None, 
            is_favorite: Optional[bool] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            exclude_person_types: Optional[List[str]] = None, 
            person_types: Optional[List[str]] = None, 
            appears_in_item_id: Optional[str] = None, 
            user_id: Optional[str] = None, 
            enable_images: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets all persons.

        Http:
            <get>: /Persons

        Args:
            limit (int): Optional. The maximum number of records to return.
            search_term (str): The search term.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply.
            is_favorite (bool): Optional filter by items that are marked as favorite, or not. userId is required.
            enable_user_data (bool): Optional, include user data.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            exclude_person_types (List[str]): Optional. If specified results will be filtered to exclude those containing the specified PersonType. Allows multiple, comma-delimited.
            person_types (List[str]): Optional. If specified results will be filtered to include only those containing the specified PersonType. Allows multiple, comma-delimited.
            appears_in_item_id (str): Optional. If specified, person results will be filtered on items related to said persons.
            user_id (str): User id.
            enable_images (bool = True): Optional, include image information in output.

        Returns:
            <200> BaseItemDtoQueryResult: Persons returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            limit=limit,
            searchTerm=search_term,
            fields=fields,
            filters=filters,
            isFavorite=is_favorite,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            excludePersonTypes=exclude_person_types,
            personTypes=person_types,
            appearsInItemId=appears_in_item_id,
            userId=user_id,
            enableImages=enable_images,
        )
        return self._get(path='/Persons', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_person(
            self, 
            name: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Get person by name.

        Http:
            <get>: /Persons/{name}

        Args:
            name (str): Person name.
            user_id (str): Optional. Filter by user id, and attach user data.

        Returns:
            <200> BaseItemDto: Person returned.
            <404> requests.Response: Person not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            userId=user_id,
        )
        return self._get(path='/Persons/{name}', request_args=request_args, response_type=BaseItemDto)

