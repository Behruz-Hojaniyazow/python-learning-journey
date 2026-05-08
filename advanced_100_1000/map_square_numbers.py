numbers = list(range(1,11))
multiply = list(map(lambda x: x * x, numbers))
result = ', '.join(map(str, multiply))
print(result)