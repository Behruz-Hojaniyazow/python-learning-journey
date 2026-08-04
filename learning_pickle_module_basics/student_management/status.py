from enum import Enum, auto

class StudentStatus(Enum):
    # 1. Umumiy va Tizim holatlari
    SUCCESS = auto()
    SAVE_ERROR = auto()
    
    # 2. Ism bilan bog'liq xatoliklar
    EMPTY_NAME = auto()
    DUPLICATE_NAME = auto()
    
    # 3. Kurs bilan bog'liq xatoliklar
    EMPTY_COURSE = auto()
    INVALID_FORMAT_COURSE = auto()
    COURSE_TOO_LOW = auto()
    COURSE_TOO_HIGH = auto()
    
    # 4. Baho bilan bog'liq xatoliklar
    EMPTY_SCORE = auto()
    INVALID_FORMAT_SCORE = auto()
    SCORE_TOO_LOW = auto()
    SCORE_TOO_HIGH = auto()
