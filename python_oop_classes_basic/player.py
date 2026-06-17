class Player:
  def __init__(self, name, hp, attack):
    self.name = name
    self.hp = hp
    self.attack = attack
    
  def attack_enemy(self):
    print(f"{self.name.title()} attacked the enemy!")
    print(f"Damage dealt: {self.attack}")
    
  def show_stats(self):
    print("\n=== PLAYER STATS ===")
    print(f"Name   : {self.name.title()}")
    print(f"HP     : {self.hp}")
    print(f"Attack : {self.attack}")
  
player = Player("knight", 100, 25)

player.attack_enemy()
player.show_stats()