import math

def get_number(prompt):
  """function that only accepts numbers from the user"""
  while True:
    try:
      val = float(input(prompt))
      return int(val) if val.is_integer() else val
    except ValueError:
      print("❌️ Error: Please enter only numbers")
      
def math_result():
  number = get_number("Enter a number: ")
  
  # 1. math.pow(x, y) - y-power of x
  degree = math.pow(number, 2)
  clear_degree = int(degree) if degree.is_integer() else round(degree, 1)
  print(f"Level 2 of {number}: {clear_degree}")
  
  # 2. math.sqrt(x) - square root of a number
  root = math.sqrt(number)
  clear_root = int(root) if root.is_integer() else round(root, 1)
  print(f"Square root of {number}: {clear_root}")
  
  # 3. math.ceil(x) - count the number upwards
  up_ceil = math.ceil(number)
  print(f"Rounding up {number}: {up_ceil}")
  
  # 4. math.floor(x) - rounds a number down
  down_floor = math.floor(number)
  print(f"Rounding down {number}: {down_floor}")
  
if __name__ == '__main__':
  math_result()