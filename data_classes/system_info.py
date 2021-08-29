from util.from_type import *
from data_classes.architecture import Architecture
from data_classes.location import Location
from data_classes.installation_info import InstallationInfo


@dataclass
class SystemInfo:
    """Class SystemInfo."""
    """Gets or sets the cache path."""
    cache_path: Optional[str] = None
    can_launch_web_browser: Optional[bool] = None
    """Gets or sets a value indicating whether this instance can self restart."""
    can_self_restart: Optional[bool] = None
    """Gets or sets the completed installations."""
    completed_installations: Optional[List[InstallationInfo]] = None
    """Enum describing the location of the FFmpeg tool."""
    encoder_location: Optional[Location] = None
    """Gets or sets a value indicating whether this instance has pending restart."""
    has_pending_restart: Optional[bool] = None
    """Gets or sets a value indicating whether this instance has update available."""
    has_update_available: Optional[bool] = None
    """Gets or sets the id."""
    id: Optional[str] = None
    """Gets or sets the internal metadata path."""
    internal_metadata_path: Optional[str] = None
    is_shutting_down: Optional[bool] = None
    """Gets or sets the items by name path."""
    items_by_name_path: Optional[str] = None
    """Gets or sets the local address."""
    local_address: Optional[str] = None
    """Gets or sets the log path."""
    log_path: Optional[str] = None
    """Gets or sets the operating system."""
    operating_system: Optional[str] = None
    """Gets or sets the display name of the operating system."""
    operating_system_display_name: Optional[str] = None
    """Get or sets the package name."""
    package_name: Optional[str] = None
    """Gets or sets the product name. This is the AssemblyProduct name."""
    product_name: Optional[str] = None
    """Gets or sets the program data path."""
    program_data_path: Optional[str] = None
    """Gets or sets the name of the server."""
    server_name: Optional[str] = None
    """Gets or sets a value indicating whether the startup wizard is completed."""
    startup_wizard_completed: Optional[bool] = None
    """Gets or sets a value indicating whether [supports library monitor]."""
    supports_library_monitor: Optional[bool] = None
    system_architecture: Optional[Architecture] = None
    """Gets or sets the transcode path."""
    transcoding_temp_path: Optional[str] = None
    """Gets or sets the server version."""
    version: Optional[str] = None
    """Gets or sets the web UI resources path."""
    web_path: Optional[str] = None
    """Gets or sets the web socket port number."""
    web_socket_port_number: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SystemInfo':
        assert isinstance(obj, dict)
        cache_path = from_union([from_str, from_none], obj.get("CachePath"))
        can_launch_web_browser = from_union([from_bool, from_none], obj.get("CanLaunchWebBrowser"))
        can_self_restart = from_union([from_bool, from_none], obj.get("CanSelfRestart"))
        completed_installations = from_union([lambda x: from_list(InstallationInfo.from_dict, x), from_none], obj.get("CompletedInstallations"))
        encoder_location = from_union([Location, from_none], obj.get("EncoderLocation"))
        has_pending_restart = from_union([from_bool, from_none], obj.get("HasPendingRestart"))
        has_update_available = from_union([from_bool, from_none], obj.get("HasUpdateAvailable"))
        id = from_union([from_str, from_none], obj.get("Id"))
        internal_metadata_path = from_union([from_str, from_none], obj.get("InternalMetadataPath"))
        is_shutting_down = from_union([from_bool, from_none], obj.get("IsShuttingDown"))
        items_by_name_path = from_union([from_str, from_none], obj.get("ItemsByNamePath"))
        local_address = from_union([from_str, from_none], obj.get("LocalAddress"))
        log_path = from_union([from_str, from_none], obj.get("LogPath"))
        operating_system = from_union([from_str, from_none], obj.get("OperatingSystem"))
        operating_system_display_name = from_union([from_str, from_none], obj.get("OperatingSystemDisplayName"))
        package_name = from_union([from_str, from_none], obj.get("PackageName"))
        product_name = from_union([from_str, from_none], obj.get("ProductName"))
        program_data_path = from_union([from_str, from_none], obj.get("ProgramDataPath"))
        server_name = from_union([from_str, from_none], obj.get("ServerName"))
        startup_wizard_completed = from_union([from_bool, from_none], obj.get("StartupWizardCompleted"))
        supports_library_monitor = from_union([from_bool, from_none], obj.get("SupportsLibraryMonitor"))
        system_architecture = from_union([Architecture, from_none], obj.get("SystemArchitecture"))
        transcoding_temp_path = from_union([from_str, from_none], obj.get("TranscodingTempPath"))
        version = from_union([from_str, from_none], obj.get("Version"))
        web_path = from_union([from_str, from_none], obj.get("WebPath"))
        web_socket_port_number = from_union([from_int, from_none], obj.get("WebSocketPortNumber"))
        return SystemInfo(cache_path, can_launch_web_browser, can_self_restart, completed_installations, encoder_location, has_pending_restart, has_update_available, id, internal_metadata_path, is_shutting_down, items_by_name_path, local_address, log_path, operating_system, operating_system_display_name, package_name, product_name, program_data_path, server_name, startup_wizard_completed, supports_library_monitor, system_architecture, transcoding_temp_path, version, web_path, web_socket_port_number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CachePath"] = from_union([from_str, from_none], self.cache_path)
        result["CanLaunchWebBrowser"] = from_union([from_bool, from_none], self.can_launch_web_browser)
        result["CanSelfRestart"] = from_union([from_bool, from_none], self.can_self_restart)
        result["CompletedInstallations"] = from_union([lambda x: from_list(lambda x: to_class(InstallationInfo, x), x), from_none], self.completed_installations)
        result["EncoderLocation"] = from_union([lambda x: to_enum(Location, x), from_none], self.encoder_location)
        result["HasPendingRestart"] = from_union([from_bool, from_none], self.has_pending_restart)
        result["HasUpdateAvailable"] = from_union([from_bool, from_none], self.has_update_available)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["InternalMetadataPath"] = from_union([from_str, from_none], self.internal_metadata_path)
        result["IsShuttingDown"] = from_union([from_bool, from_none], self.is_shutting_down)
        result["ItemsByNamePath"] = from_union([from_str, from_none], self.items_by_name_path)
        result["LocalAddress"] = from_union([from_str, from_none], self.local_address)
        result["LogPath"] = from_union([from_str, from_none], self.log_path)
        result["OperatingSystem"] = from_union([from_str, from_none], self.operating_system)
        result["OperatingSystemDisplayName"] = from_union([from_str, from_none], self.operating_system_display_name)
        result["PackageName"] = from_union([from_str, from_none], self.package_name)
        result["ProductName"] = from_union([from_str, from_none], self.product_name)
        result["ProgramDataPath"] = from_union([from_str, from_none], self.program_data_path)
        result["ServerName"] = from_union([from_str, from_none], self.server_name)
        result["StartupWizardCompleted"] = from_union([from_bool, from_none], self.startup_wizard_completed)
        result["SupportsLibraryMonitor"] = from_union([from_bool, from_none], self.supports_library_monitor)
        result["SystemArchitecture"] = from_union([lambda x: to_enum(Architecture, x), from_none], self.system_architecture)
        result["TranscodingTempPath"] = from_union([from_str, from_none], self.transcoding_temp_path)
        result["Version"] = from_union([from_str, from_none], self.version)
        result["WebPath"] = from_union([from_str, from_none], self.web_path)
        result["WebSocketPortNumber"] = from_union([from_int, from_none], self.web_socket_port_number)
        return result


