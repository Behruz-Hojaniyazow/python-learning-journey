import sys

class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
    
  def format_balance(self):
    return int(self.balance) if self.balance.is_integer() else self.balance
    
  def deposit(self):
    while True:
      user_choice = input("\nHow much money do you want to add: ").strip()
      print("Type 'stop' to stop adding money!")
      
      if not user_choice:
        print("\n❌️ Please enter a valid number!")
        continue
      
      if user_choice.lower() == 'stop':
        print("\nAdding money stopped")
        break
      try:
        deposit_amount = float(user_choice)
        if deposit_amount <= 0:
          print("\n❌️ Please enter a positive number!")
          continue
      except ValueError:
        print("\n❌️ Error, Please enter only numbers!")
        continue
      
      self.balance += deposit_amount
      print(f"\nNow you have ${self.format_balance()} in your account")
      
  def withdraw(self):
    while True:
      user_choice = input("How much money would you like to take money fron your balance: ").strip()
      print("Type stop to stop taking money!")
      
      if user_choice.lower() == 'stop':
        print("\nYou stopped to take money")
        break
      
      if not user_choice:
        print("\nPlease enter a valid number!")
        continue
      try:
        amount = float(user_choice)
        if amount <= 0:
          print("\n❌️ Please enter a positive number!")
          continue
      except ValueError:
        print("\n❌️ Error, Please enter only numbers!")
        continue
      
      if self.balance < amount:
        print(f"\nYou can't take ${amount}, Max available ${self.balance}")
        continue
      
      self.balance -= amount
      print(f"Now you have ${self.format_balance()} in your account")
      
  def show_balance(self):
    print("\n--- CURRENT STATUS ---")
    print(f"{self.owner.title()} you have ${self.format_balance()} in your balance")
      
account = BankAccount("behruz", 5000)

def exit_app():
  """
  Exit the application gracefully
  """
  print("\nThank you for using Kryos Bank! GoodBye!")
  sys.exit()
  
def main():
  menu_actions = {
    "1" : {"text" : "Add money to your balance", "func" : account.deposit},
    "2" : {"text" : "Take money from your balance", "func" : account.withdraw},
    "3" : {"text" : "Show your Balance", "func" : account.show_balance},
    "4" : {"text" : "Exit the application", "func" : exit_app}
  }
  
  while True:
    print("\n" + "=" * 40)
    print("   🏦 Welcome to KRYOS Bank company ")
    print("=" * 40)
    
    for key, value in menu_actions.items():
      print(f"{key} -> {value['text']}")
    print("-" * 40)
    choice = input("Choose an action: ").strip()
    
    if choice in menu_actions:
      menu_actions[choice]["func"]()
      
    else:
      print("Invalid choice, Please choose only 1 to 4")

if __name__ == "__main__":
  main()