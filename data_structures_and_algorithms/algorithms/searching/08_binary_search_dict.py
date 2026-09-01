def binary_search(students: dict[int, str], target_student: str) -> tuple[int, str] | None:
    """Return the matching student ID and name using binary search.

    Student names are compared case-insensitively.
    Return None if no matching student is found.
    """
    
    sorted_students = sorted(students.items(), key=lambda item: item[1].strip().lower())
    low = 0
    high = len(sorted_students) - 1
    target_name = target_student.strip().lower()
    
    while low <= high:
        
        middle = (low + high) // 2
        student_id, original_name = sorted_students[middle]
        student_name = original_name.strip().lower()
        
        if student_name == target_name:
            return student_id, original_name
            
        if student_name > target_name:
            high = middle - 1
            
        else:
            low = middle + 1
            
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
    
    result = binary_search(students, "behruz")
    print(result)