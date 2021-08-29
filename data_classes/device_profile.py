from data_classes.codec_profile import CodecProfile
from data_classes.container_profile import ContainerProfile
from data_classes.direct_play_profile import DirectPlayProfile
from data_classes.identification import Identification
from data_classes.response_profile import ResponseProfile
from data_classes.subtitle_profile import SubtitleProfile
from data_classes.transcoding_profile import TranscodingProfile
from data_classes.x_m_l_attribute import XMLAttribute
from util.from_type import *


@dataclass
class DeviceProfile:
    """Defines the MediaBrowser.Model.Dlna.DeviceProfile.
    
    Gets or sets the device profile.
    """
    """Gets or sets the AlbumArtPn."""
    album_art_pn: Optional[str] = None
    """Gets or sets the CodecProfiles."""
    codec_profiles: Optional[List[CodecProfile]] = None
    """Gets or sets the ContainerProfiles."""
    container_profiles: Optional[List[ContainerProfile]] = None
    """Gets or sets the direct play profiles."""
    direct_play_profiles: Optional[List[DirectPlayProfile]] = None
    """Gets or sets a value indicating whether EnableAlbumArtInDidl."""
    enable_album_art_in_didl: Optional[bool] = None
    """Gets or sets a value indicating whether EnableMSMediaReceiverRegistrar."""
    enable_ms_media_receiver_registrar: Optional[bool] = None
    """Gets or sets a value indicating whether EnableSingleAlbumArtLimit."""
    enable_single_album_art_limit: Optional[bool] = None
    """Gets or sets a value indicating whether EnableSingleSubtitleLimit."""
    enable_single_subtitle_limit: Optional[bool] = None
    """Gets or sets the FriendlyName."""
    friendly_name: Optional[str] = None
    """Gets or sets the Id."""
    id: Optional[str] = None
    """Gets or sets the Identification."""
    identification: Optional[Identification] = None
    """Gets or sets a value indicating whether IgnoreTranscodeByteRangeRequests."""
    ignore_transcode_byte_range_requests: Optional[bool] = None
    """Gets or sets the Manufacturer."""
    manufacturer: Optional[str] = None
    """Gets or sets the ManufacturerUrl."""
    manufacturer_url: Optional[str] = None
    """Gets or sets the MaxAlbumArtHeight."""
    max_album_art_height: Optional[int] = None
    """Gets or sets the MaxAlbumArtWidth."""
    max_album_art_width: Optional[int] = None
    """Gets or sets the MaxIconHeight."""
    max_icon_height: Optional[int] = None
    """Gets or sets the MaxIconWidth."""
    max_icon_width: Optional[int] = None
    """Gets or sets the MaxStaticBitrate."""
    max_static_bitrate: Optional[int] = None
    """Gets or sets the MaxStaticMusicBitrate."""
    max_static_music_bitrate: Optional[int] = None
    """Gets or sets the MaxStreamingBitrate."""
    max_streaming_bitrate: Optional[int] = None
    """Gets or sets the ModelDescription."""
    model_description: Optional[str] = None
    """Gets or sets the ModelName."""
    model_name: Optional[str] = None
    """Gets or sets the ModelNumber."""
    model_number: Optional[str] = None
    """Gets or sets the ModelUrl."""
    model_url: Optional[str] = None
    """Gets or sets the MusicStreamingTranscodingBitrate."""
    music_streaming_transcoding_bitrate: Optional[int] = None
    """Gets or sets the Name."""
    name: Optional[str] = None
    """Gets or sets the ProtocolInfo."""
    protocol_info: Optional[str] = None
    """Gets or sets a value indicating whether RequiresPlainFolders."""
    requires_plain_folders: Optional[bool] = None
    """Gets or sets a value indicating whether RequiresPlainVideoItems."""
    requires_plain_video_items: Optional[bool] = None
    """Gets or sets the ResponseProfiles."""
    response_profiles: Optional[List[ResponseProfile]] = None
    """Gets or sets the SerialNumber."""
    serial_number: Optional[str] = None
    """Gets or sets the content of the aggregationFlags element in the urn:schemas-sonycom:av
    namespace.
    """
    sony_aggregation_flags: Optional[str] = None
    """Gets or sets the SubtitleProfiles."""
    subtitle_profiles: Optional[List[SubtitleProfile]] = None
    """Gets or sets the SupportedMediaTypes."""
    supported_media_types: Optional[str] = None
    """Gets or sets the TimelineOffsetSeconds."""
    timeline_offset_seconds: Optional[int] = None
    """Gets or sets the transcoding profiles."""
    transcoding_profiles: Optional[List[TranscodingProfile]] = None
    """Gets or sets the UserId."""
    user_id: Optional[str] = None
    """Gets or sets the XmlRootAttributes."""
    xml_root_attributes: Optional[List[XMLAttribute]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DeviceProfile':
        assert isinstance(obj, dict)
        album_art_pn = from_union([from_str, from_none], obj.get("AlbumArtPn"))
        codec_profiles = from_union([lambda x: from_list(CodecProfile.from_dict, x), from_none], obj.get("CodecProfiles"))
        container_profiles = from_union([lambda x: from_list(ContainerProfile.from_dict, x), from_none], obj.get("ContainerProfiles"))
        direct_play_profiles = from_union([lambda x: from_list(DirectPlayProfile.from_dict, x), from_none], obj.get("DirectPlayProfiles"))
        enable_album_art_in_didl = from_union([from_bool, from_none], obj.get("EnableAlbumArtInDidl"))
        enable_ms_media_receiver_registrar = from_union([from_bool, from_none], obj.get("EnableMSMediaReceiverRegistrar"))
        enable_single_album_art_limit = from_union([from_bool, from_none], obj.get("EnableSingleAlbumArtLimit"))
        enable_single_subtitle_limit = from_union([from_bool, from_none], obj.get("EnableSingleSubtitleLimit"))
        friendly_name = from_union([from_str, from_none], obj.get("FriendlyName"))
        id = from_union([from_str, from_none], obj.get("Id"))
        identification = from_union([Identification.from_dict, from_none], obj.get("Identification"))
        ignore_transcode_byte_range_requests = from_union([from_bool, from_none], obj.get("IgnoreTranscodeByteRangeRequests"))
        manufacturer = from_union([from_str, from_none], obj.get("Manufacturer"))
        manufacturer_url = from_union([from_str, from_none], obj.get("ManufacturerUrl"))
        max_album_art_height = from_union([from_int, from_none], obj.get("MaxAlbumArtHeight"))
        max_album_art_width = from_union([from_int, from_none], obj.get("MaxAlbumArtWidth"))
        max_icon_height = from_union([from_int, from_none], obj.get("MaxIconHeight"))
        max_icon_width = from_union([from_int, from_none], obj.get("MaxIconWidth"))
        max_static_bitrate = from_union([from_int, from_none], obj.get("MaxStaticBitrate"))
        max_static_music_bitrate = from_union([from_int, from_none], obj.get("MaxStaticMusicBitrate"))
        max_streaming_bitrate = from_union([from_int, from_none], obj.get("MaxStreamingBitrate"))
        model_description = from_union([from_str, from_none], obj.get("ModelDescription"))
        model_name = from_union([from_str, from_none], obj.get("ModelName"))
        model_number = from_union([from_str, from_none], obj.get("ModelNumber"))
        model_url = from_union([from_str, from_none], obj.get("ModelUrl"))
        music_streaming_transcoding_bitrate = from_union([from_int, from_none], obj.get("MusicStreamingTranscodingBitrate"))
        name = from_union([from_str, from_none], obj.get("Name"))
        protocol_info = from_union([from_str, from_none], obj.get("ProtocolInfo"))
        requires_plain_folders = from_union([from_bool, from_none], obj.get("RequiresPlainFolders"))
        requires_plain_video_items = from_union([from_bool, from_none], obj.get("RequiresPlainVideoItems"))
        response_profiles = from_union([lambda x: from_list(ResponseProfile.from_dict, x), from_none], obj.get("ResponseProfiles"))
        serial_number = from_union([from_str, from_none], obj.get("SerialNumber"))
        sony_aggregation_flags = from_union([from_str, from_none], obj.get("SonyAggregationFlags"))
        subtitle_profiles = from_union([lambda x: from_list(SubtitleProfile.from_dict, x), from_none], obj.get("SubtitleProfiles"))
        supported_media_types = from_union([from_str, from_none], obj.get("SupportedMediaTypes"))
        timeline_offset_seconds = from_union([from_int, from_none], obj.get("TimelineOffsetSeconds"))
        transcoding_profiles = from_union([lambda x: from_list(TranscodingProfile.from_dict, x), from_none], obj.get("TranscodingProfiles"))
        user_id = from_union([from_str, from_none], obj.get("UserId"))
        xml_root_attributes = from_union([lambda x: from_list(XMLAttribute.from_dict, x), from_none], obj.get("XmlRootAttributes"))
        return DeviceProfile(album_art_pn, codec_profiles, container_profiles, direct_play_profiles, enable_album_art_in_didl, enable_ms_media_receiver_registrar, enable_single_album_art_limit, enable_single_subtitle_limit, friendly_name, id, identification, ignore_transcode_byte_range_requests, manufacturer, manufacturer_url, max_album_art_height, max_album_art_width, max_icon_height, max_icon_width, max_static_bitrate, max_static_music_bitrate, max_streaming_bitrate, model_description, model_name, model_number, model_url, music_streaming_transcoding_bitrate, name, protocol_info, requires_plain_folders, requires_plain_video_items, response_profiles, serial_number, sony_aggregation_flags, subtitle_profiles, supported_media_types, timeline_offset_seconds, transcoding_profiles, user_id, xml_root_attributes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AlbumArtPn"] = from_union([from_str, from_none], self.album_art_pn)
        result["CodecProfiles"] = from_union([lambda x: from_list(lambda x: to_class(CodecProfile, x), x), from_none], self.codec_profiles)
        result["ContainerProfiles"] = from_union([lambda x: from_list(lambda x: to_class(ContainerProfile, x), x), from_none], self.container_profiles)
        result["DirectPlayProfiles"] = from_union([lambda x: from_list(lambda x: to_class(DirectPlayProfile, x), x), from_none], self.direct_play_profiles)
        result["EnableAlbumArtInDidl"] = from_union([from_bool, from_none], self.enable_album_art_in_didl)
        result["EnableMSMediaReceiverRegistrar"] = from_union([from_bool, from_none], self.enable_ms_media_receiver_registrar)
        result["EnableSingleAlbumArtLimit"] = from_union([from_bool, from_none], self.enable_single_album_art_limit)
        result["EnableSingleSubtitleLimit"] = from_union([from_bool, from_none], self.enable_single_subtitle_limit)
        result["FriendlyName"] = from_union([from_str, from_none], self.friendly_name)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Identification"] = from_union([lambda x: to_class(Identification, x), from_none], self.identification)
        result["IgnoreTranscodeByteRangeRequests"] = from_union([from_bool, from_none], self.ignore_transcode_byte_range_requests)
        result["Manufacturer"] = from_union([from_str, from_none], self.manufacturer)
        result["ManufacturerUrl"] = from_union([from_str, from_none], self.manufacturer_url)
        result["MaxAlbumArtHeight"] = from_union([from_int, from_none], self.max_album_art_height)
        result["MaxAlbumArtWidth"] = from_union([from_int, from_none], self.max_album_art_width)
        result["MaxIconHeight"] = from_union([from_int, from_none], self.max_icon_height)
        result["MaxIconWidth"] = from_union([from_int, from_none], self.max_icon_width)
        result["MaxStaticBitrate"] = from_union([from_int, from_none], self.max_static_bitrate)
        result["MaxStaticMusicBitrate"] = from_union([from_int, from_none], self.max_static_music_bitrate)
        result["MaxStreamingBitrate"] = from_union([from_int, from_none], self.max_streaming_bitrate)
        result["ModelDescription"] = from_union([from_str, from_none], self.model_description)
        result["ModelName"] = from_union([from_str, from_none], self.model_name)
        result["ModelNumber"] = from_union([from_str, from_none], self.model_number)
        result["ModelUrl"] = from_union([from_str, from_none], self.model_url)
        result["MusicStreamingTranscodingBitrate"] = from_union([from_int, from_none], self.music_streaming_transcoding_bitrate)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ProtocolInfo"] = from_union([from_str, from_none], self.protocol_info)
        result["RequiresPlainFolders"] = from_union([from_bool, from_none], self.requires_plain_folders)
        result["RequiresPlainVideoItems"] = from_union([from_bool, from_none], self.requires_plain_video_items)
        result["ResponseProfiles"] = from_union([lambda x: from_list(lambda x: to_class(ResponseProfile, x), x), from_none], self.response_profiles)
        result["SerialNumber"] = from_union([from_str, from_none], self.serial_number)
        result["SonyAggregationFlags"] = from_union([from_str, from_none], self.sony_aggregation_flags)
        result["SubtitleProfiles"] = from_union([lambda x: from_list(lambda x: to_class(SubtitleProfile, x), x), from_none], self.subtitle_profiles)
        result["SupportedMediaTypes"] = from_union([from_str, from_none], self.supported_media_types)
        result["TimelineOffsetSeconds"] = from_union([from_int, from_none], self.timeline_offset_seconds)
        result["TranscodingProfiles"] = from_union([lambda x: from_list(lambda x: to_class(TranscodingProfile, x), x), from_none], self.transcoding_profiles)
        result["UserId"] = from_union([from_str, from_none], self.user_id)
        result["XmlRootAttributes"] = from_union([lambda x: from_list(lambda x: to_class(XMLAttribute, x), x), from_none], self.xml_root_attributes)
        return result


