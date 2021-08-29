import requests
from util.BaseRequestClass import BaseRequestClass
from typing import List
from data_classes.set_shuffle_mode_request_dto import SetShuffleModeRequestDto as SetShuffleModeRequestDto
from data_classes.set_repeat_mode_request_dto import SetRepeatModeRequestDto as SetRepeatModeRequestDto
from data_classes.set_playlist_item_request_dto import SetPlaylistItemRequestDto as SetPlaylistItemRequestDto
from data_classes.seek_request_dto import SeekRequestDto as SeekRequestDto
from data_classes.remove_from_playlist_request_dto import RemoveFromPlaylistRequestDto as RemoveFromPlaylistRequestDto
from data_classes.ready_request_dto import ReadyRequestDto as ReadyRequestDto
from data_classes.queue_request_dto import QueueRequestDto as QueueRequestDto
from data_classes.previous_item_request_dto import PreviousItemRequestDto as PreviousItemRequestDto
from data_classes.play_request_dto import PlayRequestDto as PlayRequestDto
from data_classes.ping_request_dto import PingRequestDto as PingRequestDto
from data_classes.next_item_request_dto import NextItemRequestDto as NextItemRequestDto
from data_classes.new_group_request_dto import NewGroupRequestDto as NewGroupRequestDto
from data_classes.move_playlist_item_request_dto import MovePlaylistItemRequestDto as MovePlaylistItemRequestDto
from data_classes.join_group_request_dto import JoinGroupRequestDto as JoinGroupRequestDto
from data_classes.ignore_wait_request_dto import IgnoreWaitRequestDto as IgnoreWaitRequestDto
from data_classes.group_info_dto import GroupInfoDto as GroupInfoDto
from data_classes.buffer_request_dto import BufferRequestDto as BufferRequestDto


class SyncPlay(BaseRequestClass):
    def sync_play_buffering(
            self, 
            request_body: BufferRequestDto
    ) -> requests.Response:
        """Notify SyncPlay group that member is buffering.

        Http:
            <post>: /SyncPlay/Buffering

        Args:
            request_body (BufferRequestDto): The player status.

        Returns:
            <204> requests.Response: Group state update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/Buffering', request_args=request_args)

    def sync_play_join_group(
            self, 
            request_body: JoinGroupRequestDto
    ) -> requests.Response:
        """Join an existing SyncPlay group.

        Http:
            <post>: /SyncPlay/Join

        Args:
            request_body (JoinGroupRequestDto): The group to join.

        Returns:
            <204> requests.Response: Group join successful.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/Join', request_args=request_args)

    def sync_play_leave_group(
            self
    ) -> requests.Response:
        """Leave the joined SyncPlay group.

        Http:
            <post>: /SyncPlay/Leave

        Returns:
            <204> requests.Response: Group leave successful.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/SyncPlay/Leave')

    def sync_play_get_groups(
            self
    ) -> List[GroupInfoDto]:
        """Gets all SyncPlay groups.

        Http:
            <get>: /SyncPlay/List

        Returns:
            <200> List[GroupInfoDto]: Groups returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/SyncPlay/List', response_type=List[GroupInfoDto])

    def sync_play_move_playlist_item(
            self, 
            request_body: MovePlaylistItemRequestDto
    ) -> requests.Response:
        """Request to move an item in the playlist in SyncPlay group.

        Http:
            <post>: /SyncPlay/MovePlaylistItem

        Args:
            request_body (MovePlaylistItemRequestDto): The new position for the item.

        Returns:
            <204> requests.Response: Queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/MovePlaylistItem', request_args=request_args)

    def sync_play_create_group(
            self, 
            request_body: NewGroupRequestDto
    ) -> requests.Response:
        """Create a new SyncPlay group.

        Http:
            <post>: /SyncPlay/New

        Args:
            request_body (NewGroupRequestDto): The settings of the new group.

        Returns:
            <204> requests.Response: New group created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/New', request_args=request_args)

    def sync_play_next_item(
            self, 
            request_body: NextItemRequestDto
    ) -> requests.Response:
        """Request next item in SyncPlay group.

        Http:
            <post>: /SyncPlay/NextItem

        Args:
            request_body (NextItemRequestDto): The current item information.

        Returns:
            <204> requests.Response: Next item update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/NextItem', request_args=request_args)

    def sync_play_pause(
            self
    ) -> requests.Response:
        """Request pause in SyncPlay group.

        Http:
            <post>: /SyncPlay/Pause

        Returns:
            <204> requests.Response: Pause update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/SyncPlay/Pause')

    def sync_play_ping(
            self, 
            request_body: PingRequestDto
    ) -> requests.Response:
        """Update session ping.

        Http:
            <post>: /SyncPlay/Ping

        Args:
            request_body (PingRequestDto): The new ping.

        Returns:
            <204> requests.Response: Ping updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/Ping', request_args=request_args)

    def sync_play_previous_item(
            self, 
            request_body: PreviousItemRequestDto
    ) -> requests.Response:
        """Request previous item in SyncPlay group.

        Http:
            <post>: /SyncPlay/PreviousItem

        Args:
            request_body (PreviousItemRequestDto): The current item information.

        Returns:
            <204> requests.Response: Previous item update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/PreviousItem', request_args=request_args)

    def sync_play_queue(
            self, 
            request_body: QueueRequestDto
    ) -> requests.Response:
        """Request to queue items to the playlist of a SyncPlay group.

        Http:
            <post>: /SyncPlay/Queue

        Args:
            request_body (QueueRequestDto): The items to add.

        Returns:
            <204> requests.Response: Queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/Queue', request_args=request_args)

    def sync_play_ready(
            self, 
            request_body: ReadyRequestDto
    ) -> requests.Response:
        """Notify SyncPlay group that member is ready for playback.

        Http:
            <post>: /SyncPlay/Ready

        Args:
            request_body (ReadyRequestDto): The player status.

        Returns:
            <204> requests.Response: Group state update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/Ready', request_args=request_args)

    def sync_play_remove_from_playlist(
            self, 
            request_body: RemoveFromPlaylistRequestDto
    ) -> requests.Response:
        """Request to remove items from the playlist in SyncPlay group.

        Http:
            <post>: /SyncPlay/RemoveFromPlaylist

        Args:
            request_body (RemoveFromPlaylistRequestDto): The items to remove.

        Returns:
            <204> requests.Response: Queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/RemoveFromPlaylist', request_args=request_args)

    def sync_play_seek(
            self, 
            request_body: SeekRequestDto
    ) -> requests.Response:
        """Request seek in SyncPlay group.

        Http:
            <post>: /SyncPlay/Seek

        Args:
            request_body (SeekRequestDto): The new playback position.

        Returns:
            <204> requests.Response: Seek update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/Seek', request_args=request_args)

    def sync_play_set_ignore_wait(
            self, 
            request_body: IgnoreWaitRequestDto
    ) -> requests.Response:
        """Request SyncPlay group to ignore member during group-wait.

        Http:
            <post>: /SyncPlay/SetIgnoreWait

        Args:
            request_body (IgnoreWaitRequestDto): The settings to set.

        Returns:
            <204> requests.Response: Member state updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/SetIgnoreWait', request_args=request_args)

    def sync_play_set_new_queue(
            self, 
            request_body: PlayRequestDto
    ) -> requests.Response:
        """Request to set new playlist in SyncPlay group.

        Http:
            <post>: /SyncPlay/SetNewQueue

        Args:
            request_body (PlayRequestDto): The new playlist to play in the group.

        Returns:
            <204> requests.Response: Queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/SetNewQueue', request_args=request_args)

    def sync_play_set_playlist_item(
            self, 
            request_body: SetPlaylistItemRequestDto
    ) -> requests.Response:
        """Request to change playlist item in SyncPlay group.

        Http:
            <post>: /SyncPlay/SetPlaylistItem

        Args:
            request_body (SetPlaylistItemRequestDto): The new item to play.

        Returns:
            <204> requests.Response: Queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/SetPlaylistItem', request_args=request_args)

    def sync_play_set_repeat_mode(
            self, 
            request_body: SetRepeatModeRequestDto
    ) -> requests.Response:
        """Request to set repeat mode in SyncPlay group.

        Http:
            <post>: /SyncPlay/SetRepeatMode

        Args:
            request_body (SetRepeatModeRequestDto): The new repeat mode.

        Returns:
            <204> requests.Response: Play queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/SetRepeatMode', request_args=request_args)

    def sync_play_set_shuffle_mode(
            self, 
            request_body: SetShuffleModeRequestDto
    ) -> requests.Response:
        """Request to set shuffle mode in SyncPlay group.

        Http:
            <post>: /SyncPlay/SetShuffleMode

        Args:
            request_body (SetShuffleModeRequestDto): The new shuffle mode.

        Returns:
            <204> requests.Response: Play queue update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/SyncPlay/SetShuffleMode', request_args=request_args)

    def sync_play_stop(
            self
    ) -> requests.Response:
        """Request stop in SyncPlay group.

        Http:
            <post>: /SyncPlay/Stop

        Returns:
            <204> requests.Response: Stop update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/SyncPlay/Stop')

    def sync_play_unpause(
            self
    ) -> requests.Response:
        """Request unpause in SyncPlay group.

        Http:
            <post>: /SyncPlay/Unpause

        Returns:
            <204> requests.Response: Unpause update sent to all group members.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/SyncPlay/Unpause')

