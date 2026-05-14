nums = [14, 20, 10, 5, 9, 8]
square = [num ** 2 for num in nums if num % 2 == 0]
print(', '.join(map(str, square)))