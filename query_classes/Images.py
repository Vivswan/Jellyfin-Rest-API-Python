from typing import List

import requests

from data_classes.image_by_name_info import ImageByNameInfo as ImageByNameInfo
from util.BaseRequestClass import BaseRequestClass


class Images(BaseRequestClass):
    def get_general_images(
            self
    ) -> List[ImageByNameInfo]:
        """Get all general images.

        Http:
            <get>: /Images/General

        Returns:
            <200> List[ImageByNameInfo]: Retrieved list of images.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Images/General', response_type=List[ImageByNameInfo])

    def get_general_image(
            self, 
            name: str, 
            type: str
    ) -> requests.Response:
        """Get General Image.

        Http:
            <get>: /Images/General/{name}/{type}

        Args:
            name (str): The name of the image.
            type (str): Image Type (primary, backdrop, logo, etc).

        Returns:
            <200> requests.Response: Image stream retrieved.
            <404> requests.Response: Image not found.
        """
        request_args = dict(
            name=name,
            type=type,
        )
        return self._get(path='/Images/General/{name}/{type}', request_args=request_args)

    def get_media_info_images(
            self
    ) -> List[ImageByNameInfo]:
        """Get all media info images.

        Http:
            <get>: /Images/MediaInfo

        Returns:
            <200> List[ImageByNameInfo]: Image list retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Images/MediaInfo', response_type=List[ImageByNameInfo])

    def get_media_info_image(
            self, 
            theme: str, 
            name: str
    ) -> requests.Response:
        """Get media info image.

        Http:
            <get>: /Images/MediaInfo/{theme}/{name}

        Args:
            theme (str): The theme to get the image from.
            name (str): The name of the image.

        Returns:
            <200> requests.Response: Image stream retrieved.
            <404> requests.Response: Image not found.
        """
        request_args = dict(
            theme=theme,
            name=name,
        )
        return self._get(path='/Images/MediaInfo/{theme}/{name}', request_args=request_args)

    def get_rating_images(
            self
    ) -> List[ImageByNameInfo]:
        """Get all general images.

        Http:
            <get>: /Images/Ratings

        Returns:
            <200> List[ImageByNameInfo]: Retrieved list of images.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Images/Ratings', response_type=List[ImageByNameInfo])

    def get_rating_image(
            self, 
            theme: str, 
            name: str
    ) -> requests.Response:
        """Get rating image.

        Http:
            <get>: /Images/Ratings/{theme}/{name}

        Args:
            theme (str): The theme to get the image from.
            name (str): The name of the image.

        Returns:
            <200> requests.Response: Image stream retrieved.
            <404> requests.Response: Image not found.
        """
        request_args = dict(
            theme=theme,
            name=name,
        )
        return self._get(path='/Images/Ratings/{theme}/{name}', request_args=request_args)

