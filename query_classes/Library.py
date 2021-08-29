from typing import List
from typing import Optional

import requests

from data_classes.add_virtual_folder_dto import AddVirtualFolderDto as AddVirtualFolderDto
from data_classes.base_item_dto_query_result import BaseItemDtoQueryResult as BaseItemDtoQueryResult
from data_classes.collection_type import CollectionType as CollectionTypeOptions
from data_classes.file_organization_result_query_result import \
    FileOrganizationResultQueryResult as FileOrganizationResultQueryResult
from data_classes.media_path_dto import MediaPathDto as MediaPathDto
from data_classes.media_update_info_dto import MediaUpdateInfoDto as MediaUpdateInfoDto
from data_classes.name_value_pair import NameValuePair as NameValuePair
from data_classes.smart_match_result_query_result import SmartMatchResultQueryResult as SmartMatchResultQueryResult
from data_classes.update_library_options_dto import UpdateLibraryOptionsDto as UpdateLibraryOptionsDto
from data_classes.update_media_path_request_dto import UpdateMediaPathRequestDto as UpdateMediaPathRequestDto
from data_classes.virtual_folder_info import VirtualFolderInfo as VirtualFolderInfo
from util.BaseRequestClass import BaseRequestClass


class Library(BaseRequestClass):
    def get_file_organizations(
            self, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None
    ) -> FileOrganizationResultQueryResult:
        """
        Http:
            <get>: /Library/FileOrganizations

        Args:
            start_index (int)
            limit (int)

        Returns:
            <200> FileOrganizationResultQueryResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            startIndex=start_index,
            limit=limit,
        )
        return self._get(path='/Library/FileOrganizations', request_args=request_args, response_type=FileOrganizationResultQueryResult)

    def clear_activity_log(
            self
    ) -> requests.Response:
        """
        Http:
            <delete>: /Library/FileOrganizations

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._delete(path='/Library/FileOrganizations')

    def organize_episode(
            self, 
            id: str, 
            season_number: int, 
            episode_number: int, 
            remember_correction: bool, 
            series_id: Optional[str] = None, 
            ending_episode_number: Optional[int] = None, 
            new_series_name: Optional[str] = None, 
            new_series_year: Optional[int] = None, 
            new_series_provider_ids: Optional[object] = None, 
            target_folder: Optional[str] = None
    ) -> requests.Response:
        """
        Http:
            <post>: /Library/FileOrganizations/{id}/Episode/Organize

        Args:
            id (str)
            season_number (int)
            episode_number (int)
            remember_correction (bool)
            series_id (str)
            ending_episode_number (int)
            new_series_name (str)
            new_series_year (int)
            new_series_provider_ids (object)
            target_folder (str)

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
            seasonNumber=season_number,
            episodeNumber=episode_number,
            rememberCorrection=remember_correction,
            seriesId=series_id,
            endingEpisodeNumber=ending_episode_number,
            newSeriesName=new_series_name,
            newSeriesYear=new_series_year,
            newSeriesProviderIds=new_series_provider_ids,
            targetFolder=target_folder,
        )
        return self._post(path='/Library/FileOrganizations/{id}/Episode/Organize', request_args=request_args)

    def delete_file(
            self, 
            id: str
    ) -> requests.Response:
        """
        Http:
            <delete>: /Library/FileOrganizations/{id}/File

        Args:
            id (str)

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._delete(path='/Library/FileOrganizations/{id}/File', request_args=request_args)

    def organize_movie(
            self, 
            id: str, 
            movie_id: Optional[str] = None, 
            new_movie_name: Optional[str] = None, 
            new_movie_year: Optional[int] = None, 
            new_movie_provider_ids: Optional[object] = None, 
            target_folder: Optional[str] = None
    ) -> requests.Response:
        """
        Http:
            <post>: /Library/FileOrganizations/{id}/Movie/Organize

        Args:
            id (str)
            movie_id (str)
            new_movie_name (str)
            new_movie_year (int)
            new_movie_provider_ids (object)
            target_folder (str)

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
            movieId=movie_id,
            newMovieName=new_movie_name,
            newMovieYear=new_movie_year,
            newMovieProviderIds=new_movie_provider_ids,
            targetFolder=target_folder,
        )
        return self._post(path='/Library/FileOrganizations/{id}/Movie/Organize', request_args=request_args)

    def perform_organization(
            self, 
            id: str
    ) -> requests.Response:
        """
        Http:
            <post>: /Library/FileOrganizations/{id}/Organize

        Args:
            id (str)

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            id=id,
        )
        return self._post(path='/Library/FileOrganizations/{id}/Organize', request_args=request_args)

    def clear_completed_activity_log(
            self
    ) -> requests.Response:
        """
        Http:
            <delete>: /Library/FileOrganizations/Completed

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._delete(path='/Library/FileOrganizations/Completed')

    def get_smart_match_infos(
            self, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None
    ) -> SmartMatchResultQueryResult:
        """
        Http:
            <get>: /Library/FileOrganizations/SmartMatches

        Args:
            start_index (int)
            limit (int)

        Returns:
            <200> SmartMatchResultQueryResult: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            startIndex=start_index,
            limit=limit,
        )
        return self._get(path='/Library/FileOrganizations/SmartMatches', request_args=request_args, response_type=SmartMatchResultQueryResult)

    def delete_smart_watch_entry(
            self, 
            entries: Optional[List[NameValuePair]] = None
    ) -> requests.Response:
        """
        Http:
            <post>: /Library/FileOrganizations/SmartMatches/Delete

        Args:
            entries (List[NameValuePair])

        Returns:
            <204> requests.Response: Success
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            entries=entries,
        )
        return self._post(path='/Library/FileOrganizations/SmartMatches/Delete', request_args=request_args)

    def post_updated_media(
            self, 
            request_body: MediaUpdateInfoDto
    ) -> requests.Response:
        """Reports that new movies have been added by an external source.

        Http:
            <post>: /Library/Media/Updated

        Args:
            request_body (MediaUpdateInfoDto): The update paths.

        Returns:
            <204> requests.Response: Report success.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Library/Media/Updated', request_args=request_args)

    def get_media_folders(
            self, 
            is_hidden: Optional[bool] = None
    ) -> BaseItemDtoQueryResult:
        """Gets all user media folders.

        Http:
            <get>: /Library/MediaFolders

        Args:
            is_hidden (bool): Optional. Filter by folders that are marked hidden, or not.

        Returns:
            <200> BaseItemDtoQueryResult: Media folders returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            isHidden=is_hidden,
        )
        return self._get(path='/Library/MediaFolders', request_args=request_args, response_type=BaseItemDtoQueryResult)

    def post_added_movies(
            self, 
            tmdb_id: Optional[str] = None, 
            imdb_id: Optional[str] = None
    ) -> requests.Response:
        """Reports that new movies have been added by an external source.

        Http:
            <post>: /Library/Movies/Added

        Args:
            tmdb_id (str): The tmdbId.
            imdb_id (str): The imdbId.

        Returns:
            <204> requests.Response: Report success.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            tmdbId=tmdb_id,
            imdbId=imdb_id,
        )
        return self._post(path='/Library/Movies/Added', request_args=request_args)

    def post_updated_movies(
            self, 
            tmdb_id: Optional[str] = None, 
            imdb_id: Optional[str] = None
    ) -> requests.Response:
        """Reports that new movies have been added by an external source.

        Http:
            <post>: /Library/Movies/Updated

        Args:
            tmdb_id (str): The tmdbId.
            imdb_id (str): The imdbId.

        Returns:
            <204> requests.Response: Report success.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            tmdbId=tmdb_id,
            imdbId=imdb_id,
        )
        return self._post(path='/Library/Movies/Updated', request_args=request_args)

    def get_physical_paths(
            self
    ) -> List[str]:
        """Gets a list of physical paths from virtual folders.

        Http:
            <get>: /Library/PhysicalPaths

        Returns:
            <200> List[str]: Physical paths returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Library/PhysicalPaths', response_type=List[str])

    def refresh_library(
            self
    ) -> requests.Response:
        """Starts a library scan.

        Http:
            <post>: /Library/Refresh

        Returns:
            <204> requests.Response: Library scan started.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._post(path='/Library/Refresh')

    def post_added_series(
            self, 
            tvdb_id: Optional[str] = None
    ) -> requests.Response:
        """Reports that new episodes of a series have been added by an external source.

        Http:
            <post>: /Library/Series/Added

        Args:
            tvdb_id (str): The tvdbId.

        Returns:
            <204> requests.Response: Report success.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            tvdbId=tvdb_id,
        )
        return self._post(path='/Library/Series/Added', request_args=request_args)

    def post_updated_series(
            self, 
            tvdb_id: Optional[str] = None
    ) -> requests.Response:
        """Reports that new episodes of a series have been added by an external source.

        Http:
            <post>: /Library/Series/Updated

        Args:
            tvdb_id (str): The tvdbId.

        Returns:
            <204> requests.Response: Report success.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            tvdbId=tvdb_id,
        )
        return self._post(path='/Library/Series/Updated', request_args=request_args)

    def get_virtual_folders(
            self
    ) -> List[VirtualFolderInfo]:
        """Gets all virtual folders.

        Http:
            <get>: /Library/VirtualFolders

        Returns:
            <200> List[VirtualFolderInfo]: Virtual folders retrieved.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        return self._get(path='/Library/VirtualFolders', response_type=List[VirtualFolderInfo])

    def add_virtual_folder(
            self, 
            name: Optional[str] = None, 
            collection_type: Optional[CollectionTypeOptions] = None, 
            paths: Optional[List[str]] = None, 
            refresh_library: Optional[bool] = False, 
            request_body: Optional[AddVirtualFolderDto] = None
    ) -> requests.Response:
        """Adds a virtual folder.

        Http:
            <post>: /Library/VirtualFolders

        Args:
            name (str): The name of the virtual folder.
            collection_type (CollectionTypeOptions): The type of the collection.
            paths (List[str]): The paths of the virtual folder.
            refresh_library (bool = False): Whether to refresh the library.
            request_body (AddVirtualFolderDto): The library options.

        Returns:
            <204> requests.Response: Folder added.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            collectionType=collection_type,
            paths=paths,
            refreshLibrary=refresh_library,
            requestBody=request_body,
        )
        return self._post(path='/Library/VirtualFolders', request_args=request_args)

    def remove_virtual_folder(
            self, 
            name: Optional[str] = None, 
            refresh_library: Optional[bool] = False
    ) -> requests.Response:
        """Removes a virtual folder.

        Http:
            <delete>: /Library/VirtualFolders

        Args:
            name (str): The name of the folder.
            refresh_library (bool = False): Whether to refresh the library.

        Returns:
            <204> requests.Response: Folder removed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            refreshLibrary=refresh_library,
        )
        return self._delete(path='/Library/VirtualFolders', request_args=request_args)

    def update_library_options(
            self, 
            request_body: Optional[UpdateLibraryOptionsDto] = None
    ) -> requests.Response:
        """Update library options.

        Http:
            <post>: /Library/VirtualFolders/LibraryOptions

        Args:
            request_body (UpdateLibraryOptionsDto): The library name and options.

        Returns:
            <204> requests.Response: Library updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Library/VirtualFolders/LibraryOptions', request_args=request_args)

    def rename_virtual_folder(
            self, 
            name: Optional[str] = None, 
            new_name: Optional[str] = None, 
            refresh_library: Optional[bool] = False
    ) -> requests.Response:
        """Renames a virtual folder.

        Http:
            <post>: /Library/VirtualFolders/Name

        Args:
            name (str): The name of the virtual folder.
            new_name (str): The new name.
            refresh_library (bool = False): Whether to refresh the library.

        Returns:
            <204> requests.Response: Folder renamed.
            <404> requests.Response: Library doesn't exist.
            <409> requests.Response: Library already exists.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            newName=new_name,
            refreshLibrary=refresh_library,
        )
        return self._post(path='/Library/VirtualFolders/Name', request_args=request_args)

    def add_media_path(
            self, 
            request_body: MediaPathDto, 
            refresh_library: Optional[bool] = False
    ) -> requests.Response:
        """Add a media path to a library.

        Http:
            <post>: /Library/VirtualFolders/Paths

        Args:
            request_body (MediaPathDto): The media path dto.
            refresh_library (bool = False): Whether to refresh the library.

        Returns:
            <204> requests.Response: Media path added.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
            refreshLibrary=refresh_library,
        )
        return self._post(path='/Library/VirtualFolders/Paths', request_args=request_args)

    def remove_media_path(
            self, 
            name: Optional[str] = None, 
            path: Optional[str] = None, 
            refresh_library: Optional[bool] = False
    ) -> requests.Response:
        """Remove a media path.

        Http:
            <delete>: /Library/VirtualFolders/Paths

        Args:
            name (str): The name of the library.
            path (str): The path to remove.
            refresh_library (bool = False): Whether to refresh the library.

        Returns:
            <204> requests.Response: Media path removed.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            name=name,
            path=path,
            refreshLibrary=refresh_library,
        )
        return self._delete(path='/Library/VirtualFolders/Paths', request_args=request_args)

    def update_media_path(
            self, 
            request_body: UpdateMediaPathRequestDto
    ) -> requests.Response:
        """Updates a media path.

        Http:
            <post>: /Library/VirtualFolders/Paths/Update

        Args:
            request_body (UpdateMediaPathRequestDto): The name of the library and path infos.

        Returns:
            <204> requests.Response: Media path updated.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            requestBody=request_body,
        )
        return self._post(path='/Library/VirtualFolders/Paths/Update', request_args=request_args)

