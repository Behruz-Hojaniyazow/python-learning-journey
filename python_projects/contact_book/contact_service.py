import sys
from storage import (
  load_contacts,
  save_contacts
)
from validators import (
  validate_name,
  validate_phone
)
from logger_config import get_logger

logger = get_logger()

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
    is_valid, error = validate_name(name)
    if not is_valid:
      logger.warning("Contact name left blank")
      print(f"\n❌️ {error}")
      continue
    
    
    # Check duplicate contacts
    duplicate_found = False
    
    for contact in contacts:
      if contact['name'].lower() == name.lower():
        logger.warning(f"Contact creation failed: duplicate name ({name.title()})")
        print("\n❌️ This contact already exists!")
        duplicate_found = True
        break
      
    if duplicate_found:
      continue
    
    phone_num = input("Phone Number: ").strip()
    
    # check phone number format
    is_valid, error = validate_phone(phone_num)
    if not is_valid:
      logger.warning(error)
      print(f"\n❌️ {error}")
      continue
    
    # check duplicate phone numbers
    duplicate_phone_found = False
    
    for contact in contacts:
      if contact['phone'] == phone_num:
        logger.warning(f"Contact creation failed: duplicate phone number ({phone_num})")
        print("\n❌️ This phone number already exists!")
        
        duplicate_phone_found = True
        break
      
    if duplicate_phone_found:
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
    logger.info(f"Contact created: {name.title()} ({phone_num})")
    
    order += 1
    
    print("✅️\nContact was saved successfully!")
  
def show_contacts():
  """Display all saved contacts in a formatted table"""
  
  contacts = load_contacts()
  
  # Return early if there are no saved contacts
  if not contacts:
    print("\n📂 No Contacts found!")
    return
  
  sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())
  
  # Display All Contacts
  print('\n' + '=' * 43)
  print(f" {'Name':<17} | {'Phone Number':<20}")
  print('-' * 43)
  for index, contact in enumerate(sorted_contacts, start=1):
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
    
    if user_input.lower() == 'stop':
      print("\nSearching contact stopped")
      break
    
    # Validate a user name
    is_valid, error = validate_name(user_input)
    if not is_valid:
      print(f"\n❌️ {error}")
      continue
    
    # PROFESSIONAL LOG: Who is the user looking for?
    logger.info(f"Searching for a contact, Search query: '{user_input}'")
    
    found = False
    
    for contact in contacts:
      if contact['name'].lower() == user_input.lower():
        print("\nYes! This user is in Contact!")
        print(
          f"{contact['name'].title()} | "
          f"{contact['phone']}"
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
    
    if user_input.lower() == 'stop':
      print("\nDeleting contacts stopped")
      break
    
    is_valid, error = validate_name(user_input)
    if not is_valid:
      print(f"\n❌️ {error}")
      continue
    
    deleted = False
    
    for contact in contacts[:]:
      if user_input.lower() == contact['name'].lower():
        
        while True:
          
          confirm = input(f"\nDelete {contact['name'].title()}? (yes/no) ").strip().lower()
          
          if confirm in ('yes', 'y') :
            contacts.remove(contact)
            save_contacts(contacts)
            
            # PROFESSIONAL LOG: We mark data deletion with WARNING OR INFO
            logger.warning(f"CONTACT WAS DELETED: Name {contact['name'].title()}, Phone Number {contact['phone']}")
            
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
      logger.info(f"Delete failed: Contact named {user_input.title()} does not exist in the database")
      print(f"\nNo contact found named {user_input.title()}")
    
def exit_app():
  """Exit the application gracefully"""
  print("\nThanks for using Kryos Contact Book, GoodBye!")
  
  sys.exit()