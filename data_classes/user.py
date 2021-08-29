from util.from_type import *


@dataclass
class User:
    """User data for this item based on the user it's being requested for.
    
    Class UserItemDataDto.
    """
    """Gets or sets a value indicating whether this instance is favorite."""
    is_favorite: Optional[bool] = None
    """Gets or sets the item identifier."""
    item_id: Optional[str] = None
    """Gets or sets the key."""
    key: Optional[str] = None
    """Gets or sets the last played date."""
    last_played_date: Optional[datetime] = None
    """Gets or sets a value indicating whether this MediaBrowser.Model.Dto.UserItemDataDto is
    likes.
    """
    likes: Optional[bool] = None
    """Gets or sets the playback position ticks."""
    playback_position_ticks: Optional[int] = None
    """Gets or sets the play count."""
    play_count: Optional[int] = None
    """Gets or sets a value indicating whether this MediaBrowser.Model.Dto.UserItemDataDto is
    played.
    """
    played: Optional[bool] = None
    """Gets or sets the played percentage."""
    played_percentage: Optional[float] = None
    """Gets or sets the rating."""
    rating: Optional[float] = None
    """Gets or sets the unplayed item count."""
    unplayed_item_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        is_favorite = from_union([from_bool, from_none], obj.get("IsFavorite"))
        item_id = from_union([from_str, from_none], obj.get("ItemId"))
        key = from_union([from_str, from_none], obj.get("Key"))
        last_played_date = from_union([from_datetime, from_none], obj.get("LastPlayedDate"))
        likes = from_union([from_bool, from_none], obj.get("Likes"))
        playback_position_ticks = from_union([from_int, from_none], obj.get("PlaybackPositionTicks"))
        play_count = from_union([from_int, from_none], obj.get("PlayCount"))
        played = from_union([from_bool, from_none], obj.get("Played"))
        played_percentage = from_union([from_float, from_none], obj.get("PlayedPercentage"))
        rating = from_union([from_float, from_none], obj.get("Rating"))
        unplayed_item_count = from_union([from_int, from_none], obj.get("UnplayedItemCount"))
        return User(is_favorite, item_id, key, last_played_date, likes, playback_position_ticks, play_count, played, played_percentage, rating, unplayed_item_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["IsFavorite"] = from_union([from_bool, from_none], self.is_favorite)
        result["ItemId"] = from_union([from_str, from_none], self.item_id)
        result["Key"] = from_union([from_str, from_none], self.key)
        result["LastPlayedDate"] = from_union([lambda x: x.isoformat(), from_none], self.last_played_date)
        result["Likes"] = from_union([from_bool, from_none], self.likes)
        result["PlaybackPositionTicks"] = from_union([from_int, from_none], self.playback_position_ticks)
        result["PlayCount"] = from_union([from_int, from_none], self.play_count)
        result["Played"] = from_union([from_bool, from_none], self.played)
        result["PlayedPercentage"] = from_union([to_float, from_none], self.played_percentage)
        result["Rating"] = from_union([to_float, from_none], self.rating)
        result["UnplayedItemCount"] = from_union([from_int, from_none], self.unplayed_item_count)
        return result


