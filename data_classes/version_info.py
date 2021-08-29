from util.from_type import *
from data_classes.version_number import VersionNumber


@dataclass
class VersionInfo:
    """Defines the MediaBrowser.Model.Updates.VersionInfo class."""
    """Gets or sets the changelog for this version."""
    changelog: Optional[str] = None
    """Gets or sets a checksum for the binary."""
    checksum: Optional[str] = None
    """Gets or sets the repository name."""
    repository_name: Optional[str] = None
    """Gets or sets the repository url."""
    repository_url: Optional[str] = None
    """Gets or sets the source URL."""
    source_url: Optional[str] = None
    """Gets or sets the ABI that this version was built against."""
    target_abi: Optional[str] = None
    """Gets or sets a timestamp of when the binary was built."""
    timestamp: Optional[str] = None
    """Gets or sets the version."""
    version: Optional[str] = None
    """Gets the version as a System.Version."""
    version_number: Optional[VersionNumber] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VersionInfo':
        assert isinstance(obj, dict)
        changelog = from_union([from_str, from_none], obj.get("changelog"))
        checksum = from_union([from_str, from_none], obj.get("checksum"))
        repository_name = from_union([from_str, from_none], obj.get("repositoryName"))
        repository_url = from_union([from_str, from_none], obj.get("repositoryUrl"))
        source_url = from_union([from_str, from_none], obj.get("sourceUrl"))
        target_abi = from_union([from_str, from_none], obj.get("targetAbi"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        version = from_union([from_str, from_none], obj.get("version"))
        version_number = from_union([VersionNumber.from_dict, from_none], obj.get("VersionNumber"))
        return VersionInfo(changelog, checksum, repository_name, repository_url, source_url, target_abi, timestamp, version, version_number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["changelog"] = from_union([from_str, from_none], self.changelog)
        result["checksum"] = from_union([from_str, from_none], self.checksum)
        result["repositoryName"] = from_union([from_str, from_none], self.repository_name)
        result["repositoryUrl"] = from_union([from_str, from_none], self.repository_url)
        result["sourceUrl"] = from_union([from_str, from_none], self.source_url)
        result["targetAbi"] = from_union([from_str, from_none], self.target_abi)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        result["version"] = from_union([from_str, from_none], self.version)
        result["VersionNumber"] = from_union([lambda x: to_class(VersionNumber, x), from_none], self.version_number)
        return result


