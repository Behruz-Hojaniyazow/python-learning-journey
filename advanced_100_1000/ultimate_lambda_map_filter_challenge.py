numbers = [-13, 47, -5, 8, 10, 9, 20]
new_numbers = list(
  map(lambda num: num ** 2,
  filter(lambda num: num >= 0 and num % 2 == 0, numbers)))
print(', '.join(map(str, new_numbers)))