def binary_search(numbers: list[int], target: int) -> int:
    """Return the index of target using binary search.

    The numbers must be sorted in ascending order.
    Return -1 if target is not found.
    """
    
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        m = (low + high) // 2
        
        if numbers[m] == target:
            return m
            
        if numbers[m] > target:
            high = m - 1
            
        else:
            low = m + 1
            
    return -1

if __name__ == "__main__":    
    numbers = [2, 5, 10, 45, 52, 67, 89]
    result = binary_search(numbers, 89)
    print(result)
        