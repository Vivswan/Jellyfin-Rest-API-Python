from typing import List
from typing import Optional

import requests

from data_classes.base_item_dto import BaseItemDto as BaseItemDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.image_format import ImageFormat as ImageFormat
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.item_filter import ItemFilter as ItemFilter
from util.BaseRequestClass import BaseRequestClass


class Artists(BaseRequestClass):
    def get_artists(
            self, 
            min_community_rating: Optional[float] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            search_term: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            include_item_types: Optional[List[str]] = None, 
            filters: Optional[List[ItemFilter]] = None, 
            is_favorite: Optional[bool] = None, 
            media_types: Optional[List[str]] = None, 
            genres: Optional[List[str]] = None, 
            genre_ids: Optional[List[str]] = None, 
            official_ratings: Optional[List[str]] = None, 
            tags: Optional[List[str]] = None, 
            years: Optional[List[int]] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            person: Optional[str] = None, 
            person_ids: Optional[List[str]] = None, 
            person_types: Optional[List[str]] = None, 
            studios: Optional[List[str]] = None, 
            studio_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            name_starts_with_or_greater: Optional[str] = None, 
            name_starts_with: Optional[str] = None, 
            name_less_than: Optional[str] = None, 
            enable_images: Optional[bool] = True, 
            enable_total_record_count: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets all artists from a given item, folder, or the entire library.

        Http:
            <get>: /Artists

        Args:
            min_community_rating (float): Optional filter by minimum community rating.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            search_term (str): Optional. Search term.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            exclude_item_types (List[str]): Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply.
            is_favorite (bool): Optional filter by items that are marked as favorite, or not.
            media_types (List[str]): Optional filter by MediaType. Allows multiple, comma delimited.
            genres (List[str]): Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
            genre_ids (List[str]): Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
            official_ratings (List[str]): Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
            tags (List[str]): Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
            years (List[int]): Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
            enable_user_data (bool): Optional, include user data.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            person (str): Optional. If specified, results will be filtered to include only those containing the specified person.
            person_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified person ids.
            person_types (List[str]): Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
            studios (List[str]): Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
            studio_ids (List[str]): Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
            user_id (str): User id.
            name_starts_with_or_greater (str): Optional filter by items whose name is sorted equally or greater than a given input string.
            name_starts_with (str): Optional filter by items whose name is sorted equally than a given input string.
            name_less_than (str): Optional filter by items whose name is equally or lesser than a given input string.
            enable_images (bool = True): Optional, include image information in output.
            enable_total_record_count (bool = True): Total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Artists returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            minCommunityRating=min_community_rating,
            startIndex=start_index,
            limit=limit,
            searchTerm=search_term,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            filters=filters,
            isFavorite=is_favorite,
            mediaTypes=media_types,
            genres=genres,
            genreIds=genre_ids,
            officialRatings=official_ratings,
            tags=tags,
            years=years,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            person=person,
            personIds=person_ids,
            personTypes=person_types,
            studios=studios,
            studioIds=studio_ids,
            userId=user_id,
            nameStartsWithOrGreater=name_starts_with_or_greater,
            nameStartsWith=name_starts_with,
            nameLessThan=name_less_than,
            enableImages=enable_images,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/Artists', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_artist_by_name(
            self, 
            name: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets an artist by name.

        Http:
            <get>: /Artists/{name}

        Args:
            name (str): Studio name.
            user_id (str): Optional. Filter by user id, and attach user data.

        Returns:
            <200> BaseItemDto: Artist returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            userId=user_id,
        )
        return self._get(path='/Artists/{name}', request_args=request_args, response_type=BaseItemDto)

    def get_album_artists(
            self, 
            min_community_rating: Optional[float] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            search_term: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            include_item_types: Optional[List[str]] = None, 
            filters: Optional[List[ItemFilter]] = None, 
            is_favorite: Optional[bool] = None, 
            media_types: Optional[List[str]] = None, 
            genres: Optional[List[str]] = None, 
            genre_ids: Optional[List[str]] = None, 
            official_ratings: Optional[List[str]] = None, 
            tags: Optional[List[str]] = None, 
            years: Optional[List[int]] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            person: Optional[str] = None, 
            person_ids: Optional[List[str]] = None, 
            person_types: Optional[List[str]] = None, 
            studios: Optional[List[str]] = None, 
            studio_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            name_starts_with_or_greater: Optional[str] = None, 
            name_starts_with: Optional[str] = None, 
            name_less_than: Optional[str] = None, 
            enable_images: Optional[bool] = True, 
            enable_total_record_count: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets all album artists from a given item, folder, or the entire library.

        Http:
            <get>: /Artists/AlbumArtists

        Args:
            min_community_rating (float): Optional filter by minimum community rating.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            search_term (str): Optional. Search term.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            exclude_item_types (List[str]): Optional. If specified, results will be filtered out based on item type. This allows multiple, comma delimited.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply.
            is_favorite (bool): Optional filter by items that are marked as favorite, or not.
            media_types (List[str]): Optional filter by MediaType. Allows multiple, comma delimited.
            genres (List[str]): Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
            genre_ids (List[str]): Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
            official_ratings (List[str]): Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
            tags (List[str]): Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
            years (List[int]): Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
            enable_user_data (bool): Optional, include user data.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            person (str): Optional. If specified, results will be filtered to include only those containing the specified person.
            person_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified person ids.
            person_types (List[str]): Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
            studios (List[str]): Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
            studio_ids (List[str]): Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
            user_id (str): User id.
            name_starts_with_or_greater (str): Optional filter by items whose name is sorted equally or greater than a given input string.
            name_starts_with (str): Optional filter by items whose name is sorted equally than a given input string.
            name_less_than (str): Optional filter by items whose name is equally or lesser than a given input string.
            enable_images (bool = True): Optional, include image information in output.
            enable_total_record_count (bool = True): Total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Album artists returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            minCommunityRating=min_community_rating,
            startIndex=start_index,
            limit=limit,
            searchTerm=search_term,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            filters=filters,
            isFavorite=is_favorite,
            mediaTypes=media_types,
            genres=genres,
            genreIds=genre_ids,
            officialRatings=official_ratings,
            tags=tags,
            years=years,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            person=person,
            personIds=person_ids,
            personTypes=person_types,
            studios=studios,
            studioIds=studio_ids,
            userId=user_id,
            nameStartsWithOrGreater=name_starts_with_or_greater,
            nameStartsWith=name_starts_with,
            nameLessThan=name_less_than,
            enableImages=enable_images,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/Artists/AlbumArtists', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_artist_image(
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
        """Get artist image by name.

        Http:
            <get>: /Artists/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Artist name.
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
        return self._get(path='/Artists/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def head_artist_image(
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
        """Get artist image by name.

        Http:
            <head>: /Artists/{name}/Images/{imageType}/{imageIndex}

        Args:
            name (str): Artist name.
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
        return self._head(path='/Artists/{name}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def get_instant_mix_from_artists(
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
        """Creates an instant playlist based on a given artist.

        Http:
            <get>: /Artists/{id}/InstantMix

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
        return self._get(path='/Artists/{id}/InstantMix', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_similar_artists(
            self, 
            item_id: str, 
            exclude_artist_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets similar items.

        Http:
            <get>: /Artists/{itemId}/Similar

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
        return self._get(path='/Artists/{itemId}/Similar', request_args=request_args, response_type=BaseItemDtoQueryResult)

