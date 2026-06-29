class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    # Obyektning pasporti (Har doim eng qisqa va xavfsiz matn)
    def __str__(self) -> str:
        return f"Account owner: {self.owner}"

    # Oddiy metod (Maxsus harakat va maxfiy ma'lumotlar uchun)
    def get_full_statement(self, security_token: str) -> str:
        if security_token == "SECRET_123":
            return f"Owner: {self.owner}, Balance: ${self.balance}"
        return "Access Denied"

def main():
    
    bank_owner = BankAccount("Behruz", 1245.4)
    print(bank_owner)
    secret_token = "SECRET_123"
    print(bank_owner.get_full_statement(secret_token))
    
if __name__ == "__main__":
    main()