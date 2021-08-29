import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional


class Playback(BaseRequestClass):
    def get_bitrate_test_bytes(
            self, 
            size: Optional[int] = 102400
    ) -> requests.Response:
        """Tests the network with a request with the size of the bitrate.

        Http:
            <get>: /Playback/BitrateTest

        Args:
            size (int = 102400): The bitrate. Defaults to 102400.

        Returns:
            <200> requests.Response: Test buffer returned.
            <400> requests.Response: Size has to be a numer between 0 and 10,000,000.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            size=size,
        )
        return self._get(path='/Playback/BitrateTest', request_args=request_args)

