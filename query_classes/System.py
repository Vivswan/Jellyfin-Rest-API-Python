import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.wake_on_l_a_n_info import WakeOnLANInfo as WakeOnLanInfo
from data_classes.system_info import SystemInfo as SystemInfo
from data_classes.server_configuration import ServerConfiguration as ServerConfiguration
from data_classes.public_system_info import PublicSystemInfo as PublicSystemInfo
from data_classes.metadata_options import MetadataOptions as MetadataOptions
from data_classes.media_encoder_path_dto import MediaEncoderPathDto as MediaEncoderPathDto
from data_classes.log_file import LogFile as LogFile
from data_classes.end_point_info import EndPointInfo as EndPointInfo
from data_classes.activity_log_entry_query_result import ActivityLogEntryQueryResult as ActivityLogEntryQueryResult


class System(BaseRequestClass):
    def get_log_entries(
            self, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            min_date: Optional[str] = None, 
            has_user_id: Optional[bool] = None
    ) -> ActivityLogEntryQueryResult:
        """Gets activity log entries.

        Http:
            <get>: /System/ActivityLog/Entries

        Args:
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            min_date (str): Optional. The minimum date. Format = ISO.
            has_user_id (bool): Optional. Filter log entries if it has user id, or not.

        Returns:
            <200> ActivityLogEntryQueryResult: Activity log returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            startIndex=start_index,
            limit=limit,
            minDate=min_date,
            hasUserId=has_user_id,
        )
        return self._get(path='/System/ActivityLog/Entries', request_args=request_args, response_type=ActivityLogEntryQueryResult)

    def get_configuration(
            self
    ) -> ServerConfiguration:
        """Gets application configuration.

        Http:
            <get>: /System/Configuration

        Returns:
            <200> ServerConfiguration: Application configuration returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/System/Configuration', response_type=ServerConfiguration)

    def update_configuration(
            self, 
            request_body: ServerConfiguration
    ) -> requests.Response:
        """Updates application configuration.

        Http:
            <post>: /System/Configuration

        Args:
            request_body (ServerConfiguration): Configuration.

        Returns:
            <204> requests.Response: Configuration updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/System/Configuration', request_args=request_args)

    def get_named_configuration(
            self, 
            key: str
    ) -> str:
        """Gets a named configuration.

        Http:
            <get>: /System/Configuration/{key}

        Args:
            key (str): Configuration key.

        Returns:
            <200> str: Configuration returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            key=key,
        )
        return self._get(path='/System/Configuration/{key}', request_args=request_args, response_type=str)

    def update_named_configuration(
            self, 
            key: str
    ) -> requests.Response:
        """Updates named configuration.

        Http:
            <post>: /System/Configuration/{key}

        Args:
            key (str): Configuration key.

        Returns:
            <204> requests.Response: Named configuration updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            key=key,
        )
        return self._post(path='/System/Configuration/{key}', request_args=request_args)

    def get_default_metadata_options(
            self
    ) -> MetadataOptions:
        """Gets a default MetadataOptions object.

        Http:
            <get>: /System/Configuration/MetadataOptions/Default

        Returns:
            <200> MetadataOptions: Metadata options returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/System/Configuration/MetadataOptions/Default', response_type=MetadataOptions)

    def update_media_encoder_path(
            self, 
            request_body: MediaEncoderPathDto
    ) -> requests.Response:
        """Updates the path to the media encoder.

        Http:
            <post>: /System/MediaEncoder/Path

        Args:
            request_body (MediaEncoderPathDto): Media encoder path form body.

        Returns:
            <204> requests.Response: Media encoder path updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/System/MediaEncoder/Path', request_args=request_args)

    def get_endpoint_info(
            self
    ) -> EndPointInfo:
        """Gets information about the request endpoint.

        Http:
            <get>: /System/Endpoint

        Returns:
            <200> EndPointInfo: Information retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/System/Endpoint', response_type=EndPointInfo)

    def get_system_info(
            self
    ) -> SystemInfo:
        """Gets information about the server.

        Http:
            <get>: /System/Info

        Returns:
            <200> SystemInfo: Information retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/System/Info', response_type=SystemInfo)

    def get_public_system_info(
            self
    ) -> PublicSystemInfo:
        """Gets public information about the server.

        Http:
            <get>: /System/Info/Public

        Returns:
            <200> PublicSystemInfo: Information retrieved.
        """
        return self._get(path='/System/Info/Public', response_type=PublicSystemInfo)

    def get_server_logs(
            self
    ) -> List[LogFile]:
        """Gets a list of available server log files.

        Http:
            <get>: /System/Logs

        Returns:
            <200> List[LogFile]: Information retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/System/Logs', response_type=List[LogFile])

    def get_log_file(
            self, 
            name: str
    ) -> requests.Response:
        """Gets a log file.

        Http:
            <get>: /System/Logs/Log

        Args:
            name (str): The name of the log file to get.

        Returns:
            <200> requests.Response: Log file retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
        )
        return self._get(path='/System/Logs/Log', request_args=request_args)

    def get_ping_system(
            self
    ) -> str:
        """Pings the system.

        Http:
            <get>: /System/Ping

        Returns:
            <200> str: Information retrieved.
        """
        return self._get(path='/System/Ping', response_type=str)

    def post_ping_system(
            self
    ) -> str:
        """Pings the system.

        Http:
            <post>: /System/Ping

        Returns:
            <200> str: Information retrieved.
        """
        return self._post(path='/System/Ping', response_type=str)

    def restart_application(
            self
    ) -> requests.Response:
        """Restarts the application.

        Http:
            <post>: /System/Restart

        Returns:
            <204> requests.Response: Server restarted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/System/Restart')

    def shutdown_application(
            self
    ) -> requests.Response:
        """Shuts down the application.

        Http:
            <post>: /System/Shutdown

        Returns:
            <204> requests.Response: Server shut down.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/System/Shutdown')

    def get_wake_on_lan_info(
            self
    ) -> List[WakeOnLanInfo]:
        """Gets wake on lan information.

        Http:
            <get>: /System/WakeOnLanInfo

        Returns:
            <200> List[WakeOnLanInfo]: Information retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/System/WakeOnLanInfo', response_type=List[WakeOnLanInfo])

