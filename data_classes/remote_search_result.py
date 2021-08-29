from util.from_type import *


@dataclass
class RemoteSearchResult:
    album_artist: Optional['RemoteSearchResult'] = None
    artists: Optional[List['RemoteSearchResult']] = None
    image_url: Optional[str] = None
    index_number: Optional[int] = None
    index_number_end: Optional[int] = None
    """Gets or sets the name."""
    name: Optional[str] = None
    overview: Optional[str] = None
    parent_index_number: Optional[int] = None
    premiere_date: Optional[datetime] = None
    """Gets or sets the year."""
    production_year: Optional[int] = None
    """Gets or sets the provider ids."""
    provider_ids: Optional[Dict[str, str]] = None
    search_provider_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoteSearchResult':
        assert isinstance(obj, dict)
        album_artist = from_union([RemoteSearchResult.from_dict, from_none], obj.get("AlbumArtist"))
        artists = from_union([lambda x: from_list(RemoteSearchResult.from_dict, x), from_none], obj.get("Artists"))
        image_url = from_union([from_str, from_none], obj.get("ImageUrl"))
        index_number = from_union([from_int, from_none], obj.get("IndexNumber"))
        index_number_end = from_union([from_int, from_none], obj.get("IndexNumberEnd"))
        name = from_union([from_str, from_none], obj.get("Name"))
        overview = from_union([from_str, from_none], obj.get("Overview"))
        parent_index_number = from_union([from_int, from_none], obj.get("ParentIndexNumber"))
        premiere_date = from_union([from_datetime, from_none], obj.get("PremiereDate"))
        production_year = from_union([from_int, from_none], obj.get("ProductionYear"))
        provider_ids = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("ProviderIds"))
        search_provider_name = from_union([from_str, from_none], obj.get("SearchProviderName"))
        return RemoteSearchResult(album_artist, artists, image_url, index_number, index_number_end, name, overview, parent_index_number, premiere_date, production_year, provider_ids, search_provider_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["AlbumArtist"] = from_union([lambda x: to_class(RemoteSearchResult, x), from_none], self.album_artist)
        result["Artists"] = from_union([lambda x: from_list(lambda x: to_class(RemoteSearchResult, x), x), from_none], self.artists)
        result["ImageUrl"] = from_union([from_str, from_none], self.image_url)
        result["IndexNumber"] = from_union([from_int, from_none], self.index_number)
        result["IndexNumberEnd"] = from_union([from_int, from_none], self.index_number_end)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["Overview"] = from_union([from_str, from_none], self.overview)
        result["ParentIndexNumber"] = from_union([from_int, from_none], self.parent_index_number)
        result["PremiereDate"] = from_union([lambda x: x.isoformat(), from_none], self.premiere_date)
        result["ProductionYear"] = from_union([from_int, from_none], self.production_year)
        result["ProviderIds"] = from_union([lambda x: from_dict(from_str, x), from_none], self.provider_ids)
        result["SearchProviderName"] = from_union([from_str, from_none], self.search_provider_name)
        return result


