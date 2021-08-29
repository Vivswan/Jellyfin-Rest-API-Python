import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.custom_query_data import CustomQueryData as CustomQueryData


class user_usage_stats(BaseRequestClass):
    def get_breakdown_report(
            self, 
            breakdown_type: str, 
            days: int, 
            end_date: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/{breakdownType}/BreakdownReport

        Args:
            breakdown_type (str)
            days (int)
            end_date (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            breakdownType=breakdown_type,
            days=days,
            endDate=end_date,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/{breakdownType}/BreakdownReport', request_args=request_args)

    def get_user_report_data(
            self, 
            user_id: str, 
            date: str, 
            filter: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/{userId}/{date}/GetItems

        Args:
            user_id (str)
            date (str)
            filter (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            userId=user_id,
            date=date,
            filter=filter,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/{userId}/{date}/GetItems', request_args=request_args)

    def get_duration_histogram_report(
            self, 
            days: int, 
            end_date: Optional[str] = None, 
            filter: Optional[str] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/DurationHistogramReport

        Args:
            days (int)
            end_date (str)
            filter (str)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            days=days,
            endDate=end_date,
            filter=filter,
        )
        return self._get(path='/user_usage_stats/DurationHistogramReport', request_args=request_args)

    def get_tv_shows_report(
            self, 
            days: int, 
            end_date: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/GetTvShowsReport

        Args:
            days (int)
            end_date (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            days=days,
            endDate=end_date,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/GetTvShowsReport', request_args=request_args)

    def get_hourly_report(
            self, 
            days: int, 
            end_date: Optional[str] = None, 
            filter: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/HourlyReport

        Args:
            days (int)
            end_date (str)
            filter (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            days=days,
            endDate=end_date,
            filter=filter,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/HourlyReport', request_args=request_args)

    def load_backup(
            self, 
            backup_file_path: Optional[str] = None
    ) -> List[str]:
        """
        Http:
            <get>: /user_usage_stats/load_backup

        Args:
            backup_file_path (str)

        Returns:
            <200> List[str]: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            backupFilePath=backup_file_path,
        )
        return self._get(path='/user_usage_stats/load_backup', request_args=request_args, response_type=List[str])

    def get_movie_report(
            self, 
            days: int, 
            end_date: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/MoviesReport

        Args:
            days (int)
            end_date (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            days=days,
            endDate=end_date,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/MoviesReport', request_args=request_args)

    def get_usage_stats(
            self, 
            days: int, 
            end_date: Optional[str] = None, 
            filter: Optional[str] = None, 
            data_type: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/PlayActivity

        Args:
            days (int)
            end_date (str)
            filter (str)
            data_type (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            days=days,
            endDate=end_date,
            filter=filter,
            dataType=data_type,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/PlayActivity', request_args=request_args)

    def save_backup(
            self
    ) -> List[str]:
        """
        Http:
            <get>: /user_usage_stats/save_backup

        Returns:
            <200> List[str]: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/user_usage_stats/save_backup', response_type=List[str])

    def custom_query(
            self, 
            request_body: Optional[CustomQueryData] = None
    ) -> object:
        """
        Http:
            <post>: /user_usage_stats/submit_custom_query

        Args:
            request_body (CustomQueryData)

        Returns:
            <200> object: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/user_usage_stats/submit_custom_query', request_args=request_args, response_type=object)

    def get_type_filter_list(
            self
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/type_filter_list

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/user_usage_stats/type_filter_list')

    def get_user_report(
            self, 
            days: int, 
            end_date: Optional[str] = None, 
            timezone_offset: Optional[int] = None
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/user_activity

        Args:
            days (int)
            end_date (str)
            timezone_offset (int)

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            days=days,
            endDate=end_date,
            timezoneOffset=timezone_offset,
        )
        return self._get(path='/user_usage_stats/user_activity', request_args=request_args)

    def get_jellyfin_users(
            self
    ) -> requests.Response:
        """
        Http:
            <get>: /user_usage_stats/user_list

        Returns:
            <200> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/user_usage_stats/user_list')

    def ignore_list_add(
            self, 
            id: Optional[str] = None
    ) -> bool:
        """
        Http:
            <get>: /user_usage_stats/user_manage/add

        Args:
            id (str)

        Returns:
            <200> bool: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._get(path='/user_usage_stats/user_manage/add', request_args=request_args, response_type=bool)

    def prune_unknown_users(
            self
    ) -> bool:
        """
        Http:
            <get>: /user_usage_stats/user_manage/prune

        Returns:
            <200> bool: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/user_usage_stats/user_manage/prune', response_type=bool)

    def ignore_list_remove(
            self, 
            id: Optional[str] = None
    ) -> bool:
        """
        Http:
            <get>: /user_usage_stats/user_manage/remove

        Args:
            id (str)

        Returns:
            <200> bool: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._get(path='/user_usage_stats/user_manage/remove', request_args=request_args, response_type=bool)

