numbers = list(range(1, 11))
new_nums = [num * 2 for num in numbers]
print(', '.join(map(str, new_nums)))