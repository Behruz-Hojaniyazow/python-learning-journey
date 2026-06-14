import sys
from word_service import (
  play,
  exit_app
)
from logger_config import get_logger

logger = get_logger()

def main():
  """
  Serve as the entry point of the application.

  Displays the main menu, processes user
    selections, executes the corresponding
    actions, and handles application-level
    exceptions gracefully.
  """
  menu_actions = {
    "1" : {"text" : "Start a game", "func" : play},
    "2" : {"text" : "Exit game", "func" : exit_app}
  }
  
  try:
    # main application loop
    while True:
      print("\n" + "=" * 46)
      print("   🎲 Welcome to Kryos Word Guessing Game!")
      print("-" * 46)
      for key, value in menu_actions.items():
        print(f"{key} -> {value['text']}")
      print("=" * 46)
      
      choice = input("\nChoose an action: ").strip()
      
      if choice in menu_actions:
        menu_actions[choice]['func']()
        
      else:
        print("\n❌️ Error: Invalid choice, Choose 1 or 2")
        
  except KeyboardInterrupt:
    # close gracefully without throwing an error when the user presses Ctrl+C
    print("\n\nProject was stopped by the user")
    sys.exit(0)
    
  except Exception:
    # Any unexpected critical error in the program goes here
    logger.critical(f"A critical system error has occurred.", exc_info=True)
    print("\nA serious system error has occurred. Please contact your administrator")
    
if __name__ == "__main__":
  main()