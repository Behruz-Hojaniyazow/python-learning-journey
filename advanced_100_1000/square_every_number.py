numbers = list(range(1,4))

square = list(map(lambda x: x ** 2, numbers))
result = ', '.join(map(str, square))
print(result)