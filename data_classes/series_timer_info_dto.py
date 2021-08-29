from util.from_type import *
from data_classes.day_of_week_element import DayOfWeekElement
from data_classes.day_pattern import DayPattern
from data_classes.keep_until import KeepUntil


@dataclass
class SeriesTimerInfoDto:
    """Class SeriesTimerInfoDto."""
    """ChannelId of the recording."""
    channel_id: Optional[UUID] = None
    """ChannelName of the recording."""
    channel_name: Optional[str] = None
    channel_primary_image_tag: Optional[str] = None
    """Gets or sets the day pattern."""
    day_pattern: Optional[DayPattern] = None
    """Gets or sets the days."""
    days: Optional[List[DayOfWeekElement]] = None
    """The end date of the recording, in UTC."""
    end_date: Optional[datetime] = None
    """Gets or sets the external channel identifier."""
    external_channel_id: Optional[str] = None
    """Gets or sets the external identifier."""
    external_id: Optional[str] = None
    """Gets or sets the external program identifier."""
    external_program_id: Optional[str] = None
    """Id of the recording."""
    id: Optional[str] = None
    """Gets or sets the image tags."""
    image_tags: Optional[Dict[str, str]] = None
    """Gets or sets a value indicating whether this instance is post padding required."""
    is_post_padding_required: Optional[bool] = None
    """Gets or sets a value indicating whether this instance is pre padding required."""
    is_pre_padding_required: Optional[bool] = None
    keep_until: Optional[KeepUntil] = None
    keep_up_to: Optional[int] = None
    """Name of the recording."""
    name: Optional[str] = None
    """Description of the recording."""
    overview: Optional[str] = None
    """Gets or sets the parent backdrop image tags."""
    parent_backdrop_image_tags: Optional[List[str]] = None
    """If the item does not have any backdrops, this will hold the Id of the Parent that has one."""
    parent_backdrop_item_id: Optional[str] = None
    """Gets or sets the parent primary image item identifier."""
    parent_primary_image_item_id: Optional[str] = None
    """Gets or sets the parent primary image tag."""
    parent_primary_image_tag: Optional[str] = None
    """Gets or sets the parent thumb image tag."""
    parent_thumb_image_tag: Optional[str] = None
    """Gets or sets the parent thumb item id."""
    parent_thumb_item_id: Optional[str] = None
    """Gets or sets the post padding seconds."""
    post_padding_seconds: Optional[int] = None
    """Gets or sets the pre padding seconds."""
    pre_padding_seconds: Optional[int] = None
    """Gets or sets the priority."""
    priority: Optional[int] = None
    """Gets or sets the program identifier."""
    program_id: Optional[str] = None
    """Gets or sets a value indicating whether [record any channel]."""
    record_any_channel: Optional[bool] = None
    """Gets or sets a value indicating whether [record any time]."""
    record_any_time: Optional[bool] = None
    """Gets or sets a value indicating whether [record new only]."""
    record_new_only: Optional[bool] = None
    """Gets or sets the server identifier."""
    server_id: Optional[str] = None
    """Gets or sets the name of the service."""
    service_name: Optional[str] = None
    skip_episodes_in_library: Optional[bool] = None
    """The start date of the recording, in UTC."""
    start_date: Optional[datetime] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SeriesTimerInfoDto':
        assert isinstance(obj, dict)
        channel_id = from_union([lambda x: UUID(x), from_none], obj.get("ChannelId"))
        channel_name = from_union([from_str, from_none], obj.get("ChannelName"))
        channel_primary_image_tag = from_union([from_str, from_none], obj.get("ChannelPrimaryImageTag"))
        day_pattern = from_union([DayPattern, from_none], obj.get("DayPattern"))
        days = from_union([lambda x: from_list(DayOfWeekElement, x), from_none], obj.get("Days"))
        end_date = from_union([from_datetime, from_none], obj.get("EndDate"))
        external_channel_id = from_union([from_str, from_none], obj.get("ExternalChannelId"))
        external_id = from_union([from_str, from_none], obj.get("ExternalId"))
        external_program_id = from_union([from_str, from_none], obj.get("ExternalProgramId"))
        id = from_union([from_str, from_none], obj.get("Id"))
        image_tags = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ImageTags"))
        is_post_padding_required = from_union([from_bool, from_none], obj.get("IsPostPaddingRequired"))
        is_pre_padding_required = from_union([from_bool, from_none], obj.get("IsPrePaddingRequired"))
        keep_until = from_union([KeepUntil, from_none], obj.get("KeepUntil"))
        keep_up_to = from_union([from_int, from_none], obj.get("KeepUpTo"))
        name = from_union([from_str, from_none], obj.get("Name"))
        overview = from_union([from_str, from_none], obj.get("Overview"))
        parent_backdrop_image_tags = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ParentBackdropImageTags"))
        parent_backdrop_item_id = from_union([from_str, from_none], obj.get("ParentBackdropItemId"))
        parent_primary_image_item_id = from_union([from_str, from_none], obj.get("ParentPrimaryImageItemId"))
        parent_primary_image_tag = from_union([from_str, from_none], obj.get("ParentPrimaryImageTag"))
        parent_thumb_image_tag = from_union([from_str, from_none], obj.get("ParentThumbImageTag"))
        parent_thumb_item_id = from_union([from_str, from_none], obj.get("ParentThumbItemId"))
        post_padding_seconds = from_union([from_int, from_none], obj.get("PostPaddingSeconds"))
        pre_padding_seconds = from_union([from_int, from_none], obj.get("PrePaddingSeconds"))
        priority = from_union([from_int, from_none], obj.get("Priority"))
        program_id = from_union([from_str, from_none], obj.get("ProgramId"))
        record_any_channel = from_union([from_bool, from_none], obj.get("RecordAnyChannel"))
        record_any_time = from_union([from_bool, from_none], obj.get("RecordAnyTime"))
        record_new_only = from_union([from_bool, from_none], obj.get("RecordNewOnly"))
        server_id = from_union([from_str, from_none], obj.get("ServerId"))
        service_name = from_union([from_str, from_none], obj.get("ServiceName"))
        skip_episodes_in_library = from_union([from_bool, from_none], obj.get("SkipEpisodesInLibrary"))
        start_date = from_union([from_datetime, from_none], obj.get("StartDate"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return SeriesTimerInfoDto(channel_id, channel_name, channel_primary_image_tag, day_pattern, days, end_date, external_channel_id, external_id, external_program_id, id, image_tags, is_post_padding_required, is_pre_padding_required, keep_until, keep_up_to, name, overview, parent_backdrop_image_tags, parent_backdrop_item_id, parent_primary_image_item_id, parent_primary_image_tag, parent_thumb_image_tag, parent_thumb_item_id, post_padding_seconds, pre_padding_seconds, priority, program_id, record_any_channel, record_any_time, record_new_only, server_id, service_name, skip_episodes_in_library, start_date, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ChannelId"] = from_union([lambda x: str(x), from_none], self.channel_id)
        result["ChannelName"] = from_union([from_str, from_none], self.channel_name)
        result["ChannelPrimaryImageTag"] = from_union([from_str, from_none], self.channel_primary_image_tag)
        result["DayPattern"] = from_union([lambda x: to_enum(DayPattern, x), from_none], self.day_pattern)
        result["Days"] = from_union([lambda x: from_list(lambda x: to_enum(DayOfWeekElement, x), x), from_none], self.days)
        result["EndDate"] = from_union([lambda x: x.isoformat(), from_none], self.end_date)
        result["ExternalChannelId"] = from_union([from_str, from_none], self.external_channel_id)
        result["ExternalId"] = from_union([from_str, from_none], self.external_id)
        result["ExternalProgramId"] = from_union([from_str, from_none], self.external_program_id)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["ImageTags"] = from_union([lambda x: from_dict(from_str, x), from_none], self.image_tags)
        result["IsPostPaddingRequired"] = from_union([from_bool, from_none], self.is_post_padding_required)
        result["IsPrePaddingRequired"] = from_union([from_bool, from_none], self.is_pre_padding_required)
        result["KeepUntil"] = from_union([lambda x: to_enum(KeepUntil, x), from_none], self.keep_until)
        result["KeepUpTo"] = from_union([from_int, from_none], self.keep_up_to)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Overview"] = from_union([from_str, from_none], self.overview)
        result["ParentBackdropImageTags"] = from_union([lambda x: from_list(from_str, x), from_none], self.parent_backdrop_image_tags)
        result["ParentBackdropItemId"] = from_union([from_str, from_none], self.parent_backdrop_item_id)
        result["ParentPrimaryImageItemId"] = from_union([from_str, from_none], self.parent_primary_image_item_id)
        result["ParentPrimaryImageTag"] = from_union([from_str, from_none], self.parent_primary_image_tag)
        result["ParentThumbImageTag"] = from_union([from_str, from_none], self.parent_thumb_image_tag)
        result["ParentThumbItemId"] = from_union([from_str, from_none], self.parent_thumb_item_id)
        result["PostPaddingSeconds"] = from_union([from_int, from_none], self.post_padding_seconds)
        result["PrePaddingSeconds"] = from_union([from_int, from_none], self.pre_padding_seconds)
        result["Priority"] = from_union([from_int, from_none], self.priority)
        result["ProgramId"] = from_union([from_str, from_none], self.program_id)
        result["RecordAnyChannel"] = from_union([from_bool, from_none], self.record_any_channel)
        result["RecordAnyTime"] = from_union([from_bool, from_none], self.record_any_time)
        result["RecordNewOnly"] = from_union([from_bool, from_none], self.record_new_only)
        result["ServerId"] = from_union([from_str, from_none], self.server_id)
        result["ServiceName"] = from_union([from_str, from_none], self.service_name)
        result["SkipEpisodesInLibrary"] = from_union([from_bool, from_none], self.skip_episodes_in_library)
        result["StartDate"] = from_union([lambda x: x.isoformat(), from_none], self.start_date)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


