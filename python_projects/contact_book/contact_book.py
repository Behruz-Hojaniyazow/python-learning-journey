import sys
      
def add_contact():
  """Collect contact information from the user and store it in a list"""
  
  contacts = []
  order = 1
  
  # Start collecting contact information
  while True:
    print(f"{order}-Enter information about a person!")
    name = input("Name: or type(stop) to stop adding contacts: ").strip()
    
    # Stop adding contacts
    if name.lower() == 'stop':
      print("Adding contacts stopped")
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
    
    if not phone_num.isdigit():
      print("❌️ Phone number must contain only digits!")
      continue
    
    # Create Contact dictionary
    contact = {
      'name' : name,
      'phone' : phone_num
    }
    
    # Save contact
    contacts.append(contact)
    order += 1
    
    print("✅️\nContact saved successfully!")
  
  return contacts
  
def show_contacts(contacts):
  """Display all saved contacts in a formatted table"""
  
  # Return early if there are no saved contacts
  if not contacts:
    print("\n📂 No Contacts found!")
    return
  
  # Display All Contacts
  print('\n' + '=' * 43)
  print(f'{'Name':<15} | {'Phone Number':<20}')
  print('-' * 43)
  for contact in contacts:
    print(
      f"{contact['name'].title():<15} | "
      f"{contact['phone']:<20}"
    )
  print("=" * 43)
  
def search_contact(contacts):
  """Function that searches a contact from the list"""
  
  # Return early if there are no saved contacts
  if not contacts:
    print("\n📂 No Contacts Found")
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
          f"{contact['phone']}"
        )
        found = True
        break
      
    if not found:
      print(f"No contacts found named {user_input.title()}")
      
def delete_contact(contacts):
  """Delete a contact from the contact list"""
  
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
          
          confirm = input(f"\nDelete{contact['name'].title()}? ").strip().lower()
          
          if confirm in ('yes', 'y') :
            contacts.remove(contact)
            print(f"\n{contact['name'].title()} was deleted successfully!")
            
            deleted = True
            return
        
          elif confirm in ('no', 'n'):
            print(f"\n{contact['name'].title()} was not deleted!")
            
            return
        
          else:
            print("\nPlease type yez or no!")
        
    if not deleted:
      print(f"No contact found named {user_input.title()}")
      
def save_contacts(contacts):
  """Save contacts to a text file"""
  
  filename = 'contacts_info.txt'
  
  if not contacts:
    print("📂 Not contacts info found to write!")
    return
  
  try:
    
    with open (filename, 'a', encoding = 'utf-8') as f:
        
      header = 
      f"{"Name":<15} | "
      f"{"Phone Number":<20}\n"
      f.write(header)
        
      for contact in contacts:
        formatted_contact = 
        f"{contact['name'].title():<15} | "
        f"{contact['phone']:<20}\n"
        f.write(formatted_contact)
        
      print("\nContacts Saved to the file successfully! ✅️")
      
  except IOError as e:
    print(f"File error - {e}")
    
  except Exception as e:
    print(f"An error occured - {e}")
    
def exit_app():
  """Exit the application gracefully"""
  print("Thanks for using Kryos Contact Book, GoodBye!")
  
  sys.exit()

