from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.video_type import VideoType as VideoType
from data_classes.sort_order import SortOrder as SortOrder
from data_classes.series_status import SeriesStatus as SeriesStatus
from data_classes.location_type import LocationType as LocationType
from data_classes.item_filter import ItemFilter as ItemFilter
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult


class Trailers(BaseRequestClass):
    def get_similar_trailers(
            self, 
            item_id: str, 
            exclude_artist_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets similar items.

        Http:
            <get>: /Trailers/{itemId}/Similar

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
        return self._get(path='/Trailers/{itemId}/Similar', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_trailers(
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
        """Finds movies and trailers similar to a given trailer.

        Http:
            <get>: /Trailers

        Args:
            user_id (str): The user id.
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
        return self._get(path='/Trailers', request_args=request_args, response_type=BaseItemDtoQueryResult)

