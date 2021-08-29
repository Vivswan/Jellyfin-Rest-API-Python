from data_classes.theme_media_result_class import ThemeMediaResultClass
from util.from_type import *


@dataclass
class AllThemeMediaResult:
    """Class ThemeMediaResult."""
    soundtrack_songs_result: Optional[ThemeMediaResultClass] = None
    """Class ThemeMediaResult."""
    theme_songs_result: Optional[ThemeMediaResultClass] = None
    """Class ThemeMediaResult."""
    theme_videos_result: Optional[ThemeMediaResultClass] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AllThemeMediaResult':
        assert isinstance(obj, dict)
        soundtrack_songs_result = from_union([ThemeMediaResultClass.from_dict, from_none], obj.get("SoundtrackSongsResult"))
        theme_songs_result = from_union([ThemeMediaResultClass.from_dict, from_none], obj.get("ThemeSongsResult"))
        theme_videos_result = from_union([ThemeMediaResultClass.from_dict, from_none], obj.get("ThemeVideosResult"))
        return AllThemeMediaResult(soundtrack_songs_result, theme_songs_result, theme_videos_result)

    def to_dict(self) -> dict:
        result: dict = {}
        result["SoundtrackSongsResult"] = from_union([lambda x: to_class(ThemeMediaResultClass, x), from_none], self.soundtrack_songs_result)
        result["ThemeSongsResult"] = from_union([lambda x: to_class(ThemeMediaResultClass, x), from_none], self.theme_songs_result)
        result["ThemeVideosResult"] = from_union([lambda x: to_class(ThemeMediaResultClass, x), from_none], self.theme_videos_result)
        return result


