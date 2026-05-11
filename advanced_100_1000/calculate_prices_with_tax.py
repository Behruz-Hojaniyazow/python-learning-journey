prices = [110, 50, 78, 35, 94]
new_prices = list(map(lambda x: x * 1.12, prices))
clean_price = [int(p) if isinstance(p, float) and p.is_integer() else round(p, 1) for p in new_prices]
print(', '.join(map(str, clean_price)))