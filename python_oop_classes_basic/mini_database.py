class DatabaseManager:
    """
    A class to manage a dynamic database supporting mixed data types.

    This class provides robust mechanisms to add, remove, and display elements
    consisting of integers, floats, and strings, while handling case-insensitivity
    and type conversion safely.
    """
    
    def __init__(self):
        """Initializes the DatabaseManager with its own internal database list."""
        self.db = []
        
    @staticmethod
    def parse_input(value):
        """
        Converts string input to its appropriate numeric type if possible.

        Args:
            value (str): The raw string input from the user.

        Returns:
            int | float | str: The converted typed value or original string.
        """
        
        if not isinstance(value, str):
            return value
        
        try:
            return int(value)
        except ValueError:
            pass
        
        try:
            return float(value)
        except ValueError:
            return value
    
    @staticmethod
    def format_item(item):
        """Formats the element for uniform display and presentation.

        Capitalizes strings using title-case and leaves numeric types untouched.

        Args:
            item (Any): The database item to be formatted.

        Returns:
            Any: The formatted title-case string or the original numeric item.
        """
        
        clean_item = item.title() if isinstance(item, str) else item
        return clean_item
        
    def add_item(self, item):
        """Appends an element to the database. Returns True when done."""
        self.db.append(item)
        return True
        
    def remove_item(self, item):
        """
        Removes element from the database.
        Returns:
            str: "EMPTY", "SUCCESS", or "NOT_FOUND"
        """
        
        if not self.db:
            return "EMPTY"
                                
        initial_length = len(self.db)
        parsed_item = DatabaseManager.parse_input(item)
        item_lower = item.lower() if isinstance(parsed_item, str) else None
        
        self.db[:] = [
            x for x in self.db
            if not (
                (isinstance(x, str) and x.lower() == item_lower) or 
                (not isinstance(x, str) and x == parsed_item)
                )
        ]
            
        if len(self.db) < initial_length:
            return "SUCCESS"
        return "NOT_FOUND"
        
    def get_items(self):
        """Returns the raw formatted list of items. (No UI formatting)"""
        
        return [DatabaseManager.format_item(x) for x in self.db]
    
def main():
    database = DatabaseManager()
    
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
                    user_element = DatabaseManager.parse_input(raw_element)
                    database.add_item(user_element)
                    display_element = DatabaseManager.format_item(user_element)
                    print(f"\n✅️ '{display_element}' added successfully")
                
                else:
                    print("\n❌️ Element name cannot be empty")
                
        elif user_choice == "2":
            while True:
                print("\nType 'stop' to stop deleting")
                user_element = input("\nWhich element would you like to delete: ").strip()
                
                if user_element.lower() == "stop":
                    print("\nDeleting elements stopped")
                    break
                
                status = database.remove_item(user_element)
                display_element = DatabaseManager.format_item(user_element)
                
                if status == "SUCCESS":
                    print(f"\n✅️ '{display_element}' deleted successfully")
                elif status == "EMPTY":
                    print("\n⚠️ Database is empty, First add elements")
                    break
                elif status == "NOT_FOUND":
                    print(f"\n❌️ Deleting failed: '{display_element}' element not found")
            
        elif user_choice == "3":
            elements = database.get_items()
            
            if not elements:
                print("\n⚠️ Database is empty, First add elements")
            else:
                print("\n=== ELEMENTS IN THE BASE ===")
                for index, element in enumerate(elements, start=1):
                    print(f"{index}. {element}")
                print("-" * 30)
            
        else:
            print("\n⚠️ Invalid choice, Please enter only (1/2/3) or stop")
            
if __name__ == "__main__":
    main()