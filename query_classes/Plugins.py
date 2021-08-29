import requests
from util.BaseRequestClass import BaseRequestClass
from typing import List
from data_classes.version_number import VersionNumber as Version
from data_classes.plugin_info import PluginInfo as PluginInfo
from data_classes.base_plugin_configuration import BasePluginConfiguration as BasePluginConfiguration


class Plugins(BaseRequestClass):
    def get_plugins(
            self
    ) -> List[PluginInfo]:
        """Gets a list of currently installed plugins.

        Http:
            <get>: /Plugins

        Returns:
            <200> List[PluginInfo]: Installed plugins returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Plugins', response_type=List[PluginInfo])

    def uninstall_plugin_by_version(
            self, 
            plugin_id: str, 
            version: Version
    ) -> requests.Response:
        """Uninstalls a plugin by version.

        Http:
            <delete>: /Plugins/{pluginId}/{version}

        Args:
            plugin_id (str): Plugin id.
            version (Version): Plugin version.

        Returns:
            <204> requests.Response: Plugin uninstalled.
            <404> requests.Response: Plugin not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
            version=version,
        )
        return self._delete(path='/Plugins/{pluginId}/{version}', request_args=request_args)

    def disable_plugin(
            self, 
            plugin_id: str, 
            version: Version
    ) -> requests.Response:
        """Disable a plugin.

        Http:
            <post>: /Plugins/{pluginId}/{version}/Disable

        Args:
            plugin_id (str): Plugin id.
            version (Version): Plugin version.

        Returns:
            <204> requests.Response: Plugin disabled.
            <404> requests.Response: Plugin not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
            version=version,
        )
        return self._post(path='/Plugins/{pluginId}/{version}/Disable', request_args=request_args)

    def enable_plugin(
            self, 
            plugin_id: str, 
            version: Version
    ) -> requests.Response:
        """Enables a disabled plugin.

        Http:
            <post>: /Plugins/{pluginId}/{version}/Enable

        Args:
            plugin_id (str): Plugin id.
            version (Version): Plugin version.

        Returns:
            <204> requests.Response: Plugin enabled.
            <404> requests.Response: Plugin not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
            version=version,
        )
        return self._post(path='/Plugins/{pluginId}/{version}/Enable', request_args=request_args)

    def get_plugin_image(
            self, 
            plugin_id: str, 
            version: Version
    ) -> requests.Response:
        """Gets a plugin's image.

        Http:
            <get>: /Plugins/{pluginId}/{version}/Image

        Args:
            plugin_id (str): Plugin id.
            version (Version): Plugin version.

        Returns:
            <200> requests.Response: Plugin image returned.
            <404> requests.Response: Not Found
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
            version=version,
        )
        return self._get(path='/Plugins/{pluginId}/{version}/Image', request_args=request_args)

    def get_plugin_configuration(
            self, 
            plugin_id: str
    ) -> BasePluginConfiguration:
        """Gets plugin configuration.

        Http:
            <get>: /Plugins/{pluginId}/Configuration

        Args:
            plugin_id (str): Plugin id.

        Returns:
            <200> BasePluginConfiguration: Plugin configuration returned.
            <404> requests.Response: Plugin not found or plugin configuration not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
        )
        return self._get(path='/Plugins/{pluginId}/Configuration', request_args=request_args, response_type=BasePluginConfiguration)

    def update_plugin_configuration(
            self, 
            plugin_id: str
    ) -> requests.Response:
        """Updates plugin configuration.

        Http:
            <post>: /Plugins/{pluginId}/Configuration

        Args:
            plugin_id (str): Plugin id.

        Returns:
            <204> requests.Response: Plugin configuration updated.
            <404> requests.Response: Plugin not found or plugin does not have configuration.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
        )
        return self._post(path='/Plugins/{pluginId}/Configuration', request_args=request_args)

    def get_plugin_manifest(
            self, 
            plugin_id: str
    ) -> requests.Response:
        """Gets a plugin's manifest.

        Http:
            <post>: /Plugins/{pluginId}/Manifest

        Args:
            plugin_id (str): Plugin id.

        Returns:
            <204> requests.Response: Plugin manifest returned.
            <404> requests.Response: Plugin not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            pluginId=plugin_id,
        )
        return self._post(path='/Plugins/{pluginId}/Manifest', request_args=request_args)

