temps = [-5, 10, -1, 25]
new_temps = ['HOT' if temp > 0 else 'COLD' for temp in temps]
# positives 'HOT'
# negatives 'COLD'

print(', '.join(new_temps))