from data_classes.library_option_info_dto import LibraryOptionInfoDto
from data_classes.library_type_options_dto import LibraryTypeOptionsDto
from util.from_type import *


@dataclass
class LibraryOptionsResultDto:
    """Library options result dto."""
    """Gets or sets the metadata readers."""
    metadata_readers: Optional[List[LibraryOptionInfoDto]] = None
    """Gets or sets the metadata savers."""
    metadata_savers: Optional[List[LibraryOptionInfoDto]] = None
    """Gets or sets the subtitle fetchers."""
    subtitle_fetchers: Optional[List[LibraryOptionInfoDto]] = None
    """Gets or sets the type options."""
    type_options: Optional[List[LibraryTypeOptionsDto]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LibraryOptionsResultDto':
        assert isinstance(obj, dict)
        metadata_readers = from_union([lambda x: from_list(LibraryOptionInfoDto.from_dict, x), from_none], obj.get("MetadataReaders"))
        metadata_savers = from_union([lambda x: from_list(LibraryOptionInfoDto.from_dict, x), from_none], obj.get("MetadataSavers"))
        subtitle_fetchers = from_union([lambda x: from_list(LibraryOptionInfoDto.from_dict, x), from_none], obj.get("SubtitleFetchers"))
        type_options = from_union([lambda x: from_list(LibraryTypeOptionsDto.from_dict, x), from_none], obj.get("TypeOptions"))
        return LibraryOptionsResultDto(metadata_readers, metadata_savers, subtitle_fetchers, type_options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MetadataReaders"] = from_union([lambda x: from_list(lambda x: to_class(LibraryOptionInfoDto, x), x), from_none], self.metadata_readers)
        result["MetadataSavers"] = from_union([lambda x: from_list(lambda x: to_class(LibraryOptionInfoDto, x), x), from_none], self.metadata_savers)
        result["SubtitleFetchers"] = from_union([lambda x: from_list(lambda x: to_class(LibraryOptionInfoDto, x), x), from_none], self.subtitle_fetchers)
        result["TypeOptions"] = from_union([lambda x: from_list(lambda x: to_class(LibraryTypeOptionsDto, x), x), from_none], self.type_options)
        return result


