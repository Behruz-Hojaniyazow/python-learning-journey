def selection_sort(numbers: list[int]) -> list[int]:
    """Sort a list of integers in ascending order using Selection Sort."""
        
    n = len(numbers)
    
    for i in range(n - 1):
        min_index = i
        
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
                
        if min_index != i:        
            numbers[i], numbers[min_index] = (
                numbers[min_index],
                numbers[i]
            )
            
    return numbers
    
if __name__ == "__main__":
    
    numbers = [5, 2, 1, 4, 3]
    result = selection_sort(numbers)
    print(result)