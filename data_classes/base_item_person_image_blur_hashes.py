from util.from_type import *


@dataclass
class BaseItemPersonImageBlurHashes:
    """Gets or sets the primary image blurhash."""
    art: Optional[Dict[str, str]] = None
    backdrop: Optional[Dict[str, str]] = None
    banner: Optional[Dict[str, str]] = None
    box: Optional[Dict[str, str]] = None
    box_rear: Optional[Dict[str, str]] = None
    chapter: Optional[Dict[str, str]] = None
    disc: Optional[Dict[str, str]] = None
    logo: Optional[Dict[str, str]] = None
    menu: Optional[Dict[str, str]] = None
    primary: Optional[Dict[str, str]] = None
    profile: Optional[Dict[str, str]] = None
    screenshot: Optional[Dict[str, str]] = None
    thumb: Optional[Dict[str, str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BaseItemPersonImageBlurHashes':
        assert isinstance(obj, dict)
        art = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Art"))
        backdrop = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Backdrop"))
        banner = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Banner"))
        box = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Box"))
        box_rear = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("BoxRear"))
        chapter = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Chapter"))
        disc = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Disc"))
        logo = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Logo"))
        menu = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Menu"))
        primary = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Primary"))
        profile = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Profile"))
        screenshot = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Screenshot"))
        thumb = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("Thumb"))
        return BaseItemPersonImageBlurHashes(art, backdrop, banner, box, box_rear, chapter, disc, logo, menu, primary, profile, screenshot, thumb)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Art"] = from_union([lambda x: from_dict(from_str, x), from_none], self.art)
        result["Backdrop"] = from_union([lambda x: from_dict(from_str, x), from_none], self.backdrop)
        result["Banner"] = from_union([lambda x: from_dict(from_str, x), from_none], self.banner)
        result["Box"] = from_union([lambda x: from_dict(from_str, x), from_none], self.box)
        result["BoxRear"] = from_union([lambda x: from_dict(from_str, x), from_none], self.box_rear)
        result["Chapter"] = from_union([lambda x: from_dict(from_str, x), from_none], self.chapter)
        result["Disc"] = from_union([lambda x: from_dict(from_str, x), from_none], self.disc)
        result["Logo"] = from_union([lambda x: from_dict(from_str, x), from_none], self.logo)
        result["Menu"] = from_union([lambda x: from_dict(from_str, x), from_none], self.menu)
        result["Primary"] = from_union([lambda x: from_dict(from_str, x), from_none], self.primary)
        result["Profile"] = from_union([lambda x: from_dict(from_str, x), from_none], self.profile)
        result["Screenshot"] = from_union([lambda x: from_dict(from_str, x), from_none], self.screenshot)
        result["Thumb"] = from_union([lambda x: from_dict(from_str, x), from_none], self.thumb)
        return result


