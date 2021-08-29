from data_classes.image_option import ImageOption
from data_classes.image_type_element import ImageTypeElement
from data_classes.library_option_info_dto import LibraryOptionInfoDto
from util.from_type import *


@dataclass
class LibraryTypeOptionsDto:
    """Library type options dto."""
    """Gets or sets the default image options."""
    default_image_options: Optional[List[ImageOption]] = None
    """Gets or sets the image fetchers."""
    image_fetchers: Optional[List[LibraryOptionInfoDto]] = None
    """Gets or sets the metadata fetchers."""
    metadata_fetchers: Optional[List[LibraryOptionInfoDto]] = None
    """Gets or sets the supported image types."""
    supported_image_types: Optional[List[ImageTypeElement]] = None
    """Gets or sets the type."""
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LibraryTypeOptionsDto':
        assert isinstance(obj, dict)
        default_image_options = from_union([lambda x: from_list(ImageOption.from_dict, x), from_none], obj.get("DefaultImageOptions"))
        image_fetchers = from_union([lambda x: from_list(LibraryOptionInfoDto.from_dict, x), from_none], obj.get("ImageFetchers"))
        metadata_fetchers = from_union([lambda x: from_list(LibraryOptionInfoDto.from_dict, x), from_none], obj.get("MetadataFetchers"))
        supported_image_types = from_union([lambda x: from_list(ImageTypeElement, x), from_none], obj.get("SupportedImageTypes"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return LibraryTypeOptionsDto(default_image_options, image_fetchers, metadata_fetchers, supported_image_types, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["DefaultImageOptions"] = from_union([lambda x: from_list(lambda x: to_class(ImageOption, x), x), from_none], self.default_image_options)
        result["ImageFetchers"] = from_union([lambda x: from_list(lambda x: to_class(LibraryOptionInfoDto, x), x), from_none], self.image_fetchers)
        result["MetadataFetchers"] = from_union([lambda x: from_list(lambda x: to_class(LibraryOptionInfoDto, x), x), from_none], self.metadata_fetchers)
        result["SupportedImageTypes"] = from_union([lambda x: from_list(lambda x: to_enum(ImageTypeElement, x), x), from_none], self.supported_image_types)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


