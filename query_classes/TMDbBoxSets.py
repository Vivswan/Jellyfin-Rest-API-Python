import requests
from util.BaseRequestClass import BaseRequestClass


class TMDbBoxSets(BaseRequestClass):
    def refresh_metadata_request(
            self
    ) -> requests.Response:
        """
        Http:
            <post>: /TMDbBoxSets/Refresh

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/TMDbBoxSets/Refresh')

