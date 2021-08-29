from data_classes.file_organizer_type_enum import FileOrganizerTypeEnum
from data_classes.file_sorting_status_enum import FileSortingStatusEnum
from util.from_type import *


@dataclass
class FileOrganizationResult:
    date: Optional[datetime] = None
    duplicate_paths: Optional[List[str]] = None
    extracted_ending_episode_number: Optional[int] = None
    extracted_episode_number: Optional[int] = None
    extracted_name: Optional[str] = None
    extracted_season_number: Optional[int] = None
    extracted_year: Optional[int] = None
    file_size: Optional[int] = None
    id: Optional[str] = None
    is_in_progress: Optional[bool] = None
    original_file_name: Optional[str] = None
    original_path: Optional[str] = None
    status: Optional[FileSortingStatusEnum] = None
    status_message: Optional[str] = None
    target_path: Optional[str] = None
    type: Optional[FileOrganizerTypeEnum] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileOrganizationResult':
        assert isinstance(obj, dict)
        date = from_union([from_datetime, from_none], obj.get("Date"))
        duplicate_paths = from_union([lambda x: from_list(from_str, x), from_none], obj.get("DuplicatePaths"))
        extracted_ending_episode_number = from_union([from_int, from_none], obj.get("ExtractedEndingEpisodeNumber"))
        extracted_episode_number = from_union([from_int, from_none], obj.get("ExtractedEpisodeNumber"))
        extracted_name = from_union([from_str, from_none], obj.get("ExtractedName"))
        extracted_season_number = from_union([from_int, from_none], obj.get("ExtractedSeasonNumber"))
        extracted_year = from_union([from_int, from_none], obj.get("ExtractedYear"))
        file_size = from_union([from_int, from_none], obj.get("FileSize"))
        id = from_union([from_str, from_none], obj.get("Id"))
        is_in_progress = from_union([from_bool, from_none], obj.get("IsInProgress"))
        original_file_name = from_union([from_str, from_none], obj.get("OriginalFileName"))
        original_path = from_union([from_str, from_none], obj.get("OriginalPath"))
        status = from_union([FileSortingStatusEnum, from_none], obj.get("Status"))
        status_message = from_union([from_str, from_none], obj.get("StatusMessage"))
        target_path = from_union([from_str, from_none], obj.get("TargetPath"))
        type = from_union([FileOrganizerTypeEnum, from_none], obj.get("Type"))
        return FileOrganizationResult(date, duplicate_paths, extracted_ending_episode_number, extracted_episode_number, extracted_name, extracted_season_number, extracted_year, file_size, id, is_in_progress, original_file_name, original_path, status, status_message, target_path, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Date"] = from_union([lambda x: x.isoformat(), from_none], self.date)
        result["DuplicatePaths"] = from_union([lambda x: from_list(from_str, x), from_none], self.duplicate_paths)
        result["ExtractedEndingEpisodeNumber"] = from_union([from_int, from_none], self.extracted_ending_episode_number)
        result["ExtractedEpisodeNumber"] = from_union([from_int, from_none], self.extracted_episode_number)
        result["ExtractedName"] = from_union([from_str, from_none], self.extracted_name)
        result["ExtractedSeasonNumber"] = from_union([from_int, from_none], self.extracted_season_number)
        result["ExtractedYear"] = from_union([from_int, from_none], self.extracted_year)
        result["FileSize"] = from_union([from_int, from_none], self.file_size)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IsInProgress"] = from_union([from_bool, from_none], self.is_in_progress)
        result["OriginalFileName"] = from_union([from_str, from_none], self.original_file_name)
        result["OriginalPath"] = from_union([from_str, from_none], self.original_path)
        result["Status"] = from_union([lambda x: to_enum(FileSortingStatusEnum, x), from_none], self.status)
        result["StatusMessage"] = from_union([from_str, from_none], self.status_message)
        result["TargetPath"] = from_union([from_str, from_none], self.target_path)
        result["Type"] = from_union([lambda x: to_enum(FileOrganizerTypeEnum, x), from_none], self.type)
        return result


