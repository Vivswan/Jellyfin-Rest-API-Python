import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from data_classes.startup_user_dto import StartupUserDto as StartupUserDto
from data_classes.startup_remote_access_dto import StartupRemoteAccessDto as StartupRemoteAccessDto
from data_classes.startup_configuration_dto import StartupConfigurationDto as StartupConfigurationDto


class Startup(BaseRequestClass):
    def complete_wizard(
            self
    ) -> requests.Response:
        """Completes the startup wizard.

        Http:
            <post>: /Startup/Complete

        Returns:
            <204> requests.Response: Startup wizard completed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/Startup/Complete')

    def get_startup_configuration(
            self
    ) -> StartupConfigurationDto:
        """Gets the initial startup wizard configuration.

        Http:
            <get>: /Startup/Configuration

        Returns:
            <200> StartupConfigurationDto: Initial startup wizard configuration retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Startup/Configuration', response_type=StartupConfigurationDto)

    def update_initial_configuration(
            self, 
            request_body: StartupConfigurationDto
    ) -> requests.Response:
        """Sets the initial startup wizard configuration.

        Http:
            <post>: /Startup/Configuration

        Args:
            request_body (StartupConfigurationDto): The updated startup configuration.

        Returns:
            <204> requests.Response: Configuration saved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Startup/Configuration', request_args=request_args)

    def get_first_user_2(
            self
    ) -> StartupUserDto:
        """Gets the first user.

        Http:
            <get>: /Startup/FirstUser

        Returns:
            <200> StartupUserDto: Initial user retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Startup/FirstUser', response_type=StartupUserDto)

    def set_remote_access(
            self, 
            request_body: StartupRemoteAccessDto
    ) -> requests.Response:
        """Sets remote access and UPnP.

        Http:
            <post>: /Startup/RemoteAccess

        Args:
            request_body (StartupRemoteAccessDto): The startup remote access dto.

        Returns:
            <204> requests.Response: Configuration saved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Startup/RemoteAccess', request_args=request_args)

    def get_first_user(
            self
    ) -> StartupUserDto:
        """Gets the first user.

        Http:
            <get>: /Startup/User

        Returns:
            <200> StartupUserDto: Initial user retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Startup/User', response_type=StartupUserDto)

    def update_startup_user(
            self, 
            request_body: Optional[StartupUserDto] = None
    ) -> requests.Response:
        """Sets the user name and password.

        Http:
            <post>: /Startup/User

        Args:
            request_body (StartupUserDto): The DTO containing username and password.

        Returns:
            <204> requests.Response: Updated user name and password.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Startup/User', request_args=request_args)

