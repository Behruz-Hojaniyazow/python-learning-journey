class GithubRepo:
    
    def __init__(self, name: str, files: list[str]) -> None:
        self.name = name
        self.files = files
        
    def __repr__(self) -> str:
        return f"GithubRepo: (name='{self.name.title()}', files={self.files})"
        
    def __str__(self) -> str:
        return f"Repository: '{self.name.title()}' | Total files: {len(self.files)}"
        
    def __len__(self) -> int:
        return len(self.files)
        
    def __eq__(self, other: object) -> bool:
        if isinstance(other, GithubRepo):
            return self.files == other.files
            
        return NotImplemented

if __name__ == "__main__":
    
    files_1 = ["password.py", "contact_book.py", "github_manager.py"] 
    user1 = GithubRepo("behruz", files_1)
    
    files_2 = ["mini_database.py", "football_player.py"]
    user2 = GithubRepo("mahmut", files_2)
    
    print(user1)
    print(user2)
    print(f"User 1 total files count: {len(user1)}")
    print(f"User 2 total files count: {len(user2)}")
    print(f"Are repositories equal? {user1 == user2}")
        