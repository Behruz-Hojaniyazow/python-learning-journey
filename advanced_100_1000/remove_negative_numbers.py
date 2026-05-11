nums = [-13, 4, 6, -5, 9, -8]
positive_nums = list(filter(lambda x: x >= 0, nums))
clean_result = ', '.join(map(str, positive_nums))
print(clean_result)