class BankAccount:
    
    def __init__(self, owner_name: str, balance: int) -> None:
        self.owner_name = owner_name
        self.balance = balance
        
    def __repr__(self) -> str:
        return f"BankAccount: (Owner='{self.owner_name.title()}', balance='{self.balance}')"
        
    def __str__(self) -> str:
        return f"Private Account owner {self.owner_name.title()} | Balance: ${self.balance}"
        
    def __len__(self) -> int:
        return abs(self.balance)
        
    def __gt__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        
        return NotImplemented
        
    def __eq__(self, other) -> bool:
        if isinstance(other, BankAccount):
            return self.balance == other.balance
        
        return NotImplemented

def main() -> None:
    bank_owners = []
    
    print("\nWelcome to KRYOS BANK SYSTEM")
    while True:
        print("\nChoose an action")
        print("Press 1 to add accounts")
        print("Press 2 to see accounts")
        print("Press 3 to compare accounts")
        print("Press 4 to exit")
        
        choice = input("\nChoose from 1 to 4: ").strip()
        
        if choice == '1':
            name = input("\nEnter an account owner's name: ").strip()
            if not name:
                print("\nName cannot be empty")
                continue
            try:
                balance = int(input(f"Enter {name.title()}'s balance: "))
                new_account = BankAccount(name, balance)
                bank_owners.append(new_account)
                print(f"\nSuccessfully added: {new_account}")
            except ValueError:
                print("\nError! Balance must be only integers")
                
        elif choice == '2':
            if not bank_owners:
                print("\nNo accounts found to show")
                continue
            
            print("\n--- Bank Owners ---")
            for acc in bank_owners:
                print(f"Object string: {acc}")
                print(f"Object code: {repr(acc)}")
                print(f"Object balance: {len(acc)}")
                print("-" * 25)
                
        elif choice == '3':
            if len(bank_owners) < 2:
                print("\nNo accounts found to compare. Add at least 2 accounts")
                continue
            
            if len(bank_owners) > 2:
                stopping_loop = False
                while True:
                    acc1 = None
                    acc2 = None
                    
                    print("\nTo compare accounts, you should select 2 accounts\n")
                    for ind, acc in enumerate(bank_owners, start=1):
                        print(f"{ind}. {acc.owner_name.title()}")
                        print("-" * 40)
                        
                    user_choice = input("Select the first account to compare (0 to stop): ").strip()
                    if user_choice == '0':
                        print("Comparing accounts stopped")
                        stopping_loop = False
                        break
                    
                    if user_choice.isdigit() and 1 <= int(user_choice) <= len(bank_owners):
                        first_choice = int(user_choice)
                        acc1 = bank_owners[first_choice - 1]
                        
                    else:
                        print(f"Please select from 1 to {len(bank_owners)}")
                        continue
                        
                    print("\nNow you need to select the 2nd account\n")
                    copied_owners = [acc for acc in bank_owners if acc is not acc1]
                    for ind, acc in enumerate(copied_owners, start=1):
                        print(f"{ind}. {acc.owner_name.title()}")
                        print("-" * 40)
                        
                    user_choice2 = input("Select the 2nd account (0 to stop): ").strip()
                    if user_choice2 == '0':
                        print("Comparing accounts stopped")
                        stopping_loop = False
                        break
                        
                    if user_choice2.isdigit() and 1 <= int(user_choice2) <= len(copied_owners):
                        second_choice = int(user_choice2)
                        acc2 = copied_owners[second_choice - 1]
                        
                        stopping_loop = True
                        break
                            
                            
                    else:
                        print(f"Select from 1 to {len(copied_owners)}")
                        continue
                    
            else:
                acc1 = bank_owners[0]
                acc2 = bank_owners[1]
                stopping_loop = True
            
            if not stopping_loop:
                continue
            
            clear_str = 'Yes' if acc1 > acc2 else 'No'
            clean_str2 = 'Yes' if acc1 == acc2 else 'No'
            print(f"\nComparing: {acc1.owner_name.title()} vs {acc2.owner_name.title()}")
            print(f"Is {acc1.owner_name.title()}'s balance greater than {acc2.owner_name.title()}'s balance? {clear_str}")
            print(f"Are their balances equal? {clean_str2}")
        elif choice == '4':
            print("\nThank you for using, Kryos Bank System, Bye")
            break
        
        else:
            print("\nPlease choose from 1 to 4")
        
if __name__ == "__main__":
    main()