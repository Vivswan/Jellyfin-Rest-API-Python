from util.from_type import *


@dataclass
class StartupRemoteAccessDto:
    """Startup remote access dto."""
    """Gets or sets a value indicating whether enable automatic port mapping."""
    enable_automatic_port_mapping: bool
    """Gets or sets a value indicating whether enable remote access."""
    enable_remote_access: bool

    @staticmethod
    def from_dict(obj: Any) -> 'StartupRemoteAccessDto':
        assert isinstance(obj, dict)
        enable_automatic_port_mapping = from_bool(obj.get("EnableAutomaticPortMapping"))
        enable_remote_access = from_bool(obj.get("EnableRemoteAccess"))
        return StartupRemoteAccessDto(enable_automatic_port_mapping, enable_remote_access)

    def to_dict(self) -> dict:
        result: dict = {}
        result["EnableAutomaticPortMapping"] = from_bool(self.enable_automatic_port_mapping)
        result["EnableRemoteAccess"] = from_bool(self.enable_remote_access)
        return result


