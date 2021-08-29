from util.from_type import *


@dataclass
class WakeOnLANInfo:
    """Provides the MAC address and port for wake-on-LAN functionality."""
    """Gets the MAC address of the device."""
    mac_address: Optional[str] = None
    """Gets or sets the wake-on-LAN port."""
    port: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WakeOnLANInfo':
        assert isinstance(obj, dict)
        mac_address = from_union([from_str, from_none], obj.get("MacAddress"))
        port = from_union([from_int, from_none], obj.get("Port"))
        return WakeOnLANInfo(mac_address, port)

    def to_dict(self) -> dict:
        result: dict = {}
        result["MacAddress"] = from_union([from_str, from_none], self.mac_address)
        result["Port"] = from_union([from_int, from_none], self.port)
        return result


