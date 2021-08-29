from typing import List
from typing import Optional

import requests

from data_classes.collection_creation_result import CollectionCreationResult as CollectionCreationResult
from util.BaseRequestClass import BaseRequestClass


class Collections(BaseRequestClass):
    def create_collection(
            self, 
            name: Optional[str] = None, 
            ids: Optional[List[str]] = None, 
            parent_id: Optional[str] = None, 
            is_locked: Optional[bool] = False
    ) -> CollectionCreationResult:
        """Creates a new collection.

        Http:
            <post>: /Collections

        Args:
            name (str): The name of the collection.
            ids (List[str]): Item Ids to add to the collection.
            parent_id (str): Optional. Create the collection within a specific folder.
            is_locked (bool = False): Whether or not to lock the new collection.

        Returns:
            <200> CollectionCreationResult: Collection created.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            ids=ids,
            parentId=parent_id,
            isLocked=is_locked,
        )
        return self._post(path='/Collections', request_args=request_args, response_type=CollectionCreationResult)

    def add_to_collection(
            self, 
            collection_id: str, 
            ids: List[str]
    ) -> requests.Response:
        """Adds items to a collection.

        Http:
            <post>: /Collections/{collectionId}/Items

        Args:
            collection_id (str): The collection id.
            ids (List[str]): Item ids, comma delimited.

        Returns:
            <204> requests.Response: Items added to collection.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            collectionId=collection_id,
            ids=ids,
        )
        return self._post(path='/Collections/{collectionId}/Items', request_args=request_args)

    def remove_from_collection(
            self, 
            collection_id: str, 
            ids: List[str]
    ) -> requests.Response:
        """Removes items from a collection.

        Http:
            <delete>: /Collections/{collectionId}/Items

        Args:
            collection_id (str): The collection id.
            ids (List[str]): Item ids, comma delimited.

        Returns:
            <204> requests.Response: Items removed from collection.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            collectionId=collection_id,
            ids=ids,
        )
        return self._delete(path='/Collections/{collectionId}/Items', request_args=request_args)

