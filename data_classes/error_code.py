from util.from_type import *


class ErrorCode(CaseInsensitiveEnum):
    """Gets or sets the error code."""
    NOT_ALLOWED = "NotAllowed"
    NO_COMPATIBLE_STREAM = "NoCompatibleStream"
    RATE_LIMIT_EXCEEDED = "RateLimitExceeded"


