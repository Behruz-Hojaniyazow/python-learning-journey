def recursive_count_down(n: int) -> list[int]:
    """Return a countdown from n to 1 using recursion."""
    
    if n <= 0:
        return []
    
    return [n] + recursive_count_down(n - 1)
    
if __name__ == "__main__":
    
    result = recursive_count_down(10)
    print(", ".join(map(str, result)))