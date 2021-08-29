from util.from_type import *


class MetadataRefreshMode(CaseInsensitiveEnum):
    DEFAULT = "Default"
    FULL_REFRESH = "FullRefresh"
    NONE = "None"
    VALIDATION_ONLY = "ValidationOnly"


