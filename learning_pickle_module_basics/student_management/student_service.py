from status import StudentStatus
from models import StudentData
from storage import StudentStorage

class StudentManagement:
    
    def __init__(self, storage: StudentStorage) -> None:
        self.storage = storage
        
    def add_students(self, name: str, course: str, score: str) -> StudentStatus:
        
        students: list[StudentData] = self.storage.load_students()
        
        if not name or not name.strip():
            return StudentStatus.EMPTY_NAME
            
        clean_name = name.strip().lower()
        
        if course is None or course == "":
            return StudentStatus.EMPTY_COURSE
            
        try:    
            
            clean_course = int(course)
            
            if clean_course > 4:
                return StudentStatus.COURSE_TOO_HIGH
                
            if clean_course <= 0:
                return StudentStatus.COURSE_TOO_LOW
                
        except ValueError:
            return StudentStatus.INVALID_FORMAT_COURSE
        
        if score is None or score == "":
            return StudentStatus.EMPTY_SCORE
            
        try:
                
            clean_score = float(score)
                
            if clean_score > 100:
                return StudentStatus.SCORE_TOO_HIGH
                
            if clean_score < 0:
                return StudentStatus.SCORE_TOO_LOW
            final_score = int(clean_score) if clean_score.is_integer() else clean_score
            
        except ValueError:
            return StudentStatus.INVALID_FORMAT_SCORE
            
        for student in students:
            if student["name"].lower() == clean_name:
                return StudentStatus.DUPLICATE_NAME
            
        student = {
            "name" : clean_name,
            "course" : clean_course,
            "score" : final_score
        }
        
        students.append(student)
        if self.storage.save_students(students):
            return StudentStatus.SUCCESS
            
        return StudentStatus.SAVE_ERROR
            
    def get_students_data(self) -> list[StudentData]:
        return self.storage.load_students()
        
    def is_empty(self) -> bool:
        return len(self.get_students_data()) == 0