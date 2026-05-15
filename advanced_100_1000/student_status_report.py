numbers = [34, 78, 98, 87, 63]

string_nums = ['PASS' if num >= 70 else 'FAIL' for num in numbers]
print('\n'.join(string_nums))