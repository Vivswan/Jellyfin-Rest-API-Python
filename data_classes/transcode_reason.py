from util.from_type import *


class TranscodeReason(CaseInsensitiveEnum):
    ANAMORPHIC_VIDEO_NOT_SUPPORTED = "AnamorphicVideoNotSupported"
    AUDIO_BITRATE_NOT_SUPPORTED = "AudioBitrateNotSupported"
    AUDIO_BIT_DEPTH_NOT_SUPPORTED = "AudioBitDepthNotSupported"
    AUDIO_CHANNELS_NOT_SUPPORTED = "AudioChannelsNotSupported"
    AUDIO_CODEC_NOT_SUPPORTED = "AudioCodecNotSupported"
    AUDIO_PROFILE_NOT_SUPPORTED = "AudioProfileNotSupported"
    AUDIO_SAMPLE_RATE_NOT_SUPPORTED = "AudioSampleRateNotSupported"
    CONTAINER_BITRATE_EXCEEDS_LIMIT = "ContainerBitrateExceedsLimit"
    CONTAINER_NOT_SUPPORTED = "ContainerNotSupported"
    DIRECT_PLAY_ERROR = "DirectPlayError"
    INTERLACED_VIDEO_NOT_SUPPORTED = "InterlacedVideoNotSupported"
    REF_FRAMES_NOT_SUPPORTED = "RefFramesNotSupported"
    SECONDARY_AUDIO_NOT_SUPPORTED = "SecondaryAudioNotSupported"
    SUBTITLE_CODEC_NOT_SUPPORTED = "SubtitleCodecNotSupported"
    UNKNOWN_AUDIO_STREAM_INFO = "UnknownAudioStreamInfo"
    UNKNOWN_VIDEO_STREAM_INFO = "UnknownVideoStreamInfo"
    VIDEO_BITRATE_NOT_SUPPORTED = "VideoBitrateNotSupported"
    VIDEO_BIT_DEPTH_NOT_SUPPORTED = "VideoBitDepthNotSupported"
    VIDEO_CODEC_NOT_SUPPORTED = "VideoCodecNotSupported"
    VIDEO_FRAMERATE_NOT_SUPPORTED = "VideoFramerateNotSupported"
    VIDEO_LEVEL_NOT_SUPPORTED = "VideoLevelNotSupported"
    VIDEO_PROFILE_NOT_SUPPORTED = "VideoProfileNotSupported"
    VIDEO_RESOLUTION_NOT_SUPPORTED = "VideoResolutionNotSupported"


