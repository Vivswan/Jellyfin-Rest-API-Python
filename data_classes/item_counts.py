from util.from_type import *


@dataclass
class ItemCounts:
    """Class LibrarySummary."""
    """Gets or sets the album count."""
    album_count: Optional[int] = None
    """Gets or sets the artist count."""
    artist_count: Optional[int] = None
    """Gets or sets the book count."""
    book_count: Optional[int] = None
    """Gets or sets the box set count."""
    box_set_count: Optional[int] = None
    """Gets or sets the episode count."""
    episode_count: Optional[int] = None
    """Gets or sets the item count."""
    item_count: Optional[int] = None
    """Gets or sets the movie count."""
    movie_count: Optional[int] = None
    """Gets or sets the music video count."""
    music_video_count: Optional[int] = None
    """Gets or sets the program count."""
    program_count: Optional[int] = None
    """Gets or sets the series count."""
    series_count: Optional[int] = None
    """Gets or sets the song count."""
    song_count: Optional[int] = None
    """Gets or sets the trailer count."""
    trailer_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ItemCounts':
        assert isinstance(obj, dict)
        album_count = from_union([from_int, from_none], obj.get("AlbumCount"))
        artist_count = from_union([from_int, from_none], obj.get("ArtistCount"))
        book_count = from_union([from_int, from_none], obj.get("BookCount"))
        box_set_count = from_union([from_int, from_none], obj.get("BoxSetCount"))
        episode_count = from_union([from_int, from_none], obj.get("EpisodeCount"))
        item_count = from_union([from_int, from_none], obj.get("ItemCount"))
        movie_count = from_union([from_int, from_none], obj.get("MovieCount"))
        music_video_count = from_union([from_int, from_none], obj.get("MusicVideoCount"))
        program_count = from_union([from_int, from_none], obj.get("ProgramCount"))
        series_count = from_union([from_int, from_none], obj.get("SeriesCount"))
        song_count = from_union([from_int, from_none], obj.get("SongCount"))
        trailer_count = from_union([from_int, from_none], obj.get("TrailerCount"))
        return ItemCounts(album_count, artist_count, book_count, box_set_count, episode_count, item_count, movie_count, music_video_count, program_count, series_count, song_count, trailer_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AlbumCount"] = from_union([from_int, from_none], self.album_count)
        result["ArtistCount"] = from_union([from_int, from_none], self.artist_count)
        result["BookCount"] = from_union([from_int, from_none], self.book_count)
        result["BoxSetCount"] = from_union([from_int, from_none], self.box_set_count)
        result["EpisodeCount"] = from_union([from_int, from_none], self.episode_count)
        result["ItemCount"] = from_union([from_int, from_none], self.item_count)
        result["MovieCount"] = from_union([from_int, from_none], self.movie_count)
        result["MusicVideoCount"] = from_union([from_int, from_none], self.music_video_count)
        result["ProgramCount"] = from_union([from_int, from_none], self.program_count)
        result["SeriesCount"] = from_union([from_int, from_none], self.series_count)
        result["SongCount"] = from_union([from_int, from_none], self.song_count)
        result["TrailerCount"] = from_union([from_int, from_none], self.trailer_count)
        return result


