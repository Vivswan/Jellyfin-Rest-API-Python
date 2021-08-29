from typing import List
from typing import Optional

import requests

from data_classes.album_info_remote_search_query import AlbumInfoRemoteSearchQuery as AlbumInfoRemoteSearchQuery
from data_classes.all_theme_media_result import AllThemeMediaResult as AllThemeMediaResult
from data_classes.artist_info_remote_search_query import ArtistInfoRemoteSearchQuery as ArtistInfoRemoteSearchQuery
from data_classes.base_item_dto import BaseItemDto as BaseItemDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.book_info_remote_search_query import BookInfoRemoteSearchQuery as BookInfoRemoteSearchQuery
from data_classes.box_set_info_remote_search_query import BoxSetInfoRemoteSearchQuery as BoxSetInfoRemoteSearchQuery
from data_classes.external_i_d_info import ExternalIDInfo as ExternalIdInfo
from data_classes.image_format import ImageFormat as ImageFormat
from data_classes.image_info import ImageInfo as ImageInfo
from data_classes.image_provider_info import ImageProviderInfo as ImageProviderInfo
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.item_counts import ItemCounts as ItemCounts
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.item_filter import ItemFilter as ItemFilter
from data_classes.location_type import LocationType as LocationType
from data_classes.metadata_editor_info import MetadataEditorInfo as MetadataEditorInfo
from data_classes.metadata_refresh_mode import MetadataRefreshMode as MetadataRefreshMode
from data_classes.movie_info_remote_search_query import MovieInfoRemoteSearchQuery as MovieInfoRemoteSearchQuery
from data_classes.music_video_info_remote_search_query import \
    MusicVideoInfoRemoteSearchQuery as MusicVideoInfoRemoteSearchQuery
from data_classes.person_lookup_info_remote_search_query import \
    PersonLookupInfoRemoteSearchQuery as PersonLookupInfoRemoteSearchQuery
from data_classes.playback_info_dto import PlaybackInfoDto as PlaybackInfoDto
from data_classes.playback_info_response import PlaybackInfoResponse as PlaybackInfoResponse
from data_classes.query_filters import QueryFilters as QueryFilters
from data_classes.query_filters_legacy import QueryFiltersLegacy as QueryFiltersLegacy
from data_classes.remote_image_result import RemoteImageResult as RemoteImageResult
from data_classes.remote_search_result import RemoteSearchResult as RemoteSearchResult
from data_classes.remote_subtitle_info import RemoteSubtitleInfo as RemoteSubtitleInfo
from data_classes.series_info_remote_search_query import SeriesInfoRemoteSearchQuery as SeriesInfoRemoteSearchQuery
from data_classes.series_status import SeriesStatus as SeriesStatus
from data_classes.sort_order import SortOrder as SortOrder
from data_classes.theme_media_result_class import ThemeMediaResultClass as ThemeMediaResult
from data_classes.trailer_info_remote_search_query import TrailerInfoRemoteSearchQuery as TrailerInfoRemoteSearchQuery
from data_classes.video_type import VideoType as VideoType
from util.BaseRequestClass import BaseRequestClass


class Items(BaseRequestClass):
    def get_query_filters_legacy(
            self, 
            user_id: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            include_item_types: Optional[List[str]] = None, 
            media_types: Optional[List[str]] = None
    ) -> QueryFiltersLegacy:
        """Gets legacy query filters.

        Http:
            <get>: /Items/Filters

        Args:
            user_id (str): Optional. User id.
            parent_id (str): Optional. Parent id.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            media_types (List[str]): Optional. Filter by MediaType. Allows multiple, comma delimited.

        Returns:
            <200> QueryFiltersLegacy: Legacy filters retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            parentId=parent_id,
            includeItemTypes=include_item_types,
            mediaTypes=media_types,
        )
        return self._get(path='/Items/Filters', request_args=request_args, response_type=QueryFiltersLegacy)

    def get_query_filters(
            self, 
            user_id: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            include_item_types: Optional[List[str]] = None, 
            is_airing: Optional[bool] = None, 
            is_movie: Optional[bool] = None, 
            is_sports: Optional[bool] = None, 
            is_kids: Optional[bool] = None, 
            is_news: Optional[bool] = None, 
            is_series: Optional[bool] = None, 
            recursive: Optional[bool] = None
    ) -> QueryFilters:
        """Gets query filters.

        Http:
            <get>: /Items/Filters2

        Args:
            user_id (str): Optional. User id.
            parent_id (str): Optional. Specify this to localize the search to a specific item or folder. Omit to use the root.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            is_airing (bool): Optional. Is item airing.
            is_movie (bool): Optional. Is item movie.
            is_sports (bool): Optional. Is item sports.
            is_kids (bool): Optional. Is item kids.
            is_news (bool): Optional. Is item news.
            is_series (bool): Optional. Is item series.
            recursive (bool): Optional. Search recursive.

        Returns:
            <200> QueryFilters: Filters retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            parentId=parent_id,
            includeItemTypes=include_item_types,
            isAiring=is_airing,
            isMovie=is_movie,
            isSports=is_sports,
            isKids=is_kids,
            isNews=is_news,
            isSeries=is_series,
            recursive=recursive,
        )
        return self._get(path='/Items/Filters2', request_args=request_args, response_type=QueryFilters)

    def get_item_image_infos(
            self, 
            item_id: str
    ) -> List[ImageInfo]:
        """Get item image infos.

        Http:
            <get>: /Items/{itemId}/Images

        Args:
            item_id (str): Item id.

        Returns:
            <200> List[ImageInfo]: Item images returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._get(path='/Items/{itemId}/Images', request_args=request_args, response_type=List[ImageInfo])

    def delete_item_image(
            self, 
            item_id: str, 
            image_type: ImageType, 
            image_index: Optional[int] = None
    ) -> requests.Response:
        """Delete an item's image.

        Http:
            <delete>: /Items/{itemId}/Images/{imageType}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            image_index (int): The image index.

        Returns:
            <204> requests.Response: Image deleted.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
        )
        return self._delete(path='/Items/{itemId}/Images/{imageType}', request_args=request_args)

    def set_item_image(
            self, 
            item_id: str, 
            image_type: ImageType
    ) -> requests.Response:
        """Set item image.

        Http:
            <post>: /Items/{itemId}/Images/{imageType}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.

        Returns:
            <204> requests.Response: Image saved.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
        )
        return self._post(path='/Items/{itemId}/Images/{imageType}', request_args=request_args)

    def get_item_image(
            self, 
            item_id: str, 
            image_type: ImageType, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            tag: Optional[str] = None, 
            crop_whitespace: Optional[bool] = None, 
            format: Optional[ImageFormat] = None, 
            add_played_indicator: Optional[bool] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None, 
            image_index: Optional[int] = None
    ) -> requests.Response:
        """Gets the item's image.

        Http:
            <get>: /Items/{itemId}/Images/{imageType}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            format (ImageFormat): Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
            add_played_indicator (bool): Optional. Add a played indicator.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.
            image_index (int): Image index.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            maxWidth=max_width,
            maxHeight=max_height,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            tag=tag,
            cropWhitespace=crop_whitespace,
            format=format,
            addPlayedIndicator=add_played_indicator,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
            imageIndex=image_index,
        )
        return self._get(path='/Items/{itemId}/Images/{imageType}', request_args=request_args)

    def head_item_image(
            self, 
            item_id: str, 
            image_type: ImageType, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            tag: Optional[str] = None, 
            crop_whitespace: Optional[bool] = None, 
            format: Optional[ImageFormat] = None, 
            add_played_indicator: Optional[bool] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None, 
            image_index: Optional[int] = None
    ) -> requests.Response:
        """Gets the item's image.

        Http:
            <head>: /Items/{itemId}/Images/{imageType}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            format (ImageFormat): Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
            add_played_indicator (bool): Optional. Add a played indicator.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.
            image_index (int): Image index.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            maxWidth=max_width,
            maxHeight=max_height,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            tag=tag,
            cropWhitespace=crop_whitespace,
            format=format,
            addPlayedIndicator=add_played_indicator,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
            imageIndex=image_index,
        )
        return self._head(path='/Items/{itemId}/Images/{imageType}', request_args=request_args)

    def delete_item_image_by_index(
            self, 
            item_id: str, 
            image_type: ImageType, 
            image_index: int
    ) -> requests.Response:
        """Delete an item's image.

        Http:
            <delete>: /Items/{itemId}/Images/{imageType}/{imageIndex}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            image_index (int): The image index.

        Returns:
            <204> requests.Response: Image deleted.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
        )
        return self._delete(path='/Items/{itemId}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def set_item_image_by_index(
            self, 
            item_id: str, 
            image_type: ImageType, 
            image_index: int
    ) -> requests.Response:
        """Set item image.

        Http:
            <post>: /Items/{itemId}/Images/{imageType}/{imageIndex}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            image_index (int): (Unused) Image index.

        Returns:
            <204> requests.Response: Image saved.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
        )
        return self._post(path='/Items/{itemId}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def get_item_image_by_index(
            self, 
            item_id: str, 
            image_type: ImageType, 
            image_index: int, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            tag: Optional[str] = None, 
            crop_whitespace: Optional[bool] = None, 
            format: Optional[ImageFormat] = None, 
            add_played_indicator: Optional[bool] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None
    ) -> requests.Response:
        """Gets the item's image.

        Http:
            <get>: /Items/{itemId}/Images/{imageType}/{imageIndex}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            image_index (int): Image index.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            format (ImageFormat): Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
            add_played_indicator (bool): Optional. Add a played indicator.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
            maxWidth=max_width,
            maxHeight=max_height,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            tag=tag,
            cropWhitespace=crop_whitespace,
            format=format,
            addPlayedIndicator=add_played_indicator,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
        )
        return self._get(path='/Items/{itemId}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def head_item_image_by_index(
            self, 
            item_id: str, 
            image_type: ImageType, 
            image_index: int, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            quality: Optional[int] = None, 
            fill_width: Optional[int] = None, 
            fill_height: Optional[int] = None, 
            tag: Optional[str] = None, 
            crop_whitespace: Optional[bool] = None, 
            format: Optional[ImageFormat] = None, 
            add_played_indicator: Optional[bool] = None, 
            percent_played: Optional[float] = None, 
            unplayed_count: Optional[int] = None, 
            blur: Optional[int] = None, 
            background_color: Optional[str] = None, 
            foreground_layer: Optional[str] = None
    ) -> requests.Response:
        """Gets the item's image.

        Http:
            <head>: /Items/{itemId}/Images/{imageType}/{imageIndex}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            image_index (int): Image index.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            width (int): The fixed image width to return.
            height (int): The fixed image height to return.
            quality (int): Optional. Quality setting, from 0-100. Defaults to 90 and should suffice in most cases.
            fill_width (int): Width of box to fill.
            fill_height (int): Height of box to fill.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            crop_whitespace (bool): Optional. Specify if whitespace should be cropped out of the image. True/False. If unspecified, whitespace will be cropped from logos and clear art.
            format (ImageFormat): Optional. The MediaBrowser.Model.Drawing.ImageFormat of the returned image.
            add_played_indicator (bool): Optional. Add a played indicator.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            blur (int): Optional. Blur image.
            background_color (str): Optional. Apply a background color for transparent images.
            foreground_layer (str): Optional. Apply a foreground layer on top of the image.

        Returns:
            <200> requests.Response: Image stream returned.
            <404> requests.Response: Item not found.
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
            maxWidth=max_width,
            maxHeight=max_height,
            width=width,
            height=height,
            quality=quality,
            fillWidth=fill_width,
            fillHeight=fill_height,
            tag=tag,
            cropWhitespace=crop_whitespace,
            format=format,
            addPlayedIndicator=add_played_indicator,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            blur=blur,
            backgroundColor=background_color,
            foregroundLayer=foreground_layer,
        )
        return self._head(path='/Items/{itemId}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def get_item_image2(
            self, 
            item_id: str, 
            image_type: ImageType, 
            max_width: int, 
            max_height: int, 
            tag: str, 
            format: ImageFormat, 
            percent_played: float, 
            unplayed_count: int, 
            image_index: int, 
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
        """Gets the item's image.

        Http:
            <get>: /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            format (ImageFormat): Determines the output format of the image - original,gif,jpg,png.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            image_index (int): Image index.
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
            itemId=item_id,
            imageType=image_type,
            maxWidth=max_width,
            maxHeight=max_height,
            tag=tag,
            format=format,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            imageIndex=image_index,
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
        return self._get(path='/Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}', request_args=request_args)

    def head_item_image2(
            self, 
            item_id: str, 
            image_type: ImageType, 
            max_width: int, 
            max_height: int, 
            tag: str, 
            format: ImageFormat, 
            percent_played: float, 
            unplayed_count: int, 
            image_index: int, 
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
        """Gets the item's image.

        Http:
            <head>: /Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            max_width (int): The maximum image width to return.
            max_height (int): The maximum image height to return.
            tag (str): Optional. Supply the cache tag from the item object to receive strong caching headers.
            format (ImageFormat): Determines the output format of the image - original,gif,jpg,png.
            percent_played (float): Optional. Percent to render for the percent played overlay.
            unplayed_count (int): Optional. Unplayed count overlay to render.
            image_index (int): Image index.
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
            itemId=item_id,
            imageType=image_type,
            maxWidth=max_width,
            maxHeight=max_height,
            tag=tag,
            format=format,
            percentPlayed=percent_played,
            unplayedCount=unplayed_count,
            imageIndex=image_index,
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
        return self._head(path='/Items/{itemId}/Images/{imageType}/{imageIndex}/{tag}/{format}/{maxWidth}/{maxHeight}/{percentPlayed}/{unplayedCount}', request_args=request_args)

    def update_item_image_index(
            self, 
            item_id: str, 
            image_type: ImageType, 
            image_index: int, 
            new_index: int
    ) -> requests.Response:
        """Updates the index for an item image.

        Http:
            <post>: /Items/{itemId}/Images/{imageType}/{imageIndex}/Index

        Args:
            item_id (str): Item id.
            image_type (ImageType): Image type.
            image_index (int): Old image index.
            new_index (int): New image index.

        Returns:
            <204> requests.Response: Image index updated.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            imageType=image_type,
            imageIndex=image_index,
            newIndex=new_index,
        )
        return self._post(path='/Items/{itemId}/Images/{imageType}/{imageIndex}/Index', request_args=request_args)

    def get_instant_mix_from_item(
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
        """Creates an instant playlist based on a given item.

        Http:
            <get>: /Items/{id}/InstantMix

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
        return self._get(path='/Items/{id}/InstantMix', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_external_id_infos(
            self, 
            item_id: str
    ) -> List[ExternalIdInfo]:
        """Get the item's external id info.

        Http:
            <get>: /Items/{itemId}/ExternalIdInfos

        Args:
            item_id (str): Item id.

        Returns:
            <200> List[ExternalIdInfo]: External id info retrieved.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._get(path='/Items/{itemId}/ExternalIdInfos', request_args=request_args, response_type=List[ExternalIdInfo])

    def apply_search_criteria(
            self, 
            item_id: str, 
            request_body: RemoteSearchResult, 
            replace_all_images: Optional[bool] = True
    ) -> requests.Response:
        """Applies search criteria to an item and refreshes metadata.

        Http:
            <post>: /Items/RemoteSearch/Apply/{itemId}

        Args:
            item_id (str): Item id.
            request_body (RemoteSearchResult): The remote search result.
            replace_all_images (bool = True): Optional. Whether or not to replace all images. Default: True.

        Returns:
            <204> requests.Response: Item metadata refreshed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            requestBody=request_body,
            replaceAllImages=replace_all_images,
        )
        return self._post(path='/Items/RemoteSearch/Apply/{itemId}', request_args=request_args)

    def get_book_remote_search_results(
            self, 
            request_body: BookInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get book remote search.

        Http:
            <post>: /Items/RemoteSearch/Book

        Args:
            request_body (BookInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Book remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/Book', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_box_set_remote_search_results(
            self, 
            request_body: BoxSetInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get box set remote search.

        Http:
            <post>: /Items/RemoteSearch/BoxSet

        Args:
            request_body (BoxSetInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Box set remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/BoxSet', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_movie_remote_search_results(
            self, 
            request_body: MovieInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get movie remote search.

        Http:
            <post>: /Items/RemoteSearch/Movie

        Args:
            request_body (MovieInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Movie remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/Movie', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_music_album_remote_search_results(
            self, 
            request_body: AlbumInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get music album remote search.

        Http:
            <post>: /Items/RemoteSearch/MusicAlbum

        Args:
            request_body (AlbumInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Music album remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/MusicAlbum', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_music_artist_remote_search_results(
            self, 
            request_body: ArtistInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get music artist remote search.

        Http:
            <post>: /Items/RemoteSearch/MusicArtist

        Args:
            request_body (ArtistInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Music artist remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/MusicArtist', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_music_video_remote_search_results(
            self, 
            request_body: MusicVideoInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get music video remote search.

        Http:
            <post>: /Items/RemoteSearch/MusicVideo

        Args:
            request_body (MusicVideoInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Music video remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/MusicVideo', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_person_remote_search_results(
            self, 
            request_body: PersonLookupInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get person remote search.

        Http:
            <post>: /Items/RemoteSearch/Person

        Args:
            request_body (PersonLookupInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Person remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/Person', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_series_remote_search_results(
            self, 
            request_body: SeriesInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get series remote search.

        Http:
            <post>: /Items/RemoteSearch/Series

        Args:
            request_body (SeriesInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Series remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/Series', request_args=request_args, response_type=List[RemoteSearchResult])

    def get_trailer_remote_search_results(
            self, 
            request_body: TrailerInfoRemoteSearchQuery
    ) -> List[RemoteSearchResult]:
        """Get trailer remote search.

        Http:
            <post>: /Items/RemoteSearch/Trailer

        Args:
            request_body (TrailerInfoRemoteSearchQuery): Remote search query.

        Returns:
            <200> List[RemoteSearchResult]: Trailer remote search executed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Items/RemoteSearch/Trailer', request_args=request_args, response_type=List[RemoteSearchResult])

    def post_refresh(
            self, 
            item_id: str, 
            metadata_refresh_mode: Optional[MetadataRefreshMode] = None, 
            image_refresh_mode: Optional[MetadataRefreshMode] = None, 
            replace_all_metadata: Optional[bool] = False, 
            replace_all_images: Optional[bool] = False
    ) -> requests.Response:
        """Refreshes metadata for an item.

        Http:
            <post>: /Items/{itemId}/Refresh

        Args:
            item_id (str): Item id.
            metadata_refresh_mode (MetadataRefreshMode): (Optional) Specifies the metadata refresh mode.
            image_refresh_mode (MetadataRefreshMode): (Optional) Specifies the image refresh mode.
            replace_all_metadata (bool = False): (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.
            replace_all_images (bool = False): (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.

        Returns:
            <204> requests.Response: Item metadata refresh queued.
            <404> requests.Response: Item to refresh not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            metadataRefreshMode=metadata_refresh_mode,
            imageRefreshMode=image_refresh_mode,
            replaceAllMetadata=replace_all_metadata,
            replaceAllImages=replace_all_images,
        )
        return self._post(path='/Items/{itemId}/Refresh', request_args=request_args)

    def get_items(
            self, 
            user_id: Optional[str] = None, 
            max_official_rating: Optional[str] = None, 
            has_theme_song: Optional[bool] = None, 
            has_theme_video: Optional[bool] = None, 
            has_subtitles: Optional[bool] = None, 
            has_special_feature: Optional[bool] = None, 
            has_trailer: Optional[bool] = None, 
            adjacent_to: Optional[str] = None, 
            parent_index_number: Optional[int] = None, 
            has_parental_rating: Optional[bool] = None, 
            is_hd: Optional[bool] = None, 
            is4_k: Optional[bool] = None, 
            location_types: Optional[List[LocationType]] = None, 
            exclude_location_types: Optional[List[LocationType]] = None, 
            is_missing: Optional[bool] = None, 
            is_unaired: Optional[bool] = None, 
            min_community_rating: Optional[float] = None, 
            min_critic_rating: Optional[float] = None, 
            min_premiere_date: Optional[str] = None, 
            min_date_last_saved: Optional[str] = None, 
            min_date_last_saved_for_user: Optional[str] = None, 
            max_premiere_date: Optional[str] = None, 
            has_overview: Optional[bool] = None, 
            has_imdb_id: Optional[bool] = None, 
            has_tmdb_id: Optional[bool] = None, 
            has_tvdb_id: Optional[bool] = None, 
            exclude_item_ids: Optional[List[str]] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            recursive: Optional[bool] = None, 
            search_term: Optional[str] = None, 
            sort_order: Optional[List[SortOrder]] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            include_item_types: Optional[List[str]] = None, 
            filters: Optional[List[ItemFilter]] = None, 
            is_favorite: Optional[bool] = None, 
            media_types: Optional[List[str]] = None, 
            image_types: Optional[List[ImageType]] = None, 
            sort_by: Optional[List[str]] = None, 
            is_played: Optional[bool] = None, 
            genres: Optional[List[str]] = None, 
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
            artists: Optional[List[str]] = None, 
            exclude_artist_ids: Optional[List[str]] = None, 
            artist_ids: Optional[List[str]] = None, 
            album_artist_ids: Optional[List[str]] = None, 
            contributing_artist_ids: Optional[List[str]] = None, 
            albums: Optional[List[str]] = None, 
            album_ids: Optional[List[str]] = None, 
            ids: Optional[List[str]] = None, 
            video_types: Optional[List[VideoType]] = None, 
            min_official_rating: Optional[str] = None, 
            is_locked: Optional[bool] = None, 
            is_place_holder: Optional[bool] = None, 
            has_official_rating: Optional[bool] = None, 
            collapse_box_set_items: Optional[bool] = None, 
            min_width: Optional[int] = None, 
            min_height: Optional[int] = None, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            is3_d: Optional[bool] = None, 
            series_status: Optional[List[SeriesStatus]] = None, 
            name_starts_with_or_greater: Optional[str] = None, 
            name_starts_with: Optional[str] = None, 
            name_less_than: Optional[str] = None, 
            studio_ids: Optional[List[str]] = None, 
            genre_ids: Optional[List[str]] = None, 
            enable_total_record_count: Optional[bool] = True, 
            enable_images: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets items based on a query.

        Http:
            <get>: /Items

        Args:
            user_id (str): The user id supplied as query parameter.
            max_official_rating (str): Optional filter by maximum official rating (PG, PG-13, TV-MA, etc).
            has_theme_song (bool): Optional filter by items with theme songs.
            has_theme_video (bool): Optional filter by items with theme videos.
            has_subtitles (bool): Optional filter by items with subtitles.
            has_special_feature (bool): Optional filter by items with special features.
            has_trailer (bool): Optional filter by items with trailers.
            adjacent_to (str): Optional. Return items that are siblings of a supplied item.
            parent_index_number (int): Optional filter by parent index number.
            has_parental_rating (bool): Optional filter by items that have or do not have a parental rating.
            is_hd (bool): Optional filter by items that are HD or not.
            is4_k (bool): Optional filter by items that are 4K or not.
            location_types (List[LocationType]): Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimited.
            exclude_location_types (List[LocationType]): Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimited.
            is_missing (bool): Optional filter by items that are missing episodes or not.
            is_unaired (bool): Optional filter by items that are unaired episodes or not.
            min_community_rating (float): Optional filter by minimum community rating.
            min_critic_rating (float): Optional filter by minimum critic rating.
            min_premiere_date (str): Optional. The minimum premiere date. Format = ISO.
            min_date_last_saved (str): Optional. The minimum last saved date. Format = ISO.
            min_date_last_saved_for_user (str): Optional. The minimum last saved date for the current user. Format = ISO.
            max_premiere_date (str): Optional. The maximum premiere date. Format = ISO.
            has_overview (bool): Optional filter by items that have an overview or not.
            has_imdb_id (bool): Optional filter by items that have an imdb id or not.
            has_tmdb_id (bool): Optional filter by items that have a tmdb id or not.
            has_tvdb_id (bool): Optional filter by items that have a tvdb id or not.
            exclude_item_ids (List[str]): Optional. If specified, results will be filtered by excluding item ids. This allows multiple, comma delimited.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            recursive (bool): When searching within folders, this determines whether or not the search will be recursive. true/false.
            search_term (str): Optional. Filter based on a search term.
            sort_order (List[SortOrder]): Sort Order - Ascending,Descending.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
            exclude_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply. This allows multiple, comma delimited. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
            is_favorite (bool): Optional filter by items that are marked as favorite, or not.
            media_types (List[str]): Optional filter by MediaType. Allows multiple, comma delimited.
            image_types (List[ImageType]): Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.
            sort_by (List[str]): Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
            is_played (bool): Optional filter by items that are played, or not.
            genres (List[str]): Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimited.
            official_ratings (List[str]): Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimited.
            tags (List[str]): Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimited.
            years (List[int]): Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimited.
            enable_user_data (bool): Optional, include user data.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            person (str): Optional. If specified, results will be filtered to include only those containing the specified person.
            person_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified person id.
            person_types (List[str]): Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
            studios (List[str]): Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimited.
            artists (List[str]): Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimited.
            exclude_artist_ids (List[str]): Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimited.
            artist_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified artist id.
            album_artist_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified album artist id.
            contributing_artist_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified contributing artist id.
            albums (List[str]): Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimited.
            album_ids (List[str]): Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimited.
            ids (List[str]): Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited.
            video_types (List[VideoType]): Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimited.
            min_official_rating (str): Optional filter by minimum official rating (PG, PG-13, TV-MA, etc).
            is_locked (bool): Optional filter by items that are locked.
            is_place_holder (bool): Optional filter by items that are placeholders.
            has_official_rating (bool): Optional filter by items that have official ratings.
            collapse_box_set_items (bool): Whether or not to hide items behind their boxsets.
            min_width (int): Optional. Filter by the minimum width of the item.
            min_height (int): Optional. Filter by the minimum height of the item.
            max_width (int): Optional. Filter by the maximum width of the item.
            max_height (int): Optional. Filter by the maximum height of the item.
            is3_d (bool): Optional filter by items that are 3D, or not.
            series_status (List[SeriesStatus]): Optional filter by Series Status. Allows multiple, comma delimited.
            name_starts_with_or_greater (str): Optional filter by items whose name is sorted equally or greater than a given input string.
            name_starts_with (str): Optional filter by items whose name is sorted equally than a given input string.
            name_less_than (str): Optional filter by items whose name is equally or lesser than a given input string.
            studio_ids (List[str]): Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimited.
            genre_ids (List[str]): Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimited.
            enable_total_record_count (bool = True): Optional. Enable the total record count.
            enable_images (bool = True): Optional, include image information in output.

        Returns:
            <200> BaseItemDtoQueryResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            maxOfficialRating=max_official_rating,
            hasThemeSong=has_theme_song,
            hasThemeVideo=has_theme_video,
            hasSubtitles=has_subtitles,
            hasSpecialFeature=has_special_feature,
            hasTrailer=has_trailer,
            adjacentTo=adjacent_to,
            parentIndexNumber=parent_index_number,
            hasParentalRating=has_parental_rating,
            isHd=is_hd,
            is4K=is4_k,
            locationTypes=location_types,
            excludeLocationTypes=exclude_location_types,
            isMissing=is_missing,
            isUnaired=is_unaired,
            minCommunityRating=min_community_rating,
            minCriticRating=min_critic_rating,
            minPremiereDate=min_premiere_date,
            minDateLastSaved=min_date_last_saved,
            minDateLastSavedForUser=min_date_last_saved_for_user,
            maxPremiereDate=max_premiere_date,
            hasOverview=has_overview,
            hasImdbId=has_imdb_id,
            hasTmdbId=has_tmdb_id,
            hasTvdbId=has_tvdb_id,
            excludeItemIds=exclude_item_ids,
            startIndex=start_index,
            limit=limit,
            recursive=recursive,
            searchTerm=search_term,
            sortOrder=sort_order,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            filters=filters,
            isFavorite=is_favorite,
            mediaTypes=media_types,
            imageTypes=image_types,
            sortBy=sort_by,
            isPlayed=is_played,
            genres=genres,
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
            artists=artists,
            excludeArtistIds=exclude_artist_ids,
            artistIds=artist_ids,
            albumArtistIds=album_artist_ids,
            contributingArtistIds=contributing_artist_ids,
            albums=albums,
            albumIds=album_ids,
            ids=ids,
            videoTypes=video_types,
            minOfficialRating=min_official_rating,
            isLocked=is_locked,
            isPlaceHolder=is_place_holder,
            hasOfficialRating=has_official_rating,
            collapseBoxSetItems=collapse_box_set_items,
            minWidth=min_width,
            minHeight=min_height,
            maxWidth=max_width,
            maxHeight=max_height,
            is3D=is3_d,
            seriesStatus=series_status,
            nameStartsWithOrGreater=name_starts_with_or_greater,
            nameStartsWith=name_starts_with,
            nameLessThan=name_less_than,
            studioIds=studio_ids,
            genreIds=genre_ids,
            enableTotalRecordCount=enable_total_record_count,
            enableImages=enable_images,
        )
        return self._get(path='/Items', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def delete_items(
            self, 
            ids: Optional[List[str]] = None
    ) -> requests.Response:
        """Deletes items from the library and filesystem.

        Http:
            <delete>: /Items

        Args:
            ids (List[str]): The item ids.

        Returns:
            <204> requests.Response: Items deleted.
            <401> requests.Response: Unauthorized access.
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            ids=ids,
        )
        return self._delete(path='/Items', request_args=request_args)

    def update_item(
            self, 
            item_id: str, 
            request_body: BaseItemDto
    ) -> requests.Response:
        """Updates an item.

        Http:
            <post>: /Items/{itemId}

        Args:
            item_id (str): The item id.
            request_body (BaseItemDto): The new item properties.

        Returns:
            <204> requests.Response: Item updated.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """

        request_args = dict(
            itemId=item_id,
            requestBody=request_body,
        )
        return self._post(path='/Items/{itemId}', request_args=request_args)

    def delete_item(
            self, 
            item_id: str
    ) -> requests.Response:
        """Deletes an item from the library and filesystem.

        Http:
            <delete>: /Items/{itemId}

        Args:
            item_id (str): The item id.

        Returns:
            <204> requests.Response: Item deleted.
            <401> requests.Response: Unauthorized access.
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._delete(path='/Items/{itemId}', request_args=request_args)

    def update_item_content_type(
            self, 
            item_id: str, 
            content_type: Optional[str] = None
    ) -> requests.Response:
        """Updates an item's content type.

        Http:
            <post>: /Items/{itemId}/ContentType

        Args:
            item_id (str): The item id.
            content_type (str): The content type of the item.

        Returns:
            <204> requests.Response: Item content type updated.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            contentType=content_type,
        )
        return self._post(path='/Items/{itemId}/ContentType', request_args=request_args)

    def get_metadata_editor_info(
            self, 
            item_id: str
    ) -> MetadataEditorInfo:
        """Gets metadata editor info for an item.

        Http:
            <get>: /Items/{itemId}/MetadataEditor

        Args:
            item_id (str): The item id.

        Returns:
            <200> MetadataEditorInfo: Item metadata editor returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._get(path='/Items/{itemId}/MetadataEditor', request_args=request_args, response_type=MetadataEditorInfo)

    def get_ancestors(
            self, 
            item_id: str, 
            user_id: Optional[str] = None
    ) -> List[BaseItemDto]:
        """Gets all parents of an item.

        Http:
            <get>: /Items/{itemId}/Ancestors

        Args:
            item_id (str): The item id.
            user_id (str): Optional. Filter by user id, and attach user data.

        Returns:
            <200> List[BaseItemDto]: Item parents returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
        )
        return self._get(path='/Items/{itemId}/Ancestors', request_args=request_args, response_type=List[BaseItemDto])

    def get_download(
            self, 
            item_id: str
    ) -> requests.Response:
        """Downloads item media.

        Http:
            <get>: /Items/{itemId}/Download

        Args:
            item_id (str): The item id.

        Returns:
            <200> requests.Response: Media downloaded.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._get(path='/Items/{itemId}/Download', request_args=request_args)

    def get_file(
            self, 
            item_id: str
    ) -> requests.Response:
        """Get the original file of an item.

        Http:
            <get>: /Items/{itemId}/File

        Args:
            item_id (str): The item id.

        Returns:
            <200> requests.Response: File stream returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._get(path='/Items/{itemId}/File', request_args=request_args)

    def get_similar_items(
            self, 
            item_id: str, 
            exclude_artist_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets similar items.

        Http:
            <get>: /Items/{itemId}/Similar

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
        return self._get(path='/Items/{itemId}/Similar', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_theme_media(
            self, 
            item_id: str, 
            user_id: Optional[str] = None, 
            inherit_from_parent: Optional[bool] = False
    ) -> AllThemeMediaResult:
        """Get theme songs and videos for an item.

        Http:
            <get>: /Items/{itemId}/ThemeMedia

        Args:
            item_id (str): The item id.
            user_id (str): Optional. Filter by user id, and attach user data.
            inherit_from_parent (bool = False): Optional. Determines whether or not parent items should be searched for theme media.

        Returns:
            <200> AllThemeMediaResult: Theme songs and videos returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
            inheritFromParent=inherit_from_parent,
        )
        return self._get(path='/Items/{itemId}/ThemeMedia', request_args=request_args, response_type=AllThemeMediaResult)

    def get_theme_songs(
            self, 
            item_id: str, 
            user_id: Optional[str] = None, 
            inherit_from_parent: Optional[bool] = False
    ) -> ThemeMediaResult:
        """Get theme songs for an item.

        Http:
            <get>: /Items/{itemId}/ThemeSongs

        Args:
            item_id (str): The item id.
            user_id (str): Optional. Filter by user id, and attach user data.
            inherit_from_parent (bool = False): Optional. Determines whether or not parent items should be searched for theme media.

        Returns:
            <200> ThemeMediaResult: Theme songs returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
            inheritFromParent=inherit_from_parent,
        )
        return self._get(path='/Items/{itemId}/ThemeSongs', request_args=request_args, response_type=ThemeMediaResult)

    def get_theme_videos(
            self, 
            item_id: str, 
            user_id: Optional[str] = None, 
            inherit_from_parent: Optional[bool] = False
    ) -> ThemeMediaResult:
        """Get theme videos for an item.

        Http:
            <get>: /Items/{itemId}/ThemeVideos

        Args:
            item_id (str): The item id.
            user_id (str): Optional. Filter by user id, and attach user data.
            inherit_from_parent (bool = False): Optional. Determines whether or not parent items should be searched for theme media.

        Returns:
            <200> ThemeMediaResult: Theme videos returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
            inheritFromParent=inherit_from_parent,
        )
        return self._get(path='/Items/{itemId}/ThemeVideos', request_args=request_args, response_type=ThemeMediaResult)

    def get_item_counts(
            self, 
            user_id: Optional[str] = None, 
            is_favorite: Optional[bool] = None
    ) -> ItemCounts:
        """Get item counts.

        Http:
            <get>: /Items/Counts

        Args:
            user_id (str): Optional. Get counts from a specific user's library.
            is_favorite (bool): Optional. Get counts of favorite items.

        Returns:
            <200> ItemCounts: Item counts returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            isFavorite=is_favorite,
        )
        return self._get(path='/Items/Counts', request_args=request_args, response_type=ItemCounts)

    def get_playback_info(
            self, 
            item_id: str, 
            user_id: str
    ) -> PlaybackInfoResponse:
        """Gets live playback media info for an item.

        Http:
            <get>: /Items/{itemId}/PlaybackInfo

        Args:
            item_id (str): The item id.
            user_id (str): The user id.

        Returns:
            <200> PlaybackInfoResponse: Playback info returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
        )
        return self._get(path='/Items/{itemId}/PlaybackInfo', request_args=request_args, response_type=PlaybackInfoResponse)

    def get_posted_playback_info(
            self, 
            item_id: str, 
            user_id: Optional[str] = None, 
            max_streaming_bitrate: Optional[int] = None, 
            start_time_ticks: Optional[int] = None, 
            audio_stream_index: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            live_stream_id: Optional[str] = None, 
            auto_open_live_stream: Optional[bool] = None, 
            enable_direct_play: Optional[bool] = None, 
            enable_direct_stream: Optional[bool] = None, 
            enable_transcoding: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            request_body: Optional[PlaybackInfoDto] = None
    ) -> PlaybackInfoResponse:
        """Gets live playback media info for an item.

        Http:
            <post>: /Items/{itemId}/PlaybackInfo

        Args:
            item_id (str): The item id.
            user_id (str): The user id.
            max_streaming_bitrate (int): The maximum streaming bitrate.
            start_time_ticks (int): The start time in ticks.
            audio_stream_index (int): The audio stream index.
            subtitle_stream_index (int): The subtitle stream index.
            max_audio_channels (int): The maximum number of audio channels.
            media_source_id (str): The media source id.
            live_stream_id (str): The livestream id.
            auto_open_live_stream (bool): Whether to auto open the livestream.
            enable_direct_play (bool): Whether to enable direct play. Default: true.
            enable_direct_stream (bool): Whether to enable direct stream. Default: true.
            enable_transcoding (bool): Whether to enable transcoding. Default: true.
            allow_video_stream_copy (bool): Whether to allow to copy the video stream. Default: true.
            allow_audio_stream_copy (bool): Whether to allow to copy the audio stream. Default: true.
            request_body (PlaybackInfoDto): The playback info.

        Returns:
            <200> PlaybackInfoResponse: Playback info returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
            maxStreamingBitrate=max_streaming_bitrate,
            startTimeTicks=start_time_ticks,
            audioStreamIndex=audio_stream_index,
            subtitleStreamIndex=subtitle_stream_index,
            maxAudioChannels=max_audio_channels,
            mediaSourceId=media_source_id,
            liveStreamId=live_stream_id,
            autoOpenLiveStream=auto_open_live_stream,
            enableDirectPlay=enable_direct_play,
            enableDirectStream=enable_direct_stream,
            enableTranscoding=enable_transcoding,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            requestBody=request_body,
        )
        return self._post(path='/Items/{itemId}/PlaybackInfo', request_args=request_args, response_type=PlaybackInfoResponse)

    def get_remote_images(
            self, 
            item_id: str, 
            type: Optional[ImageType] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            provider_name: Optional[str] = None, 
            include_all_languages: Optional[bool] = False
    ) -> RemoteImageResult:
        """Gets available remote images for an item.

        Http:
            <get>: /Items/{itemId}/RemoteImages

        Args:
            item_id (str): Item Id.
            type (ImageType): The image type.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            provider_name (str): Optional. The image provider to use.
            include_all_languages (bool = False): Optional. Include all languages.

        Returns:
            <200> RemoteImageResult: Remote Images returned.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            type=type,
            startIndex=start_index,
            limit=limit,
            providerName=provider_name,
            includeAllLanguages=include_all_languages,
        )
        return self._get(path='/Items/{itemId}/RemoteImages', request_args=request_args, response_type=RemoteImageResult)

    def download_remote_image(
            self, 
            item_id: str, 
            type: ImageType, 
            image_url: Optional[str] = None
    ) -> requests.Response:
        """Downloads a remote image for an item.

        Http:
            <post>: /Items/{itemId}/RemoteImages/Download

        Args:
            item_id (str): Item Id.
            type (ImageType): The image type.
            image_url (str): The image url.

        Returns:
            <204> requests.Response: Remote image downloaded.
            <404> requests.Response: Remote image not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            type=type,
            imageUrl=image_url,
        )
        return self._post(path='/Items/{itemId}/RemoteImages/Download', request_args=request_args)

    def get_remote_image_providers(
            self, 
            item_id: str
    ) -> List[ImageProviderInfo]:
        """Gets available remote image providers for an item.

        Http:
            <get>: /Items/{itemId}/RemoteImages/Providers

        Args:
            item_id (str): Item Id.

        Returns:
            <200> List[ImageProviderInfo]: Returned remote image providers.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._get(path='/Items/{itemId}/RemoteImages/Providers', request_args=request_args, response_type=List[ImageProviderInfo])

    def search_remote_subtitles(
            self, 
            item_id: str, 
            language: str, 
            is_perfect_match: Optional[bool] = None
    ) -> List[RemoteSubtitleInfo]:
        """Search remote subtitles.

        Http:
            <get>: /Items/{itemId}/RemoteSearch/Subtitles/{language}

        Args:
            item_id (str): The item id.
            language (str): The language of the subtitles.
            is_perfect_match (bool): Optional. Only show subtitles which are a perfect match.

        Returns:
            <200> List[RemoteSubtitleInfo]: Subtitles retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            language=language,
            isPerfectMatch=is_perfect_match,
        )
        return self._get(path='/Items/{itemId}/RemoteSearch/Subtitles/{language}', request_args=request_args, response_type=List[RemoteSubtitleInfo])

    def download_remote_subtitles(
            self, 
            item_id: str, 
            subtitle_id: str
    ) -> requests.Response:
        """Downloads a remote subtitle.

        Http:
            <post>: /Items/{itemId}/RemoteSearch/Subtitles/{subtitleId}

        Args:
            item_id (str): The item id.
            subtitle_id (str): The subtitle id.

        Returns:
            <204> requests.Response: Subtitle downloaded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            subtitleId=subtitle_id,
        )
        return self._post(path='/Items/{itemId}/RemoteSearch/Subtitles/{subtitleId}', request_args=request_args)

