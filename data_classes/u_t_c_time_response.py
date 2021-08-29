from util.from_type import *


@dataclass
class UTCTimeResponse:
    """Class UtcTimeResponse."""
    """Gets the UTC time when request has been received."""
    request_reception_time: Optional[datetime] = None
    """Gets the UTC time when response has been sent."""
    response_transmission_time: Optional[datetime] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UTCTimeResponse':
        assert isinstance(obj, dict)
        request_reception_time = from_union([from_datetime, from_none], obj.get("RequestReceptionTime"))
        response_transmission_time = from_union([from_datetime, from_none], obj.get("ResponseTransmissionTime"))
        return UTCTimeResponse(request_reception_time, response_transmission_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["RequestReceptionTime"] = from_union([lambda x: x.isoformat(), from_none], self.request_reception_time)
        result["ResponseTransmissionTime"] = from_union([lambda x: x.isoformat(), from_none], self.response_transmission_time)
        return result


