def recursive_countup(n: int) -> list[int]:
    """Return a sequence of integers starting from n."""
    
    if n >= 11:
        return []
        
    return [n] + recursive_countup(n + 1)
    
if __name__ == "__main__":
    
    result = recursive_countup(1)
    print(", ".join(map(str, result)))