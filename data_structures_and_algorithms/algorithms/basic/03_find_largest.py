def find_bigger(a: int | float, b: int | float, c: int | float) -> int | float:
    
    # error handling added by myself
    if not all(isinstance(number, (int, float)) for number in (a, b, c)):
        
        raise TypeError("Please enter valid numbers")
        
    # algorithm found by sariq dev
    if a > b:
        if a > c:
            return a
			
        else:
            return c
	
    if b > c:
        return b
			
    return c
			
			
try:
    print(find_bigger(1, 3.5, 3.5))
    
except TypeError as e:
    print(e)