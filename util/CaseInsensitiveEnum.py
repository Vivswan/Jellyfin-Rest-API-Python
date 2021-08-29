from enum import Enum


class CaseInsensitiveEnum(str, Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.name.lower() == value.lower():
                return member
        for member in cls:
            if member.value.lower() == value.lower():
                return member

    def __str__(self):
        return str(self.value)
