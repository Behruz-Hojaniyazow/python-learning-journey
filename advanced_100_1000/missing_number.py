import random

MAX_NUMBER = 100

def remove_number(start_n: int, stop_n: int) -> tuple[list[int], int]:
	"""Create a range and remove one random number from it."""

	numbers = list(range(start_n, stop_n + 1))
	removed_number = numbers.pop(random.			randint(0, (stop_n - start_n)))
	
	return numbers, removed_number
	
def find_missing(start_n: int, stop_n: int) -> tuple[list[int], int]:
	"""Find the missing number in a given integer range."""
		
	remaining_numbers, _ = remove_number(start_n, stop_n)
	
	expected_sum = (start_n + stop_n) * (stop_n - start_n + 1) // 2
	missing_number = expected_sum - sum(remaining_numbers)
	
	return remaining_numbers, missing_number
	

def main() -> None:
	
	while True:
		print("\n--- 🔍 Missing Number Finder 🔎 ---")
		
		print("\nType 'stop' to stop")
		print("Enter the beginning number:")
		start_input = input("Beginning Number: ").strip()
		
		if start_input.lower() == 'stop':
			print("\nProject stopped, Goodbye!")
			break
		
		if not start_input.isdigit():
			print("\n❌️ Error, Please enter a non-negative integer.")
			continue
			
		print("\nEnter the ending number:")
		stop_input = input("Ending number: ").strip()
		
		if stop_input.lower() == 'stop':
			print("\nProject stopped, Goodbye!")
			break
		
		if not stop_input.isdigit():
			print("\n❌️ Error, Please enter only integers")
			continue
		
		start_num, stop_num = int(start_input), int(stop_input)
		
		if start_num > stop_num:
			print("\n❌️ Beginning number cannot be greater than ending number")
			continue
		
		if stop_num > MAX_NUMBER:
			print(f"\n⚠️ Please enter an ending number between {start_num} and 100")
			continue
		
		remaining_numbers, missing_number = find_missing(start_num, stop_num)
		
		print(f"\n✅️ Range created: {start_num} -> {stop_num}")
		print("\n🗑 One number has been secretly removed from the range")
		print("\n🔍 Searching for the missing number...")
			
		print(f"\n✅️ Missing number found: {missing_number}")
		if remaining_numbers:
			print("Numbers remaining after removal:")
			print(", ".join(map(str, remaining_numbers)))
				
if __name__ == '__main__':
	main()	