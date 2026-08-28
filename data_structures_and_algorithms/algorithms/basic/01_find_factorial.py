def find_factorial(n: int) -> int:
	
	# error handling added by myself
	if n < 0:
	    raise ValueError("Factorial is not defined for negative numbers")
	
	# algorithm found by sariq dev   
	factorial = 1
	for i in range(1, n+1):
		factorial *= i
		
	return factorial

try:	
    print(find_factorial(7))

except ValueError as e:
    print("An error occured,", e)