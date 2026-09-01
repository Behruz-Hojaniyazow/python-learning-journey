def linear_search(student_ids: list[int], target_id: int) -> int:
    """Return the index of target_id using linear search.

    Return -1 if target_id is not found.
    """
    
    for index, student_id in enumerate(student_ids):
        if student_id == target_id:
            return index
            
    return -1
    
if __name__ == "__main__":
    
    student_ids = [1045, 2031, 1008, 3056, 1077, 4012, 2099, 1502]
    print(linear_search(student_ids, 3056))