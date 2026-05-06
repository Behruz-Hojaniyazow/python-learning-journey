import random
from car_module import car_info

def main() -> None:
  brand_name = "Kryos Aura"
  
  colors = ["white", "gray", "black", "silver", "blue", "red", "green", "beige", "orange"]
  
  random_color = random.choice(colors)
  
  cost = 12500
  result = car_info(brand_name, random_color, cost)
  
  print(result)
  
if __name__ == '__main__':
  main()