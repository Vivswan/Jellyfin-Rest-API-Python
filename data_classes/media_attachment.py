from util.from_type import *


@dataclass
class MediaAttachment:
    """Class MediaAttachment."""
    """Gets or sets the codec."""
    codec: Optional[str] = None
    """Gets or sets the codec tag."""
    codec_tag: Optional[str] = None
    """Gets or sets the comment."""
    comment: Optional[str] = None
    """Gets or sets the delivery URL."""
    delivery_url: Optional[str] = None
    """Gets or sets the filename."""
    file_name: Optional[str] = None
    """Gets or sets the index."""
    index: Optional[int] = None
    """Gets or sets the MIME type."""
    mime_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MediaAttachment':
        assert isinstance(obj, dict)
        codec = from_union([from_str, from_none], obj.get("Codec"))
        codec_tag = from_union([from_str, from_none], obj.get("CodecTag"))
        comment = from_union([from_str, from_none], obj.get("Comment"))
        delivery_url = from_union([from_str, from_none], obj.get("DeliveryUrl"))
        file_name = from_union([from_str, from_none], obj.get("FileName"))
        index = from_union([from_int, from_none], obj.get("Index"))
        mime_type = from_union([from_str, from_none], obj.get("MimeType"))
        return MediaAttachment(codec, codec_tag, comment, delivery_url, file_name, index, mime_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Codec"] = from_union([from_str, from_none], self.codec)
        result["CodecTag"] = from_union([from_str, from_none], self.codec_tag)
        result["Comment"] = from_union([from_str, from_none], self.comment)
        result["DeliveryUrl"] = from_union([from_str, from_none], self.delivery_url)
        result["FileName"] = from_union([from_str, from_none], self.file_name)
        result["Index"] = from_union([from_int, from_none], self.index)
        result["MimeType"] = from_union([from_str, from_none], self.mime_type)
        return result


