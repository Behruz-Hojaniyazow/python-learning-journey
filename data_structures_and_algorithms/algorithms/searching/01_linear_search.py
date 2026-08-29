def linear_search(numbers: list[int], target: int) -> int:
    """Return the index of target using linear search.

    Return -1 if target is not found.
    """
    
    for index, number in enumerate(numbers):
        if target == number:
            return index
            
    return -1

if __name__ == "__main__":   
    numbers = [19, 3, 20, 99, 67, 76]
    result = linear_search(numbers, 99)
    print(result)