import random

def get_numbers(prompt):
  """Function that accepts only numbers"""
  while True:
    try:
      val = float(input(prompt))
      clean_val = int(val) if val.is_integer() else val
      return clean_val
    except ValueError:
      print("\nInvalid input, Please enter a valid number")

def find_number(x):
  """
    Facilitates the player's attempt to guess the AI's randomly generated number.

    Args:
        x (int): The upper limit for the secret number (inclusive, from 1 to x).

    Returns:
        int: The total number of attempts it took the player to guess correctly.
    """   
  
  print("\n---Welcome to Kryos Game---")
  print(f"\nI thought of a number from 1 to {x} Can you find it")
  ai_num = random.randint(1, x)
  attempts = 1
  while True:
    
    num = get_numbers(f"\nAttempt {attempts}-Enter your number: ")
    if num > ai_num:
      print("Enter a smaller number!")
      
    elif num < ai_num:
      print("Enter a bigger number!")
      
    else:
      plural_suffix = "attempt" if attempts == 1 else " attempts"
      print(f"\n✅️Well done, it was {ai_num}!")
      print(f"You found it in {attempts} {plural_suffix}")
      break
    attempts += 1
    
  return attempts

def find_user_num(x):
  """
    Attempts to guess the number the user is thinking of using guided bounds.

    Args:
        x (int): The maximum limit for the user's secret number (inclusive).

    Returns:
        int: The number of attempts the AI took to guess the number.
    """
  
  input(f"\nNow think of a number between 1 to {x} and press Enter to start the game, I will try to find it: ")
  
  lowest = 1
  highest = x
  ai_attempt = 1
  
  while True:
    if lowest > highest:
      print("\nHold on! The hints contradict each other. Let's just say I give up on this round.")
      return ai_attempt
    if lowest != highest:
      ai_num = random.randint(lowest, highest)
    else:
      ai_num = lowest
    
    user_input = input(f"\nAttempt {ai_attempt}: Is it {ai_num}? True = (t), My number is smaller (-), or bigger  (+)").lower()
    if user_input == '-':
      highest = ai_num - 1
        
    elif user_input == '+':
      lowest = ai_num + 1
      
    elif user_input == 't':
      plural_suffix = "attempt" if ai_attempt == 1 else "attempts"
      print(f"\nI found it in {ai_attempt} {plural_suffix}")
      break
    
    else:
      print("\nInvalid Input! Please enter only 't', '-', '+'.")
    ai_attempt += 1
  return ai_attempt
  
def play(x):
  """
    Orchestrates the main game loop, comparing the player's and AI's scores to determine a winner.

    Args:
        x (int): The maximum range for the numbers in the game.
    """
    
  while True:
    
    user_attempt = find_number(x)
    ai_attempt = find_user_num(x)
    plural_suffix_user = "attempt" if user_attempt == 1 else "attempts"
    plural_suffix_ai = "attempt" if ai_attempt == 1 else "attempts"
    
    if user_attempt < ai_attempt:
      print(f"\nI found it in {ai_attempt} {plural_suffix_ai} and you found the number in {user_attempt} {plural_suffix_user}, so You beat me")
      
    elif user_attempt > ai_attempt:
      print(f"\nYou found the number in {user_attempt} {plural_suffix_user}, I found the number in {ai_attempt} {plural_suffix_ai}, so I beat you")
    
    else:
      print("\nDraw")
    
    while True:
      play_again = get_numbers("\nShall we play? Yes(1) No(0): ")
      
      if play_again in [1, 0]:
        break
      print("Invalid Input. Please enter only 1 or 0")
    if play_again == 0:
      print("\nThanks for playing!")
      break
        
if __name__ == '__main__':
  play(10)