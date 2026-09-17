def recursive_factorial(x: int) -> int:
	
	if x < 0:
		raise ValueError("Not allowed numbers lower than 1")

	if x <= 1:
		return 1
		
	return x * recursive_factorial(x - 1)

if __name__ == "__main__":
	try:		
		print(recursive_factorial(5))
	except ValueError as e:
		print(e)