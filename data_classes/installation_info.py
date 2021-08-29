from data_classes.package_info import PackageInfo
from data_classes.version_number import VersionNumber
from util.from_type import *


@dataclass
class InstallationInfo:
    """Class InstallationInfo."""
    """Gets or sets the changelog for this version."""
    changelog: Optional[str] = None
    """Gets or sets a checksum for the binary."""
    checksum: Optional[str] = None
    """Gets or sets the Id."""
    guid: Optional[UUID] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    """Gets or sets package information for the installation."""
    package_info: Optional[PackageInfo] = None
    """Gets or sets the source URL."""
    source_url: Optional[str] = None
    """Gets or sets the version."""
    version: Optional[VersionNumber] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InstallationInfo':
        assert isinstance(obj, dict)
        changelog = from_union([from_str, from_none], obj.get("Changelog"))
        checksum = from_union([from_str, from_none], obj.get("Checksum"))
        guid = from_union([lambda x: UUID(x), from_none], obj.get("Guid"))
        name = from_union([from_str, from_none], obj.get("Name"))
        package_info = from_union([PackageInfo.from_dict, from_none], obj.get("PackageInfo"))
        source_url = from_union([from_str, from_none], obj.get("SourceUrl"))
        version = from_union([VersionNumber.from_dict, from_none], obj.get("Version"))
        return InstallationInfo(changelog, checksum, guid, name, package_info, source_url, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Changelog"] = from_union([from_str, from_none], self.changelog)
        result["Checksum"] = from_union([from_str, from_none], self.checksum)
        result["Guid"] = from_union([lambda x: str(x), from_none], self.guid)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["PackageInfo"] = from_union([lambda x: to_class(PackageInfo, x), from_none], self.package_info)
        result["SourceUrl"] = from_union([from_str, from_none], self.source_url)
        result["Version"] = from_union([lambda x: to_class(VersionNumber, x), from_none], self.version)
        return result


