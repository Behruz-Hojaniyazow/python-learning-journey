class Tactic:
    """Empty method in parent class (Acts as an Interface)"""
    
    def execute(self) -> str:
        """Every tactic must implement its own logic."""
        
        raise NotImplementedError("Every tactic must implement its own 'execute' method!")
        
class PossessionGame(Tactic):
    """A game tactic based on ball control."""
    
    def execute(self) -> str:
        return "Possession Game logic: Control the game through short passes and high ball control."
        
class QuickCounter(Tactic):
    """A game tactic based on quick counterattacks."""
    
    def execute(self) -> str:
        return "Quick Counter logic: Quickly transition from dense defense to vertical counterattack."
        
def start_match_tactic(tactic: Tactic):
    """Runs the given tactic logic."""
    # The function doesn't know which class it is coming from, but it calls a method with the same name
    
    print("\n", tactic.execute())
    
def main():
    
    tactic_a = PossessionGame()
    tactic_b = QuickCounter()
    
    start_match_tactic(tactic_a)
    start_match_tactic(tactic_b)

if __name__ == "__main__":
    main()