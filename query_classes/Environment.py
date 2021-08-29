from typing import List
from typing import Optional

import requests

from data_classes.default_directory_browser_info_dto import \
    DefaultDirectoryBrowserInfoDto as DefaultDirectoryBrowserInfoDto
from data_classes.file_system_entry_info import FileSystemEntryInfo as FileSystemEntryInfo
from data_classes.validate_path_dto import ValidatePathDto as ValidatePathDto
from util.BaseRequestClass import BaseRequestClass


class Environment(BaseRequestClass):
    def get_default_directory_browser(
            self
    ) -> DefaultDirectoryBrowserInfoDto:
        """Get Default directory browser.

        Http:
            <get>: /Environment/DefaultDirectoryBrowser

        Returns:
            <200> DefaultDirectoryBrowserInfoDto: Default directory browser returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Environment/DefaultDirectoryBrowser', response_type=DefaultDirectoryBrowserInfoDto)

    def get_directory_contents(
            self, 
            path: str, 
            include_files: Optional[bool] = False, 
            include_directories: Optional[bool] = False
    ) -> List[FileSystemEntryInfo]:
        """Gets the contents of a given directory in the file system.

        Http:
            <get>: /Environment/DirectoryContents

        Args:
            path (str): The path.
            include_files (bool = False): An optional filter to include or exclude files from the results. true/false.
            include_directories (bool = False): An optional filter to include or exclude folders from the results. true/false.

        Returns:
            <200> List[FileSystemEntryInfo]: Directory contents returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            path=path,
            includeFiles=include_files,
            includeDirectories=include_directories,
        )
        return self._get(path='/Environment/DirectoryContents', request_args=request_args, response_type=List[FileSystemEntryInfo])

    def get_drives(
            self
    ) -> List[FileSystemEntryInfo]:
        """Gets available drives from the server's file system.

        Http:
            <get>: /Environment/Drives

        Returns:
            <200> List[FileSystemEntryInfo]: List of entries returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Environment/Drives', response_type=List[FileSystemEntryInfo])

    def get_parent_path(
            self, 
            path: str
    ) -> str:
        """Gets the parent path of a given path.

        Http:
            <get>: /Environment/ParentPath

        Args:
            path (str): The path.

        Returns:
            <200> str: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            path=path,
        )
        return self._get(path='/Environment/ParentPath', request_args=request_args, response_type=str)

    def validate_path(
            self, 
            request_body: ValidatePathDto
    ) -> requests.Response:
        """Validates path.

        Http:
            <post>: /Environment/ValidatePath

        Args:
            request_body (ValidatePathDto): Validate request object.

        Returns:
            <204> requests.Response: Path validated.
            <404> requests.Response: Path not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Environment/ValidatePath', request_args=request_args)

