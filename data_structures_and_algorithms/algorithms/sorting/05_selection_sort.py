def selection_sort(cars: list[int]) -> list[int]:
    """Sort a list of integers in descending order using selection sort."""
    
    n = len(cars)
    
    for i in range(n - 1):
        max_index = i
        
        for j in range(i + 1, n):
            if cars[j] > cars[max_index]:
                max_index = j
                
        if max_index != i:
            cars[i], cars[max_index] = (
                cars[max_index],
                cars[i]
            )
            
    return cars
            
if __name__ == "__main__":
    
    cars = [10000, 8700, 15000, 9000]
    print(selection_sort(cars))