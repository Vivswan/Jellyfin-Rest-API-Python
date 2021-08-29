import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.session_info import SessionInfo as SessionInfo
from data_classes.playstate_command_enum import PlaystateCommandEnum as PlaystateCommand
from data_classes.playback_stop_info import PlaybackStopInfo as PlaybackStopInfo
from data_classes.playback_start_info import PlaybackStartInfo as PlaybackStartInfo
from data_classes.playback_progress_info import PlaybackProgressInfo as PlaybackProgressInfo
from data_classes.play_command import PlayCommand as PlayCommand
from data_classes.message_command import MessageCommand as MessageCommand
from data_classes.general_command_type import GeneralCommandType as GeneralCommandType
from data_classes.general_command import GeneralCommand as GeneralCommand
from data_classes.client_capabilities_dto import ClientCapabilitiesDto as ClientCapabilitiesDto


class Sessions(BaseRequestClass):
    def report_playback_start(
            self, 
            request_body: Optional[PlaybackStartInfo] = None
    ) -> requests.Response:
        """Reports playback has started within a session.

        Http:
            <post>: /Sessions/Playing

        Args:
            request_body (PlaybackStartInfo): The playback start info.

        Returns:
            <204> requests.Response: Playback start recorded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Sessions/Playing', request_args=request_args)

    def ping_playback_session(
            self, 
            play_session_id: str
    ) -> requests.Response:
        """Pings a playback session.

        Http:
            <post>: /Sessions/Playing/Ping

        Args:
            play_session_id (str): Playback session id.

        Returns:
            <204> requests.Response: Playback session pinged.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            playSessionId=play_session_id,
        )
        return self._post(path='/Sessions/Playing/Ping', request_args=request_args)

    def report_playback_progress(
            self, 
            request_body: Optional[PlaybackProgressInfo] = None
    ) -> requests.Response:
        """Reports playback progress within a session.

        Http:
            <post>: /Sessions/Playing/Progress

        Args:
            request_body (PlaybackProgressInfo): The playback progress info.

        Returns:
            <204> requests.Response: Playback progress recorded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Sessions/Playing/Progress', request_args=request_args)

    def report_playback_stopped(
            self, 
            request_body: Optional[PlaybackStopInfo] = None
    ) -> requests.Response:
        """Reports playback has stopped within a session.

        Http:
            <post>: /Sessions/Playing/Stopped

        Args:
            request_body (PlaybackStopInfo): The playback stop info.

        Returns:
            <204> requests.Response: Playback stop recorded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Sessions/Playing/Stopped', request_args=request_args)

    def get_sessions(
            self, 
            controllable_by_user_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            active_within_seconds: Optional[int] = None
    ) -> List[SessionInfo]:
        """Gets a list of sessions.

        Http:
            <get>: /Sessions

        Args:
            controllable_by_user_id (str): Filter by sessions that a given user is allowed to remote control.
            device_id (str): Filter by device Id.
            active_within_seconds (int): Optional. Filter by sessions that were active in the last n seconds.

        Returns:
            <200> List[SessionInfo]: List of sessions returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            controllableByUserId=controllable_by_user_id,
            deviceId=device_id,
            activeWithinSeconds=active_within_seconds,
        )
        return self._get(path='/Sessions', request_args=request_args, response_type=List[SessionInfo])

    def send_full_general_command(
            self, 
            session_id: str, 
            request_body: GeneralCommand
    ) -> requests.Response:
        """Issues a full general command to a client.

        Http:
            <post>: /Sessions/{sessionId}/Command

        Args:
            session_id (str): The session id.
            request_body (GeneralCommand): The MediaBrowser.Model.Session.GeneralCommand.

        Returns:
            <204> requests.Response: Full general command sent to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            requestBody=request_body,
        )
        return self._post(path='/Sessions/{sessionId}/Command', request_args=request_args)

    def send_general_command(
            self, 
            session_id: str, 
            command: GeneralCommandType
    ) -> requests.Response:
        """Issues a general command to a client.

        Http:
            <post>: /Sessions/{sessionId}/Command/{command}

        Args:
            session_id (str): The session id.
            command (GeneralCommandType): The command to send.

        Returns:
            <204> requests.Response: General command sent to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            command=command,
        )
        return self._post(path='/Sessions/{sessionId}/Command/{command}', request_args=request_args)

    def send_message_command(
            self, 
            session_id: str, 
            request_body: MessageCommand
    ) -> requests.Response:
        """Issues a command to a client to display a message to the user.

        Http:
            <post>: /Sessions/{sessionId}/Message

        Args:
            session_id (str): The session id.
            request_body (MessageCommand): The MediaBrowser.Model.Session.MessageCommand object containing Header, Message Text, and TimeoutMs.

        Returns:
            <204> requests.Response: Message sent.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            requestBody=request_body,
        )
        return self._post(path='/Sessions/{sessionId}/Message', request_args=request_args)

    def play(
            self, 
            session_id: str, 
            play_command: PlayCommand, 
            item_ids: List[str], 
            start_position_ticks: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            start_index: Optional[int] = None
    ) -> requests.Response:
        """Instructs a session to play an item.

        Http:
            <post>: /Sessions/{sessionId}/Playing

        Args:
            session_id (str): The session id.
            play_command (PlayCommand): The type of play command to issue (PlayNow, PlayNext, PlayLast). Clients who have not yet implemented play next and play last may play now.
            item_ids (List[str]): The ids of the items to play, comma delimited.
            start_position_ticks (int): The starting position of the first item.
            media_source_id (str): Optional. The media source id.
            audio_stream_index (int): Optional. The index of the audio stream to play.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to play.
            start_index (int): Optional. The start index.

        Returns:
            <204> requests.Response: Instruction sent to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            playCommand=play_command,
            itemIds=item_ids,
            startPositionTicks=start_position_ticks,
            mediaSourceId=media_source_id,
            audioStreamIndex=audio_stream_index,
            subtitleStreamIndex=subtitle_stream_index,
            startIndex=start_index,
        )
        return self._post(path='/Sessions/{sessionId}/Playing', request_args=request_args)

    def send_playstate_command(
            self, 
            session_id: str, 
            command: PlaystateCommand, 
            seek_position_ticks: Optional[int] = None, 
            controlling_user_id: Optional[str] = None
    ) -> requests.Response:
        """Issues a playstate command to a client.

        Http:
            <post>: /Sessions/{sessionId}/Playing/{command}

        Args:
            session_id (str): The session id.
            command (PlaystateCommand): The MediaBrowser.Model.Session.PlaystateCommand.
            seek_position_ticks (int): The optional position ticks.
            controlling_user_id (str): The optional controlling user id.

        Returns:
            <204> requests.Response: Playstate command sent to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            command=command,
            seekPositionTicks=seek_position_ticks,
            controllingUserId=controlling_user_id,
        )
        return self._post(path='/Sessions/{sessionId}/Playing/{command}', request_args=request_args)

    def send_system_command(
            self, 
            session_id: str, 
            command: GeneralCommandType
    ) -> requests.Response:
        """Issues a system command to a client.

        Http:
            <post>: /Sessions/{sessionId}/System/{command}

        Args:
            session_id (str): The session id.
            command (GeneralCommandType): The command to send.

        Returns:
            <204> requests.Response: System command sent to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            command=command,
        )
        return self._post(path='/Sessions/{sessionId}/System/{command}', request_args=request_args)

    def add_user_to_session(
            self, 
            session_id: str, 
            user_id: str
    ) -> requests.Response:
        """Adds an additional user to a session.

        Http:
            <post>: /Sessions/{sessionId}/User/{userId}

        Args:
            session_id (str): The session id.
            user_id (str): The user id.

        Returns:
            <204> requests.Response: User added to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            userId=user_id,
        )
        return self._post(path='/Sessions/{sessionId}/User/{userId}', request_args=request_args)

    def remove_user_from_session(
            self, 
            session_id: str, 
            user_id: str
    ) -> requests.Response:
        """Removes an additional user from a session.

        Http:
            <delete>: /Sessions/{sessionId}/User/{userId}

        Args:
            session_id (str): The session id.
            user_id (str): The user id.

        Returns:
            <204> requests.Response: User removed from session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            userId=user_id,
        )
        return self._delete(path='/Sessions/{sessionId}/User/{userId}', request_args=request_args)

    def display_content(
            self, 
            session_id: str, 
            item_type: str, 
            item_id: str, 
            item_name: str
    ) -> requests.Response:
        """Instructs a session to browse to an item or view.

        Http:
            <post>: /Sessions/{sessionId}/Viewing

        Args:
            session_id (str): The session Id.
            item_type (str): The type of item to browse to.
            item_id (str): The Id of the item.
            item_name (str): The name of the item.

        Returns:
            <204> requests.Response: Instruction sent to session.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            sessionId=session_id,
            itemType=item_type,
            itemId=item_id,
            itemName=item_name,
        )
        return self._post(path='/Sessions/{sessionId}/Viewing', request_args=request_args)

    def post_capabilities(
            self, 
            id: Optional[str] = None, 
            playable_media_types: Optional[List[str]] = None, 
            supported_commands: Optional[List[GeneralCommandType]] = None, 
            supports_media_control: Optional[bool] = False, 
            supports_sync: Optional[bool] = False, 
            supports_persistent_identifier: Optional[bool] = True
    ) -> requests.Response:
        """Updates capabilities for a device.

        Http:
            <post>: /Sessions/Capabilities

        Args:
            id (str): The session id.
            playable_media_types (List[str]): A list of playable media types, comma delimited. Audio, Video, Book, Photo.
            supported_commands (List[GeneralCommandType]): A list of supported remote control commands, comma delimited.
            supports_media_control (bool = False): Determines whether media can be played remotely..
            supports_sync (bool = False): Determines whether sync is supported.
            supports_persistent_identifier (bool = True): Determines whether the device supports a unique identifier.

        Returns:
            <204> requests.Response: Capabilities posted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
            playableMediaTypes=playable_media_types,
            supportedCommands=supported_commands,
            supportsMediaControl=supports_media_control,
            supportsSync=supports_sync,
            supportsPersistentIdentifier=supports_persistent_identifier,
        )
        return self._post(path='/Sessions/Capabilities', request_args=request_args)

    def post_full_capabilities(
            self, 
            request_body: ClientCapabilitiesDto, 
            id: Optional[str] = None
    ) -> requests.Response:
        """Updates capabilities for a device.

        Http:
            <post>: /Sessions/Capabilities/Full

        Args:
            request_body (ClientCapabilitiesDto): The MediaBrowser.Model.Session.ClientCapabilities.
            id (str): The session id.

        Returns:
            <204> requests.Response: Capabilities updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
            id=id,
        )
        return self._post(path='/Sessions/Capabilities/Full', request_args=request_args)

    def report_session_ended(
            self
    ) -> requests.Response:
        """Reports that a session has ended.

        Http:
            <post>: /Sessions/Logout

        Returns:
            <204> requests.Response: Session end reported to server.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/Sessions/Logout')

    def report_viewing(
            self, 
            item_id: str, 
            session_id: Optional[str] = None
    ) -> requests.Response:
        """Reports that a session is viewing an item.

        Http:
            <post>: /Sessions/Viewing

        Args:
            item_id (str): The item id.
            session_id (str): The session id.

        Returns:
            <204> requests.Response: Session reported to server.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            sessionId=session_id,
        )
        return self._post(path='/Sessions/Viewing', request_args=request_args)

