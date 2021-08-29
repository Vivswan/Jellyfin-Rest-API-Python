from typing import List
from typing import Optional

import requests

from data_classes.context import Context as EncodingContext
from data_classes.method import Method as SubtitleDeliveryMethod
from util.BaseRequestClass import BaseRequestClass


class Audio(BaseRequestClass):
    def get_audio_stream(
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
        """Gets an audio stream.

        Http:
            <get>: /Audio/{itemId}/stream

        Args:
            item_id (str): The item id.
            container (str): The audio container.
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
            <200> requests.Response: Audio stream returned.
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
        return self._get(path='/Audio/{itemId}/stream', request_args=request_args)

    def head_audio_stream(
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
        """Gets an audio stream.

        Http:
            <head>: /Audio/{itemId}/stream

        Args:
            item_id (str): The item id.
            container (str): The audio container.
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
            <200> requests.Response: Audio stream returned.
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
        return self._head(path='/Audio/{itemId}/stream', request_args=request_args)

    def get_audio_stream_by_container(
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
        """Gets an audio stream.

        Http:
            <get>: /Audio/{itemId}/stream.{container}

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
            require_non_anamorphic (bool): Optional. Whether to require a non anamporphic stream.
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
            <200> requests.Response: Audio stream returned.
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
        return self._get(path='/Audio/{itemId}/stream.{container}', request_args=request_args)

    def head_audio_stream_by_container(
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
        """Gets an audio stream.

        Http:
            <head>: /Audio/{itemId}/stream.{container}

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
            require_non_anamorphic (bool): Optional. Whether to require a non anamporphic stream.
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
            <200> requests.Response: Audio stream returned.
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
        return self._head(path='/Audio/{itemId}/stream.{container}', request_args=request_args)

    def get_hls_audio_segment(
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
            max_streaming_bitrate: Optional[int] = None, 
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
            <get>: /Audio/{itemId}/hls1/{playlistId}/{segmentId}.{container}

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
            max_streaming_bitrate (int): Optional. The maximum streaming bitrate.
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
            maxStreamingBitrate=max_streaming_bitrate,
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
        return self._get(path='/Audio/{itemId}/hls1/{playlistId}/{segmentId}.{container}', request_args=request_args)

    def get_variant_hls_audio_playlist(
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
            max_streaming_bitrate: Optional[int] = None, 
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
        """Gets an audio stream using HTTP live streaming.

        Http:
            <get>: /Audio/{itemId}/main.m3u8

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
            max_streaming_bitrate (int): Optional. The maximum streaming bitrate.
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
            <200> requests.Response: Audio stream returned.
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
            maxStreamingBitrate=max_streaming_bitrate,
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
        return self._get(path='/Audio/{itemId}/main.m3u8', request_args=request_args)

    def get_master_hls_audio_playlist(
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
            max_streaming_bitrate: Optional[int] = None, 
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
        """Gets an audio hls playlist stream.

        Http:
            <get>: /Audio/{itemId}/master.m3u8

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
            max_streaming_bitrate (int): Optional. The maximum streaming bitrate.
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
            <200> requests.Response: Audio stream returned.
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
            maxStreamingBitrate=max_streaming_bitrate,
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
        return self._get(path='/Audio/{itemId}/master.m3u8', request_args=request_args)

    def head_master_hls_audio_playlist(
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
            max_streaming_bitrate: Optional[int] = None, 
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
        """Gets an audio hls playlist stream.

        Http:
            <head>: /Audio/{itemId}/master.m3u8

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
            max_streaming_bitrate (int): Optional. The maximum streaming bitrate.
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
            <200> requests.Response: Audio stream returned.
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
            maxStreamingBitrate=max_streaming_bitrate,
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
        return self._head(path='/Audio/{itemId}/master.m3u8', request_args=request_args)

    def get_hls_audio_segment_legacy_aac(
            self, 
            item_id: str, 
            segment_id: str
    ) -> requests.Response:
        """Gets the specified audio segment for an audio item.

        Http:
            <get>: /Audio/{itemId}/hls/{segmentId}/stream.aac

        Args:
            item_id (str): The item id.
            segment_id (str): The segment id.

        Returns:
            <200> requests.Response: Hls audio segment returned.
        """
        request_args = dict(
            itemId=item_id,
            segmentId=segment_id,
        )
        return self._get(path='/Audio/{itemId}/hls/{segmentId}/stream.aac', request_args=request_args)

    def get_hls_audio_segment_legacy_mp3(
            self, 
            item_id: str, 
            segment_id: str
    ) -> requests.Response:
        """Gets the specified audio segment for an audio item.

        Http:
            <get>: /Audio/{itemId}/hls/{segmentId}/stream.mp3

        Args:
            item_id (str): The item id.
            segment_id (str): The segment id.

        Returns:
            <200> requests.Response: Hls audio segment returned.
        """
        request_args = dict(
            itemId=item_id,
            segmentId=segment_id,
        )
        return self._get(path='/Audio/{itemId}/hls/{segmentId}/stream.mp3', request_args=request_args)

    def get_universal_audio_stream(
            self, 
            item_id: str, 
            container: Optional[List[str]] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            user_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            max_audio_channels: Optional[int] = None, 
            transcoding_audio_channels: Optional[int] = None, 
            max_streaming_bitrate: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            start_time_ticks: Optional[int] = None, 
            transcoding_container: Optional[str] = None, 
            transcoding_protocol: Optional[str] = None, 
            max_audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            enable_remote_media: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = False, 
            enable_redirection: Optional[bool] = True
    ) -> requests.Response:
        """Gets an audio stream.

        Http:
            <get>: /Audio/{itemId}/universal

        Args:
            item_id (str): The item id.
            container (List[str]): Optional. The audio container.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            user_id (str): Optional. The user id.
            audio_codec (str): Optional. The audio codec to transcode to.
            max_audio_channels (int): Optional. The maximum number of audio channels.
            transcoding_audio_channels (int): Optional. The number of how many audio channels to transcode to.
            max_streaming_bitrate (int): Optional. The maximum streaming bitrate.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            transcoding_container (str): Optional. The container to transcode to.
            transcoding_protocol (str): Optional. The transcoding protocol.
            max_audio_sample_rate (int): Optional. The maximum audio sample rate.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            enable_remote_media (bool): Optional. Whether to enable remote media.
            break_on_non_key_frames (bool = False): Optional. Whether to break on non key frames.
            enable_redirection (bool = True): Whether to enable redirection. Defaults to true.

        Returns:
            <200> requests.Response: Audio stream returned.
            <302> requests.Response: Redirected to remote audio stream.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            userId=user_id,
            audioCodec=audio_codec,
            maxAudioChannels=max_audio_channels,
            transcodingAudioChannels=transcoding_audio_channels,
            maxStreamingBitrate=max_streaming_bitrate,
            audioBitRate=audio_bit_rate,
            startTimeTicks=start_time_ticks,
            transcodingContainer=transcoding_container,
            transcodingProtocol=transcoding_protocol,
            maxAudioSampleRate=max_audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            enableRemoteMedia=enable_remote_media,
            breakOnNonKeyFrames=break_on_non_key_frames,
            enableRedirection=enable_redirection,
        )
        return self._get(path='/Audio/{itemId}/universal', request_args=request_args)

    def head_universal_audio_stream(
            self, 
            item_id: str, 
            container: Optional[List[str]] = None, 
            media_source_id: Optional[str] = None, 
            device_id: Optional[str] = None, 
            user_id: Optional[str] = None, 
            audio_codec: Optional[str] = None, 
            max_audio_channels: Optional[int] = None, 
            transcoding_audio_channels: Optional[int] = None, 
            max_streaming_bitrate: Optional[int] = None, 
            audio_bit_rate: Optional[int] = None, 
            start_time_ticks: Optional[int] = None, 
            transcoding_container: Optional[str] = None, 
            transcoding_protocol: Optional[str] = None, 
            max_audio_sample_rate: Optional[int] = None, 
            max_audio_bit_depth: Optional[int] = None, 
            enable_remote_media: Optional[bool] = None, 
            break_on_non_key_frames: Optional[bool] = False, 
            enable_redirection: Optional[bool] = True
    ) -> requests.Response:
        """Gets an audio stream.

        Http:
            <head>: /Audio/{itemId}/universal

        Args:
            item_id (str): The item id.
            container (List[str]): Optional. The audio container.
            media_source_id (str): The media version id, if playing an alternate version.
            device_id (str): The device id of the client requesting. Used to stop encoding processes when needed.
            user_id (str): Optional. The user id.
            audio_codec (str): Optional. The audio codec to transcode to.
            max_audio_channels (int): Optional. The maximum number of audio channels.
            transcoding_audio_channels (int): Optional. The number of how many audio channels to transcode to.
            max_streaming_bitrate (int): Optional. The maximum streaming bitrate.
            audio_bit_rate (int): Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
            start_time_ticks (int): Optional. Specify a starting offset, in ticks. 1 tick = 10000 ms.
            transcoding_container (str): Optional. The container to transcode to.
            transcoding_protocol (str): Optional. The transcoding protocol.
            max_audio_sample_rate (int): Optional. The maximum audio sample rate.
            max_audio_bit_depth (int): Optional. The maximum audio bit depth.
            enable_remote_media (bool): Optional. Whether to enable remote media.
            break_on_non_key_frames (bool = False): Optional. Whether to break on non key frames.
            enable_redirection (bool = True): Whether to enable redirection. Defaults to true.

        Returns:
            <200> requests.Response: Audio stream returned.
            <302> requests.Response: Redirected to remote audio stream.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            itemId=item_id,
            container=container,
            mediaSourceId=media_source_id,
            deviceId=device_id,
            userId=user_id,
            audioCodec=audio_codec,
            maxAudioChannels=max_audio_channels,
            transcodingAudioChannels=transcoding_audio_channels,
            maxStreamingBitrate=max_streaming_bitrate,
            audioBitRate=audio_bit_rate,
            startTimeTicks=start_time_ticks,
            transcodingContainer=transcoding_container,
            transcodingProtocol=transcoding_protocol,
            maxAudioSampleRate=max_audio_sample_rate,
            maxAudioBitDepth=max_audio_bit_depth,
            enableRemoteMedia=enable_remote_media,
            breakOnNonKeyFrames=break_on_non_key_frames,
            enableRedirection=enable_redirection,
        )
        return self._head(path='/Audio/{itemId}/universal', request_args=request_args)

