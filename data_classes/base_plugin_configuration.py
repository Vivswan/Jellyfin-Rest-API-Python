from util.from_type import *


@dataclass
class BasePluginConfiguration:
    """Class BasePluginConfiguration."""
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'BasePluginConfiguration':
        assert isinstance(obj, dict)
        return BasePluginConfiguration()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


