fruits = ['apple', 'banana', 'lemon', 'watermelon', 'melon']
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(', '.join(long_fruits))