from util.from_type import *


class PluginStatusEnum(CaseInsensitiveEnum):
    """Gets or sets a value indicating the status of the plugin.
    
    Plugin load status.
    """
    ACTIVE = "Active"
    DELETED = "Deleted"
    DISABLED = "Disabled"
    MALFUNCTIONED = "Malfunctioned"
    NOT_SUPPORTED = "NotSupported"
    RESTART = "Restart"
    SUPERCEDED = "Superceded"


