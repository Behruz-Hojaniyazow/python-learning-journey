def selection_sort(names: list[str]) -> list[str]:
    """Sort a list of strings in descending order using Selection Sort."""
    
    n = len(names)
    
    for i in range(n - 1):
        max_index = i
        
        for j in range(i + 1, n):
            if names[j] > names[max_index]:
                max_index = j
                
        if max_index != i:
            names[i], names[max_index] = (
                names[max_index],
                names[i]
            )
    
    return names
    
if __name__ == "__main__":
    
    names = ["anvar", "behruz", "zamira"]
    print(selection_sort(names))