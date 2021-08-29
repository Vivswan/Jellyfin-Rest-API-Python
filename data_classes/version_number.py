from util.from_type import *


@dataclass
class VersionNumber:
    """Gets the version as a System.Version.
    
    Gets or sets the version.
    
    Gets the plugin version.
    
    Gets or sets the last known version that was ran using the configuration.
    """
    build: Optional[int] = None
    major: Optional[int] = None
    major_revision: Optional[int] = None
    minor: Optional[int] = None
    minor_revision: Optional[int] = None
    revision: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'VersionNumber':
        assert isinstance(obj, dict)
        build = from_union([from_int, from_none], obj.get("Build"))
        major = from_union([from_int, from_none], obj.get("Major"))
        major_revision = from_union([from_int, from_none], obj.get("MajorRevision"))
        minor = from_union([from_int, from_none], obj.get("Minor"))
        minor_revision = from_union([from_int, from_none], obj.get("MinorRevision"))
        revision = from_union([from_int, from_none], obj.get("Revision"))
        return VersionNumber(build, major, major_revision, minor, minor_revision, revision)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Build"] = from_union([from_int, from_none], self.build)
        result["Major"] = from_union([from_int, from_none], self.major)
        result["MajorRevision"] = from_union([from_int, from_none], self.major_revision)
        result["Minor"] = from_union([from_int, from_none], self.minor)
        result["MinorRevision"] = from_union([from_int, from_none], self.minor_revision)
        result["Revision"] = from_union([from_int, from_none], self.revision)
        return result


