from util.from_type import *


@dataclass
class ServerDiscoveryInfo:
    """Gets or sets the address."""
    address: Optional[str] = None
    """Gets or sets the endpoint address."""
    endpoint_address: Optional[str] = None
    """Gets or sets the server identifier."""
    id: Optional[str] = None
    """Gets or sets the name."""
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ServerDiscoveryInfo':
        assert isinstance(obj, dict)
        address = from_union([from_str, from_none], obj.get("Address"))
        endpoint_address = from_union([from_str, from_none], obj.get("EndpointAddress"))
        id = from_union([from_str, from_none], obj.get("Id"))
        name = from_union([from_str, from_none], obj.get("Name"))
        return ServerDiscoveryInfo(address, endpoint_address, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Address"] = from_union([from_str, from_none], self.address)
        result["EndpointAddress"] = from_union([from_str, from_none], self.endpoint_address)
        result["Id"] = from_union([from_str, from_none], self.id)
        result["Name"] = from_union([from_str, from_none], self.name)
        return result


