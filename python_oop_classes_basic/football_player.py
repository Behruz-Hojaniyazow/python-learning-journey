class Player:
  
    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina
        
    def sprint(self):
        if self.stamina < 10:
            return "❌ Stamina is too low, the player cannot run!"
        
        else:
            self.stamina -= 10
            return self.stamina
    
    def rest(self):
        if self.stamina >= 100:
            return "🔋 The player has had enough rest (Stamina 100)"
        
        else:    
            self.stamina += 20
            if self.stamina > 100:
                self.stamina = 100
            return self.stamina

def main():
    print("\n⚽️ KRYOS PLAYER CARE, Welcome to the Player care program ⚽️")
    print("-" * 35)
    
    player1 = Player("Cristiano Ronaldo", 100)
    
    while True:
    
        print("\n📊 CURRENT CONDITION:")
        print(f"Player name: {player1.name.title()}, Stamina Condition: {player1.stamina}")
        
        print("Type 'stop' to end the game")
        user_input = input("Would you like to sub on this player (yes/no): ").strip()
        
        if user_input.lower() == "stop":
            print("\n✨️ Thank you for using KRYOS programm!")
            break
        
        if user_input.lower() in ("yes", "y"):
            result = player1.sprint()
            
            if isinstance(result, str):
                print(result)
            else:
                print("\n🏃🏻 After playing a football")
                print(f"Player name: {player1.name.title()}, Stamina Condition: {player1.stamina}")
        
        elif user_input.lower() in ("no", "n"):
            result = player1.rest()
            
            if isinstance(result, str):
                print(result)
            
            else:
                print("\n💤 After resting")
                print(f"Player name: {player1.name.title()}, Stamina Condition: {player1.stamina}")
            
        else:
            print("\n❌️ Invalid choice, Please enter only (yes/no)")
    
    print("-" * 35)

if __name__ == "__main__":
    main()