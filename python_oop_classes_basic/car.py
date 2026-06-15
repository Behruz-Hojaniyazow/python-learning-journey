class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
    
  def car_info(self):
    print("  Car Info: ⬇️")
    print(
      f"\tBrand: {self.brand.upper()}"
    )
    print(
      f"\tModel: {self.model.title()}"
    )
    print(
      f"\tYear: {self.year}"
    )
  
  def start_engine(self):
    print(f"\n{self.brand.upper()} engine started")
    
car = Car("mercedes-benz", "maybach", 2023)
car.car_info()
car.start_engine()