from util.from_type import *


@dataclass
class PublicSystemInfo:
    """Gets or sets the id."""
    id: Optional[str] = None
    """Gets or sets the local address."""
    local_address: Optional[str] = None
    """Gets or sets the operating system."""
    operating_system: Optional[str] = None
    """Gets or sets the product name. This is the AssemblyProduct name."""
    product_name: Optional[str] = None
    """Gets or sets the name of the server."""
    server_name: Optional[str] = None
    """Gets or sets a value indicating whether the startup wizard is completed."""
    startup_wizard_completed: Optional[bool] = None
    """Gets or sets the server version."""
    version: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PublicSystemInfo':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("Id"))
        local_address = from_union([from_str, from_none], obj.get("LocalAddress"))
        operating_system = from_union([from_str, from_none], obj.get("OperatingSystem"))
        product_name = from_union([from_str, from_none], obj.get("ProductName"))
        server_name = from_union([from_str, from_none], obj.get("ServerName"))
        startup_wizard_completed = from_union([from_bool, from_none], obj.get("StartupWizardCompleted"))
        version = from_union([from_str, from_none], obj.get("Version"))
        return PublicSystemInfo(id, local_address, operating_system, product_name, server_name, startup_wizard_completed, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_union([from_str, from_none], self.id)
        result["LocalAddress"] = from_union([from_str, from_none], self.local_address)
        result["OperatingSystem"] = from_union([from_str, from_none], self.operating_system)
        result["ProductName"] = from_union([from_str, from_none], self.product_name)
        result["ServerName"] = from_union([from_str, from_none], self.server_name)
        result["StartupWizardCompleted"] = from_union([from_bool, from_none], self.startup_wizard_completed)
        result["Version"] = from_union([from_str, from_none], self.version)
        return result


