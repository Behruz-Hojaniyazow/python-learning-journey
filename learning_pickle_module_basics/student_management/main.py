import sys
from student_service import StudentManagement
from storage import StudentStorage
from status import StudentStatus
from models import StudentData
from config import FILE_NAME

STUDENT_ERRORS = {
    # Muvaffaqiyatli holat
    StudentStatus.SUCCESS: "✅ Student successfully added and saved!",
    # Tizimli / Fayl bilan bog'liq xatolik
    StudentStatus.SAVE_ERROR: "❌ Critical error: Failed to save data to the file system.",
    
    # Ism xatoliklari
    StudentStatus.EMPTY_NAME: "❌ Student name cannot be empty.",
    StudentStatus.DUPLICATE_NAME: "⚠️ This student already exists in the database.",
    
    # Kurs xatoliklari
    StudentStatus.EMPTY_COURSE: "❌ Course cannot be empty.",
    StudentStatus.INVALID_FORMAT_COURSE: "❌ Invalid course format. Please use digits only.",
    StudentStatus.COURSE_TOO_HIGH: "❌ Course is too high. Max course allowed is 4.",
    StudentStatus.COURSE_TOO_LOW: "❌ Course is too low. Course must be 1 or higher.",
    
    # Ball xatoliklari
    StudentStatus.EMPTY_SCORE: "❌ Score cannot be empty.",
    StudentStatus.INVALID_FORMAT_SCORE: "❌ Invalid score format. Please enter a valid number.",
    StudentStatus.SCORE_TOO_HIGH: "❌ Score is too high. Max score allowed is 100.",
    StudentStatus.SCORE_TOO_LOW: "❌ Score cannot be negative."
}

def ui_add_student(manager: StudentManagement) -> None:
    
    print("\n--- Adding Students Started ---")
    while True:
        print("Type 'stop' or 0 to stop")
        name = input("Enter a name: ").strip()
        if name.lower() in ('stop', '0'):
            print("\nAdding students stopped")
            break
        
        course = input("Enter a course: ").strip()
        if course.lower() in ('stop', '0'):
            print("\nAdding students stopped")
            break
        
        score = input("Enter a score: ").strip()
        if score.lower() in ('stop', '0'):
            print("\nAdding students stopped")
            break
        
        status = manager.add_students(name, course, score)
        message = STUDENT_ERRORS.get(status, f"Unexpected status: {status.name}")
        print(message)
    
def ui_show_students(manager: StudentManagement) -> None:
    if manager.is_empty():
        print("\nNo students found to show, Database is empty")
        return
    
    students: list[StudentData] = manager.get_students_data()
    
    print("=" * 40)
    print(f" {'Name':<17} | {'Course':<5} | {'Score':<7}")
    print("-" * 40)
    for ind, student in enumerate(students, start=1):
        print(f"{ind}. {student['name'].title():<15} | {student['course']:<6} | {student['score']:<7}")
        print("-" * 40)
        
    
def main() -> None:
    
    storage = StudentStorage(FILE_NAME)
    manager = StudentManagement(storage)
    
    while True:
        print("\n1 -> Add a new student")
        print("2 -> Show all students")
        print("3 -> Exit the program")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '1':
            ui_add_student(manager)
            
        elif choice == '2':
            ui_show_students(manager)
        
        elif choice == '3':
            print("\nThank you for using KRYOS Student Management System, Bye👋🏼")
            sys.exit()
            
        else:
            print("\nPlease choose from 1 to 3")
            
if __name__ == "__main__":
    main()