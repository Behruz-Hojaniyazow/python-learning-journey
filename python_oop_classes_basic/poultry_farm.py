class BrahmaChicken:
  
    def __init__(self, age, weight,   is_hungry = True):
        self.age = age
        self.weight = weight
        self.is_hungry = is_hungry
        
    def feed(self):
        self.is_hungry = False
        self.weight += 1
        
        
    def show_result(self):
        return self.age, self.weight, self.is_hungry
        
print("\n🐓 KRYOS CARE: Welcome to the Brahma Chicken Program!")
print("-" * 35)

chicken1 = BrahmaChicken(3, 5)

age, weight, is_hungry = chicken1.show_result()
hunger_status = "Yes" if is_hungry else "No"

print("📊 CURRENT CONDITION")
print(f"\nAge: {age}, Weight: {weight} kg, Is chicken hungry?: {hunger_status}")

print("\n⏳ The chicken is being fed grain (the feed method has been activated)...")


chicken1.feed()
age, weight, is_hungry = chicken1.show_result()
hunger_status = "Yes" if is_hungry else "No"

print("\n✅ AFTER FEEDING:")
print(f"Age: {age}, Weight: {weight} kg, Is chicken hungry?: {hunger_status}")
print("-" * 35)