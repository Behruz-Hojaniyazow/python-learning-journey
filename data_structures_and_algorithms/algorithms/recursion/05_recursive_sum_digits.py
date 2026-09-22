def recursive_sum_digits(nums: int) -> int:
    """Return the sum of the digits in a non-negative integer using recursion."""
    
    if nums <= 0:
        return 0
        
    return nums % 10 + recursive_sum_digits(nums // 10)
    
if __name__ == "__main__":
    
    print(recursive_sum_digits(4567))