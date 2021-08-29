from data_classes.song_info import SongInfo
from util.from_type import *


@dataclass
class AlbumInfoClass:
    """Gets or sets the album artist."""
    album_artists: Optional[List[str]] = None
    """Gets or sets the artist provider ids."""
    artist_provider_ids: Optional[Dict[str, str]] = None
    index_number: Optional[int] = None
    is_automated: Optional[bool] = None
    """Gets or sets the metadata country code."""
    metadata_country_code: Optional[str] = None
    """Gets or sets the metadata language."""
    metadata_language: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    parent_index_number: Optional[int] = None
    """Gets or sets the path."""
    path: Optional[str] = None
    premiere_date: Optional[datetime] = None
    """Gets or sets the provider ids."""
    provider_ids: Optional[Dict[str, str]] = None
    song_infos: Optional[List[SongInfo]] = None
    """Gets or sets the year."""
    year: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AlbumInfoClass':
        assert isinstance(obj, dict)
        album_artists = from_union([lambda x: from_list(from_str, x), from_none], obj.get("AlbumArtists"))
        artist_provider_ids = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ArtistProviderIds"))
        index_number = from_union([from_int, from_none], obj.get("IndexNumber"))
        is_automated = from_union([from_bool, from_none], obj.get("IsAutomated"))
        metadata_country_code = from_union([from_str, from_none], obj.get("MetadataCountryCode"))
        metadata_language = from_union([from_str, from_none], obj.get("MetadataLanguage"))
        name = from_union([from_str, from_none], obj.get("Name"))
        parent_index_number = from_union([from_int, from_none], obj.get("ParentIndexNumber"))
        path = from_union([from_str, from_none], obj.get("Path"))
        premiere_date = from_union([from_datetime, from_none], obj.get("PremiereDate"))
        provider_ids = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ProviderIds"))
        song_infos = from_union([lambda x: from_list(SongInfo.from_dict, x), from_none], obj.get("SongInfos"))
        year = from_union([from_int, from_none], obj.get("Year"))
        return AlbumInfoClass(album_artists, artist_provider_ids, index_number, is_automated, metadata_country_code, metadata_language, name, parent_index_number, path, premiere_date, provider_ids, song_infos, year)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AlbumArtists"] = from_union([lambda x: from_list(from_str, x), from_none], self.album_artists)
        result["ArtistProviderIds"] = from_union([lambda x: from_dict(from_str, x), from_none], self.artist_provider_ids)
        result["IndexNumber"] = from_union([from_int, from_none], self.index_number)
        result["IsAutomated"] = from_union([from_bool, from_none], self.is_automated)
        result["MetadataCountryCode"] = from_union([from_str, from_none], self.metadata_country_code)
        result["MetadataLanguage"] = from_union([from_str, from_none], self.metadata_language)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ParentIndexNumber"] = from_union([from_int, from_none], self.parent_index_number)
        result["Path"] = from_union([from_str, from_none], self.path)
        result["PremiereDate"] = from_union([lambda x: x.isoformat(), from_none], self.premiere_date)
        result["ProviderIds"] = from_union([lambda x: from_dict(from_str, x), from_none], self.provider_ids)
        result["SongInfos"] = from_union([lambda x: from_list(lambda x: to_class(SongInfo, x), x), from_none], self.song_infos)
        result["Year"] = from_union([from_int, from_none], self.year)
        return result


