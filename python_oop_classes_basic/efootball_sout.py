class EfootballPlayer:
    
    def __init__(self, name: str, rating: int) -> None:
        self.name = name
        self.rating = rating
        
    def __repr__(self) -> str:
        return f"EfootballPlayer(name='{self.name.title()}', rating={self.rating}"
        
    def __str__(self) -> str:
        return f"{self.name.title()} rating: {self.rating}"
        
    def __gt__(self, other: object) -> bool:
        if isinstance(other, EfootballPlayer):
            return self.rating > other.rating
        
        return NotImplemented
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, EfootballPlayer):
            return self.rating == other.rating
        
        return NotImplemented

if __name__ == "__main__":
    
    player1 = EfootballPlayer("cristiano ronaldo", 95)
    player2 = EfootballPlayer("lionel messi", 95)
    print(player1)
    print(player2)
    print(f"{player1.name.title()} > {player2.name.title()}: {player1 > player2}")
    print(f"Equal rating: {player1 == player2}")