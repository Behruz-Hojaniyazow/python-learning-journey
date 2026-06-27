class MuayThaiFighter:
    
    def __init__(self, name, strike_power):
        self.name = name
        self.strike_power = strike_power
        
    def show_stats(self):
        return f"Warrior: {self.name.title()}, Strike Power: {self.strike_power}"
        
class TrainingCamp:
    
    def __init__(self, camp_name):
        self.camp_name = camp_name
        
    def start_drill(self, fighter_object):
        
        fighter_object.strike_power += 5
    
        return f"\n[{self.camp_name.title()}] Training Completed! {fighter_object.name}'s attack power increased"
        
fighter = MuayThaiFighter("Behruz", 20)
train_camp = TrainingCamp("KRYOS Muay Thai Home Camp")
print("\nBefore Training:")
print(fighter.show_stats())

print(train_camp.start_drill(fighter))

print("\nAfter training:")
print(fighter.show_stats())