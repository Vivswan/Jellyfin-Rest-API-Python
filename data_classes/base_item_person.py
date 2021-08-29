from data_classes.base_item_person_image_blur_hashes import BaseItemPersonImageBlurHashes
from util.from_type import *


@dataclass
class BaseItemPerson:
    """This is used by the api to get information about a Person within a BaseItem."""
    """Gets or sets the identifier."""
    id: Optional[str] = None
    """Gets or sets the primary image blurhash."""
    image_blur_hashes: Optional[BaseItemPersonImageBlurHashes] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets the primary image tag."""
    primary_image_tag: Optional[str] = None
    """Gets or sets the role."""
    role: Optional[str] = None
    """Gets or sets the type."""
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BaseItemPerson':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        image_blur_hashes = from_union([BaseItemPersonImageBlurHashes.from_dict, from_none], obj.get("ImageBlurHashes"))
        name = from_union([from_str, from_none], obj.get("Name"))
        primary_image_tag = from_union([from_str, from_none], obj.get("PrimaryImageTag"))
        role = from_union([from_str, from_none], obj.get("Role"))
        type = from_union([from_str, from_none], obj.get("Type"))
        return BaseItemPerson(id, image_blur_hashes, name, primary_image_tag, role, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["ImageBlurHashes"] = from_union([lambda x: to_class(BaseItemPersonImageBlurHashes, x), from_none], self.image_blur_hashes)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["PrimaryImageTag"] = from_union([from_str, from_none], self.primary_image_tag)
        result["Role"] = from_union([from_str, from_none], self.role)
        result["Type"] = from_union([from_str, from_none], self.type)
        return result


