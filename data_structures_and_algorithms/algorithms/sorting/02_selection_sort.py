def selection_sort(numbers: list[int]) -> list[int]:
    
    n = len(numbers)
    
    for i in range(n - 1):
        max_index = i
        
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_index]:
                max_index = j
                
        if max_index != i:
            numbers[i], numbers[max_index] = (
                numbers[max_index],
                numbers[i]
            )
    
    return numbers
    
if __name__ == "__main__":
    
    numbers = [1, 2, 3, 4, 5]
    descending_order = selection_sort(numbers)
    print(descending_order)