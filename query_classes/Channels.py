from typing import List
from typing import Optional

from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.channel_features import ChannelFeatures as ChannelFeatures
from data_classes.item_fields import ItemFields as ItemFields
from data_classes.item_filter import ItemFilter as ItemFilter
from data_classes.sort_order import SortOrder as SortOrder
from util.BaseRequestClass import BaseRequestClass


class Channels(BaseRequestClass):
    def get_channels(
            self, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            supports_latest_items: Optional[bool] = None, 
            supports_media_deletion: Optional[bool] = None, 
            is_favorite: Optional[bool] = None
    ) -> BaseItemDtoQueryResult:
        """Gets available channels.

        Http:
            <get>: /Channels

        Args:
            user_id (str): User Id to filter by. Use System.Guid.Empty to not filter by user.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            supports_latest_items (bool): Optional. Filter by channels that support getting latest items.
            supports_media_deletion (bool): Optional. Filter by channels that support media deletion.
            is_favorite (bool): Optional. Filter by channels that are favorite.

        Returns:
            <200> BaseItemDtoQueryResult: Channels returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            supportsLatestItems=supports_latest_items,
            supportsMediaDeletion=supports_media_deletion,
            isFavorite=is_favorite,
        )
        return self._get(path='/Channels', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_channel_features(
            self, 
            channel_id: str
    ) -> ChannelFeatures:
        """Get channel features.

        Http:
            <get>: /Channels/{channelId}/Features

        Args:
            channel_id (str): Channel id.

        Returns:
            <200> ChannelFeatures: Channel features returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            channelId=channel_id,
        )
        return self._get(path='/Channels/{channelId}/Features', request_args=request_args, response_type=ChannelFeatures)

    def get_channel_items(
            self, 
            channel_id: str, 
            folder_id: Optional[str] = None, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            sort_order: Optional[List[SortOrder]] = None, 
            filters: Optional[List[ItemFilter]] = None, 
            sort_by: Optional[List[str]] = None, 
            fields: Optional[List[ItemFields]] = None
    ) -> BaseItemDtoQueryResult:
        """Get channel items.

        Http:
            <get>: /Channels/{channelId}/Items

        Args:
            channel_id (str): Channel Id.
            folder_id (str): Optional. Folder Id.
            user_id (str): Optional. User Id.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            sort_order (List[SortOrder]): Optional. Sort Order - Ascending,Descending.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply.
            sort_by (List[str]): Optional. Specify one or more sort orders, comma delimited. Options: Album, AlbumArtist, Artist, Budget, CommunityRating, CriticRating, DateCreated, DatePlayed, PlayCount, PremiereDate, ProductionYear, SortName, Random, Revenue, Runtime.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.

        Returns:
            <200> BaseItemDtoQueryResult: Channel items returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            channelId=channel_id,
            folderId=folder_id,
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            sortOrder=sort_order,
            filters=filters,
            sortBy=sort_by,
            fields=fields,
        )
        return self._get(path='/Channels/{channelId}/Items', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def get_all_channel_features(
            self
    ) -> List[ChannelFeatures]:
        """Get all channel features.

        Http:
            <get>: /Channels/Features

        Returns:
            <200> List[ChannelFeatures]: All channel features returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Channels/Features', response_type=List[ChannelFeatures])

    def get_latest_channel_items(
            self, 
            user_id: Optional[str] = None, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            filters: Optional[List[ItemFilter]] = None, 
            fields: Optional[List[ItemFields]] = None, 
            channel_ids: Optional[List[str]] = None
    ) -> BaseItemDtoQueryResult:
        """Gets latest channel items.

        Http:
            <get>: /Channels/Items/Latest

        Args:
            user_id (str): Optional. User Id.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            filters (List[ItemFilter]): Optional. Specify additional filters to apply.
            fields (List[ItemFields]): Optional. Specify additional fields of information to return in the output.
            channel_ids (List[str]): Optional. Specify one or more channel id's, comma delimited.

        Returns:
            <200> BaseItemDtoQueryResult: Latest channel items returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            startIndex=start_index,
            limit=limit,
            filters=filters,
            fields=fields,
            channelIds=channel_ids,
        )
        return self._get(path='/Channels/Items/Latest', request_args=request_args, response_type=BaseItemDtoQueryResult)

