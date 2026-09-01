def binary_search(student_names: list[str], target_student: str) -> int | None:
    """Return the index of a matching student name using binary search.

    Names must be sorted alphabetically.
    Matching is case-insensitive.
    Return None if no matching student is found.
    """
    
    low = 0
    high = len(student_names) - 1
    target_student_name = target_student.strip().lower()
    
    while low <= high:
        middle = (low + high) // 2
        student_name = student_names[middle].strip().lower()
        
        if student_name == target_student_name:
            
            return middle
            
        if student_name > target_student_name:
            high = middle - 1
        
        else:
            low = middle + 1
            
    return None
    
if __name__ == "__main__":
        
    student_names = [
        "Ali",
        "Aziz",
        "Behruz",
        "Jasur",
        "Kamron",
        "Sardor"
    ]
    
    print(binary_search(student_names, "Behruz"))
    print(binary_search(student_names, "mahmut"))