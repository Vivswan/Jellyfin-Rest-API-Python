from util.from_type import *
from data_classes.version_info import VersionInfo


@dataclass
class PackageInfo:
    """Gets or sets package information for the installation.
    
    Class PackageInfo.
    """
    """Gets or sets the category."""
    category: Optional[str] = None
    """Gets or sets a long description of the plugin containing features or helpful explanations."""
    description: Optional[str] = None
    """Gets or sets the guid of the assembly associated with this plugin.
    This is used to identify the proper item for automatic updates.
    """
    guid: Optional[str] = None
    """Gets or sets the image url for the package."""
    image_url: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets a short overview of what the plugin does."""
    overview: Optional[str] = None
    """Gets or sets the owner."""
    owner: Optional[str] = None
    """Gets or sets the versions."""
    versions: Optional[List[VersionInfo]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PackageInfo':
        assert isinstance(obj, dict)
        category = from_union([from_str, from_none], obj.get("category"))
        description = from_union([from_str, from_none], obj.get("description"))
        guid = from_union([from_str, from_none], obj.get("guid"))
        image_url = from_union([from_str, from_none], obj.get("imageUrl"))
        name = from_union([from_str, from_none], obj.get("name"))
        overview = from_union([from_str, from_none], obj.get("overview"))
        owner = from_union([from_str, from_none], obj.get("owner"))
        versions = from_union([lambda x: from_list(VersionInfo.from_dict, x), from_none], obj.get("versions"))
        return PackageInfo(category, description, guid, image_url, name, overview, owner, versions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["category"] = from_union([from_str, from_none], self.category)
        result["description"] = from_union([from_str, from_none], self.description)
        result["guid"] = from_union([from_str, from_none], self.guid)
        result["imageUrl"] = from_union([from_str, from_none], self.image_url)
        result["name"] = from_union([from_str, from_none], self.name)
        result["overview"] = from_union([from_str, from_none], self.overview)
        result["owner"] = from_union([from_str, from_none], self.owner)
        result["versions"] = from_union([lambda x: from_list(lambda x: to_class(VersionInfo, x), x), from_none], self.versions)
        return result


