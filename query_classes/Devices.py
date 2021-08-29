from typing import Optional

import requests

from data_classes.device_info import DeviceInfo as DeviceInfo
from data_classes.device_info_query_result import DeviceInfoQueryResult as DeviceInfoQueryResult
from data_classes.device_options import DeviceOptions as DeviceOptions
from util.BaseRequestClass import BaseRequestClass


class Devices(BaseRequestClass):
    def get_devices(
            self, 
            supports_sync: Optional[bool] = None, 
            user_id: Optional[str] = None
    ) -> DeviceInfoQueryResult:
        """Get Devices.

        Http:
            <get>: /Devices

        Args:
            supports_sync (bool): Gets or sets a value indicating whether [supports synchronize].
            user_id (str): Gets or sets the user identifier.

        Returns:
            <200> DeviceInfoQueryResult: Devices retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            supportsSync=supports_sync,
            userId=user_id,
        )
        return self._get(path='/Devices', request_args=request_args, response_type=DeviceInfoQueryResult)

    def delete_device(
            self, 
            id: str
    ) -> requests.Response:
        """Deletes a device.

        Http:
            <delete>: /Devices

        Args:
            id (str): Device Id.

        Returns:
            <204> requests.Response: Device deleted.
            <404> requests.Response: Device not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._delete(path='/Devices', request_args=request_args)

    def get_device_info(
            self, 
            id: str
    ) -> DeviceInfo:
        """Get info for a device.

        Http:
            <get>: /Devices/Info

        Args:
            id (str): Device Id.

        Returns:
            <200> DeviceInfo: Device info retrieved.
            <404> requests.Response: Device not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._get(path='/Devices/Info', request_args=request_args, response_type=DeviceInfo)

    def get_device_options(
            self, 
            id: str
    ) -> DeviceOptions:
        """Get options for a device.

        Http:
            <get>: /Devices/Options

        Args:
            id (str): Device Id.

        Returns:
            <200> DeviceOptions: Device options retrieved.
            <404> requests.Response: Device not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._get(path='/Devices/Options', request_args=request_args, response_type=DeviceOptions)

    def update_device_options(
            self, 
            id: str, 
            request_body: DeviceOptions
    ) -> requests.Response:
        """Update device options.

        Http:
            <post>: /Devices/Options

        Args:
            id (str): Device Id.
            request_body (DeviceOptions): Device Options.

        Returns:
            <204> requests.Response: Device options updated.
            <404> requests.Response: Device not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
            requestBody=request_body,
        )
        return self._post(path='/Devices/Options', request_args=request_args)

