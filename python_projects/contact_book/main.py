import sys
from contact_service import (
  add_contact,
  show_contacts,
  search_contact,
  delete_contact,
  exit_app
)
from logger_config import get_logger

logger = get_logger()

def main():
  
  menu_actions = {
    '1' : {'text' : 'Add Contact', 'func' : add_contact},
    '2' : {'text' : 'Show Contacts', 'func' : show_contacts},
    '3' : {'text' : 'Search Contacts', 'func' : search_contact},
    '4' : {'text' : 'Delete Contacts', 'func' : delete_contact},
    '5' : {'text' : 'Exit app', 'func' : exit_app}
  }
  
  try:
    while True:
      print("\n" + "=" * 40)
      print("Welcome to KRYOS Contact Book!")
      print("-" * 40)
      for key, value in menu_actions.items():
        print(f"{key} -> {value['text']}")
      print("=" * 40)
    
      choice = input("\nChoose an action: ").strip()
    
      if choice in menu_actions:
        menu_actions[choice]['func']()
      
      else:
        print("\n❌️Invalid choice, Please choose (1 to 5)")
        
  except KeyboardInterrupt:
    # close gracefully without throwing an error when the user presses Ctrl+C
    print('\n\nProject was stopped by the user')
    sys.exit(0)
    
  except Exception as e:
    # Any unexpected critical error in the program goes here
    logger.critical(f"A critical system error has occured and the program has stopped! Global Error - {e}", exc_info=True)
    print("\n❌️ A serious system error has occured, Please contact your adminstrator")
    sys.exit(1)
  
if __name__ == '__main__':
  main()