class InputValidator:
    
    @staticmethod
    def validate_name(name: str):
        """
        Validation functions for Contact Book.
        """
        user_name = name.strip()
        if not user_name:
            return False, "Name cannot be empty"
        
        return True, None
        
    @staticmethod    
    def validate_phone(phone: str):
        user_phone = phone.strip()
        if not user_phone:
            return False, "Phone number cannot be empty"
        
        if not user_phone.startswith('+'):
            return False, "Phone number must start with '+'"
          
        if not user_phone[1:].isdigit():
            return False, "Only digits are allowed after '+'"
          
        if len(user_phone) <= 8:
            return False, "Phone number must be longer than 8 digits"
          
        return True, None