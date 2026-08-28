def add(num1: int | float, num2: int | float) -> int | float:
	
	# error handling added by mysefl
	if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
		raise ValueError("Please enter only valid numbers")
	
	# algorithm found by sariq dev	
	return num1 + num2
	
try:
	print(add(5, 10))
	
except ValueError as e:
	print(e)