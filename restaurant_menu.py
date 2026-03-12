#top 16 best dishes in the world
restaurant_menu = {
          "Pizza" : 12,
          "Sushi" : 15,
          "Tacos" : 8,
          "Rendang" : 14,
          "Pad Thai" : 11,
          "Gyros" : 9,
          "Biryani" : 13,
          "Peking Duck" : 25,
          "Steak" : 30,
          "Burger" : 10,
          "Carbonara" : 14,
          "Pilof" : 5,
          "Shawarma" : 7,
          "Paella" : 20,
          "Dumplings" : 9,
          "Nasi Lemak" : 8
}
total_price = 0
orders = []
#asking 3 dishes from the user
for i in range(1,4):
  query = input(f"{i} What kind of food do you want to order ?")
  if query in restaurant_menu:
    print(f"Okay, {query} will be ready in 5 minutes")
    orders.append(query)
    total_price += restaurant_menu[query]
  else:
    print(f"Sorry we don't have {query} in our menu")
print(f"Your orders: {', '.join(orders)}")
print(f"Total cost {total_price}")