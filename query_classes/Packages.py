import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.package_info import PackageInfo as PackageInfo


class Packages(BaseRequestClass):
    def get_packages(
            self
    ) -> List[PackageInfo]:
        """Gets available packages.

        Http:
            <get>: /Packages

        Returns:
            <200> List[PackageInfo]: Available packages returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Packages', response_type=List[PackageInfo])

    def get_package_info(
            self, 
            name: str, 
            assembly_guid: Optional[str] = None
    ) -> PackageInfo:
        """Gets a package by name or assembly GUID.

        Http:
            <get>: /Packages/{name}

        Args:
            name (str): The name of the package.
            assembly_guid (str): The GUID of the associated assembly.

        Returns:
            <200> PackageInfo: Package retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            assemblyGuid=assembly_guid,
        )
        return self._get(path='/Packages/{name}', request_args=request_args, response_type=PackageInfo)

    def install_package(
            self, 
            name: str, 
            assembly_guid: Optional[str] = None, 
            version: Optional[str] = None, 
            repository_url: Optional[str] = None
    ) -> requests.Response:
        """Installs a package.

        Http:
            <post>: /Packages/Installed/{name}

        Args:
            name (str): Package name.
            assembly_guid (str): GUID of the associated assembly.
            version (str): Optional version. Defaults to latest version.
            repository_url (str): Optional. Specify the repository to install from.

        Returns:
            <204> requests.Response: Package found.
            <404> requests.Response: Package not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            assemblyGuid=assembly_guid,
            version=version,
            repositoryUrl=repository_url,
        )
        return self._post(path='/Packages/Installed/{name}', request_args=request_args)

    def cancel_package_installation(
            self, 
            package_id: str
    ) -> requests.Response:
        """Cancels a package installation.

        Http:
            <delete>: /Packages/Installing/{packageId}

        Args:
            package_id (str): Installation Id.

        Returns:
            <204> requests.Response: Installation cancelled.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            packageId=package_id,
        )
        return self._delete(path='/Packages/Installing/{packageId}', request_args=request_args)

