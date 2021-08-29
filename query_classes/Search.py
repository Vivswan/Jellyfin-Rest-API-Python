from util.BaseRequestClass import BaseRequestClass
from typing import Optional
from typing import List
from data_classes.search_hint_result import SearchHintResult as SearchHintResult


class Search(BaseRequestClass):
    def get_hints(
            self, 
            search_term: str, 
            start_index: Optional[int] = None, 
            limit: Optional[int] = None, 
            user_id: Optional[str] = None, 
            include_item_types: Optional[List[str]] = None, 
            exclude_item_types: Optional[List[str]] = None, 
            media_types: Optional[List[str]] = None, 
            parent_id: Optional[str] = None, 
            is_movie: Optional[bool] = None, 
            is_series: Optional[bool] = None, 
            is_news: Optional[bool] = None, 
            is_kids: Optional[bool] = None, 
            is_sports: Optional[bool] = None, 
            include_people: Optional[bool] = True, 
            include_media: Optional[bool] = True, 
            include_genres: Optional[bool] = True, 
            include_studios: Optional[bool] = True, 
            include_artists: Optional[bool] = True
    ) -> SearchHintResult:
        """Gets the search hint result.

        Http:
            <get>: /Search/Hints

        Args:
            search_term (str): The search term to filter on.
            start_index (int): Optional. The record index to start at. All items with a lower index will be dropped from the results.
            limit (int): Optional. The maximum number of records to return.
            user_id (str): Optional. Supply a user id to search within a user's library or omit to search all.
            include_item_types (List[str]): If specified, only results with the specified item types are returned. This allows multiple, comma delimeted.
            exclude_item_types (List[str]): If specified, results with these item types are filtered out. This allows multiple, comma delimeted.
            media_types (List[str]): If specified, only results with the specified media types are returned. This allows multiple, comma delimeted.
            parent_id (str): If specified, only children of the parent are returned.
            is_movie (bool): Optional filter for movies.
            is_series (bool): Optional filter for series.
            is_news (bool): Optional filter for news.
            is_kids (bool): Optional filter for kids.
            is_sports (bool): Optional filter for sports.
            include_people (bool = True): Optional filter whether to include people.
            include_media (bool = True): Optional filter whether to include media.
            include_genres (bool = True): Optional filter whether to include genres.
            include_studios (bool = True): Optional filter whether to include studios.
            include_artists (bool = True): Optional filter whether to include artists.

        Returns:
            <200> SearchHintResult: Search hint returned.
            <401> requests.Response: Unauthorized
            <403> requests.Response: Forbidden
        """
        request_args = dict(
            searchTerm=search_term,
            startIndex=start_index,
            limit=limit,
            userId=user_id,
            includeItemTypes=include_item_types,
            excludeItemTypes=exclude_item_types,
            mediaTypes=media_types,
            parentId=parent_id,
            isMovie=is_movie,
            isSeries=is_series,
            isNews=is_news,
            isKids=is_kids,
            isSports=is_sports,
            includePeople=include_people,
            includeMedia=include_media,
            includeGenres=include_genres,
            includeStudios=include_studios,
            includeArtists=include_artists,
        )
        return self._get(path='/Search/Hints', request_args=request_args, response_type=SearchHintResult)

