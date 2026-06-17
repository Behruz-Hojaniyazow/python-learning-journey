class Phone:
  def __init__(self, brand, battery):
    self.brand = brand
    self.battery = battery
    
  def call(self):
    print(f"📞 Calling from {self.brand.title()} phone...")
    
  def charge(self):
    print(f"{self.brand.title()} is charging.")
    print(f"Battery capacity: {self.battery} mAh")
    
phone1 = Phone("samsung", 5000)
phone1.call()
phone1.charge()