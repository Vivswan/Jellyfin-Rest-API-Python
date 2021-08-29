import requests
from util.BaseRequestClass import BaseRequestClass


class Providers(BaseRequestClass):
    def get_remote_subtitles(
            self, 
            id: str
    ) -> requests.Response:
        """Gets the remote subtitles.

        Http:
            <get>: /Providers/Subtitles/Subtitles/{id}

        Args:
            id (str): The item id.

        Returns:
            <200> requests.Response: File returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._get(path='/Providers/Subtitles/Subtitles/{id}', request_args=request_args)

