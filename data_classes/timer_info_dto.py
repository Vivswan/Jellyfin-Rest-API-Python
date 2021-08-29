from util.from_type import *
from data_classes.base_item_dto import BaseItemDto
from data_classes.keep_until import KeepUntil
from data_classes.recording_status_enum import RecordingStatusEnum


@dataclass
class TimerInfoDto:
    """ChannelId of the recording."""
    channel_id: Optional[UUID] = None
    """ChannelName of the recording."""
    channel_name: Optional[str] = None
    channel_primary_image_tag: Optional[str] = None
    """The end date of the recording, in UTC."""
    end_date: Optional[datetime] = None
    """Gets or sets the external channel identifier."""
    external_channel_id: Optional[str] = None
    """Gets or sets the external identifier."""
    external_id: Optional[str] = None
    """Gets or sets the external program identifier."""
    external_program_id: Optional[str] = None
    """Gets or sets the external series timer identifier."""
    external_series_timer_id: Optional[str] = None
    """Id of the recording."""
    id: Optional[str] = None
    """Gets or sets a value indicating whether this instance is post padding required."""
    is_post_padding_required: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is pre padding required."""
    is_pre_padding_required: Optional[bool] = None
    keep_until: Optional[KeepUntil] = None
    """Name of the recording."""
    name: Optional[str] = None
    """Description of the recording."""
    overview: Optional[str] = None
    """Gets or sets the parent backdrop image tags."""
    parent_backdrop_image_tags: Optional[List[str]] = None
    """If the item does not have any backdrops, this will hold the Id of the Parent that has one."""
    parent_backdrop_item_id: Optional[str] = None
    """Gets or sets the post padding seconds."""
    post_padding_seconds: Optional[int] = None
    """Gets or sets the pre padding seconds."""
    pre_padding_seconds: Optional[int] = None
    """Gets or sets the priority."""
    priority: Optional[int] = None
    """Gets or sets the program identifier."""
    program_id: Optional[str] = None
    """Gets or sets the program information."""
    program_info: Optional[BaseItemDto] = None
    """Gets or sets the run time ticks."""
    run_time_ticks: Optional[int] = None
    """Gets or sets the series timer identifier."""
    series_timer_id: Optional[str] = None
    """Gets or sets the server identifier."""
    server_id: Optional[str] = None
    """Gets or sets the name of the service."""
    service_name: Optional[str] = None
    """The start date of the recording, in UTC."""
    start_date: Optional[datetime] = None
    """Gets or sets the status."""
    status: Optional[RecordingStatusEnum] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TimerInfoDto':
        assert isinstance(obj, dict)
        channel_id = from_union([lambda x: UUID(x), from_none], obj.get("ChannelId"))
        channel_name = from_union([from_str, from_none], obj.get("ChannelName"))
        channel_primary_image_tag = from_union([from_str, from_none], obj.get("ChannelPrimaryImageTag"))
        end_date = from_union([from_datetime, from_none], obj.get("EndDate"))
        external_channel_id = from_union([from_str, from_none], obj.get("ExternalChannelId"))
        external_id = from_union([from_str, from_none], obj.get("ExternalId"))
        external_program_id = from_union([from_str, from_none], obj.get("ExternalProgramId"))
        external_series_timer_id = from_union([from_str, from_none], obj.get("ExternalSeriesTimerId"))
        id = from_union([from_str, from_none], obj.get("Id"))
        is_post_padding_required = from_union([from_bool, from_none], obj.get("IsPostPaddingRequired"))
        is_pre_padding_required = from_union([from_bool, from_none], obj.get("IsPrePaddingRequired"))
        keep_until = from_union([KeepUntil, from_none], obj.get("KeepUntil"))
        name = from_union([from_str, from_none], obj.get("Name"))
        overview = from_union([from_str, from_none], obj.get("Overview"))
        parent_backdrop_image_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ParentBackdropImageTags"))
        parent_backdrop_item_id = from_union([from_str, from_none], obj.get("ParentBackdropItemId"))
        post_padding_seconds = from_union([from_int, from_none], obj.get("PostPaddingSeconds"))
        pre_padding_seconds = from_union([from_int, from_none], obj.get("PrePaddingSeconds"))
        priority = from_union([from_int, from_none], obj.get("Priority"))
        program_id = from_union([from_str, from_none], obj.get("ProgramId"))
        program_info = from_union([BaseItemDto.from_dict, from_none], obj.get("ProgramInfo"))
        run_time_ticks = from_union([from_int, from_none], obj.get("RunTimeTicks"))
        series_timer_id = from_union([from_str, from_none], obj.get("SeriesTimerId"))
        server_id = from_union([from_str, from_none], obj.get("ServerId"))
        service_name = from_union([from_str, from_none], obj.get("ServiceName"))
        start_date = from_union([from_datetime, from_none], obj.get("StartDate"))
        status = from_union([RecordingStatusEnum, from_none], obj.get("Status"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return TimerInfoDto(channel_id, channel_name, channel_primary_image_tag, end_date, external_channel_id, external_id, external_program_id, external_series_timer_id, id, is_post_padding_required, is_pre_padding_required, keep_until, name, overview, parent_backdrop_image_tags, parent_backdrop_item_id, post_padding_seconds, pre_padding_seconds, priority, program_id, program_info, run_time_ticks, series_timer_id, server_id, service_name, start_date, status, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ChannelId"] = from_union([lambda x: str(x), from_none], self.channel_id)
        result["ChannelName"] = from_union([from_str, from_none], self.channel_name)
        result["ChannelPrimaryImageTag"] = from_union([from_str, from_none], self.channel_primary_image_tag)
        result["EndDate"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
        result["ExternalChannelId"] = from_union([from_str, from_none], self.external_channel_id)
        result["ExternalId"] = from_union([from_str, from_none], self.external_id)
        result["ExternalProgramId"] = from_union([from_str, from_none], self.external_program_id)
        result["ExternalSeriesTimerId"] = from_union([from_str, from_none], self.external_series_timer_id)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IsPostPaddingRequired"] = from_union([from_bool, from_none], self.is_post_padding_required)
        result["IsPrePaddingRequired"] = from_union([from_bool, from_none], self.is_pre_padding_required)
        result["KeepUntil"] = from_union([lambda x: to_enum(KeepUntil, x), from_none], self.keep_until)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Overview"] = from_union([from_str, from_none], self.overview)
        result["ParentBackdropImageTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.parent_backdrop_image_tags)
        result["ParentBackdropItemId"] = from_union([from_str, from_none], self.parent_backdrop_item_id)
        result["PostPaddingSeconds"] = from_union([from_int, from_none], self.post_padding_seconds)
        result["PrePaddingSeconds"] = from_union([from_int, from_none], self.pre_padding_seconds)
        result["Priority"] = from_union([from_int, from_none], self.priority)
        result["ProgramId"] = from_union([from_str, from_none], self.program_id)
        result["ProgramInfo"] = from_union([lambda x: to_class(BaseItemDto, x), from_none], self.program_info)
        result["RunTimeTicks"] = from_union([from_int, from_none], self.run_time_ticks)
        result["SeriesTimerId"] = from_union([from_str, from_none], self.series_timer_id)
        result["ServerId"] = from_union([from_str, from_none], self.server_id)
        result["ServiceName"] = from_union([from_str, from_none], self.service_name)
        result["StartDate"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        result["Status"] = from_union([lambda x: to_enum(RecordingStatusEnum, x), from_none], self.status)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


