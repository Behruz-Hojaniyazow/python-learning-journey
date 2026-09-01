def binary_search(isbn_numbers: list[int], target_isbn: int) -> int:
    """Return the index of target_isbn using binary search.

    The ISBN numbers must be sorted in ascending order.
    Return -1 if target_isbn is not found.
    """
    
    low = 0
    high = len(isbn_numbers) - 1
    
    while low <= high:
        middle = (low + high) // 2
        
        if isbn_numbers[middle] == target_isbn:
            return middle
            
        if isbn_numbers[middle] > target_isbn:
            high = middle - 1
            
        else:
            low = middle + 1
            
    return -1
    
if __name__ == "__main__":
    
    isbn_numbers = [
        1001,
        1025,
        1050,
        1088,
        1120,
        1155,
        1200,
        1250,
        1305,
        1400,
        1500,
        1600,
        1750,
        1800,
        1900
    ]
    print(binary_search(isbn_numbers, 1500))