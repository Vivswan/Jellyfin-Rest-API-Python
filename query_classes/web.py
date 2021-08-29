import requests
from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.configuration_page_type import ConfigurationPageType as ConfigurationPageType
from data_classes.configuration_page_info import ConfigurationPageInfo as ConfigurationPageInfo


class web(BaseRequestClass):
    def get_dashboard_configuration_page(
            self, 
            name: Optional[str] = None
    ) -> requests.Response:
        """Gets a dashboard configuration page.

        Http:
            <get>: /web/ConfigurationPage

        Args:
            name (str): The name of the page.

        Returns:
            <200> requests.Response: ConfigurationPage returned.
            <404> requests.Response: Plugin configuration page not found.
        """
        request_args = dict(
            name=name,
        )
        return self._get(path='/web/ConfigurationPage', request_args=request_args)

    def get_configuration_pages(
            self, 
            enable_in_main_menu: Optional[bool] = None, 
            page_type: Optional[ConfigurationPageType] = None
    ) -> List[ConfigurationPageInfo]:
        """Gets the configuration pages.

        Http:
            <get>: /web/ConfigurationPages

        Args:
            enable_in_main_menu (bool): Whether to enable in the main menu.
            page_type (ConfigurationPageType): The Jellyfin.Api.Models.ConfigurationPageInfo.

        Returns:
            <200> List[ConfigurationPageInfo]: ConfigurationPages returned.
            <404> requests.Response: Server still loading.
        """
        request_args = dict(
            enableInMainMenu=enable_in_main_menu,
            pageType=page_type,
        )
        return self._get(path='/web/ConfigurationPages', request_args=request_args, response_type=List[ConfigurationPageInfo])

