from typing import List
from typing import Optional

import requests

from data_classes.device_profile import DeviceProfile as DeviceProfile
from data_classes.device_profile_info import DeviceProfileInfo as DeviceProfileInfo
from util.BaseRequestClass import BaseRequestClass


class Dlna(BaseRequestClass):
    def get_profile_infos(
            self
    ) -> List[DeviceProfileInfo]:
        """Get profile infos.

        Http:
            <get>: /Dlna/ProfileInfos

        Returns:
            <200> List[DeviceProfileInfo]: Device profile infos returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Dlna/ProfileInfos', response_type=List[DeviceProfileInfo])

    def create_profile(
            self, 
            request_body: Optional[DeviceProfile] = None
    ) -> requests.Response:
        """Creates a profile.

        Http:
            <post>: /Dlna/Profiles

        Args:
            request_body (DeviceProfile): Device profile.

        Returns:
            <204> requests.Response: Device profile created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Dlna/Profiles', request_args=request_args)

    def get_profile(
            self, 
            profile_id: str
    ) -> DeviceProfile:
        """Gets a single profile.

        Http:
            <get>: /Dlna/Profiles/{profileId}

        Args:
            profile_id (str): Profile Id.

        Returns:
            <200> DeviceProfile: Device profile returned.
            <404> requests.Response: Device profile not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            profileId=profile_id,
        )
        return self._get(path='/Dlna/Profiles/{profileId}', request_args=request_args, response_type=DeviceProfile)

    def delete_profile(
            self, 
            profile_id: str
    ) -> requests.Response:
        """Deletes a profile.

        Http:
            <delete>: /Dlna/Profiles/{profileId}

        Args:
            profile_id (str): Profile id.

        Returns:
            <204> requests.Response: Device profile deleted.
            <404> requests.Response: Device profile not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            profileId=profile_id,
        )
        return self._delete(path='/Dlna/Profiles/{profileId}', request_args=request_args)

    def update_profile(
            self, 
            profile_id: str, 
            request_body: Optional[DeviceProfile] = None
    ) -> requests.Response:
        """Updates a profile.

        Http:
            <post>: /Dlna/Profiles/{profileId}

        Args:
            profile_id (str): Profile id.
            request_body (DeviceProfile): Device profile.

        Returns:
            <204> requests.Response: Device profile updated.
            <404> requests.Response: Device profile not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            profileId=profile_id,
            requestBody=request_body,
        )
        return self._post(path='/Dlna/Profiles/{profileId}', request_args=request_args)

    def get_default_profile(
            self
    ) -> DeviceProfile:
        """Gets the default profile.

        Http:
            <get>: /Dlna/Profiles/Default

        Returns:
            <200> DeviceProfile: Default device profile returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Dlna/Profiles/Default', response_type=DeviceProfile)

    def get_connection_manager(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna media receiver registrar xml.

        Http:
            <get>: /Dlna/{serverId}/ConnectionManager

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna media receiver registrar xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/ConnectionManager', request_args=request_args)

    def get_connection_manager_2(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna media receiver registrar xml.

        Http:
            <get>: /Dlna/{serverId}/ConnectionManager/ConnectionManager

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna media receiver registrar xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/ConnectionManager/ConnectionManager', request_args=request_args)

    def get_connection_manager_3(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna media receiver registrar xml.

        Http:
            <get>: /Dlna/{serverId}/ConnectionManager/ConnectionManager.xml

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna media receiver registrar xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/ConnectionManager/ConnectionManager.xml', request_args=request_args)

    def process_connection_manager_control_request(
            self, 
            server_id: str
    ) -> requests.Response:
        """Process a connection manager control request.

        Http:
            <post>: /Dlna/{serverId}/ConnectionManager/Control

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Request processed.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._post(path='/Dlna/{serverId}/ConnectionManager/Control', request_args=request_args)

    def get_content_directory(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna content directory xml.

        Http:
            <get>: /Dlna/{serverId}/ContentDirectory

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna content directory returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/ContentDirectory', request_args=request_args)

    def get_content_directory_2(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna content directory xml.

        Http:
            <get>: /Dlna/{serverId}/ContentDirectory/ContentDirectory

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna content directory returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/ContentDirectory/ContentDirectory', request_args=request_args)

    def get_content_directory_3(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna content directory xml.

        Http:
            <get>: /Dlna/{serverId}/ContentDirectory/ContentDirectory.xml

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna content directory returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/ContentDirectory/ContentDirectory.xml', request_args=request_args)

    def process_content_directory_control_request(
            self, 
            server_id: str
    ) -> requests.Response:
        """Process a content directory control request.

        Http:
            <post>: /Dlna/{serverId}/ContentDirectory/Control

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Request processed.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._post(path='/Dlna/{serverId}/ContentDirectory/Control', request_args=request_args)

    def get_description_xml(
            self, 
            server_id: str
    ) -> requests.Response:
        """Get Description Xml.

        Http:
            <get>: /Dlna/{serverId}/description

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Description xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/description', request_args=request_args)

    def get_description_xml_2(
            self, 
            server_id: str
    ) -> requests.Response:
        """Get Description Xml.

        Http:
            <get>: /Dlna/{serverId}/description.xml

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Description xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/description.xml', request_args=request_args)

    def get_icon_id(
            self, 
            server_id: str, 
            file_name: str
    ) -> requests.Response:
        """Gets a server icon.

        Http:
            <get>: /Dlna/{serverId}/icons/{fileName}

        Args:
            server_id (str): Server UUID.
            file_name (str): The icon filename.

        Returns:
            <200> requests.Response: Request processed.
            <404> requests.Response: Not Found.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
            fileName=file_name,
        )
        return self._get(path='/Dlna/{serverId}/icons/{fileName}', request_args=request_args)

    def get_media_receiver_registrar(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna media receiver registrar xml.

        Http:
            <get>: /Dlna/{serverId}/MediaReceiverRegistrar

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna media receiver registrar xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/MediaReceiverRegistrar', request_args=request_args)

    def process_media_receiver_registrar_control_request(
            self, 
            server_id: str
    ) -> requests.Response:
        """Process a media receiver registrar control request.

        Http:
            <post>: /Dlna/{serverId}/MediaReceiverRegistrar/Control

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Request processed.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._post(path='/Dlna/{serverId}/MediaReceiverRegistrar/Control', request_args=request_args)

    def get_media_receiver_registrar_2(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna media receiver registrar xml.

        Http:
            <get>: /Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna media receiver registrar xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar', request_args=request_args)

    def get_media_receiver_registrar_3(
            self, 
            server_id: str
    ) -> requests.Response:
        """Gets Dlna media receiver registrar xml.

        Http:
            <get>: /Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar.xml

        Args:
            server_id (str): Server UUID.

        Returns:
            <200> requests.Response: Dlna media receiver registrar xml returned.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            serverId=server_id,
        )
        return self._get(path='/Dlna/{serverId}/MediaReceiverRegistrar/MediaReceiverRegistrar.xml', request_args=request_args)

    def get_icon(
            self, 
            file_name: str
    ) -> requests.Response:
        """Gets a server icon.

        Http:
            <get>: /Dlna/icons/{fileName}

        Args:
            file_name (str): The icon filename.

        Returns:
            <200> requests.Response: Request processed.
            <404> requests.Response: Not Found.
            <503> requests.Response: DLNA is disabled.
        """
        request_args = dict(
            fileName=file_name,
        )
        return self._get(path='/Dlna/icons/{fileName}', request_args=request_args)

