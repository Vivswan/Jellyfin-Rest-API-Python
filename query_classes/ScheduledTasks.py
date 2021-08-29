import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.task_trigger_info import TaskTriggerInfo as TaskTriggerInfo
from data_classes.task_info import TaskInfo as TaskInfo


class ScheduledTasks(BaseRequestClass):
    def get_tasks(
            self, 
            is_hidden: Optional[bool] = None, 
            is_enabled: Optional[bool] = None
    ) -> List[TaskInfo]:
        """Get tasks.

        Http:
            <get>: /ScheduledTasks

        Args:
            is_hidden (bool): Optional filter tasks that are hidden, or not.
            is_enabled (bool): Optional filter tasks that are enabled, or not.

        Returns:
            <200> List[TaskInfo]: Scheduled tasks retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            isHidden=is_hidden,
            isEnabled=is_enabled,
        )
        return self._get(path='/ScheduledTasks', request_args=request_args, response_type=List[TaskInfo])

    def get_task(
            self, 
            task_id: str
    ) -> TaskInfo:
        """Get task by id.

        Http:
            <get>: /ScheduledTasks/{taskId}

        Args:
            task_id (str): Task Id.

        Returns:
            <200> TaskInfo: Task retrieved.
            <404> requests.Response: Task not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            taskId=task_id,
        )
        return self._get(path='/ScheduledTasks/{taskId}', request_args=request_args, response_type=TaskInfo)

    def update_task(
            self, 
            task_id: str, 
            request_body: List[TaskTriggerInfo]
    ) -> requests.Response:
        """Update specified task triggers.

        Http:
            <post>: /ScheduledTasks/{taskId}/Triggers

        Args:
            task_id (str): Task Id.
            request_body (List[TaskTriggerInfo]): Triggers.

        Returns:
            <204> requests.Response: Task triggers updated.
            <404> requests.Response: Task not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            taskId=task_id,
            requestBody=request_body,
        )
        return self._post(path='/ScheduledTasks/{taskId}/Triggers', request_args=request_args)

    def start_task(
            self, 
            task_id: str
    ) -> requests.Response:
        """Start specified task.

        Http:
            <post>: /ScheduledTasks/Running/{taskId}

        Args:
            task_id (str): Task Id.

        Returns:
            <204> requests.Response: Task started.
            <404> requests.Response: Task not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            taskId=task_id,
        )
        return self._post(path='/ScheduledTasks/Running/{taskId}', request_args=request_args)

    def stop_task(
            self, 
            task_id: str
    ) -> requests.Response:
        """Stop specified task.

        Http:
            <delete>: /ScheduledTasks/Running/{taskId}

        Args:
            task_id (str): Task Id.

        Returns:
            <204> requests.Response: Task stopped.
            <404> requests.Response: Task not found.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            taskId=task_id,
        )
        return self._delete(path='/ScheduledTasks/Running/{taskId}', request_args=request_args)

