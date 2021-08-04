from enum import Enum


class CaseInsensitiveEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.name.lower() == value.lower():
                return member
        for member in cls:
            if member.value.lower() == value.lower():
                return member
