def linear_search(student_names: list[str], target_student: str) -> int | None:
    """Return the index of a matching student name using linear search.

    Matching is case-insensitive.
    Return None if no matching student is found.
    """
    
    for index, student_name in enumerate(student_names):
        if target_student.strip().lower() == student_name.strip().lower():
            return index
            
    return None
    
if __name__ == "__main__":
    
    student_names = [
        "Ali",
        "Jasur",
        "Behruz",
        "Sardor",
        "Aziz",
        "Kamron"
    ]
    print(linear_search(student_names, "behruz"))
    print(linear_search(student_names, "mahmut"))