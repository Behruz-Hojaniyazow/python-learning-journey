class IncubatorTracker:
    
    def __init__(self, day: int, temp: int | float, humidity: int | float) -> None:
        self.day = day
        self.temp = temp
        self.humidity = humidity
        
    def __str__(self) -> str:
        return f"Incubation period: Day {self.day}. Temperature {self.temp}°C, Humidity {self.humidity}%"
        
    def __repr__(self) -> str:
        return f"IncubatorTracker(day='{self.day}' temp='{self.temp}' humidity='{self.humidity})'"

if __name__ == "__main__":        
    incubator = IncubatorTracker(15, 37.6, 65)
    print(incubator)
    
    incubator_list = [incubator]
    print(incubator_list)