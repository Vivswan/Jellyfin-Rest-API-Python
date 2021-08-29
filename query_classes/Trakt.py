import requests
from util.BaseRequestClass import BaseRequestClass
from typing import List
from data_classes.trakt_sync_response import TraktSyncResponse as TraktSyncResponse
from data_classes.trakt_show import TraktShow as TraktShow
from data_classes.trakt_movie import TraktMovie as TraktMovie


class Trakt(BaseRequestClass):
    def trakt_device_authorization(
            self, 
            user_id: str
    ) -> requests.Response:
        """
        Http:
            <post>: /Trakt/Users/{userId}/Authorize

        Args:
            user_id (str)

        Returns:
            <200> requests.Response: Success
        """
        request_args = dict(
            userId=user_id,
        )
        return self._post(path='/Trakt/Users/{userId}/Authorize', request_args=request_args)

    def trakt_rate_item(
            self, 
            user_id: str, 
            item_id: str, 
            rating: int
    ) -> TraktSyncResponse:
        """
        Http:
            <post>: /Trakt/Users/{userId}/Items/{itemId}/Rate

        Args:
            user_id (str)
            item_id (str)
            rating (int)

        Returns:
            <200> TraktSyncResponse: Success
        """
        request_args = dict(
            userId=user_id,
            itemId=item_id,
            rating=rating,
        )
        return self._post(path='/Trakt/Users/{userId}/Items/{itemId}/Rate', request_args=request_args, response_type=TraktSyncResponse)

    def trakt_poll_authorization_status(
            self, 
            user_id: str
    ) -> requests.Response:
        """
        Http:
            <get>: /Trakt/Users/{userId}/PollAuthorizationStatus

        Args:
            user_id (str)

        Returns:
            <200> requests.Response: Success
        """
        request_args = dict(
            userId=user_id,
        )
        return self._get(path='/Trakt/Users/{userId}/PollAuthorizationStatus', request_args=request_args)

    def recommended_trakt_movies(
            self, 
            user_id: str
    ) -> List[TraktMovie]:
        """
        Http:
            <post>: /Trakt/Users/{userId}/RecommendedMovies

        Args:
            user_id (str)

        Returns:
            <200> List[TraktMovie]: Success
        """
        request_args = dict(
            userId=user_id,
        )
        return self._post(path='/Trakt/Users/{userId}/RecommendedMovies', request_args=request_args, response_type=List[TraktMovie])

    def recommended_trakt_shows(
            self, 
            user_id: str
    ) -> List[TraktShow]:
        """
        Http:
            <post>: /Trakt/Users/{userId}/RecommendedShows

        Args:
            user_id (str)

        Returns:
            <200> List[TraktShow]: Success
        """
        request_args = dict(
            userId=user_id,
        )
        return self._post(path='/Trakt/Users/{userId}/RecommendedShows', request_args=request_args, response_type=List[TraktShow])

