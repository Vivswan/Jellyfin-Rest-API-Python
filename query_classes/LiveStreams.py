from typing import Optional

import requests

from data_classes.live_stream_response import LiveStreamResponse as LiveStreamResponse
from data_classes.open_live_stream_dto import OpenLiveStreamDto as OpenLiveStreamDto
from util.BaseRequestClass import BaseRequestClass


class LiveStreams(BaseRequestClass):
    def close_live_stream(
            self, 
            live_stream_id: str
    ) -> requests.Response:
        """Closes a media source.

        Http:
            <post>: /LiveStreams/Close

        Args:
            live_stream_id (str): The livestream id.

        Returns:
            <204> requests.Response: Livestream closed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            liveStreamId=live_stream_id,
        )
        return self._post(path='/LiveStreams/Close', request_args=request_args)

    def open_live_stream(
            self, 
            open_token: Optional[str] = None, 
            user_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            max_streaming_bitrate: Optional[int] = None, 
            start_time_ticks: Optional[int] = None, 
            audio_stream_index: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            item_id: Optional[str] = None, 
            enable_direct_play: Optional[bool] = None, 
            enable_direct_stream: Optional[bool] = None, 
            request_body: Optional[OpenLiveStreamDto] = None
    ) -> LiveStreamResponse:
        """Opens a media source.

        Http:
            <post>: /LiveStreams/Open

        Args:
            open_token (str): The open token.
            user_id (str): The user id.
            play_session_id (str): The play session id.
            max_streaming_bitrate (int): The maximum streaming bitrate.
            start_time_ticks (int): The start time in ticks.
            audio_stream_index (int): The audio stream index.
            subtitle_stream_index (int): The subtitle stream index.
            max_audio_channels (int): The maximum number of audio channels.
            item_id (str): The item id.
            enable_direct_play (bool): Whether to enable direct play. Default: true.
            enable_direct_stream (bool): Whether to enable direct stream. Default: true.
            request_body (OpenLiveStreamDto): The open live stream dto.

        Returns:
            <200> LiveStreamResponse: Media source opened.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            openToken=open_token,
            userId=user_id,
            playSessionId=play_session_id,
            maxStreamingBitrate=max_streaming_bitrate,
            startTimeTicks=start_time_ticks,
            audioStreamIndex=audio_stream_index,
            subtitleStreamIndex=subtitle_stream_index,
            maxAudioChannels=max_audio_channels,
            itemId=item_id,
            enableDirectPlay=enable_direct_play,
            enableDirectStream=enable_direct_stream,
            requestBody=request_body,
        )
        return self._post(path='/LiveStreams/Open', request_args=request_args, response_type=LiveStreamResponse)

