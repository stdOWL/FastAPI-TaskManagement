from enum import Enum


class ExceptionStatus(str, Enum):
    SUCCESS = 0
    APPROVED = 0
    WARNING = 2
    FAIL = 1
