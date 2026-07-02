class DatabaseManager:
    """
    A class to manage a dynamic database supporting mixed data types.

    This class provides robust mechanisms to add, remove, and display elements
    consisting of integers, floats, and strings, while handling case-insensitivity
    and type conversion safely.
    """
    
    def __init__(self, db):
        """Initializes the DatabaseManager with a reference to a database list.

        Args:
            db (list): The underlying list acting as the database storage.
        """
        self.db = db
        
    @staticmethod
    def parse_input(value):
        """
        Converts string input to its appropriate numeric type if possible.

        Args:
            value (str): The raw string input from the user.

        Returns:
            int | float | str: The converted typed value or original string.
        """
        
        if value.isdigit():
            return int(value)
        
        try:
            return float(value)
        except ValueError:
            return value
    
    def _format_item(self, item):
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
        """
        Appends an element to the database and returns a success message.

        Args:
            item (Any): The element (int, float, or str) to add.

        Returns:
            str: A formatted user-friendly success message.
        """
        self.db.append(item)
        display_element = self._format_item(item)
        
        return f"\n✅️ '{display_element}' added successfully"
        
    def remove_item(self, item):
        """
        Removes all matching instances of an element from the database.

        Handles case-insensitive comparisons for strings and securely matches
        string representations of numeric types.

        Args:
            item (str): The raw string identifier of the element to delete.

        Returns:
            str: A status message indicating success, failure, or an empty database.
        """
        
        if not self.db:
            return "\n⚠️ Database is empty, First add elements"
        
        display_element = self._format_item(item)    
        initial_length = len(self.db)
        item_lower = item.lower()
        
        self.db[:] = [
            x for x in self.db
            if not (isinstance(x, str) and x.lower() == item_lower) and str(x) != item
        ]
            
        if len(self.db) < initial_length:
            return f"✅️ '{display_element}' deleted successfully!"
        return f"\n❌️ Deleting failed: '{display_element}' element not found"
        
    def show_items(self):
        """
        Returns the elements of the base.
        Returns a tuple of the form (State, Result).
        """
        
        if not self.db:
            return "\n⚠️ Database is empty, First add elements"
            
        formatted_list = [self._format_item(x) for x in self.db]
        result = "\n=== ELEMENTS IN THE BASE ===\n"
        for index, element in enumerate(formatted_list, start=1):
            result += f"{index}. {element}\n"
        result += "=" * 30
        
        return result
    
def main():
    elements = []
    database = DatabaseManager(elements)
    
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
                    result = database.add_item(user_element)
                    
                    print(result)
                
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
                print(status)
            
        elif user_choice == "3":
            print(database.show_items())
            
        else:
            print("\n⚠️ Invalid choice, Please enter only (1/2/3) or stop")
            
if __name__ == "__main__":
    main()