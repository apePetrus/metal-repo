from enum import Enum

class BandStatus(Enum):
    ACTIVE       = 1
    SPLIT_UP     = 2
    CHANGED_NAME = 3
    UNKNOWN      = 4
