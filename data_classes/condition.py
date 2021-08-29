from util.from_type import *


class Condition(CaseInsensitiveEnum):
    EQUALS = "Equals"
    EQUALS_ANY = "EqualsAny"
    GREATER_THAN_EQUAL = "GreaterThanEqual"
    LESS_THAN_EQUAL = "LessThanEqual"
    NOT_EQUALS = "NotEquals"


