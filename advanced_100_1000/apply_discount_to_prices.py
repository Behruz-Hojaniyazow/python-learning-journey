previous_prices = {
  'iPhone 17e' : 600,
  'iPhone 17' : 800,
  'iPhone Air' : 1000,
  'iPhone 17 Pro' : 1100,
  'iPhone 17 Pro Max' : 1200
}
new_prices = dict(
  map(lambda item: (
    item[0],
    int(item[1] * 0.8) if (item[1] 
* 0.8).is_integer() else item[1] * 0.8), previous_prices.items())
)
print("Previous price of Apple phones")
for item, price in previous_prices.items():
  print(f" - {item} costs ${price}!")
print("\nNew Prices for Apple phones")
for item, price in new_prices.items():
  print(f" - {item} costs ${price}!")