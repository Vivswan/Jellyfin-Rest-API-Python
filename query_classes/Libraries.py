from typing import Optional

from data_classes.library_options_result_dto import LibraryOptionsResultDto as LibraryOptionsResultDto
from util.BaseRequestClass import BaseRequestClass


class Libraries(BaseRequestClass):
    def get_library_options_info(
            self, 
            library_content_type: Optional[str] = None, 
            is_new_library: Optional[bool] = False
    ) -> LibraryOptionsResultDto:
        """Gets the library options info.

        Http:
            <get>: /Libraries/AvailableOptions

        Args:
            library_content_type (str): Library content type.
            is_new_library (bool = False): Whether this is a new library.

        Returns:
            <200> LibraryOptionsResultDto: Library options info returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            libraryContentType=library_content_type,
            isNewLibrary=is_new_library,
        )
        return self._get(path='/Libraries/AvailableOptions', request_args=request_args, response_type=LibraryOptionsResultDto)

