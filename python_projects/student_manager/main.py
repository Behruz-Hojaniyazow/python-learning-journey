import sys
from student_service import (
  add_student,
  show_students,
  search_students,
  delete_students,
  exit_app
)
from logger_config import get_logger

logger = get_logger()

def main():
  
  menu_actions = {
    '1' : {'text' : 'Add Student', 'func' : add_student},
    '2' : {'text' : 'Show Student', 'func' : show_students},
    '3' : {'text' : 'Search Student', 'func' : search_students},
    '4' : {'text' : 'Delete Student', 'func' : delete_students},
    '5' : {'text' : 'Exit App', 'func' : exit_app}
  }
  
  try:
    # Main application loop
    while True:
      print('\n' + '=' * 46)
      print("💎 Welcome to the Kryos Student Manager System!")
      print("-" * 46)
      for key, value in menu_actions.items():
        print(f"{key} -> {value['text']}")
      print("=" * 46)
    
      choice = input("\nChoose an Action: ").strip()
    
      if choice in menu_actions:
        menu_actions[choice]['func']()
      
      else:
        print("\n❌️ Error: Invalid choice, Choose 1 to 5!")
  
  except KeyboardInterrupt:
    # close gracefully without throwing an error when the user presses Ctrl+C
    print("\n\nProject was stopped by the user")
    sys.exit(0)
    
  except Exception:
    # Any unexpected critical error in the program goes here
    logger.critical(f"A critical system error has occurred.", exc_info=True)
    print("\nA serious system error has occurred, Please contact your administrator")
    sys.exit(1)
    
if __name__ == '__main__':
  main()