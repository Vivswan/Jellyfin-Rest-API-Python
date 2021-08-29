import requests
from util.BaseRequestClass import BaseRequestClass
from typing import List
from data_classes.repository_info import RepositoryInfo as RepositoryInfo


class Repositories(BaseRequestClass):
    def get_repositories(
            self
    ) -> List[RepositoryInfo]:
        """Gets all package repositories.

        Http:
            <get>: /Repositories

        Returns:
            <200> List[RepositoryInfo]: Package repositories returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Repositories', response_type=List[RepositoryInfo])

    def set_repositories(
            self, 
            request_body: List[RepositoryInfo]
    ) -> requests.Response:
        """Sets the enabled and existing package repositories.

        Http:
            <post>: /Repositories

        Args:
            request_body (List[RepositoryInfo]): The list of package repositories.

        Returns:
            <204> requests.Response: Package repositories saved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Repositories', request_args=request_args)

