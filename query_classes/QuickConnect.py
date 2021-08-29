import requests
from util.BaseRequestClass import BaseRequestClass
from data_classes.quick_connect_state import QuickConnectState as QuickConnectState
from data_classes.quick_connect_result import QuickConnectResult as QuickConnectResult


class QuickConnect(BaseRequestClass):
    def activate(
            self
    ) -> requests.Response:
        """Temporarily activates quick connect for five minutes.

        Http:
            <post>: /QuickConnect/Activate

        Returns:
            <204> requests.Response: Quick connect has been temporarily activated.
            <403> requests.Response: Quick connect is unavailable on this server.
            <401> requests.Response: Unauthorized
        """
        return self._post(path='/QuickConnect/Activate')

    def authorize(
            self, 
            code: str
    ) -> bool:
        """Authorizes a pending quick connect request.

        Http:
            <post>: /QuickConnect/Authorize

        Args:
            code (str): Quick connect code to authorize.

        Returns:
            <200> bool: Quick connect result authorized successfully.
            <403> requests.Response: Unknown user id.
            <401> requests.Response: Unauthorized
        """
        request_args = dict(
            code=code,
        )
        return self._post(path='/QuickConnect/Authorize', request_args=request_args, response_type=bool)

    def available(
            self, 
            status: QuickConnectState
    ) -> requests.Response:
        """Enables or disables quick connect.

        Http:
            <post>: /QuickConnect/Available

        Args:
            status (QuickConnectState): New MediaBrowser.Model.QuickConnect.QuickConnectState.

        Returns:
            <204> requests.Response: Quick connect state set successfully.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            status=status,
        )
        return self._post(path='/QuickConnect/Available', request_args=request_args)

    def connect(
            self, 
            secret: str
    ) -> QuickConnectResult:
        """Attempts to retrieve authentication information.

        Http:
            <get>: /QuickConnect/Connect

        Args:
            secret (str): Secret previously returned from the Initiate endpoint.

        Returns:
            <200> QuickConnectResult: Quick connect result returned.
            <404> requests.Response: Unknown quick connect secret.
        """
        request_args = dict(
            secret=secret,
        )
        return self._get(path='/QuickConnect/Connect', request_args=request_args, response_type=QuickConnectResult)

    def deauthorize(
            self
    ) -> int:
        """Deauthorize all quick connect devices for the current user.

        Http:
            <post>: /QuickConnect/Deauthorize

        Returns:
            <200> int: All quick connect devices were deleted.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/QuickConnect/Deauthorize', response_type=int)

    def initiate(
            self
    ) -> QuickConnectResult:
        """Initiate a new quick connect request.

        Http:
            <get>: /QuickConnect/Initiate

        Returns:
            <200> QuickConnectResult: Quick connect request successfully created.
            <401> requests.Response: Quick connect is not active on this server.
        """
        return self._get(path='/QuickConnect/Initiate', response_type=QuickConnectResult)

    def get_status(
            self
    ) -> QuickConnectState:
        """Gets the current quick connect state.

        Http:
            <get>: /QuickConnect/Status

        Returns:
            <200> QuickConnectState: Quick connect state returned.
        """
        return self._get(path='/QuickConnect/Status', response_type=QuickConnectState)

