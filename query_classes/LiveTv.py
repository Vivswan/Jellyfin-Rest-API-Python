from typing import List
from typing import Optional

import requests

from data_classes.base_item_dto import BaseItemDto as BaseItemDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.channel_mapping_options_dto import ChannelMappingOptionsDto as ChannelMappingOptionsDto
from data_classes.channel_type import ChannelType as ChannelType
from data_classes.get_programs_dto import GetProgramsDto as GetProgramsDto
from data_classes.guide_info import GuideInfo as GuideInfo
from data_classes.image_type_element import ImageTypeElement as ImageType
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.listings_provider_info import ListingsProviderInfo as ListingsProviderInfo
from data_classes.live_tv_info import LiveTvInfo as LiveTvInfo
from data_classes.name_i_d_pair import NameIDPair as NameIdPair
from data_classes.recording_status_enum import RecordingStatusEnum as RecordingStatus
from data_classes.series_timer_info_dto import SeriesTimerInfoDto as SeriesTimerInfoDto
from data_classes.series_timer_info_dto_query_result import \
    SeriesTimerInfoDtoQueryResult as SeriesTimerInfoDtoQueryResult
from data_classes.set_channel_mapping_dto import SetChannelMappingDto as SetChannelMappingDto
from data_classes.sort_order import SortOrder as SortOrder
from data_classes.timer_info_dto import TimerInfoDto as TimerInfoDto
from data_classes.timer_info_dto_query_result import TimerInfoDtoQueryResult as TimerInfoDtoQueryResult
from data_classes.tuner_channel_mapping import TunerChannelMapping as TunerChannelMapping
from data_classes.tuner_host_info import TunerHostInfo as TunerHostInfo
from util.BaseRequestClass import BaseRequestClass


class LiveTv(BaseRequestClass):
    def get_channel_mapping_options(
            self, 
            provider_id: Optional[str] = None
    ) -> ChannelMappingOptionsDto:
        """Get channel mapping options.

        Http:
            <get>: /LiveTv/ChannelMappingOptions

        Args:
            provider_id (str): Provider id.

        Returns:
            <200> ChannelMappingOptionsDto: Channel mapping options returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            providerId=provider_id,
        )
        return self._get(path='/LiveTv/ChannelMappingOptions', request_args=request_args, response_type=ChannelMappingOptionsDto)

    def set_channel_mapping(
            self, 
            request_body: SetChannelMappingDto
    ) -> TunerChannelMapping:
        """Set channel mappings.

        Http:
            <post>: /LiveTv/ChannelMappings

        Args:
            request_body (SetChannelMappingDto): The set channel mapping dto.

        Returns:
            <200> TunerChannelMapping: Created channel mapping returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/ChannelMappings', request_args=request_args, response_type=TunerChannelMapping)

    def get_live_tv_channels(
            self, 
            type: Optional[ChannelType] = None, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            is_movie: Optional[bool] = None, 
            is_series: Optional[bool] = None, 
            is_news: Optional[bool] = None, 
            is_kids: Optional[bool] = None, 
            is_sports: Optional[bool] = None, 
            limit: Optional[int] = None, 
            is_favorite: Optional[bool] = None, 
            is_liked: Optional[bool] = None, 
            is_disliked: Optional[bool] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_user_data: Optional[bool] = None, 
            sort_by: Optional[List[str]] = None, 
            sort_order: Optional[SortOrder] = None, 
            enable_favorite_sorting: Optional[bool] = False, 
            add_current_program: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets available live tv channels.

        Http:
            <get>: /LiveTv/Channels

        Args:
            type (ChannelType): Optional. Filter by channel type.
            user_id (str): Optional. Filter by user and attach user data.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            is_movie (bool): Optional. Filter for movies.
            is_series (bool): Optional. Filter for series.
            is_news (bool): Optional. Filter for news.
            is_kids (bool): Optional. Filter for kids.
            is_sports (bool): Optional. Filter for sports.
            limit (int): Optional. The maximum number of records to return.
            is_favorite (bool): Optional. Filter by channels that are favorites, or not.
            is_liked (bool): Optional. Filter by channels that are liked, or not.
            is_disliked (bool): Optional. Filter by channels that are disliked, or not.
            enable_images (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): "Optional. The image types to include in the output.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            enable_user_data (bool): Optional. Include user data.
            sort_by (List[str]): Optional. Key to sort by.
            sort_order (SortOrder): Optional. Sort order.
            enable_favorite_sorting (bool = False): Optional. Incorporate favorite and like status into channel sorting.
            add_current_program (bool = True): Optional. Adds current program info to each channel.

        Returns:
            <200> BaseItemDtoQueryResult: Available live tv channels returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            type=type,
            userId=user_id,
            startIndex=start_index,
            isMovie=is_movie,
            isSeries=is_series,
            isNews=is_news,
            isKids=is_kids,
            isSports=is_sports,
            limit=limit,
            isFavorite=is_favorite,
            isLiked=is_liked,
            isDisliked=is_disliked,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            fields=fields,
            enableUserData=enable_user_data,
            sortBy=sort_by,
            sortOrder=sort_order,
            enableFavoriteSorting=enable_favorite_sorting,
            addCurrentProgram=add_current_program,
        )
        return self._get(path='/LiveTv/Channels', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_channel(
            self, 
            channel_id: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets a live tv channel.

        Http:
            <get>: /LiveTv/Channels/{channelId}

        Args:
            channel_id (str): Channel id.
            user_id (str): Optional. Attach user data.

        Returns:
            <200> BaseItemDto: Live tv channel returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            channelId=channel_id,
            userId=user_id,
        )
        return self._get(path='/LiveTv/Channels/{channelId}', request_args=request_args, response_type=BaseItemDto)

    def get_guide_info(
            self
    ) -> GuideInfo:
        """Get guid info.

        Http:
            <get>: /LiveTv/GuideInfo

        Returns:
            <200> GuideInfo: Guid info returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/LiveTv/GuideInfo', response_type=GuideInfo)

    def get_live_tv_info(
            self
    ) -> LiveTvInfo:
        """Gets available live tv services.

        Http:
            <get>: /LiveTv/Info

        Returns:
            <200> LiveTvInfo: Available live tv services returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/LiveTv/Info', response_type=LiveTvInfo)

    def add_listing_provider(
            self, 
            pw: Optional[str] = None, 
            validate_listings: Optional[bool] = False, 
            validate_login: Optional[bool] = False, 
            request_body: Optional[ListingsProviderInfo] = None
    ) -> ListingsProviderInfo:
        """Adds a listings provider.

        Http:
            <post>: /LiveTv/ListingProviders

        Args:
            pw (str): Password.
            validate_listings (bool = False): Validate listings.
            validate_login (bool = False): Validate login.
            request_body (ListingsProviderInfo): New listings info.

        Returns:
            <200> ListingsProviderInfo: Created listings provider returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pw=pw,
            validateListings=validate_listings,
            validateLogin=validate_login,
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/ListingProviders', request_args=request_args, response_type=ListingsProviderInfo)

    def delete_listing_provider(
            self, 
            id: Optional[str] = None
    ) -> requests.Response:
        """Delete listing provider.

        Http:
            <delete>: /LiveTv/ListingProviders

        Args:
            id (str): Listing provider id.

        Returns:
            <204> requests.Response: Listing provider deleted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._delete(path='/LiveTv/ListingProviders', request_args=request_args)

    def get_default_listing_provider(
            self
    ) -> ListingsProviderInfo:
        """Gets default listings provider info.

        Http:
            <get>: /LiveTv/ListingProviders/Default

        Returns:
            <200> ListingsProviderInfo: Default listings provider info returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/LiveTv/ListingProviders/Default', response_type=ListingsProviderInfo)

    def get_lineups(
            self, 
            id: Optional[str] = None, 
            type: Optional[str] = None, 
            location: Optional[str] = None, 
            country: Optional[str] = None
    ) -> List[NameIdPair]:
        """Gets available lineups.

        Http:
            <get>: /LiveTv/ListingProviders/Lineups

        Args:
            id (str): Provider id.
            type (str): Provider type.
            location (str): Location.
            country (str): Country.

        Returns:
            <200> List[NameIdPair]: Available lineups returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
            type=type,
            location=location,
            country=country,
        )
        return self._get(path='/LiveTv/ListingProviders/Lineups', request_args=request_args, response_type=List[NameIdPair])

    def get_schedules_direct_countries(
            self
    ) -> str:
        """Gets available countries.

        Http:
            <get>: /LiveTv/ListingProviders/SchedulesDirect/Countries

        Returns:
            <200> str: Available countries returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/LiveTv/ListingProviders/SchedulesDirect/Countries', response_type=str)

    def get_live_recording_file(
            self, 
            recording_id: str
    ) -> requests.Response:
        """Gets a live tv recording stream.

        Http:
            <get>: /LiveTv/LiveRecordings/{recordingId}/stream

        Args:
            recording_id (str): Recording id.

        Returns:
            <200> requests.Response: Recording stream returned.
            <404> requests.Response: Recording not found.
        """
        request_args = dict(
            recordingId=recording_id,
        )
        return self._get(path='/LiveTv/LiveRecordings/{recordingId}/stream', request_args=request_args)

    def get_live_stream_file(
            self, 
            stream_id: str, 
            container: str
    ) -> requests.Response:
        """Gets a live tv channel stream.

        Http:
            <get>: /LiveTv/LiveStreamFiles/{streamId}/stream.{container}

        Args:
            stream_id (str): Stream id.
            container (str): Container type.

        Returns:
            <200> requests.Response: Stream returned.
            <404> requests.Response: Stream not found.
        """
        request_args = dict(
            streamId=stream_id,
            container=container,
        )
        return self._get(path='/LiveTv/LiveStreamFiles/{streamId}/stream.{container}', request_args=request_args)

    def get_live_tv_programs(
            self, 
            channel_ids: Optional[List[str]] = None, 
            user_id: Optional[str] = None, 
            min_start_date: Optional[str] = None, 
            has_aired: Optional[bool] = None, 
            is_airing: Optional[bool] = None, 
            max_start_date: Optional[str] = None, 
            min_end_date: Optional[str] = None, 
            max_end_date: Optional[str] = None, 
            is_movie: Optional[bool] = None, 
            is_series: Optional[bool] = None, 
            is_news: Optional[bool] = None, 
            is_kids: Optional[bool] = None, 
            is_sports: Optional[bool] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            sort_by: Optional[List[str]] = None, 
            sort_order: Optional[List[SortOrder]] = None, 
            genres: Optional[List[str]] = None, 
            genre_ids: Optional[List[str]] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            enable_user_data: Optional[bool] = None, 
            series_timer_id: Optional[str] = None, 
            library_series_id: Optional[str] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_total_record_count: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets available live tv epgs.

        Http:
            <get>: /LiveTv/Programs

        Args:
            channel_ids (List[str]): The channels to return guide information for.
            user_id (str): Optional. Filter by user id.
            min_start_date (str): Optional. The minimum premiere start date.
            has_aired (bool): Optional. Filter by programs that have completed airing, or not.
            is_airing (bool): Optional. Filter by programs that are currently airing, or not.
            max_start_date (str): Optional. The maximum premiere start date.
            min_end_date (str): Optional. The minimum premiere end date.
            max_end_date (str): Optional. The maximum premiere end date.
            is_movie (bool): Optional. Filter for movies.
            is_series (bool): Optional. Filter for series.
            is_news (bool): Optional. Filter for news.
            is_kids (bool): Optional. Filter for kids.
            is_sports (bool): Optional. Filter for sports.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            sort_by (List[str]): Optional. Specify one or more sort orders, comma delimited. Options: Name, StartDate.
            sort_order (List[SortOrder]): Sort Order - Ascending,Descending.
            genres (List[str]): The genres to return guide information for.
            genre_ids (List[str]): The genre ids to return guide information for.
            enable_images (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            enable_user_data (bool): Optional. Include user data.
            series_timer_id (str): Optional. Filter by series timer id.
            library_series_id (str): Optional. Filter by library series id.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            enable_total_record_count (bool = True): Retrieve total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Live tv epgs returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            channelIds=channel_ids,
            userId=user_id,
            minStartDate=min_start_date,
            hasAired=has_aired,
            isAiring=is_airing,
            maxStartDate=max_start_date,
            minEndDate=min_end_date,
            maxEndDate=max_end_date,
            isMovie=is_movie,
            isSeries=is_series,
            isNews=is_news,
            isKids=is_kids,
            isSports=is_sports,
            startIndex=start_index,
            limit=limit,
            sortBy=sort_by,
            sortOrder=sort_order,
            genres=genres,
            genreIds=genre_ids,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            enableUserData=enable_user_data,
            seriesTimerId=series_timer_id,
            librarySeriesId=library_series_id,
            fields=fields,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/LiveTv/Programs', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_programs(
            self, 
            request_body: Optional[GetProgramsDto] = None
    ) -> BaseItemDtoQueryResult:
        """Gets available live tv epgs.

        Http:
            <post>: /LiveTv/Programs

        Args:
            request_body (GetProgramsDto): Request body.

        Returns:
            <200> BaseItemDtoQueryResult: Live tv epgs returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/Programs', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_program(
            self, 
            program_id: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets a live tv program.

        Http:
            <get>: /LiveTv/Programs/{programId}

        Args:
            program_id (str): Program id.
            user_id (str): Optional. Attach user data.

        Returns:
            <200> BaseItemDto: Program returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            programId=program_id,
            userId=user_id,
        )
        return self._get(path='/LiveTv/Programs/{programId}', request_args=request_args, response_type=BaseItemDto)

    def get_recommended_programs(
            self, 
            user_id: Optional[str] = None, 
            limit: Optional[int] = None, 
            is_airing: Optional[bool] = None, 
            has_aired: Optional[bool] = None, 
            is_series: Optional[bool] = None, 
            is_movie: Optional[bool] = None, 
            is_news: Optional[bool] = None, 
            is_kids: Optional[bool] = None, 
            is_sports: Optional[bool] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            genre_ids: Optional[List[str]] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_user_data: Optional[bool] = None, 
            enable_total_record_count: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets recommended live tv epgs.

        Http:
            <get>: /LiveTv/Programs/Recommended

        Args:
            user_id (str): Optional. filter by user id.
            limit (int): Optional. The maximum number of records to return.
            is_airing (bool): Optional. Filter by programs that are currently airing, or not.
            has_aired (bool): Optional. Filter by programs that have completed airing, or not.
            is_series (bool): Optional. Filter for series.
            is_movie (bool): Optional. Filter for movies.
            is_news (bool): Optional. Filter for news.
            is_kids (bool): Optional. Filter for kids.
            is_sports (bool): Optional. Filter for sports.
            enable_images (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            genre_ids (List[str]): The genres to return guide information for.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            enable_user_data (bool): Optional. include user data.
            enable_total_record_count (bool = True): Retrieve total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Recommended epgs returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            limit=limit,
            isAiring=is_airing,
            hasAired=has_aired,
            isSeries=is_series,
            isMovie=is_movie,
            isNews=is_news,
            isKids=is_kids,
            isSports=is_sports,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            genreIds=genre_ids,
            fields=fields,
            enableUserData=enable_user_data,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/LiveTv/Programs/Recommended', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_recordings(
            self, 
            channel_id: Optional[str] = None, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            status: Optional[RecordingStatus] = None, 
            is_in_progress: Optional[bool] = None, 
            series_timer_id: Optional[str] = None, 
            enable_images: Optional[bool] = None, 
            image_type_limit: Optional[int] = None, 
            enable_image_types: Optional[List[ImageType]] = None, 
            fields: Optional[List[ItemFields]] = None, 
            enable_user_data: Optional[bool] = None, 
            is_movie: Optional[bool] = None, 
            is_series: Optional[bool] = None, 
            is_kids: Optional[bool] = None, 
            is_sports: Optional[bool] = None, 
            is_news: Optional[bool] = None, 
            is_library_item: Optional[bool] = None, 
            enable_total_record_count: Optional[bool] = True
    ) -> BaseItemDtoQueryResult:
        """Gets live tv recordings.

        Http:
            <get>: /LiveTv/Recordings

        Args:
            channel_id (str): Optional. Filter by channel id.
            user_id (str): Optional. Filter by user and attach user data.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            status (RecordingStatus): Optional. Filter by recording status.
            is_in_progress (bool): Optional. Filter by recordings that are in progress, or not.
            series_timer_id (str): Optional. Filter by recordings belonging to a series timer.
            enable_images (bool): Optional. Include image information in output.
            image_type_limit (int): Optional. The max number of images to return, per image type.
            enable_image_types (List[ImageType]): Optional. The image types to include in the output.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            enable_user_data (bool): Optional. Include user data.
            is_movie (bool): Optional. Filter for movies.
            is_series (bool): Optional. Filter for series.
            is_kids (bool): Optional. Filter for kids.
            is_sports (bool): Optional. Filter for sports.
            is_news (bool): Optional. Filter for news.
            is_library_item (bool): Optional. Filter for is library item.
            enable_total_record_count (bool = True): Optional. Return total record count.

        Returns:
            <200> BaseItemDtoQueryResult: Live tv recordings returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            channelId=channel_id,
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            status=status,
            isInProgress=is_in_progress,
            seriesTimerId=series_timer_id,
            enableImages=enable_images,
            imageTypeLimit=image_type_limit,
            enableImageTypes=enable_image_types,
            fields=fields,
            enableUserData=enable_user_data,
            isMovie=is_movie,
            isSeries=is_series,
            isKids=is_kids,
            isSports=is_sports,
            isNews=is_news,
            isLibraryItem=is_library_item,
            enableTotalRecordCount=enable_total_record_count,
        )
        return self._get(path='/LiveTv/Recordings', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_recording(
            self, 
            recording_id: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDto:
        """Gets a live tv recording.

        Http:
            <get>: /LiveTv/Recordings/{recordingId}

        Args:
            recording_id (str): Recording id.
            user_id (str): Optional. Attach user data.

        Returns:
            <200> BaseItemDto: Recording returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            recordingId=recording_id,
            userId=user_id,
        )
        return self._get(path='/LiveTv/Recordings/{recordingId}', request_args=request_args, response_type=BaseItemDto)

    def delete_recording(
            self, 
            recording_id: str
    ) -> requests.Response:
        """Deletes a live tv recording.

        Http:
            <delete>: /LiveTv/Recordings/{recordingId}

        Args:
            recording_id (str): Recording id.

        Returns:
            <204> requests.Response: Recording deleted.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            recordingId=recording_id,
        )
        return self._delete(path='/LiveTv/Recordings/{recordingId}', request_args=request_args)

    def get_recording_folders(
            self, 
            user_id: Optional[str] = None
    ) -> BaseItemDtoQueryResult:
        """Gets recording folders.

        Http:
            <get>: /LiveTv/Recordings/Folders

        Args:
            user_id (str): Optional. Filter by user and attach user data.

        Returns:
            <200> BaseItemDtoQueryResult: Recording folders returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/LiveTv/Recordings/Folders', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_series_timers(
            self, 
            sort_by: Optional[str] = None, 
            sort_order: Optional[SortOrder] = None
    ) -> SeriesTimerInfoDtoQueryResult:
        """Gets live tv series timers.

        Http:
            <get>: /LiveTv/SeriesTimers

        Args:
            sort_by (str): Optional. Sort by SortName or Priority.
            sort_order (SortOrder): Optional. Sort in Ascending or Descending order.

        Returns:
            <200> SeriesTimerInfoDtoQueryResult: Timers returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sortBy=sort_by,
            sortOrder=sort_order,
        )
        return self._get(path='/LiveTv/SeriesTimers', request_args=request_args, response_type=SeriesTimerInfoDtoQueryResult)

    def create_series_timer(
            self, 
            request_body: Optional[SeriesTimerInfoDto] = None
    ) -> requests.Response:
        """Creates a live tv series timer.

        Http:
            <post>: /LiveTv/SeriesTimers

        Args:
            request_body (SeriesTimerInfoDto): New series timer info.

        Returns:
            <204> requests.Response: Series timer info created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/SeriesTimers', request_args=request_args)

    def get_series_timer(
            self, 
            timer_id: str
    ) -> SeriesTimerInfoDto:
        """Gets a live tv series timer.

        Http:
            <get>: /LiveTv/SeriesTimers/{timerId}

        Args:
            timer_id (str): Timer id.

        Returns:
            <200> SeriesTimerInfoDto: Series timer returned.
            <404> requests.Response: Series timer not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            timerId=timer_id,
        )
        return self._get(path='/LiveTv/SeriesTimers/{timerId}', request_args=request_args, response_type=SeriesTimerInfoDto)

    def cancel_series_timer(
            self, 
            timer_id: str
    ) -> requests.Response:
        """Cancels a live tv series timer.

        Http:
            <delete>: /LiveTv/SeriesTimers/{timerId}

        Args:
            timer_id (str): Timer id.

        Returns:
            <204> requests.Response: Timer cancelled.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            timerId=timer_id,
        )
        return self._delete(path='/LiveTv/SeriesTimers/{timerId}', request_args=request_args)

    def update_series_timer(
            self, 
            timer_id: str, 
            request_body: Optional[SeriesTimerInfoDto] = None
    ) -> requests.Response:
        """Updates a live tv series timer.

        Http:
            <post>: /LiveTv/SeriesTimers/{timerId}

        Args:
            timer_id (str): Timer id.
            request_body (SeriesTimerInfoDto): New series timer info.

        Returns:
            <204> requests.Response: Series timer updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            timerId=timer_id,
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/SeriesTimers/{timerId}', request_args=request_args)

    def get_timers(
            self, 
            channel_id: Optional[str] = None, 
            series_timer_id: Optional[str] = None, 
            is_active: Optional[bool] = None, 
            is_scheduled: Optional[bool] = None
    ) -> TimerInfoDtoQueryResult:
        """Gets the live tv timers.

        Http:
            <get>: /LiveTv/Timers

        Args:
            channel_id (str): Optional. Filter by channel id.
            series_timer_id (str): Optional. Filter by timers belonging to a series timer.
            is_active (bool): Optional. Filter by timers that are active.
            is_scheduled (bool): Optional. Filter by timers that are scheduled.

        Returns:
            <200> TimerInfoDtoQueryResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            channelId=channel_id,
            seriesTimerId=series_timer_id,
            isActive=is_active,
            isScheduled=is_scheduled,
        )
        return self._get(path='/LiveTv/Timers', request_args=request_args, response_type=TimerInfoDtoQueryResult)

    def create_timer(
            self, 
            request_body: Optional[TimerInfoDto] = None
    ) -> requests.Response:
        """Creates a live tv timer.

        Http:
            <post>: /LiveTv/Timers

        Args:
            request_body (TimerInfoDto): New timer info.

        Returns:
            <204> requests.Response: Timer created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/Timers', request_args=request_args)

    def get_timer(
            self, 
            timer_id: str
    ) -> TimerInfoDto:
        """Gets a timer.

        Http:
            <get>: /LiveTv/Timers/{timerId}

        Args:
            timer_id (str): Timer id.

        Returns:
            <200> TimerInfoDto: Timer returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            timerId=timer_id,
        )
        return self._get(path='/LiveTv/Timers/{timerId}', request_args=request_args, response_type=TimerInfoDto)

    def cancel_timer(
            self, 
            timer_id: str
    ) -> requests.Response:
        """Cancels a live tv timer.

        Http:
            <delete>: /LiveTv/Timers/{timerId}

        Args:
            timer_id (str): Timer id.

        Returns:
            <204> requests.Response: Timer deleted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            timerId=timer_id,
        )
        return self._delete(path='/LiveTv/Timers/{timerId}', request_args=request_args)

    def update_timer(
            self, 
            timer_id: str, 
            request_body: Optional[TimerInfoDto] = None
    ) -> requests.Response:
        """Updates a live tv timer.

        Http:
            <post>: /LiveTv/Timers/{timerId}

        Args:
            timer_id (str): Timer id.
            request_body (TimerInfoDto): New timer info.

        Returns:
            <204> requests.Response: Timer updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            timerId=timer_id,
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/Timers/{timerId}', request_args=request_args)

    def get_default_timer(
            self, 
            program_id: Optional[str] = None
    ) -> SeriesTimerInfoDto:
        """Gets the default values for a new timer.

        Http:
            <get>: /LiveTv/Timers/Defaults

        Args:
            program_id (str): Optional. To attach default values based on a program.

        Returns:
            <200> SeriesTimerInfoDto: Default values returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            programId=program_id,
        )
        return self._get(path='/LiveTv/Timers/Defaults', request_args=request_args, response_type=SeriesTimerInfoDto)

    def add_tuner_host(
            self, 
            request_body: Optional[TunerHostInfo] = None
    ) -> TunerHostInfo:
        """Adds a tuner host.

        Http:
            <post>: /LiveTv/TunerHosts

        Args:
            request_body (TunerHostInfo): New tuner host.

        Returns:
            <200> TunerHostInfo: Created tuner host returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/LiveTv/TunerHosts', request_args=request_args, response_type=TunerHostInfo)

    def delete_tuner_host(
            self, 
            id: Optional[str] = None
    ) -> requests.Response:
        """Deletes a tuner host.

        Http:
            <delete>: /LiveTv/TunerHosts

        Args:
            id (str): Tuner host id.

        Returns:
            <204> requests.Response: Tuner host deleted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._delete(path='/LiveTv/TunerHosts', request_args=request_args)

    def get_tuner_host_types(
            self
    ) -> List[NameIdPair]:
        """Get tuner host types.

        Http:
            <get>: /LiveTv/TunerHosts/Types

        Returns:
            <200> List[NameIdPair]: Tuner host types returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/LiveTv/TunerHosts/Types', response_type=List[NameIdPair])

    def reset_tuner(
            self, 
            tuner_id: str
    ) -> requests.Response:
        """Resets a tv tuner.

        Http:
            <post>: /LiveTv/Tuners/{tunerId}/Reset

        Args:
            tuner_id (str): Tuner id.

        Returns:
            <204> requests.Response: Tuner reset.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            tunerId=tuner_id,
        )
        return self._post(path='/LiveTv/Tuners/{tunerId}/Reset', request_args=request_args)

    def discover_tuners(
            self, 
            new_devices_only: Optional[bool] = False
    ) -> List[TunerHostInfo]:
        """Discover tuners.

        Http:
            <get>: /LiveTv/Tuners/Discover

        Args:
            new_devices_only (bool = False): Only discover new tuners.

        Returns:
            <200> List[TunerHostInfo]: Tuners returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            newDevicesOnly=new_devices_only,
        )
        return self._get(path='/LiveTv/Tuners/Discover', request_args=request_args, response_type=List[TunerHostInfo])

    def discvover_tuners(
            self, 
            new_devices_only: Optional[bool] = False
    ) -> List[TunerHostInfo]:
        """Discover tuners.

        Http:
            <get>: /LiveTv/Tuners/Discvover

        Args:
            new_devices_only (bool = False): Only discover new tuners.

        Returns:
            <200> List[TunerHostInfo]: Tuners returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            newDevicesOnly=new_devices_only,
        )
        return self._get(path='/LiveTv/Tuners/Discvover', request_args=request_args, response_type=List[TunerHostInfo])

