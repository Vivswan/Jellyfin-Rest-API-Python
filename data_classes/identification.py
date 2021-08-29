from data_classes.h_t_t_p_header_info import HTTPHeaderInfo
from util.from_type import *


@dataclass
class Identification:
    """Gets or sets the Identification."""
    """Gets or sets the name of the friendly."""
    friendly_name: Optional[str] = None
    """Gets or sets the headers."""
    headers: Optional[List[HTTPHeaderInfo]] = None
    """Gets or sets the manufacturer."""
    manufacturer: Optional[str] = None
    """Gets or sets the manufacturer URL."""
    manufacturer_url: Optional[str] = None
    """Gets or sets the model description."""
    model_description: Optional[str] = None
    """Gets or sets the name of the model."""
    model_name: Optional[str] = None
    """Gets or sets the model number."""
    model_number: Optional[str] = None
    """Gets or sets the model URL."""
    model_url: Optional[str] = None
    """Gets or sets the serial number."""
    serial_number: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Identification':
        assert isinstance(obj, dict)
        friendly_name = from_union([from_str, from_none], obj.get("FriendlyName"))
        headers = from_union([lambda x: from_list(HTTPHeaderInfo.from_dict, x), from_none], obj.get("Headers"))
        manufacturer = from_union([from_str, from_none], obj.get("Manufacturer"))
        manufacturer_url = from_union([from_str, from_none], obj.get("ManufacturerUrl"))
        model_description = from_union([from_str, from_none], obj.get("ModelDescription"))
        model_name = from_union([from_str, from_none], obj.get("ModelName"))
        model_number = from_union([from_str, from_none], obj.get("ModelNumber"))
        model_url = from_union([from_str, from_none], obj.get("ModelUrl"))
        serial_number = from_union([from_str, from_none], obj.get("SerialNumber"))
        return Identification(friendly_name, headers, manufacturer, manufacturer_url, model_description, model_name, model_number, model_url, serial_number)

    def to_dict(self) -> dict:
        result: dict = {}
        result["FriendlyName"] = from_union([from_str, from_none], self.friendly_name)
        result["Headers"] = from_union([lambda x: from_list(lambda x: to_class(HTTPHeaderInfo, x), x), from_none], self.headers)
        result["Manufacturer"] = from_union([from_str, from_none], self.manufacturer)
        result["ManufacturerUrl"] = from_union([from_str, from_none], self.manufacturer_url)
        result["ModelDescription"] = from_union([from_str, from_none], self.model_description)
        result["ModelName"] = from_union([from_str, from_none], self.model_name)
        result["ModelNumber"] = from_union([from_str, from_none], self.model_number)
        result["ModelUrl"] = from_union([from_str, from_none], self.model_url)
        result["SerialNumber"] = from_union([from_str, from_none], self.serial_number)
        return result


