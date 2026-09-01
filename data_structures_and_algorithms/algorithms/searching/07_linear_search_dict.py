def linear_search(students: dict[int, str], target_name: str) -> tuple[int, str] | None:
    """Return the matching student ID and name using linear search.

    Student names are compared case-insensitively.
    Return None if no matching student is found.
    """
    
    for student_id, student_name in students.items():
        if student_name.strip().lower() == target_name.strip().lower():
            
            return student_id, student_name
            
    return None
    
if __name__ == "__main__":
    
    students = {
        1001: "Ali",
        1005: "Behruz",
        1010: "Jasur",
        1020: "Sardor",
        1030: "Aziz",
        1050: "Kamron"
    }
    
    result = linear_search(students, "behruz")
    if result is not None:
        student_id, name = result
        print(f"{student_id}, {name.title()}")
        
    else:
        print(result)
    