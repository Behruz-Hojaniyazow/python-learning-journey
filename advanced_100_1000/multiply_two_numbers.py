num1 = [5, 8, 10]
num2 = [3, 2, 5]
multiply = list(map(lambda x, y: f"{x} × {y} = {x * y}", num1, num2))
clean_result = '\n'.join(map(str, multiply))
print(clean_result)