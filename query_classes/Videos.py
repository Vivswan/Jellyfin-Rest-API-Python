import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.upload_subtitle_dto import UploadSubtitleDto as UploadSubtitleDto
from data_classes.method import Method as SubtitleDeliveryMethod
from data_classes.context import Context as EncodingContext
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult


class Videos(BaseRequestClass):
    def get_hls_video_segment(
            self, 
            item_id: str, 
            playlist_id: str, 
            segment_id: int, 
            container: str, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None
    ) -> requests.Response:
        """Gets a video stream using HTTP live streaming.

        Http:
            <get>: /Videos/{itemId}/hls1/{playlistId}/{segmentId}.{container}

        Args:
            item_id (str): The item id.
            playlist_id (str): The playlist id.
            segment_id (int): The segment id.
            container (str): The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment lenght.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.

        Returns:
            <200> requests.Response: Video stream returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            playlistId=playlist_id,
            segmentId=segment_id,
            container=container,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
        )
        return self._get(path='/Videos/{itemId}/hls1/{playlistId}/{segmentId}.{container}', request_args=request_args)

    def get_variant_hls_video_playlist(
            self, 
            item_id: str, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None
    ) -> requests.Response:
        """Gets a video stream using HTTP live streaming.

        Http:
            <get>: /Videos/{itemId}/main.m3u8

        Args:
            item_id (str): The item id.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.

        Returns:
            <200> requests.Response: Video stream returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
        )
        return self._get(path='/Videos/{itemId}/main.m3u8', request_args=request_args)

    def get_master_hls_video_playlist(
            self, 
            item_id: str, 
            media_source_id: str, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None, 
            enable_adaptive_bitrate_streaming: Optional[bool] = True
    ) -> requests.Response:
        """Gets a video hls playlist stream.

        Http:
            <get>: /Videos/{itemId}/master.m3u8

        Args:
            item_id (str): The item id.
            media_source_id (str): The media version id, if playing an alternate version.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.
            enable_adaptive_bitrate_streaming (bool = True): Enable adaptive bitrate streaming.

        Returns:
            <200> requests.Response: Video stream returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            mediaSourceId=media_source_id,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
            enableAdaptiveBitrateStreaming=enable_adaptive_bitrate_streaming,
        )
        return self._get(path='/Videos/{itemId}/master.m3u8', request_args=request_args)

    def head_master_hls_video_playlist(
            self, 
            item_id: str, 
            media_source_id: str, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None, 
            enable_adaptive_bitrate_streaming: Optional[bool] = True
    ) -> requests.Response:
        """Gets a video hls playlist stream.

        Http:
            <head>: /Videos/{itemId}/master.m3u8

        Args:
            item_id (str): The item id.
            media_source_id (str): The media version id, if playing an alternate version.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.
            enable_adaptive_bitrate_streaming (bool = True): Enable adaptive bitrate streaming.

        Returns:
            <200> requests.Response: Video stream returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            mediaSourceId=media_source_id,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
            enableAdaptiveBitrateStreaming=enable_adaptive_bitrate_streaming,
        )
        return self._head(path='/Videos/{itemId}/master.m3u8', request_args=request_args)

    def get_hls_video_segment_legacy(
            self, 
            item_id: str, 
            playlist_id: str, 
            segment_id: str, 
            segment_container: str
    ) -> requests.Response:
        """Gets a hls video segment.

        Http:
            <get>: /Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer}

        Args:
            item_id (str): The item id.
            playlist_id (str): The playlist id.
            segment_id (str): The segment id.
            segment_container (str): The segment container.

        Returns:
            <200> requests.Response: Hls video segment returned.
            <404> requests.Response: Hls segment not found.
        """
        request_args = dict(
            itemId=item_id,
            playlistId=playlist_id,
            segmentId=segment_id,
            segmentContainer=segment_container,
        )
        return self._get(path='/Videos/{itemId}/hls/{playlistId}/{segmentId}.{segmentContainer}', request_args=request_args)

    def get_hls_playlist_legacy(
            self, 
            item_id: str, 
            playlist_id: str
    ) -> requests.Response:
        """Gets a hls video playlist.

        Http:
            <get>: /Videos/{itemId}/hls/{playlistId}/stream.m3u8

        Args:
            item_id (str): The video id.
            playlist_id (str): The playlist id.

        Returns:
            <200> requests.Response: Hls video playlist returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            playlistId=playlist_id,
        )
        return self._get(path='/Videos/{itemId}/hls/{playlistId}/stream.m3u8', request_args=request_args)

    def stop_encoding_process(
            self, 
            device_id: str, 
            play_session_id: str
    ) -> requests.Response:
        """Stops an active encoding.

        Http:
            <delete>: /Videos/ActiveEncodings

        Args:
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            play_session_id (str): The play session id.

        Returns:
            <204> requests.Response: Encoding stopped successfully.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            deviceId=device_id,
            playSessionId=play_session_id,
        )
        return self._delete(path='/Videos/ActiveEncodings', request_args=request_args)

    def get_subtitle_playlist(
            self, 
            item_id: str, 
            index: int, 
            media_source_id: str, 
            segment_length: int
    ) -> requests.Response:
        """Gets an HLS subtitle playlist.

        Http:
            <get>: /Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8

        Args:
            item_id (str): The item id.
            index (int): The subtitle stream index.
            media_source_id (str): The media source id.
            segment_length (int): The subtitle segment length.

        Returns:
            <200> requests.Response: Subtitle playlist retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            index=index,
            mediaSourceId=media_source_id,
            segmentLength=segment_length,
        )
        return self._get(path='/Videos/{itemId}/{mediaSourceId}/Subtitles/{index}/subtitles.m3u8', request_args=request_args)

    def upload_subtitle(
            self, 
            item_id: str, 
            request_body: UploadSubtitleDto
    ) -> requests.Response:
        """Upload an external subtitle file.

        Http:
            <post>: /Videos/{itemId}/Subtitles

        Args:
            item_id (str): The item the subtitle belongs to.
            request_body (UploadSubtitleDto): The request body.

        Returns:
            <204> requests.Response: Subtitle uploaded.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            requestBody=request_body,
        )
        return self._post(path='/Videos/{itemId}/Subtitles', request_args=request_args)

    def delete_subtitle(
            self, 
            item_id: str, 
            index: int
    ) -> requests.Response:
        """Deletes an external subtitle file.

        Http:
            <delete>: /Videos/{itemId}/Subtitles/{index}

        Args:
            item_id (str): The item id.
            index (int): The index of the subtitle file.

        Returns:
            <204> requests.Response: Subtitle deleted.
            <404> requests.Response: Item not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            index=index,
        )
        return self._delete(path='/Videos/{itemId}/Subtitles/{index}', request_args=request_args)

    def get_subtitle_with_ticks(
            self, 
            route_item_id: str, 
            route_media_source_id: str, 
            route_index: int, 
            route_start_position_ticks: int, 
            route_format: str, 
            item_id: Optional[str] = None, 
            media_source_id: Optional[str] = None, 
            index: Optional[int] = None, 
            start_position_ticks: Optional[int] = None, 
            format: Optional[str] = None, 
            end_position_ticks: Optional[int] = None, 
            copy_timestamps: Optional[bool] = False, 
            add_vtt_time_map: Optional[bool] = False
    ) -> requests.Response:
        """Gets subtitles in a specified format.

        Http:
            <get>: /Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat}

        Args:
            route_item_id (str): The (route) item id.
            route_media_source_id (str): The (route) media source id.
            route_index (int): The (route) subtitle stream index.
            route_start_position_ticks (int): The (route) start position of the subtitle in ticks.
            route_format (str): The (route) format of the returned subtitle.
            item_id (str): The item id.
            media_source_id (str): The media source id.
            index (int): The subtitle stream index.
            start_position_ticks (int): The start position of the subtitle in ticks.
            format (str): The format of the returned subtitle.
            end_position_ticks (int): Optional. The end position of the subtitle in ticks.
            copy_timestamps (bool = False): Optional. Whether to copy the timestamps.
            add_vtt_time_map (bool = False): Optional. Whether to add a VTT time map.

        Returns:
            <200> requests.Response: File returned.
        """
        request_args = dict(
            routeItemId=route_item_id,
            routeMediaSourceId=route_media_source_id,
            routeIndex=route_index,
            routeStartPositionTicks=route_start_position_ticks,
            routeFormat=route_format,
            itemId=item_id,
            mediaSourceId=media_source_id,
            index=index,
            startPositionTicks=start_position_ticks,
            format=format,
            endPositionTicks=end_position_ticks,
            copyTimestamps=copy_timestamps,
            addVttTimeMap=add_vtt_time_map,
        )
        return self._get(path='/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/{routeStartPositionTicks}/Stream.{routeFormat}', request_args=request_args)

    def get_subtitle(
            self, 
            route_item_id: str, 
            route_media_source_id: str, 
            route_index: int, 
            route_format: str, 
            item_id: Optional[str] = None, 
            media_source_id: Optional[str] = None, 
            index: Optional[int] = None, 
            format: Optional[str] = None, 
            end_position_ticks: Optional[int] = None, 
            copy_timestamps: Optional[bool] = False, 
            add_vtt_time_map: Optional[bool] = False, 
            start_position_ticks: Optional[int] = 0
    ) -> requests.Response:
        """Gets subtitles in a specified format.

        Http:
            <get>: /Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/Stream.{routeFormat}

        Args:
            route_item_id (str): The (route) item id.
            route_media_source_id (str): The (route) media source id.
            route_index (int): The (route) subtitle stream index.
            route_format (str): The (route) format of the returned subtitle.
            item_id (str): The item id.
            media_source_id (str): The media source id.
            index (int): The subtitle stream index.
            format (str): The format of the returned subtitle.
            end_position_ticks (int): Optional. The end position of the subtitle in ticks.
            copy_timestamps (bool = False): Optional. Whether to copy the timestamps.
            add_vtt_time_map (bool = False): Optional. Whether to add a VTT time map.
            start_position_ticks (int = 0): The start position of the subtitle in ticks.

        Returns:
            <200> requests.Response: File returned.
        """
        request_args = dict(
            routeItemId=route_item_id,
            routeMediaSourceId=route_media_source_id,
            routeIndex=route_index,
            routeFormat=route_format,
            itemId=item_id,
            mediaSourceId=media_source_id,
            index=index,
            format=format,
            endPositionTicks=end_position_ticks,
            copyTimestamps=copy_timestamps,
            addVttTimeMap=add_vtt_time_map,
            startPositionTicks=start_position_ticks,
        )
        return self._get(path='/Videos/{routeItemId}/{routeMediaSourceId}/Subtitles/{routeIndex}/Stream.{routeFormat}', request_args=request_args)

    def get_attachment(
            self, 
            video_id: str, 
            media_source_id: str, 
            index: int
    ) -> requests.Response:
        """Get video attachment.

        Http:
            <get>: /Videos/{videoId}/{mediaSourceId}/Attachments/{index}

        Args:
            video_id (str): Video ID.
            media_source_id (str): Media Source ID.
            index (int): Attachment Index.

        Returns:
            <200> requests.Response: Attachment retrieved.
            <404> requests.Response: Video or attachment not found.
        """
        request_args = dict(
            videoId=video_id,
            mediaSourceId=media_source_id,
            index=index,
        )
        return self._get(path='/Videos/{videoId}/{mediaSourceId}/Attachments/{index}', request_args=request_args)

    def get_live_hls_stream(
            self, 
            item_id: str, 
            container: Optional[str] = None, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None, 
            max_width: Optional[int] = None, 
            max_height: Optional[int] = None, 
            enable_subtitles_in_manifest: Optional[bool] = None
    ) -> requests.Response:
        """Gets a hls live stream.

        Http:
            <get>: /Videos/{itemId}/live.m3u8

        Args:
            item_id (str): The item id.
            container (str): The audio container.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment lenght.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.
            max_width (int): Optional. The max width.
            max_height (int): Optional. The max height.
            enable_subtitles_in_manifest (bool): Optional. Whether to enable subtitles in the manifest.

        Returns:
            <200> requests.Response: Hls live stream retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
            maxWidth=max_width,
            maxHeight=max_height,
            enableSubtitlesInManifest=enable_subtitles_in_manifest,
        )
        return self._get(path='/Videos/{itemId}/live.m3u8', request_args=request_args)

    def get_additional_part(
            self, 
            item_id: str, 
            user_id: Optional[str] = None
    ) -> BaseItemDtoQueryResult:
        """Gets additional parts for a video.

        Http:
            <get>: /Videos/{itemId}/AdditionalParts

        Args:
            item_id (str): The item id.
            user_id (str): Optional. Filter by user id, and attach user data.

        Returns:
            <200> BaseItemDtoQueryResult: Additional parts returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            userId=user_id,
        )
        return self._get(path='/Videos/{itemId}/AdditionalParts', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def delete_alternate_sources(
            self, 
            item_id: str
    ) -> requests.Response:
        """Removes alternate video sources.

        Http:
            <delete>: /Videos/{itemId}/AlternateSources

        Args:
            item_id (str): The item id.

        Returns:
            <204> requests.Response: Alternate sources deleted.
            <404> requests.Response: Video not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
        )
        return self._delete(path='/Videos/{itemId}/AlternateSources', request_args=request_args)

    def get_video_stream(
            self, 
            item_id: str, 
            container: Optional[str] = None, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None
    ) -> requests.Response:
        """Gets a video stream.

        Http:
            <get>: /Videos/{itemId}/stream

        Args:
            item_id (str): The item id.
            container (str): The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.

        Returns:
            <200> requests.Response: Video stream returned.
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
        )
        return self._get(path='/Videos/{itemId}/stream', request_args=request_args)

    def head_video_stream(
            self, 
            item_id: str, 
            container: Optional[str] = None, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None
    ) -> requests.Response:
        """Gets a video stream.

        Http:
            <head>: /Videos/{itemId}/stream

        Args:
            item_id (str): The item id.
            container (str): The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.

        Returns:
            <200> requests.Response: Video stream returned.
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
        )
        return self._head(path='/Videos/{itemId}/stream', request_args=request_args)

    def get_video_stream_by_container(
            self, 
            item_id: str, 
            container: str, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None
    ) -> requests.Response:
        """Gets a video stream.

        Http:
            <get>: /Videos/{itemId}/stream.{container}

        Args:
            item_id (str): The item id.
            container (str): The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.

        Returns:
            <200> requests.Response: Video stream returned.
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
        )
        return self._get(path='/Videos/{itemId}/stream.{container}', request_args=request_args)

    def head_video_stream_by_container(
            self, 
            item_id: str, 
            container: str, 
            static: Optional[bool] = None, 
            params: Optional[str] = None, 
            tag: Optional[str] = None, 
            device_profile_id: Optional[str] = None, 
            play_session_id: Optional[str] = None, 
            segment_container: Optional[str] = None, 
            segment_length: Optional[int] = None, 
            min_segments: Optional[int] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            enable_auto_stream_copy: Optional[bool] = None, 
            allow_video_stream_copy: Optional[bool] = None, 
            allow_audio_stream_copy: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = None, 
            audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            audio_channels: Optional[int] = None, 
            max_audio_channels: Optional[int] = None, 
            profile: Optional[str] = None, 
            level: Optional[str] = None, 
            framerate: Optional[float] = None, 
            max_framerate: Optional[float] = None, 
            copy_timestamps: Optional[bool] = None, 
            start_time_ticks: Optional[int] = None, 
            width: Optional[int] = None, 
            height: Optional[int] = None, 
            video_bit_rate: Optional[int] = None, 
            subtitle_stream_index: Optional[int] = None, 
            subtitle_method: Optional[SubtitleDeliveryMethod] = None, 
            max_ref_frames: Optional[int] = None, 
            max_video_bit_depth: Optional[int] = None, 
            require_avc: Optional[bool] = None, 
            de_interlace: Optional[bool] = None, 
            require_non_anamorphic: Optional[bool] = None, 
            transcoding_max_audio_channels: Optional[int] = None, 
            cpu_core_limit: Optional[int] = None, 
            live_stream_id: Optional[str] = None, 
            enable_mpegts_m2_ts_mode: Optional[bool] = None, 
            video_codec: Optional[str] = None, 
            subtitle_codec: Optional[str] = None, 
            transcode_reasons: Optional[str] = None, 
            audio_stream_index: Optional[int] = None, 
            video_stream_index: Optional[int] = None, 
            context: Optional[EncodingContext] = None, 
            stream_options: Optional[object] = None
    ) -> requests.Response:
        """Gets a video stream.

        Http:
            <head>: /Videos/{itemId}/stream.{container}

        Args:
            item_id (str): The item id.
            container (str): The video container. Possible values are: ts, webm, asf, wmv, ogv, mp4, m4v, mkv, mpeg, mpg, avi, 3gp, wmv, wtv, m2ts, mov, iso, flv.
            static (bool): Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
            params (str): The streaming parameters.
            tag (str): The tag.
            device_profile_id (str): Optional. The dlna device profile id to utilize.
            play_session_id (str): The play session id.
            segment_container (str): The segment container.
            segment_length (int): The segment length.
            min_segments (int): The minimum number of segments.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            audio_codec (str): Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url's extension. Options: aac, mp3, vorbis, wma.
            enable_auto_stream_copy (bool): Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
            allow_video_stream_copy (bool): Whether or not to allow copying of the video stream url.
            allow_audio_stream_copy (bool): Whether or not to allow copying of the audio stream url.
            break_on_non_key_frames (bool): Optional. Whether to break on non key frames.
            audio_sample_rate (int): Optional. Specify a specific audio sample rate, e.g. 44100.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            audio_channels (int): Optional. Specify a specific number of audio channels to encode to, e.g. 2.
            max_audio_channels (int): Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
            profile (str): Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
            level (str): Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
            framerate (float): Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            max_framerate (float): Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
            copy_timestamps (bool): Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            width (int): Optional. The fixed horizontal resolution of the encoded video.
            height (int): Optional. The fixed vertical resolution of the encoded video.
            video_bit_rate (int): Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
            subtitle_stream_index (int): Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
            subtitle_method (SubtitleDeliveryMethod): Optional. Specify the subtitle delivery method.
            max_ref_frames (int): Optional.
            max_video_bit_depth (int): Optional. The maximum video bit depth.
            require_avc (bool): Optional. Whether to require avc.
            de_interlace (bool): Optional. Whether to deinterlace the video.
            require_non_anamorphic (bool): Optional. Whether to require a non anamorphic stream.
            transcoding_max_audio_channels (int): Optional. The maximum number of audio channels to transcode.
            cpu_core_limit (int): Optional. The limit of how many cpu cores to use.
            live_stream_id (str): The live stream id.
            enable_mpegts_m2_ts_mode (bool): Optional. Whether to enable the MpegtsM2Ts mode.
            video_codec (str): Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url's extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
            subtitle_codec (str): Optional. Specify a subtitle codec to encode to.
            transcode_reasons (str): Optional. The transcoding reason.
            audio_stream_index (int): Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
            video_stream_index (int): Optional. The index of the video stream to use. If omitted the first video stream will be used.
            context (EncodingContext): Optional. The MediaBrowser.Model.Dlna.EncodingContext.
            stream_options (object): Optional. The streaming options.

        Returns:
            <200> requests.Response: Video stream returned.
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            static=static,
            params=params,
            tag=tag,
            deviceProfileId=device_profile_id,
            playSessionId=play_session_id,
            segmentContainer=segment_container,
            segmentLength=segment_length,
            minSegments=min_segments,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            audioCodec=audio_codec,
            enableAutoStreamCopy=enable_auto_stream_copy,
            allowVideoStreamCopy=allow_video_stream_copy,
            allowAudioStreamCopy=allow_audio_stream_copy,
            breakOnNonKeyFrames=break_on_non_key_frames,
            audioSampleRate=audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            audioBitRate=audio_bit_rate,
            audioChannels=audio_channels,
            maxAudioChannels=max_audio_channels,
            profile=profile,
            level=level,
            framerate=framerate,
            maxFramerate=max_framerate,
            copyTimestamps=copy_timestamps,
            startTimeTicks=start_time_ticks,
            width=width,
            height=height,
            videoBitRate=video_bit_rate,
            subtitleStreamIndex=subtitle_stream_index,
            subtitleMethod=subtitle_method,
            maxRefFrames=max_ref_frames,
            maxVideoBitDepth=max_video_bit_depth,
            requireAvc=require_avc,
            deInterlace=de_interlace,
            requireNonAnamorphic=require_non_anamorphic,
            transcodingMaxAudioChannels=transcoding_max_audio_channels,
            cpuCoreLimit=cpu_core_limit,
            liveStreamId=live_stream_id,
            enableMpegtsM2TsMode=enable_mpegts_m2_ts_mode,
            videoCodec=video_codec,
            subtitleCodec=subtitle_codec,
            transcodeReasons=transcode_reasons,
            audioStreamIndex=audio_stream_index,
            videoStreamIndex=video_stream_index,
            context=context,
            streamOptions=stream_options,
        )
        return self._head(path='/Videos/{itemId}/stream.{container}', request_args=request_args)

    def merge_versions(
            self, 
            ids: List[str]
    ) -> requests.Response:
        """Merges videos into a single record.

        Http:
            <post>: /Videos/MergeVersions

        Args:
            ids (List[str]): Item id list. This allows multiple, comma delimited.

        Returns:
            <204> requests.Response: Videos merged.
            <400> requests.Response: Supply at least 2 video ids.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            ids=ids,
        )
        return self._post(path='/Videos/MergeVersions', request_args=request_args)

