"""
Entry point for the Contact Book application.

This module provides the command-line user interface, handles
user interaction, displays the application menu, and delegates
operations to the ContactService.

It also manages application startup, graceful shutdown, and
global exception handling.
"""

import sys
from contact_service import ContactService, ContactStatus
from logger_config import get_logger

logger = get_logger()
#creating an object
contacts = ContactService()

def ui_add_contact():
    """
    Display the user interface for creating new contacts.

    This function continuously prompts the user to enter contact
    information until the user chooses to stop. Each contact is
    validated and processed through the ContactService.

    Appropriate success messages and validation errors are displayed
    based on the returned ContactStatus values.

    Returns:
        None
    """
    
    print("\n--- 🗂 Adding Contacts 🗂 ---")
    while True:
        print("\nType 'stop' to stop adding contacts")
        name = input("Enter a name or (stop) ").strip()
        if name.lower() == 'stop':
            print("\nAdding contacts stopped")
            break
        
        phone_num = input(f"Enter a phone number: ")
        
        status, result = contacts.add_contact(name, phone_num)
        if status == ContactStatus.EMPTY_NAME:
            print("\n❌️ Error: Name left blank")
            continue
        elif status == ContactStatus.DUPLICATE_NAME:
            print("\n⚠️ This name already exists in the database")
            continue
        elif status == ContactStatus.INVALID_PHONE:
            print(f"\n❌️ {result}")
            continue
        elif status == ContactStatus.DUPLICATE_PHONE:
            print("\n⚠️ This phone number already exists in the database")
            continue
        elif status == ContactStatus.SAVE_ERROR:
            print("\n❌️ System Error: Failed to save the contact to the file.")
            continue
        else:
            print(f"\nContact saved successfully: Name {name.title()} | Phone number {phone_num}")

def ui_search_contact():
    """
    Display the user interface for searching contacts.

    Allows the user to search for contacts using a full or partial
    name. Matching contacts are displayed in a readable format,
    while appropriate messages are shown when no matches are found
    or the search input is invalid.

    Returns:
        None
    """
    
    print("\n--- 🔍 Searching Contact 🔎 ---")
    
    if not contacts.get_contacts():
        print("\n⚠️ The contact book is completely empty. Please add some contacts first.")
        return
    
    while True:
        print("\nType 'stop' to stop searching contact")
        name = input("Enter a name: ").strip()
        if name.lower() == 'stop':
            print("\nSearching Contact stopped")
            break
        
        status, result = contacts.search_contact(name)
        if status == ContactStatus.EMPTY_NAME:
            print("\n❌️ Error: Name left blank")
            continue
        elif status == ContactStatus.NOT_FOUND:
            print(f"\nNo contact found named: '{name.title()}'")
            continue
        else:
            print(f"\n🔍 Found {len(result)} contact(s) matching your '{name.title()}'")
            print("-" * 40)
            for c in result:
                print(
                f"👤 Name: {c['name'].title()}\n"
                f"📞 Phone number: {c['phone']}"
                )
                print("-" * 40)

def ui_show_contacts():
    """
    Display all stored contacts in alphabetical order.

    Retrieves every saved contact from the storage, sorts the
    collection alphabetically by name, and presents the data in
    a formatted table. If no contacts exist, an informative
    message is displayed.

    Returns:
        None
    """
    
    all_contacts = contacts.get_contacts()
    
    if not all_contacts:
        print("\n⚠️ No contacts found to show")
        return
        
    sorted_contacts = sorted(all_contacts, key=lambda x: x['name'].lower())
    
    print("\n" + "=" * 43)
    print(f" 👤 {'Name':<14} | 📞 {'Phone Number':<20}")
    print("-" * 43)
    for index, contact in enumerate(sorted_contacts, start=1):
        print(
            f"{index}. "
            f"{contact['name'].title():<15} | "
            f"{contact['phone']:<20}"
        )
    print("=" * 43)
    
def ui_delete_contact():
    """
    Display the user interface for deleting contacts.

    Allows the user to search for existing contacts, select a
    matching contact when multiple results are found, confirm the
    deletion, and permanently remove the selected contact from the
    storage.

    Informative messages are displayed for invalid input,
    unsuccessful searches, cancellation requests, and successful
    deletions.

    Returns:
        None
    """
    
    print("\n--- 🗑 Deleting Contacts 🗑 ---")
    
    if not contacts.get_contacts():
        print("\n⚠️ The contact book is completely empty. There is nothing to delete.")
        return
    
    while True:
        print("\nType 'stop' to stop deleting contacts")
        user_name = input("Enter a name: ").strip()
        if user_name.lower() == 'stop':
            print("\nDeleting contacts stopped")
            break
        
        status, results = contacts.search_contact(user_name)
        
        if status == ContactStatus.EMPTY_NAME:
            print("\n❌️ Error: Name left blank")
            continue
        
        elif status == ContactStatus.NOT_FOUND:
            print(f"\nNo contacts found matching: '{user_name.title()}'")
            continue
        
        elif status == ContactStatus.SUCCESS:
            
            if len(results) == 1:
                selected_contact = results[0]
                
            else:
                print(f"\n🔍 Found {len(results)} contacts matching '{user_name.title()}'")
                for index, contact in enumerate(results, start=1):
                    print(f" {index}. 👤{contact['name'].title()} - 📞{contact['phone']}")
                    
                choice = input("\nEnter the number of the contact to delete (or '0' to cancel): ").strip()
                
                if choice == '0':
                    print("\n🛑 Deletion cancelled")
                    continue
                
                if not choice.isdigit() or not (1 <= int(choice) <= len(results)):
                    print("\n❌️ Invalid selection, Please enter a valid number")
                    continue
                
                selected_contact = results[int(choice) - 1]
            
            print(f"\n📌 Target 👤{selected_contact['name'].title()} - 📞{selected_contact['phone']}")    
            confirm = input(f"Delete {selected_contact['name'].title()}: (yes/no) ").strip()
            if confirm.lower() in ('yes', 'y'):
                delete_status = contacts.delete_contact(selected_contact['name'])
                if delete_status == ContactStatus.SUCCESS:
                    print("\n✅️ Contact deleted successfully")
                else:
                    print("\n❌️ An error occurred while deleting a contact, Try again")
            
            elif confirm.lower() in ('no', 'n'):
                print("\n🛑 Deleting contact cancelled")
                
            else:
                print("\n⚠️ Please enter only (yes/no)")
            
def ui_exit_app():
    """
    Terminate the application gracefully.

    Displays a farewell message to the user and exits the
    application with a successful termination status.

    Returns:
        None

    Raises:
        SystemExit:
            Raised to terminate the program.
    """
    
    print("\nThank you for using KRYOS CONTACT BOOK MANAGER, Bye!")
    sys.exit()

def main():
    """
    Run the application's main control loop.

    Initializes the application's interactive menu, displays the
    available operations, processes user selections, and delegates
    execution to the corresponding user interface functions.

    The function also provides centralized exception handling to
    ensure graceful termination when interrupted by the user and
    to log unexpected critical errors before exiting the program.

    Returns:
        None

    Raises:
        SystemExit:
            Raised when the application exits normally or after
            encountering a critical unrecoverable error.
    """
  
    menu_actions = {
      '1' : {'text' : 'Add Contact', 'func' : ui_add_contact},
      '2' : {'text' : 'Show Contacts', 'func' : ui_show_contacts},
      '3' : {'text' : 'Search Contacts', 'func' : ui_search_contact},
      '4' : {'text' : 'Delete Contacts', 'func' : ui_delete_contact},
      '5' : {'text' : 'Exit app', 'func' : ui_exit_app}
    }
    
    try:
        while True:
            print("\n" + "=" * 40)
            print("    Welcome to KRYOS Contact Book!")
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
        print("\n❌️ A serious system error has occured, Please contact your administrator")
        sys.exit(1)
  
if __name__ == '__main__':
    main()