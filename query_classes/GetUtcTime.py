from data_classes.u_t_c_time_response import UTCTimeResponse as UtcTimeResponse
from util.BaseRequestClass import BaseRequestClass


class GetUtcTime(BaseRequestClass):
    def get_utc_time(
            self
    ) -> UtcTimeResponse:
        """Gets the current UTC time.

        Http:
            <get>: /GetUtcTime

        Returns:
            <200> UtcTimeResponse: Time returned.
        """
        return self._get(path='/GetUtcTime', response_type=UtcTimeResponse)

