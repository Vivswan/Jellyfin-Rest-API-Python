from util.from_type import *


@dataclass
class RemoteSubtitleInfo:
    author: Optional[str] = None
    comment: Optional[str] = None
    community_rating: Optional[float] = None
    date_created: Optional[datetime] = None
    download_count: Optional[int] = None
    format: Optional[str] = None
    id: Optional[str] = None
    is_hash_match: Optional[bool] = None
    name: Optional[str] = None
    provider_name: Optional[str] = None
    three_letter_iso_language_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemoteSubtitleInfo':
        assert isinstance(obj, dict)
        author = from_union([from_str, from_none], obj.get("Author"))
        comment = from_union([from_str, from_none], obj.get("Comment"))
        community_rating = from_union([from_float, from_none], obj.get("CommunityRating"))
        date_created = from_union([from_datetime, from_none], obj.get("DateCreated"))
        download_count = from_union([from_int, from_none], obj.get("DownloadCount"))
        format = from_union([from_str, from_none], obj.get("Format"))
        id = from_union([from_str, from_none], obj.get("Id"))
        is_hash_match = from_union([from_bool, from_none], obj.get("IsHashMatch"))
        name = from_union([from_str, from_none], obj.get("Name"))
        provider_name = from_union([from_str, from_none], obj.get("ProviderName"))
        three_letter_iso_language_name = from_union([from_str, from_none], obj.get("ThreeLetterISOLanguageName"))
        return RemoteSubtitleInfo(author, comment, community_rating, date_created, download_count, format, id, is_hash_match, name, provider_name, three_letter_iso_language_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Author"] = from_union([from_str, from_none], self.author)
        result["Comment"] = from_union([from_str, from_none], self.comment)
        result["CommunityRating"] = from_union([to_float, from_none], self.community_rating)
        result["DateCreated"] = from_union([lambda x: x.isoformat(), from_none], self.date_created)
        result["DownloadCount"] = from_union([from_int, from_none], self.download_count)
        result["Format"] = from_union([from_str, from_none], self.format)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["IsHashMatch"] = from_union([from_bool, from_none], self.is_hash_match)
        result["Name"] = from_union([from_str, from_none], self.name)
        result["ProviderName"] = from_union([from_str, from_none], self.provider_name)
        result["ThreeLetterISOLanguageName"] = from_union([from_str, from_none], self.three_letter_iso_language_name)
        return result


