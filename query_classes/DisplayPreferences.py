import requests

from data_classes.display_preferences_dto import DisplayPreferencesDto as DisplayPreferencesDto
from util.BaseRequestClass import BaseRequestClass


class DisplayPreferences(BaseRequestClass):
    def get_display_preferences(
            self, 
            display_preferences_id: str, 
            user_id: str, 
            client: str
    ) -> DisplayPreferencesDto:
        """Get Display Preferences.

        Http:
            <get>: /DisplayPreferences/{displayPreferencesId}

        Args:
            display_preferences_id (str): Display preferences id.
            user_id (str): User id.
            client (str): Client.

        Returns:
            <200> DisplayPreferencesDto: Display preferences retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            displayPreferencesId=display_preferences_id,
            userId=user_id,
            client=client,
        )
        return self._get(path='/DisplayPreferences/{displayPreferencesId}', request_args=request_args, response_type=DisplayPreferencesDto)

    def update_display_preferences(
            self, 
            display_preferences_id: str, 
            user_id: str, 
            client: str, 
            request_body: DisplayPreferencesDto
    ) -> requests.Response:
        """Update Display Preferences.

        Http:
            <post>: /DisplayPreferences/{displayPreferencesId}

        Args:
            display_preferences_id (str): Display preferences id.
            user_id (str): User Id.
            client (str): Client.
            request_body (DisplayPreferencesDto): New Display Preferences object.

        Returns:
            <204> requests.Response: Display preferences updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            displayPreferencesId=display_preferences_id,
            userId=user_id,
            client=client,
            requestBody=request_body,
        )
        return self._post(path='/DisplayPreferences/{displayPreferencesId}', request_args=request_args)

