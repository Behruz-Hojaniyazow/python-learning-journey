import sys
import json
import logging

FILE_NAME = 'contacts_info.json'

logging.basicConfig(level=logging.ERROR)

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
    
    return []

  except json.JSONDecodeError as e:
    logging.error(f"\nInvalid JSON format - {e}")
    
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
      
  except IOError as e:
    print(f"File error - {e}")
    
  except Exception as e:
    print(f"An error occured - {e}")
      
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
      print("\nAdding contacts stopped")
      break
    
    # Validate name input
    if not name:
      print("❌️Name cannot be empty!")
      continue
    
    phone_num = input("Phone Number: ").strip()
    
    # Validate phone number
    if not phone_num:
      print("❌️ Phone number cannot be empty!")
      continue
    
    if not phone_num.isdigit() or len(phone_num) < 7:
      print("❌️ Phone number must contain only digits!")
      continue
    
    # Check duplicate contacts
    duplicate_found = False
    
    for contact in contacts:
      if contact['name'].lower() == name.lower():
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
    order += 1
    
    print("✅️\nContact saved successfully!")
  
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
      f"+{contact['phone']:<20}"
    )
  print("=" * 43)
  
def search_contact():
  """Function that searches a contact from the list"""
  
  contacts = load_contacts()
  
  # Return early if there are no saved contacts
  if not contacts:
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
            print(f"\n{contact['name'].title()} was deleted successfully!")
            
            save_contacts(contacts)
            
            deleted = True
            break
        
          elif confirm in ('no', 'n'):
            print(f"\n{contact['name'].title()} was not deleted!")
            
            deleted = True
            break
        
          else:
            print("\nPlease type yes or no!")
                                   
                                  
        break                      
    if not deleted:
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
      
if __name__ == '__main__':
  main()