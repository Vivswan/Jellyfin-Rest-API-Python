import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.video_type import VideoType as VideoType
from data_classes.policy import Policy as UserPolicy
from data_classes.user import User as UserItemDataDto
from data_classes.user_dto_class import UserDtoClass as UserDto
from data_classes.configuration import Configuration as UserConfiguration
from data_classes.update_user_password import UpdateUserPassword as UpdateUserPassword
from data_classes.update_user_easy_password import UpdateUserEasyPassword as UpdateUserEasyPassword
from data_classes.special_view_option_dto import SpecialViewOptionDto as SpecialViewOptionDto
from data_classes.sort_order import SortOrder as SortOrder
from data_classes.series_status import SeriesStatus as SeriesStatus
from data_classes.group_repeat_mode_enum import GroupRepeatModeEnum as RepeatMode
from data_classes.quick_connect_dto import QuickConnectDto as QuickConnectDto
from data_classes.play_method import PlayMethod as PlayMethod
from data_classes.pin_redeem_result import PinRedeemResult as PinRedeemResult
from data_classes.location_type import LocationType as LocationType
from data_classes.item_filter import ItemFilter as ItemFilter
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.image_format import ImageFormat as ImageFormat
from data_classes.forgot_password_result import ForgotPasswordResult as ForgotPasswordResult
from data_classes.forgot_password_pin_dto import ForgotPasswordPinDto as ForgotPasswordPinDto
from data_classes.forgot_password_dto import ForgotPasswordDto as ForgotPasswordDto
from data_classes.create_user_by_name import CreateUserByName as CreateUserByName
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.base_item_dto import BaseItemDto as BaseItemDto
from data_classes.authentication_result import AuthenticationResult as AuthenticationResult
from data_classes.authenticate_user_by_name import AuthenticateUserByName as AuthenticateUserByName


class Users(BaseRequestClass):
    def post_user_image(
            self, 
            user_id: str, 
            image_type: ImageType, 
            index: Optional[int] = None
    ) -> requests.Response:
        """Sets the user image.

        Http:
            <post>: /Users/{userId}/Images/{imageType}

        Args:
            user_id (str): User Id.
            image_type (ImageType): (Unused) Image type.
            index (int): (Unused) Image index.

        Returns:
            <204> requests.Response: Image updated.
            <403> requests.Response: User does not have permission to delete the image.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            imageType=image_type,
            index=index,
        )
        return self._post(path='/Users/{userId}/Images/{imageType}', request_args=request_args)

    def delete_user_image(
            self, 
            user_id: str, 
            image_type: ImageType, 
            index: Optional[int] = None
    ) -> requests.Response:
        """Delete the user's image.

        Http:
            <delete>: /Users/{userId}/Images/{imageType}

        Args:
            user_id (str): User Id.
            image_type (ImageType): (Unused) Image type.
            index (int): (Unused) Image index.

        Returns:
            <204> requests.Response: Image deleted.
            <403> requests.Response: User does not have permission to delete the image.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            imageType=image_type,
            index=index,
        )
        return self._delete(path='/Users/{userId}/Images/{imageType}', request_args=request_args)

    def get_user_image(
            self, 
            user_id: str, 
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
        """Get user profile image.

        Http:
            <get>: /Users/{userId}/Images/{imageType}

        Args:
            user_id (str): User id.
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
            userId=user_id,
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
        return self._get(path='/Users/{userId}/Images/{imageType}', request_args=request_args)

    def head_user_image(
            self, 
            user_id: str, 
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
        """Get user profile image.

        Http:
            <head>: /Users/{userId}/Images/{imageType}

        Args:
            user_id (str): User id.
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
            userId=user_id,
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
        return self._head(path='/Users/{userId}/Images/{imageType}', request_args=request_args)

    def get_user_image_by_index(
            self, 
            user_id: str, 
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
        """Get user profile image.

        Http:
            <get>: /Users/{userId}/Images/{imageType}/{imageIndex}

        Args:
            user_id (str): User id.
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
            userId=user_id,
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
        return self._get(path='/Users/{userId}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def head_user_image_by_index(
            self, 
            user_id: str, 
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
        """Get user profile image.

        Http:
            <head>: /Users/{userId}/Images/{imageType}/{imageIndex}

        Args:
            user_id (str): User id.
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
            userId=user_id,
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
        return self._head(path='/Users/{userId}/Images/{imageType}/{imageIndex}', request_args=request_args)

    def post_user_image_by_index(
            self, 
            user_id: str, 
            image_type: ImageType, 
            index: int
    ) -> requests.Response:
        """Sets the user image.

        Http:
            <post>: /Users/{userId}/Images/{imageType}/{index}

        Args:
            user_id (str): User Id.
            image_type (ImageType): (Unused) Image type.
            index (int): (Unused) Image index.

        Returns:
            <204> requests.Response: Image updated.
            <403> requests.Response: User does not have permission to delete the image.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            imageType=image_type,
            index=index,
        )
        return self._post(path='/Users/{userId}/Images/{imageType}/{index}', request_args=request_args)

    def delete_user_image_by_index(
            self, 
            user_id: str, 
            image_type: ImageType, 
            index: int
    ) -> requests.Response:
        """Delete the user's image.

        Http:
            <delete>: /Users/{userId}/Images/{imageType}/{index}

        Args:
            user_id (str): User Id.
            image_type (ImageType): (Unused) Image type.
            index (int): (Unused) Image index.

        Returns:
            <204> requests.Response: Image deleted.
            <403> requests.Response: User does not have permission to delete the image.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            imageType=image_type,
            index=index,
        )
        return self._delete(path='/Users/{userId}/Images/{imageType}/{index}', request_args=request_args)

    def get_items_by_user_id(
            self, 
            user_id: str, 
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
            <get>: /Users/{userId}/Items

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
            location_types (List[LocationType]): Optional. If specified, results will be filtered based on LocationType. This allows multiple, comma delimeted.
            exclude_location_types (List[LocationType]): Optional. If specified, results will be filtered based on the LocationType. This allows multiple, comma delimeted.
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
            exclude_item_ids (List[str]): Optional. If specified, results will be filtered by exxcluding item ids. This allows multiple, comma delimeted.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            recursive (bool): When searching within folders, this determines whether or not the search will be recursive. true/false.
            search_term (str): Optional. Filter based on a search term.
            sort_order (List[SortOrder]): Sort Order - Ascending,Descending.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimeted. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
            exclude_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimeted.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimeted.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply. This allows multiple, comma delimeted. Options: IsFolder, IsNotFolder, IsUnplayed, IsPlayed, IsFavorite, IsResumable, Likes, Dislikes.
            is_favorite (bool): Optional filter by items that are marked as favorite, or not.
            media_types (List[str]): Optional filter by MediaType. Allows multiple, comma delimited.
            image_types (List[ImageType]): Optional. If specified, results will be filtered based on those containing image types. This allows multiple, comma delimited.
            sort_by (List[str]): Optional. Specify one or more sort orders, comma delimeted. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
            is_played (bool): Optional filter by items that are played, or not.
            genres (List[str]): Optional. If specified, results will be filtered based on genre. This allows multiple, pipe delimeted.
            official_ratings (List[str]): Optional. If specified, results will be filtered based on OfficialRating. This allows multiple, pipe delimeted.
            tags (List[str]): Optional. If specified, results will be filtered based on tag. This allows multiple, pipe delimeted.
            years (List[int]): Optional. If specified, results will be filtered based on production year. This allows multiple, comma delimeted.
            enable_user_data (bool): Optional, include user data.
            image_type_limit (int): Optional, the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            person (str): Optional. If specified, results will be filtered to include only those containing the specified person.
            person_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified person id.
            person_types (List[str]): Optional. If specified, along with Person, results will be filtered to include only those containing the specified person and PersonType. Allows multiple, comma-delimited.
            studios (List[str]): Optional. If specified, results will be filtered based on studio. This allows multiple, pipe delimeted.
            artists (List[str]): Optional. If specified, results will be filtered based on artists. This allows multiple, pipe delimeted.
            exclude_artist_ids (List[str]): Optional. If specified, results will be filtered based on artist id. This allows multiple, pipe delimeted.
            artist_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified artist id.
            album_artist_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified album artist id.
            contributing_artist_ids (List[str]): Optional. If specified, results will be filtered to include only those containing the specified contributing artist id.
            albums (List[str]): Optional. If specified, results will be filtered based on album. This allows multiple, pipe delimeted.
            album_ids (List[str]): Optional. If specified, results will be filtered based on album id. This allows multiple, pipe delimeted.
            ids (List[str]): Optional. If specific items are needed, specify a list of item id's to retrieve. This allows multiple, comma delimited.
            video_types (List[VideoType]): Optional filter by VideoType (videofile, dvd, bluray, iso). Allows multiple, comma delimeted.
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
            series_status (List[SeriesStatus]): Optional filter by Series Status. Allows multiple, comma delimeted.
            name_starts_with_or_greater (str): Optional filter by items whose name is sorted equally or greater than a given input string.
            name_starts_with (str): Optional filter by items whose name is sorted equally than a given input string.
            name_less_than (str): Optional filter by items whose name is equally or lesser than a given input string.
            studio_ids (List[str]): Optional. If specified, results will be filtered based on studio id. This allows multiple, pipe delimeted.
            genre_ids (List[str]): Optional. If specified, results will be filtered based on genre id. This allows multiple, pipe delimeted.
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
        return self._get(path='/Users/{userId}/Items', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_resume_items(
            self, 
            user_id: str, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            search_term: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            media_types: Optional[List[str]] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            include_item_types: Optional[List[str]] = None, 
            enable_total_record_count: Optional[bool] = True, 
            enable_images: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets items based on a query.

        Http:
            <get>: /Users/{userId}/Items/Resume

        Args:
            user_id (str): The user id.
            start_index (int): The start index.
            limit (int): The item limit.
            search_term (str): The search term.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output. This allows multiple, comma delimited. Options: Budget, Chapters, DateCreated, Genres, HomePageUrl, IndexOptions, MediaStreams, Overview, ParentId, Path, People, ProviderIds, PrimaryImageAspectRatio, Revenue, SortName, Studios, Taglines.
            media_types (List[str]): Optional. Filter by MediaType. Allows multiple, comma delimited.
            enable_user_data (bool): Optional. Include user data.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            exclude_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on the item type. This allows multiple, comma delimited.
            enable_total_record_count (bool = True): Optional. Enable the total record count.
            enable_images (bool = True): Optional. Include image information in output.

        Returns:
            <200> BaseItemDtoQueryResult: Items returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            searchTerm=search_term,
            parentId=parent_id,
            fields=fields,
            mediaTypes=media_types,
            enableUserData=enable_user_data,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            enableTotalRecordCount=enable_total_record_count,
            enableImages=enable_images,
        )
        return self._get(path='/Users/{userId}/Items/Resume', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def mark_played_item(
            self, 
            user_id: str, 
            item_id: str, 
            date_played: Optional[str] = None
    ) -> UserItemDataDto:
        """Marks an item as played for user.

        Http:
            <post>: /Users/{userId}/PlayedItems/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.
            date_played (str): Optional. The date the item was played.

        Returns:
            <200> UserItemDataDto: Item marked as played.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
            datePlayed=date_played,
        )
        return self._post(path='/Users/{userId}/PlayedItems/{itemId}', request_args=request_args, response_type=UserItemDataDto)

    def mark_unplayed_item(
            self, 
            user_id: str, 
            item_id: str
    ) -> UserItemDataDto:
        """Marks an item as unplayed for user.

        Http:
            <delete>: /Users/{userId}/PlayedItems/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> UserItemDataDto: Item marked as unplayed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._delete(path='/Users/{userId}/PlayedItems/{itemId}', request_args=request_args, response_type=UserItemDataDto)

    def on_playback_start(
            self, 
            user_id: str, 
            item_id: str, 
            media_source_id: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            play_method: Optional[PlayMethod] = None, 
            live_stream_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            can_seek: Optional[bool] = False
    ) -> requests.Response:
        """Reports that a user has begun playing an item.

        Http:
            <post>: /Users/{userId}/PlayingItems/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.
            media_source_id (str): The id of the MediaSource.
            audio_stream_index (int): The audio stream index.
            subtitle_stream_index (int): The subtitle stream index.
            play_method (PlayMethod): The play method.
            live_stream_id (str): The live stream id.
            play_session_id (str): The play session id.
            can_seek (bool = False): Indicates if the client can seek.

        Returns:
            <204> requests.Response: Play start recorded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
            mediaSourceId=media_source_id,
            audioStreamIndex=audio_stream_index,
            subtitleStreamIndex=subtitle_stream_index,
            playMethod=play_method,
            liveStreamId=live_stream_id,
            playSessionId=play_session_id,
            canSeek=can_seek,
        )
        return self._post(path='/Users/{userId}/PlayingItems/{itemId}', request_args=request_args)

    def on_playback_stopped(
            self, 
            user_id: str, 
            item_id: str, 
            media_source_id: Optional[str] = None, 
            next_media_type: Optional[str] = None, 
            position_ticks: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            play_session_id: Optional[str] = None
    ) -> requests.Response:
        """Reports that a user has stopped playing an item.

        Http:
            <delete>: /Users/{userId}/PlayingItems/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.
            media_source_id (str): The id of the MediaSource.
            next_media_type (str): The next media type that will play.
            position_ticks (int): Optional. The position, in ticks, where playback stopped. 1 tick = 10000 ms.
            live_stream_id (str): The live stream id.
            play_session_id (str): The play session id.

        Returns:
            <204> requests.Response: Playback stop recorded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
            mediaSourceId=media_source_id,
            nextMediaType=next_media_type,
            positionTicks=position_ticks,
            liveStreamId=live_stream_id,
            playSessionId=play_session_id,
        )
        return self._delete(path='/Users/{userId}/PlayingItems/{itemId}', request_args=request_args)

    def on_playback_progress(
            self, 
            user_id: str, 
            item_id: str, 
            media_source_id: Optional[str] = None, 
            position_ticks: Optional[int] = None, 
            audio_stream_index: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            volume_level: Optional[int] = None, 
            play_method: Optional[PlayMethod] = None, 
            live_stream_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            repeat_mode: Optional[RepeatMode] = None, 
            is_paused: Optional[bool] = False, 
            is_muted: Optional[bool] = False
    ) -> requests.Response:
        """Reports a user's playback progress.

        Http:
            <post>: /Users/{userId}/PlayingItems/{itemId}/Progress

        Args:
            user_id (str): User id.
            item_id (str): Item id.
            media_source_id (str): The id of the MediaSource.
            position_ticks (int): Optional. The current position, in ticks. 1 tick = 10000 ms.
            audio_stream_index (int): The audio stream index.
            subtitle_stream_index (int): The subtitle stream index.
            volume_level (int): Scale of 0-100.
            play_method (PlayMethod): The play method.
            live_stream_id (str): The live stream id.
            play_session_id (str): The play session id.
            repeat_mode (RepeatMode): The repeat mode.
            is_paused (bool = False): Indicates if the player is paused.
            is_muted (bool = False): Indicates if the player is muted.

        Returns:
            <204> requests.Response: Play progress recorded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
            mediaSourceId=media_source_id,
            positionTicks=position_ticks,
            audioStreamIndex=audio_stream_index,
            subtitleStreamIndex=subtitle_stream_index,
            volumeLevel=volume_level,
            playMethod=play_method,
            liveStreamId=live_stream_id,
            playSessionId=play_session_id,
            repeatMode=repeat_mode,
            isPaused=is_paused,
            isMuted=is_muted,
        )
        return self._post(path='/Users/{userId}/PlayingItems/{itemId}/Progress', request_args=request_args)

    def get_suggestions(
            self, 
            user_id: str, 
            media_type: Optional[List[str]] = None, 
            type: Optional[List[str]] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            enable_total_record_count: Optional[bool] = False
    ) -> BaseItemDtoQueryResult:
        """Gets suggestions.

        Http:
            <get>: /Users/{userId}/Suggestions

        Args:
            user_id (str): The user id.
            media_type (List[str]): The media types.
            type (List[str]): The type.
            start_index (int): Optional. The start index.
            limit (int): Optional. The limit.
            enable_total_record_count (bool = False): Whether to enable the total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Suggestions returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            mediaType=media_type,
            type=type,
            startIndex=start_index,
            limit=limit,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/Users/{userId}/Suggestions', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_users(
            self, 
            is_hidden: Optional[bool] = None, 
            is_disabled: Optional[bool] = None
    ) -> List[UserDto]:
        """Gets a list of users.

        Http:
            <get>: /Users

        Args:
            is_hidden (bool): Optional filter by IsHidden=true or false.
            is_disabled (bool): Optional filter by IsDisabled=true or false.

        Returns:
            <200> List[UserDto]: Users returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            isHidden=is_hidden,
            isDisabled=is_disabled,
        )
        return self._get(path='/Users', request_args=request_args, response_type=List[UserDto])

    def get_user_by_id(
            self, 
            user_id: str
    ) -> UserDto:
        """Gets a user by Id.

        Http:
            <get>: /Users/{userId}

        Args:
            user_id (str): The user id.

        Returns:
            <200> UserDto: User returned.
            <404> requests.Response: User not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/Users/{userId}', request_args=request_args, response_type=UserDto)

    def delete_user(
            self, 
            user_id: str
    ) -> requests.Response:
        """Deletes a user.

        Http:
            <delete>: /Users/{userId}

        Args:
            user_id (str): The user id.

        Returns:
            <204> requests.Response: User deleted.
            <404> requests.Response: User not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._delete(path='/Users/{userId}', request_args=request_args)

    def update_user(
            self, 
            user_id: str, 
            request_body: UserDto
    ) -> requests.Response:
        """Updates a user.

        Http:
            <post>: /Users/{userId}

        Args:
            user_id (str): The user id.
            request_body (UserDto): The updated user model.

        Returns:
            <204> requests.Response: User updated.
            <400> requests.Response: User information was not supplied.
            <403> requests.Response: User update forbidden.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            requestBody=request_body,
        )
        return self._post(path='/Users/{userId}', request_args=request_args)

    def authenticate_user(
            self, 
            user_id: str, 
            pw: str, 
            password: Optional[str] = None
    ) -> AuthenticationResult:
        """Authenticates a user.

        Http:
            <post>: /Users/{userId}/Authenticate

        Args:
            user_id (str): The user id.
            pw (str): The password as plain text.
            password (str): The password sha1-hash.

        Returns:
            <200> AuthenticationResult: User authenticated.
            <403> requests.Response: Sha1-hashed password only is not allowed.
            <404> requests.Response: User not found.
        """
        request_args = dict(
            userId=user_id,
            pw=pw,
            password=password,
        )
        return self._post(path='/Users/{userId}/Authenticate', request_args=request_args, response_type=AuthenticationResult)

    def update_user_configuration(
            self, 
            user_id: str, 
            request_body: UserConfiguration
    ) -> requests.Response:
        """Updates a user configuration.

        Http:
            <post>: /Users/{userId}/Configuration

        Args:
            user_id (str): The user id.
            request_body (UserConfiguration): The new user configuration.

        Returns:
            <204> requests.Response: User configuration updated.
            <403> requests.Response: User configuration update forbidden.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            requestBody=request_body,
        )
        return self._post(path='/Users/{userId}/Configuration', request_args=request_args)

    def update_user_easy_password(
            self, 
            user_id: str, 
            request_body: UpdateUserEasyPassword
    ) -> requests.Response:
        """Updates a user's easy password.

        Http:
            <post>: /Users/{userId}/EasyPassword

        Args:
            user_id (str): The user id.
            request_body (UpdateUserEasyPassword): The M:Jellyfin.Api.Controllers.UserController.UpdateUserEasyPassword(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserEasyPassword) request.

        Returns:
            <204> requests.Response: Password successfully reset.
            <403> requests.Response: User is not allowed to update the password.
            <404> requests.Response: User not found.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            requestBody=request_body,
        )
        return self._post(path='/Users/{userId}/EasyPassword', request_args=request_args)

    def update_user_password(
            self, 
            user_id: str, 
            request_body: UpdateUserPassword
    ) -> requests.Response:
        """Updates a user's password.

        Http:
            <post>: /Users/{userId}/Password

        Args:
            user_id (str): The user id.
            request_body (UpdateUserPassword): The M:Jellyfin.Api.Controllers.UserController.UpdateUserPassword(System.Guid,Jellyfin.Api.Models.UserDtos.UpdateUserPassword) request.

        Returns:
            <204> requests.Response: Password successfully reset.
            <403> requests.Response: User is not allowed to update the password.
            <404> requests.Response: User not found.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            requestBody=request_body,
        )
        return self._post(path='/Users/{userId}/Password', request_args=request_args)

    def update_user_policy(
            self, 
            user_id: str, 
            request_body: UserPolicy
    ) -> requests.Response:
        """Updates a user policy.

        Http:
            <post>: /Users/{userId}/Policy

        Args:
            user_id (str): The user id.
            request_body (UserPolicy): The new user policy.

        Returns:
            <204> requests.Response: User policy updated.
            <400> requests.Response: User policy was not supplied.
            <403> requests.Response: User policy update forbidden.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            userId=user_id,
            requestBody=request_body,
        )
        return self._post(path='/Users/{userId}/Policy', request_args=request_args)

    def authenticate_user_by_name(
            self, 
            request_body: AuthenticateUserByName
    ) -> AuthenticationResult:
        """Authenticates a user by name.

        Http:
            <post>: /Users/AuthenticateByName

        Args:
            request_body (AuthenticateUserByName): The M:Jellyfin.Api.Controllers.UserController.AuthenticateUserByName(Jellyfin.Api.Models.UserDtos.AuthenticateUserByName) request.

        Returns:
            <200> AuthenticationResult: User authenticated.
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Users/AuthenticateByName', request_args=request_args, response_type=AuthenticationResult)

    def authenticate_with_quick_connect(
            self, 
            request_body: QuickConnectDto
    ) -> AuthenticationResult:
        """Authenticates a user with quick connect.

        Http:
            <post>: /Users/AuthenticateWithQuickConnect

        Args:
            request_body (QuickConnectDto): The Jellyfin.Api.Models.UserDtos.QuickConnectDto request.

        Returns:
            <200> AuthenticationResult: User authenticated.
            <400> requests.Response: Missing token.
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Users/AuthenticateWithQuickConnect', request_args=request_args, response_type=AuthenticationResult)

    def forgot_password(
            self, 
            request_body: ForgotPasswordDto
    ) -> ForgotPasswordResult:
        """Initiates the forgot password process for a local user.

        Http:
            <post>: /Users/ForgotPassword

        Args:
            request_body (ForgotPasswordDto): The forgot password request containing the entered username.

        Returns:
            <200> ForgotPasswordResult: Password reset process started.
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Users/ForgotPassword', request_args=request_args, response_type=ForgotPasswordResult)

    def forgot_password_pin(
            self, 
            request_body: ForgotPasswordPinDto
    ) -> PinRedeemResult:
        """Redeems a forgot password pin.

        Http:
            <post>: /Users/ForgotPassword/Pin

        Args:
            request_body (ForgotPasswordPinDto): The forgot password pin request containing the entered pin.

        Returns:
            <200> PinRedeemResult: Pin reset process started.
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Users/ForgotPassword/Pin', request_args=request_args, response_type=PinRedeemResult)

    def get_current_user(
            self
    ) -> UserDto:
        """Gets the user based on auth token.

        Http:
            <get>: /Users/Me

        Returns:
            <200> UserDto: User returned.
            <400> requests.Response: Token is not owned by a user.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Users/Me', response_type=UserDto)

    def create_user_by_name(
            self, 
            request_body: CreateUserByName
    ) -> UserDto:
        """Creates a user.

        Http:
            <post>: /Users/New

        Args:
            request_body (CreateUserByName): The create user by name request body.

        Returns:
            <200> UserDto: User created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Users/New', request_args=request_args, response_type=UserDto)

    def get_public_users(
            self
    ) -> List[UserDto]:
        """Gets a list of publicly visible users for display on a login screen.

        Http:
            <get>: /Users/Public

        Returns:
            <200> List[UserDto]: Public users returned.
        """
        return self._get(path='/Users/Public', response_type=List[UserDto])

    def mark_favorite_item(
            self, 
            user_id: str, 
            item_id: str
    ) -> UserItemDataDto:
        """Marks an item as a favorite.

        Http:
            <post>: /Users/{userId}/FavoriteItems/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> UserItemDataDto: Item marked as favorite.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._post(path='/Users/{userId}/FavoriteItems/{itemId}', request_args=request_args, response_type=UserItemDataDto)

    def unmark_favorite_item(
            self, 
            user_id: str, 
            item_id: str
    ) -> UserItemDataDto:
        """Unmarks item as a favorite.

        Http:
            <delete>: /Users/{userId}/FavoriteItems/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> UserItemDataDto: Item unmarked as favorite.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._delete(path='/Users/{userId}/FavoriteItems/{itemId}', request_args=request_args, response_type=UserItemDataDto)

    def get_item(
            self, 
            user_id: str, 
            item_id: str
    ) -> BaseItemDto:
        """Gets an item from a user's library.

        Http:
            <get>: /Users/{userId}/Items/{itemId}

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> BaseItemDto: Item returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._get(path='/Users/{userId}/Items/{itemId}', request_args=request_args, response_type=BaseItemDto)

    def get_intros(
            self, 
            user_id: str, 
            item_id: str
    ) -> BaseItemDtoQueryResult:
        """Gets intros to play before the main media item plays.

        Http:
            <get>: /Users/{userId}/Items/{itemId}/Intros

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> BaseItemDtoQueryResult: Intros returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._get(path='/Users/{userId}/Items/{itemId}/Intros', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_local_trailers(
            self, 
            user_id: str, 
            item_id: str
    ) -> List[BaseItemDto]:
        """Gets local trailers for an item.

        Http:
            <get>: /Users/{userId}/Items/{itemId}/LocalTrailers

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> List[BaseItemDto]: An Microsoft.AspNetCore.Mvc.OkResult containing the item's local trailers.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._get(path='/Users/{userId}/Items/{itemId}/LocalTrailers', request_args=request_args, response_type=List[BaseItemDto])

    def delete_user_item_rating(
            self, 
            user_id: str, 
            item_id: str
    ) -> UserItemDataDto:
        """Deletes a user's saved personal rating for an item.

        Http:
            <delete>: /Users/{userId}/Items/{itemId}/Rating

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> UserItemDataDto: Personal rating removed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._delete(path='/Users/{userId}/Items/{itemId}/Rating', request_args=request_args, response_type=UserItemDataDto)

    def update_user_item_rating(
            self, 
            user_id: str, 
            item_id: str, 
            likes: Optional[bool] = None
    ) -> UserItemDataDto:
        """Updates a user's rating for an item.

        Http:
            <post>: /Users/{userId}/Items/{itemId}/Rating

        Args:
            user_id (str): User id.
            item_id (str): Item id.
            likes (bool): Whether this M:Jellyfin.Api.Controllers.UserLibraryController.UpdateUserItemRating(System.Guid,System.Guid,System.Nullable{System.Boolean}) is likes.

        Returns:
            <200> UserItemDataDto: Item rating updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
            likes=likes,
        )
        return self._post(path='/Users/{userId}/Items/{itemId}/Rating', request_args=request_args, response_type=UserItemDataDto)

    def get_special_features(
            self, 
            user_id: str, 
            item_id: str
    ) -> List[BaseItemDto]:
        """Gets special features for an item.

        Http:
            <get>: /Users/{userId}/Items/{itemId}/SpecialFeatures

        Args:
            user_id (str): User id.
            item_id (str): Item id.

        Returns:
            <200> List[BaseItemDto]: Special features returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
        )
        return self._get(path='/Users/{userId}/Items/{itemId}/SpecialFeatures', request_args=request_args, response_type=List[BaseItemDto])

    def get_latest_media(
            self, 
            user_id: str, 
            parent_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            include_item_types: Optional[List[str]] = None, 
            is_played: Optional[bool] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            enable_user_data: Optional[bool] = None, 
            limit: Optional[int] = 20, 
            group_items: Optional[bool] = True
    ) -> List[BaseItemDto]:
        """Gets latest media.

        Http:
            <get>: /Users/{userId}/Items/Latest

        Args:
            user_id (str): User id.
            parent_id (str): Specify this to localize the search to a specific item or folder. Omit to use the root.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            include_item_types (List[str]): Optional. If specified, results will be filtered based on item type. This allows multiple, comma delimited.
            is_played (bool): Filter by items that are played, or not.
            enable_images (bool): Optional. include image information in output.
            image_type_limit (int): Optional. the max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            enable_user_data (bool): Optional. include user data.
            limit (int = 20): Return item limit.
            group_items (bool = True): Whether or not to group items into a parent container.

        Returns:
            <200> List[BaseItemDto]: Latest media returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            parentId=parent_id,
            fields=fields,
            includeItemTypes=include_item_types,
            isPlayed=is_played,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            enableUserData=enable_user_data,
            limit=limit,
            groupItems=group_items,
        )
        return self._get(path='/Users/{userId}/Items/Latest', request_args=request_args, response_type=List[BaseItemDto])

    def get_root_folder(
            self, 
            user_id: str
    ) -> BaseItemDto:
        """Gets the root folder from a user's library.

        Http:
            <get>: /Users/{userId}/Items/Root

        Args:
            user_id (str): User id.

        Returns:
            <200> BaseItemDto: Root folder returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/Users/{userId}/Items/Root', request_args=request_args, response_type=BaseItemDto)

    def get_grouping_options(
            self, 
            user_id: str
    ) -> List[SpecialViewOptionDto]:
        """Get user view grouping options.

        Http:
            <get>: /Users/{userId}/GroupingOptions

        Args:
            user_id (str): User id.

        Returns:
            <200> List[SpecialViewOptionDto]: User view grouping options returned.
            <404> requests.Response: User not found.
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/Users/{userId}/GroupingOptions', request_args=request_args, response_type=List[SpecialViewOptionDto])

    def get_user_views(
            self, 
            user_id: str, 
            include_external_content: Optional[bool] = None, 
            preset_views: Optional[List[str]] = None, 
            include_hidden: Optional[bool] = False
    ) -> BaseItemDtoQueryResult:
        """Get user views.

        Http:
            <get>: /Users/{userId}/Views

        Args:
            user_id (str): User id.
            include_external_content (bool): Whether or not to include external views such as channels or live tv.
            preset_views (List[str]): Preset views.
            include_hidden (bool = False): Whether or not to include hidden content.

        Returns:
            <200> BaseItemDtoQueryResult: User views returned.
        """
        request_args = dict(
            userId=user_id,
            includeExternalContent=include_external_content,
            presetViews=preset_views,
            includeHidden=include_hidden,
        )
        return self._get(path='/Users/{userId}/Views', request_args=request_args, response_type=BaseItemDtoQueryResult)
