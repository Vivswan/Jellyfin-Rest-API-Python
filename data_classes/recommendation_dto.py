from util.from_type import *
from data_classes.base_item_dto import BaseItemDto
from data_classes.recommendation_type import RecommendationType


@dataclass
class RecommendationDto:
    baseline_item_name: Optional[str] = None
    category_id: Optional[UUID] = None
    items: Optional[List[BaseItemDto]] = None
    recommendation_type: Optional[RecommendationType] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RecommendationDto':
        assert isinstance(obj, dict)
        baseline_item_name = from_union([from_str, from_none], obj.get("BaselineItemName"))
        category_id = from_union([lambda x: UUID(x), from_none], obj.get("CategoryId"))
        items = from_union([lambda x: from_list(BaseItemDto.from_dict, x), from_none], obj.get("Items"))
        recommendation_type = from_union([RecommendationType, from_none], obj.get("RecommendationType"))
        return RecommendationDto(baseline_item_name, category_id, items, recommendation_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["BaselineItemName"] = from_union([from_str, from_none], self.baseline_item_name)
        result["CategoryId"] = from_union([lambda x: str(x), from_none], self.category_id)
        result["Items"] = from_union([lambda x: from_list(lambda x: to_class(BaseItemDto, x), x), from_none], self.items)
        result["RecommendationType"] = from_union([lambda x: to_enum(RecommendationType, x), from_none], self.recommendation_type)
        return result


