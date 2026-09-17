def recursive_sum(x: int) -> int:
    """Return the sum of integers from 1 to x using recursion."""
    
    if x <= 1:
        return 1
        
    return x + sum(x - 1)
    
if __name__ == "__main__":
    print(recursive_sum(5))