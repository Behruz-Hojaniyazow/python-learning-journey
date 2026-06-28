class Engine:
    """Engine model for KRYOS cars."""
  
    def __init__(self, horse_power):
        self.horse_power = horse_power
        
class KryosAuraCar:
    """KRYOS AURA car model."""
    
    def __init__(self, engine: Engine):
        self.engine = engine
        
    def start_engine(self) -> str:
        """Start the engine and restore its power."""
        
        return f"KRYOS AURA CAR has {self.engine.horse_power} horse power"

def main():
    """Main initialization block (with local variables)."""
    
    aura_engine = Engine(450)
    aura_car = KryosAuraCar(aura_engine)
    print(aura_car.start_engine())
    
if __name__ == "__main__":
    main()