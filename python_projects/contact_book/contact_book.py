import sys
import json
import logging

FILE_NAME = 'contacts_info.json'
LOG_FILE = 'app.log'

# creating a log
logger = logging.getLogger('ContactBook')
logger.setLevel(logging.DEBUG) # Accepts logs of all levels

# 1.Handler for writing to a file(ALL ERROR and CRITICAL ERRORS are written to a file for analysis)
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter(
  '[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s'
)
file_handler.setFormatter(file_formatter)

# 2.Handler for output to the console (Only for the user or programmer can see on the screen)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)

# Add handlers to the loggger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def load_contacts():
  """
  Reads contacts from a JSON file.

  If the file does not exist:
  - returns an empty list

  If the file exists:
  - returns the data in the JSON
  """
  
  try:
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
      contacts = json.load(file)
      
      return contacts
      
  except FileNotFoundError:
    # It is normal for file not to exist(when opened for the first time) this can be done with a small warning (DEBUG)
    logger.debug(f"\n{FILE_NAME} not found, returned an empty list")
    
    return []

  except json.JSONDecodeError as e:
    # JSON structure is corrupted - this is a serious error!
    logger.exception(f"\nInvalid JSON format - {e}")
    
    return []
    
  except Exception as e:
    logger.exception(f"\nUnexpected error occured (load_contacts) - {e}")
    
    return []
    
def save_contacts(contacts):
  """Save contacts to a json file"""
  
  try:
    
    with open (FILE_NAME, 'w', encoding = 'utf-8') as file:
      json.dump(
        contacts,
        file, 
        indent=4,
        ensure_ascii=False
      )
    logger.info("Contacts were saved successfully")
      
  except IOError as e:
    logger.exception(f"File error - {e}")
    
  except Exception as e:
    logger.exception(f"An error occured while saving contacts - {e}")
      
def add_contact():
  """Collect contact information from the user and store it in a list"""
  
  contacts = load_contacts()
  order = len(contacts) + 1
  
  print("\nType 'stop' to stop adding contacts!")
  # Start collecting contact information
  while True:
    print(f"\n{order}-Enter information about a person!")
    name = input("Name: or (stop): ").strip()
    
    # Stop adding contacts
    if name.lower() == 'stop':
      logger.info("User stopped adding contacts")
      print("\nAdding contacts stopped")
      break
    
    # Validate name input
    if not name:
      logger.warning("ERROR adding contact: Contact name left blank")
      print("❌️Name cannot be empty!")
      continue
    
    phone_num = input("Phone Number: ").strip()
    
    # Validate phone number
    if not phone_num:
      logger.warning(f"ERROR adding contact {name.title()}: Phone number left blank")
      print("❌️ Phone number cannot be empty!")
      continue
    
    if not phone_num.startswith('+'):
      logger.warning(f"ERROR adding contact ({name.title()}): Phone number wasn't started with '+': {phone_num}")
      print("\n❌️ Must start with '+' !")
      continue
    
    if not phone_num[1:].isdigit() and len(phone_num) <= 8:
      logger.warning(f"ERROR adding contact ({name.title()}): Invalid phone number format: {phone_num}")
      print("\n❌️ Only digits are allowed after '+' \nand must be longer than 8 digits!")
      continue
    
    # Check duplicate contacts
    duplicate_found = False
    
    for contact in contacts:
      if contact['name'].lower() == name.lower():
        logger.warning(f"ERROR adding contact ({name.title()}): This contact already exists")
        print("\n❌️ This contact already exists!")
        duplicate_found = True
        break
    if duplicate_found:
      continue
    
    # Create Contact dictionary
    contact = {
      'name' : name,
      'phone' : phone_num
    }
    
    # Save contact
    contacts.append(contact)
    save_contacts(contacts)
    
    # PROFESSIONAL LOG: Who was joined
    logger.info(f"New contact was saved successfully: Name: {name.title()}, Phone number: {phone_num}")
    
    order += 1
    
    print("✅️\nContact was saved successfully!")
  
def show_contacts():
  """Display all saved contacts in a formatted table"""
  
  contacts = load_contacts()
  
  # Return early if there are no saved contacts
  if not contacts:
    print("\n📂 No Contacts found!")
    return
  
  # Display All Contacts
  print('\n' + '=' * 43)
  print(f" {'Name':<17} | {'Phone Number':<20}")
  print('-' * 43)
  for index, contact in enumerate(contacts, start=1):
    print(
      f"{index}. "
      f"{contact['name'].title():<15} | "
      f"{contact['phone']:<20}"
    )
  print("=" * 43)
  
def search_contact():
  """Function that searches a contact from the list"""
  
  contacts = load_contacts()
  
  # Return early if there are no saved contacts
  if not contacts:
    logger.info("Search failed, Contact list is empty")
    print("\n📂 No Contacts found to search")
    return
  
  while True:
    print("\nType (stop) to stop searching")
    user_input = input("Enter a contact name that you're looking for: ").strip()
    
    # Validate a user name
    if not user_input:
      print("\n❌️ Name cannot be empty")
      continue
    
    if user_input.lower() == 'stop':
      print("\nSearching contact stopped")
      break
    
    # PROFESSIONAL LOG: Who is the user looking for?
    logger.info(f"Searching for a contact, Search query: '{user_input}'")
    
    found = False
    
    for contact in contacts:
      if contact['name'].lower() == user_input.lower():
        print("\nYes! This user is in Contact!")
        print(
          f"{contact['name'].title()} | "
          f"+{contact['phone']}"
        )
        found = True
        break
      
    if not found:
      # We write at INFO level because this is not an error, just a result not found
      logger.info(f"Search result: No contact named '{user_input.title()}' found")
      print(f"\nNo contacts found named {user_input.title()}")
      
def delete_contact():
  """Delete a contact from the contact list"""
  
  contacts = load_contacts()
  
  # Return early if there are no saved contacts
  if not contacts:
    print("\n📂 No contacts found to delete!")
    return
  
  while True:
    print("\nType (stop) to stop deleting")
    user_input = input("Enter the contact name to delete: ").strip()
    
    if not user_input:
      print("\nName cannot be empty!")
      continue
    
    if user_input.lower() == 'stop':
      print("\nDeleting contacts stopped")
      break
    
    deleted = False
    
    for contact in contacts[:]:
      if user_input.lower() == contact['name'].lower():
        
        while True:
          
          confirm = input(f"\nDelete {contact['name'].title()}? (yes/no) ").strip().lower()
          
          if confirm in ('yes', 'y') :
            contacts.remove(contact)
            save_contacts(contacts)
            
            # PROFESSIONAL LOG: We mark data deletion with WARNING OR INFO
            logger.warning(f"CONTACT WAS DELETED: Name {contact['name'].title()}, Phone Number {contact['phone_num']}")
            
            print(f"\n{contact['name'].title()} was deleted successfully!")
            
            
            
            deleted = True
            break
        
          elif confirm in ('no', 'n'):
            logger.info(f"Deleting contact was refused: {contact['name'].title()}")
            print(f"\n{contact['name'].title()} was not deleted!")
            
            deleted = True
            break
        
          else:
            print("\nPlease type yes or no!")
                                   
                                  
        break                      
    if not deleted:
      logger.info(f"Delete failed: Contact named {user_input.title()} does not exist in thr database")
      print(f"\nNo contact found named {user_input.title()}")
    
def exit_app():
  """Exit the application gracefully"""
  print("\nThanks for using Kryos Contact Book, GoodBye!")
  
  sys.exit()

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
    logging.critical(f"A critical system error has occured and the program has stopped! Global Error - {e}", exc_info=True)
    print("\n❌️ A serious system error has occured, Please contact your adminstrator")
    sys.exit(1)
  
if __name__ == '__main__':
  main()