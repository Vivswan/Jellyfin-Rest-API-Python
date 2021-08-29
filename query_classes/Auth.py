from typing import List

import requests

from data_classes.authentication_info_query_result import AuthenticationInfoQueryResult as AuthenticationInfoQueryResult
from data_classes.name_i_d_pair import NameIDPair as NameIdPair
from util.BaseRequestClass import BaseRequestClass


class Auth(BaseRequestClass):
    def get_keys(
            self
    ) -> AuthenticationInfoQueryResult:
        """Get all keys.

        Http:
            <get>: /Auth/Keys

        Returns:
            <200> AuthenticationInfoQueryResult: Api keys retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Auth/Keys', response_type=AuthenticationInfoQueryResult)

    def create_key(
            self, 
            app: str
    ) -> requests.Response:
        """Create a new api key.

        Http:
            <post>: /Auth/Keys

        Args:
            app (str): Name of the app using the authentication key.

        Returns:
            <204> requests.Response: Api key created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            app=app,
        )
        return self._post(path='/Auth/Keys', request_args=request_args)

    def revoke_key(
            self, 
            key: str
    ) -> requests.Response:
        """Remove an api key.

        Http:
            <delete>: /Auth/Keys/{key}

        Args:
            key (str): The access token to delete.

        Returns:
            <204> requests.Response: Api key deleted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            key=key,
        )
        return self._delete(path='/Auth/Keys/{key}', request_args=request_args)

    def get_password_reset_providers(
            self
    ) -> List[NameIdPair]:
        """Get all password reset providers.

        Http:
            <get>: /Auth/PasswordResetProviders

        Returns:
            <200> List[NameIdPair]: Password reset providers retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Auth/PasswordResetProviders', response_type=List[NameIdPair])

    def get_auth_providers(
            self
    ) -> List[NameIdPair]:
        """Get all auth providers.

        Http:
            <get>: /Auth/Providers

        Returns:
            <200> List[NameIdPair]: Auth providers retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Auth/Providers', response_type=List[NameIdPair])

