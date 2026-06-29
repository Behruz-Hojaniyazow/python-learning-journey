class UniversitySystem:
    # Class variable - information shared by all students
    total_students: int = 0
    
    def __init__(self, name: str) -> None:
        """Runs every time a new student is created."""
        # Instance variable - personal information of each student
        self.name: str = name
        
        # We increment the class variable directly by the class name
        UniversitySystem.total_students += 1
# --- System Testing ---    
if __name__ == "__main__":
    
    print(f"Number of starting students: {UniversitySystem.total_students}")
    
    # creating 1st student
    student_1 = UniversitySystem("Behruz")
    print(f"\nNew student added: {student_1.name}, Over Alll students: {UniversitySystem.total_students}")
    
    #creating 2nd student
    student_2 = UniversitySystem("Mahmut")
    print(f"\nNew student added: {student_2.name}, Over All students: {UniversitySystem.total_students}")
    
    # We check if the instance variables are different
    print(f"\n1st object name: {student_1.name}, 2nd object name: {student_2.name}")