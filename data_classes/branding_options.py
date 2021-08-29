from util.from_type import *


@dataclass
class BrandingOptions:
    """Gets or sets the custom CSS."""
    custom_css: Optional[str] = None
    """Gets or sets the login disclaimer."""
    login_disclaimer: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BrandingOptions':
        assert isinstance(obj, dict)
        custom_css = from_union([from_str, from_none], obj.get("CustomCss"))
        login_disclaimer = from_union([from_str, from_none], obj.get("LoginDisclaimer"))
        return BrandingOptions(custom_css, login_disclaimer)

    def to_dict(self) -> dict:
        result: dict = {}
        result["CustomCss"] = from_union([from_str, from_none], self.custom_css)
        result["LoginDisclaimer"] = from_union([from_str, from_none], self.login_disclaimer)
        return result


