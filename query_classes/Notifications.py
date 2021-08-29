import requests
from util.BaseRequestClass import BaseRequestClass
from typing import List
from data_classes.notifications_summary_dto import NotificationsSummaryDto as NotificationsSummaryDto
from data_classes.notification_type_info import NotificationTypeInfo as NotificationTypeInfo
from data_classes.notification_result_dto import NotificationResultDto as NotificationResultDto
from data_classes.name_i_d_pair import NameIDPair as NameIdPair
from data_classes.admin_notification_dto import AdminNotificationDto as AdminNotificationDto


class Notifications(BaseRequestClass):
    def get_notifications(
            self, 
            user_id: str
    ) -> NotificationResultDto:
        """Gets a user's notifications.

        Http:
            <get>: /Notifications/{userId}

        Args:
            user_id (str)

        Returns:
            <200> NotificationResultDto: Notifications returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/Notifications/{userId}', request_args=request_args, response_type=NotificationResultDto)

    def set_read(
            self, 
            user_id: str
    ) -> requests.Response:
        """Sets notifications as read.

        Http:
            <post>: /Notifications/{userId}/Read

        Args:
            user_id (str)

        Returns:
            <204> requests.Response: Notifications set as read.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._post(path='/Notifications/{userId}/Read', request_args=request_args)

    def get_notifications_summary(
            self, 
            user_id: str
    ) -> NotificationsSummaryDto:
        """Gets a user's notification summary.

        Http:
            <get>: /Notifications/{userId}/Summary

        Args:
            user_id (str)

        Returns:
            <200> NotificationsSummaryDto: Summary of user's notifications returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/Notifications/{userId}/Summary', request_args=request_args, response_type=NotificationsSummaryDto)

    def set_unread(
            self, 
            user_id: str
    ) -> requests.Response:
        """Sets notifications as unread.

        Http:
            <post>: /Notifications/{userId}/Unread

        Args:
            user_id (str)

        Returns:
            <204> requests.Response: Notifications set as unread.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
        )
        return self._post(path='/Notifications/{userId}/Unread', request_args=request_args)

    def create_admin_notification(
            self, 
            request_body: AdminNotificationDto
    ) -> requests.Response:
        """Sends a notification to all admins.

        Http:
            <post>: /Notifications/Admin

        Args:
            request_body (AdminNotificationDto): The notification request.

        Returns:
            <204> requests.Response: Notification sent.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Notifications/Admin', request_args=request_args)

    def get_notification_services(
            self
    ) -> List[NameIdPair]:
        """Gets notification services.

        Http:
            <get>: /Notifications/Services

        Returns:
            <200> List[NameIdPair]: All notification services returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Notifications/Services', response_type=List[NameIdPair])

    def get_notification_types(
            self
    ) -> List[NotificationTypeInfo]:
        """Gets notification types.

        Http:
            <get>: /Notifications/Types

        Returns:
            <200> List[NotificationTypeInfo]: All notification types returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Notifications/Types', response_type=List[NotificationTypeInfo])

