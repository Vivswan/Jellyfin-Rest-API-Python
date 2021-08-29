from typing import List

import requests

from data_classes.font_file import FontFile as FontFile
from util.BaseRequestClass import BaseRequestClass


class FallbackFont(BaseRequestClass):
    def get_fallback_font_list(
            self
    ) -> List[FontFile]:
        """Gets a list of available fallback font files.

        Http:
            <get>: /FallbackFont/Fonts

        Returns:
            <200> List[FontFile]: Information retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/FallbackFont/Fonts', response_type=List[FontFile])

    def get_fallback_font(
            self, 
            name: str
    ) -> requests.Response:
        """Gets a fallback font file.

        Http:
            <get>: /FallbackFont/Fonts/{name}

        Args:
            name (str): The name of the fallback font file to get.

        Returns:
            <200> requests.Response: Fallback font file retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
        )
        return self._get(path='/FallbackFont/Fonts/{name}', request_args=request_args)

