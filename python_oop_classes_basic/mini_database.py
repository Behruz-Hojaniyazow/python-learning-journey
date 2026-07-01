def parse_input(value):
    """Converts text to int or float whenever possible, leaves it as text if not possible."""
    
    if value.isdigit():
        return int(value)
    
    try:
        return float(value)
    except ValueError:
        return value

def add_item(db, item):
    """Adds an element to the database."""
    db.append(item)
    
def remove_item(db, item):
    """
    Deletes an element and returns a status code:
    - "EMPTY": If the database is empty
    - "SUCCESS": If the element was found and deleted successfully
    - "NOT_FOUND": If the element was not found in the database
    """
    
    if not db:
        return "EMPTY"
        
    initial_length = len(db)
    item_lower = item.lower()
    
    db[:] = [
        x for x in db
        if not (isinstance(x, str) and x.lower() == item_lower) and str(x) != item
    ]
        
    if len(db) < initial_length:
        return "SUCCESS"
    return "NOT_FOUND"
    
def show_items(db):
    """
    Returns the elements of the base.
    Returns a tuple of the form (State, Result).
    """
    
    if not db:
        return "EMPTY", ""
        
    formatted_list = [x.title() if isinstance(x, str) else x for x in db]
    
    return "SUCCESS", ", ".join(map(str, formatted_list))
    
def main():
    elements = []
    
    menu_actions = {
        "1" : "add item",
        "2" : "remove item",
        "3" : "show items"
    }
    
    print("\n--- Welcome to KRYOS Database Manager System ---")
    while True:
        print("\n" + "-" * 35)
        for key, value in menu_actions.items():
            print(f"{key} -> {value.title()}")
        print("-" * 35)
        
        print("\nType 'stop' to finish")
            
        user_choice = input("Choose an action: ").strip()
        
        if user_choice.lower() == "stop":
            print("\nProject stopped")
            break
        
        if user_choice == "1":
            while True:
                print("\nType 'stop' to stop adding elements")
                raw_element = input("\nWhat kind of element would you like to add? ").strip()
                
                if raw_element.lower() == "stop":
                    print("\nAdding elements stopped")
                    break
                
                if raw_element:
                    user_element = parse_input(raw_element)
                    add_item(elements, user_element)
                    
                    display_element = user_element.title() if isinstance(user_element, str) else user_element
                    print(f"✅️ '{display_element}' element added successfully")
                
                else:
                    print("\n❌️ Element name cannot be empty")
                
        elif user_choice == "2":
            while True:
                print("\nType 'stop' to stop deleting")
                user_element = input("\nWhich element would you like to delete: ").strip()
                
                if user_element.lower() == "stop":
                    print("\nDeleting elements stopped")
                    break
                
                status = remove_item(elements, user_element)
                
                if status == "EMPTY":
                    print("\n⚠️ Database is empty, First add elements")
                    break
                elif status == "NOT_FOUND":
                    print(f"\n❌️ Deleting failed: '{user_element.title()}' element not found")
                elif status == "SUCCESS":
                    print(f"✅️ '{user_element.title()}' deleted successfully!")
            
        elif user_choice == "3":
            status, result = show_items(elements)
            
            if status == "EMPTY":
                print("\n⚠️ Database is empty, First add elements")
            else:
                print("\nThese are the elements which you have collected")
                print(result)
            
        else:
            print("\n⚠️ Invalid choice, Please enter only (1/2/3) or stop")
            
if __name__ == "__main__":
    main()