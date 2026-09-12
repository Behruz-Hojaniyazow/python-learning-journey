def selection_sort(names: list[str]) -> list[str]:
    """Sort a list of strings in ascending order using Selection Sort."""
    
    n = len(names)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i + 1, n):
            if names[j] < names[min_index]:
                min_index = j
                
        if min_index != i:
            names[i], names[min_index] = (
                names[min_index],
                names[i]
            )
            
    return names
            
if __name__ == "__main__":
    
    names = ["anvar", "nuriya", "mahmut"]
    print(selection_sort(names))