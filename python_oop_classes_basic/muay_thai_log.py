class MuayThaiSession:
  
    def __init__(self, date: str, time: int, calories: int | float) -> None:
        self.date = date
        self.time = time
        self.calories = calories
        
    def __repr__(self) -> str:
        return f"MuayThaiSession(date='{self.date}', time={self.time}, calories={self.calories})"
        
    def __str__(self) -> str:
        return f"Muay Thai Session [{self.date}] | Duration: {self.time} min | Calories: {self.calories} kcal"
        
    def __len__(self) -> int:
        return int(self.time)
    
    def __gt__(self, other: object) -> bool:
        if isinstance(other, MuayThaiSession):
            return self.calories > other.calories
        
        return NotImplemented
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, MuayThaiSession):
            return self.calories == other.calories and self.time == other.time
            
        return NotImplemented
        
if __name__ == "__main__":
    
    session1 = MuayThaiSession("2026-08-04", 60, 700)
    session2 = MuayThaiSession("2026-08-05", 90, 950)
    
    print(session1)
    print(session2)
    
    print(f"\n1-Duration of training: {len(session1)} minutes")
    print(f"2-Duration of training: {len(session2)} minutes")
    
    print(f"\nDid workout 2 burn more calories than workout 1: {session2 > session1}")
    print(f"Are workout 1 and workout 2 equal? {session1 == session2}")