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
    '1' : 'Add Contact',
    '2' : 'Show Contacts',
    '3' : 'Search Contacts',
    '4' : 'Delete Contacts',
    '5' : 'Exit app'
  }
  
  try:
    while True:
      print("\n" + "=" * 40)
      print("Welcome to KRYOS Contact Book!")
      print("-" * 40)
      for key, value in menu_actions.items():
        print(f"{key} -> {value}")
      print("=" * 40)
    
      choice = input("\nChoose an action: ").strip()
    
      if choice == '1':
        add_contact()
      
      elif choice == '2':
        show_contacts()
      
      elif choice == '3':
        search_contact()
      
      elif choice == '4':
        delete_contact()
      
      elif choice == '5':
        exit_app()
      
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