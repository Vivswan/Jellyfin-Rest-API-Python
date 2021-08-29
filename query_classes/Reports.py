import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from data_classes.report_result import ReportResult as ReportResult
from data_classes.report_export_type import ReportExportType as ReportExportType


class Reports(BaseRequestClass):
    def get_activity_logs(
            self, 
            report_view: Optional[str] = None, 
            display_type: Optional[str] = None, 
            has_query_limit: Optional[bool] = None, 
            group_by: Optional[str] = None, 
            report_columns: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            min_date: Optional[str] = None, 
            include_item_types: Optional[str] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /Reports/Activities

        Args:
            report_view (str)
            display_type (str)
            has_query_limit (bool)
            group_by (str)
            report_columns (str)
            start_index (int)
            limit (int)
            min_date (str)
            include_item_types (str)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            reportView=report_view,
            displayType=display_type,
            hasQueryLimit=has_query_limit,
            groupBy=group_by,
            reportColumns=report_columns,
            startIndex=start_index,
            limit=limit,
            minDate=min_date,
            includeItemTypes=include_item_types,
        )
        return self._get(path='/Reports/Activities', request_args=request_args)

    def get_report_headers(
            self, 
            report_view: Optional[str] = None, 
            include_item_types: Optional[str] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /Reports/Headers

        Args:
            report_view (str)
            include_item_types (str)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            reportView=report_view,
            includeItemTypes=include_item_types,
        )
        return self._get(path='/Reports/Headers', request_args=request_args)

    def get_item_report(
            self, 
            has_theme_song: Optional[bool] = None, 
            has_theme_video: Optional[bool] = None, 
            has_subtitles: Optional[bool] = None, 
            has_special_feature: Optional[bool] = None, 
            has_trailer: Optional[bool] = None, 
            adjacent_to: Optional[str] = None, 
            min_index_number: Optional[int] = None, 
            parent_index_number: Optional[int] = None, 
            has_parental_rating: Optional[bool] = None, 
            is_hd: Optional[bool] = None, 
            location_types: Optional[str] = None, 
            exclude_location_types: Optional[str] = None, 
            is_missing: Optional[bool] = None, 
            is_unaried: Optional[bool] = None, 
            min_community_rating: Optional[float] = None, 
            min_critic_rating: Optional[float] = None, 
            aired_during_season: Optional[int] = None, 
            min_premiere_date: Optional[str] = None, 
            min_date_last_saved: Optional[str] = None, 
            min_date_last_saved_for_user: Optional[str] = None, 
            max_premiere_date: Optional[str] = None, 
            has_overview: Optional[bool] = None, 
            has_imdb_id: Optional[bool] = None, 
            has_tmdb_id: Optional[bool] = None, 
            has_tvdb_id: Optional[bool] = None, 
            is_in_box_set: Optional[bool] = None, 
            exclude_item_ids: Optional[str] = None, 
            enable_total_record_count: Optional[bool] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            recursive: Optional[bool] = None, 
            sort_order: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[str] = None, 
            exclude_item_types: Optional[str] = None, 
            include_item_types: Optional[str] = None, 
            filters: Optional[str] = None, 
            is_favorite: Optional[bool] = None, 
            is_not_favorite: Optional[bool] = None, 
            media_types: Optional[str] = None, 
            image_types: Optional[str] = None, 
            sort_by: Optional[str] = None, 
            is_played: Optional[bool] = None, 
            genres: Optional[str] = None, 
            genre_ids: Optional[str] = None, 
            official_ratings: Optional[str] = None, 
            tags: Optional[str] = None, 
            years: Optional[str] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[str] = None, 
            person: Optional[str] = None, 
            person_ids: Optional[str] = None, 
            person_types: Optional[str] = None, 
            studios: Optional[str] = None, 
            studio_ids: Optional[str] = None, 
            artists: Optional[str] = None, 
            exclude_artist_ids: Optional[str] = None, 
            artist_ids: Optional[str] = None, 
            albums: Optional[str] = None, 
            album_ids: Optional[str] = None, 
            ids: Optional[str] = None, 
            video_types: Optional[str] = None, 
            user_id: Optional[str] = None, 
            min_official_rating: Optional[str] = None, 
            is_locked: Optional[bool] = None, 
            is_place_holder: Optional[bool] = None, 
            has_official_rating: Optional[bool] = None, 
            collapse_box_set_items: Optional[bool] = None, 
            is3_d: Optional[bool] = None, 
            series_status: Optional[str] = None, 
            name_starts_with_or_greater: Optional[str] = None, 
            name_starts_with: Optional[str] = None, 
            name_less_than: Optional[str] = None, 
            report_view: Optional[str] = None, 
            display_type: Optional[str] = None, 
            has_query_limit: Optional[bool] = None, 
            group_by: Optional[str] = None, 
            report_columns: Optional[str] = None, 
            enable_images: Optional[bool] = True
    ) -> ReportResult:
        """
        Http:
            <get>: /Reports/Items

        Args:
            has_theme_song (bool)
            has_theme_video (bool)
            has_subtitles (bool)
            has_special_feature (bool)
            has_trailer (bool)
            adjacent_to (str)
            min_index_number (int)
            parent_index_number (int)
            has_parental_rating (bool)
            is_hd (bool)
            location_types (str)
            exclude_location_types (str)
            is_missing (bool)
            is_unaried (bool)
            min_community_rating (float)
            min_critic_rating (float)
            aired_during_season (int)
            min_premiere_date (str)
            min_date_last_saved (str)
            min_date_last_saved_for_user (str)
            max_premiere_date (str)
            has_overview (bool)
            has_imdb_id (bool)
            has_tmdb_id (bool)
            has_tvdb_id (bool)
            is_in_box_set (bool)
            exclude_item_ids (str)
            enable_total_record_count (bool)
            start_index (int)
            limit (int)
            recursive (bool)
            sort_order (str)
            parent_id (str)
            fields (str)
            exclude_item_types (str)
            include_item_types (str)
            filters (str)
            is_favorite (bool)
            is_not_favorite (bool)
            media_types (str)
            image_types (str)
            sort_by (str)
            is_played (bool)
            genres (str)
            genre_ids (str)
            official_ratings (str)
            tags (str)
            years (str)
            enable_user_data (bool)
            image_type_limit (int)
            enable_image_types (str)
            person (str)
            person_ids (str)
            person_types (str)
            studios (str)
            studio_ids (str)
            artists (str)
            exclude_artist_ids (str)
            artist_ids (str)
            albums (str)
            album_ids (str)
            ids (str)
            video_types (str)
            user_id (str)
            min_official_rating (str)
            is_locked (bool)
            is_place_holder (bool)
            has_official_rating (bool)
            collapse_box_set_items (bool)
            is3_d (bool)
            series_status (str)
            name_starts_with_or_greater (str)
            name_starts_with (str)
            name_less_than (str)
            report_view (str)
            display_type (str)
            has_query_limit (bool)
            group_by (str)
            report_columns (str)
            enable_images (bool = True)

        Returns:
            <200> ReportResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            hasThemeSong=has_theme_song,
            hasThemeVideo=has_theme_video,
            hasSubtitles=has_subtitles,
            hasSpecialFeature=has_special_feature,
            hasTrailer=has_trailer,
            adjacentTo=adjacent_to,
            minIndexNumber=min_index_number,
            parentIndexNumber=parent_index_number,
            hasParentalRating=has_parental_rating,
            isHd=is_hd,
            locationTypes=location_types,
            excludeLocationTypes=exclude_location_types,
            isMissing=is_missing,
            isUnaried=is_unaried,
            minCommunityRating=min_community_rating,
            minCriticRating=min_critic_rating,
            airedDuringSeason=aired_during_season,
            minPremiereDate=min_premiere_date,
            minDateLastSaved=min_date_last_saved,
            minDateLastSavedForUser=min_date_last_saved_for_user,
            maxPremiereDate=max_premiere_date,
            hasOverview=has_overview,
            hasImdbId=has_imdb_id,
            hasTmdbId=has_tmdb_id,
            hasTvdbId=has_tvdb_id,
            isInBoxSet=is_in_box_set,
            excludeItemIds=exclude_item_ids,
            enableTotalRecordCount=enable_total_record_count,
            startIndex=start_index,
            limit=limit,
            recursive=recursive,
            sortOrder=sort_order,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            filters=filters,
            isFavorite=is_favorite,
            isNotFavorite=is_not_favorite,
            mediaTypes=media_types,
            imageTypes=image_types,
            sortBy=sort_by,
            isPlayed=is_played,
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
            artists=artists,
            excludeArtistIds=exclude_artist_ids,
            artistIds=artist_ids,
            albums=albums,
            albumIds=album_ids,
            ids=ids,
            videoTypes=video_types,
            userId=user_id,
            minOfficialRating=min_official_rating,
            isLocked=is_locked,
            isPlaceHolder=is_place_holder,
            hasOfficialRating=has_official_rating,
            collapseBoxSetItems=collapse_box_set_items,
            is3D=is3_d,
            seriesStatus=series_status,
            nameStartsWithOrGreater=name_starts_with_or_greater,
            nameStartsWith=name_starts_with,
            nameLessThan=name_less_than,
            reportView=report_view,
            displayType=display_type,
            hasQueryLimit=has_query_limit,
            groupBy=group_by,
            reportColumns=report_columns,
            enableImages=enable_images,
        )
        return self._get(path='/Reports/Items', request_args=request_args, response_type=ReportResult)

    def get_report_download(
            self, 
            export_type: ReportExportType, 
            has_theme_song: Optional[bool] = None, 
            has_theme_video: Optional[bool] = None, 
            has_subtitles: Optional[bool] = None, 
            has_special_feature: Optional[bool] = None, 
            has_trailer: Optional[bool] = None, 
            adjacent_to: Optional[str] = None, 
            min_index_number: Optional[int] = None, 
            parent_index_number: Optional[int] = None, 
            has_parental_rating: Optional[bool] = None, 
            is_hd: Optional[bool] = None, 
            location_types: Optional[str] = None, 
            exclude_location_types: Optional[str] = None, 
            is_missing: Optional[bool] = None, 
            is_unaried: Optional[bool] = None, 
            min_community_rating: Optional[float] = None, 
            min_critic_rating: Optional[float] = None, 
            aired_during_season: Optional[int] = None, 
            min_premiere_date: Optional[str] = None, 
            min_date_last_saved: Optional[str] = None, 
            min_date_last_saved_for_user: Optional[str] = None, 
            max_premiere_date: Optional[str] = None, 
            has_overview: Optional[bool] = None, 
            has_imdb_id: Optional[bool] = None, 
            has_tmdb_id: Optional[bool] = None, 
            has_tvdb_id: Optional[bool] = None, 
            is_in_box_set: Optional[bool] = None, 
            exclude_item_ids: Optional[str] = None, 
            enable_total_record_count: Optional[bool] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            recursive: Optional[bool] = None, 
            sort_order: Optional[str] = None, 
            parent_id: Optional[str] = None, 
            fields: Optional[str] = None, 
            exclude_item_types: Optional[str] = None, 
            include_item_types: Optional[str] = None, 
            filters: Optional[str] = None, 
            is_favorite: Optional[bool] = None, 
            is_not_favorite: Optional[bool] = None, 
            media_types: Optional[str] = None, 
            image_types: Optional[str] = None, 
            sort_by: Optional[str] = None, 
            is_played: Optional[bool] = None, 
            genres: Optional[str] = None, 
            genre_ids: Optional[str] = None, 
            official_ratings: Optional[str] = None, 
            tags: Optional[str] = None, 
            years: Optional[str] = None, 
            enable_user_data: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[str] = None, 
            person: Optional[str] = None, 
            person_ids: Optional[str] = None, 
            person_types: Optional[str] = None, 
            studios: Optional[str] = None, 
            studio_ids: Optional[str] = None, 
            artists: Optional[str] = None, 
            exclude_artist_ids: Optional[str] = None, 
            artist_ids: Optional[str] = None, 
            albums: Optional[str] = None, 
            album_ids: Optional[str] = None, 
            ids: Optional[str] = None, 
            video_types: Optional[str] = None, 
            user_id: Optional[str] = None, 
            min_official_rating: Optional[str] = None, 
            is_locked: Optional[bool] = None, 
            is_place_holder: Optional[bool] = None, 
            has_official_rating: Optional[bool] = None, 
            collapse_box_set_items: Optional[bool] = None, 
            is3_d: Optional[bool] = None, 
            series_status: Optional[str] = None, 
            name_starts_with_or_greater: Optional[str] = None, 
            name_starts_with: Optional[str] = None, 
            name_less_than: Optional[str] = None, 
            report_view: Optional[str] = None, 
            display_type: Optional[str] = None, 
            has_query_limit: Optional[bool] = None, 
            group_by: Optional[str] = None, 
            report_columns: Optional[str] = None, 
            min_date: Optional[str] = None, 
            enable_images: Optional[bool] = True
    ) -> ReportResult:
        """
        Http:
            <get>: /Reports/Items/Download

        Args:
            export_type (ReportExportType)
            has_theme_song (bool)
            has_theme_video (bool)
            has_subtitles (bool)
            has_special_feature (bool)
            has_trailer (bool)
            adjacent_to (str)
            min_index_number (int)
            parent_index_number (int)
            has_parental_rating (bool)
            is_hd (bool)
            location_types (str)
            exclude_location_types (str)
            is_missing (bool)
            is_unaried (bool)
            min_community_rating (float)
            min_critic_rating (float)
            aired_during_season (int)
            min_premiere_date (str)
            min_date_last_saved (str)
            min_date_last_saved_for_user (str)
            max_premiere_date (str)
            has_overview (bool)
            has_imdb_id (bool)
            has_tmdb_id (bool)
            has_tvdb_id (bool)
            is_in_box_set (bool)
            exclude_item_ids (str)
            enable_total_record_count (bool)
            start_index (int)
            limit (int)
            recursive (bool)
            sort_order (str)
            parent_id (str)
            fields (str)
            exclude_item_types (str)
            include_item_types (str)
            filters (str)
            is_favorite (bool)
            is_not_favorite (bool)
            media_types (str)
            image_types (str)
            sort_by (str)
            is_played (bool)
            genres (str)
            genre_ids (str)
            official_ratings (str)
            tags (str)
            years (str)
            enable_user_data (bool)
            image_type_limit (int)
            enable_image_types (str)
            person (str)
            person_ids (str)
            person_types (str)
            studios (str)
            studio_ids (str)
            artists (str)
            exclude_artist_ids (str)
            artist_ids (str)
            albums (str)
            album_ids (str)
            ids (str)
            video_types (str)
            user_id (str)
            min_official_rating (str)
            is_locked (bool)
            is_place_holder (bool)
            has_official_rating (bool)
            collapse_box_set_items (bool)
            is3_d (bool)
            series_status (str)
            name_starts_with_or_greater (str)
            name_starts_with (str)
            name_less_than (str)
            report_view (str)
            display_type (str)
            has_query_limit (bool)
            group_by (str)
            report_columns (str)
            min_date (str)
            enable_images (bool = True)

        Returns:
            <200> ReportResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            exportType=export_type,
            hasThemeSong=has_theme_song,
            hasThemeVideo=has_theme_video,
            hasSubtitles=has_subtitles,
            hasSpecialFeature=has_special_feature,
            hasTrailer=has_trailer,
            adjacentTo=adjacent_to,
            minIndexNumber=min_index_number,
            parentIndexNumber=parent_index_number,
            hasParentalRating=has_parental_rating,
            isHd=is_hd,
            locationTypes=location_types,
            excludeLocationTypes=exclude_location_types,
            isMissing=is_missing,
            isUnaried=is_unaried,
            minCommunityRating=min_community_rating,
            minCriticRating=min_critic_rating,
            airedDuringSeason=aired_during_season,
            minPremiereDate=min_premiere_date,
            minDateLastSaved=min_date_last_saved,
            minDateLastSavedForUser=min_date_last_saved_for_user,
            maxPremiereDate=max_premiere_date,
            hasOverview=has_overview,
            hasImdbId=has_imdb_id,
            hasTmdbId=has_tmdb_id,
            hasTvdbId=has_tvdb_id,
            isInBoxSet=is_in_box_set,
            excludeItemIds=exclude_item_ids,
            enableTotalRecordCount=enable_total_record_count,
            startIndex=start_index,
            limit=limit,
            recursive=recursive,
            sortOrder=sort_order,
            parentId=parent_id,
            fields=fields,
            excludeItemTypes=exclude_item_types,
            includeItemTypes=include_item_types,
            filters=filters,
            isFavorite=is_favorite,
            isNotFavorite=is_not_favorite,
            mediaTypes=media_types,
            imageTypes=image_types,
            sortBy=sort_by,
            isPlayed=is_played,
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
            artists=artists,
            excludeArtistIds=exclude_artist_ids,
            artistIds=artist_ids,
            albums=albums,
            albumIds=album_ids,
            ids=ids,
            videoTypes=video_types,
            userId=user_id,
            minOfficialRating=min_official_rating,
            isLocked=is_locked,
            isPlaceHolder=is_place_holder,
            hasOfficialRating=has_official_rating,
            collapseBoxSetItems=collapse_box_set_items,
            is3D=is3_d,
            seriesStatus=series_status,
            nameStartsWithOrGreater=name_starts_with_or_greater,
            nameStartsWith=name_starts_with,
            nameLessThan=name_less_than,
            reportView=report_view,
            displayType=display_type,
            hasQueryLimit=has_query_limit,
            groupBy=group_by,
            reportColumns=report_columns,
            minDate=min_date,
            enableImages=enable_images,
        )
        return self._get(path='/Reports/Items/Download', request_args=request_args, response_type=ReportResult)

