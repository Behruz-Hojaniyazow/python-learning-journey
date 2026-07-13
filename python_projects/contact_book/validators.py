"""
Input validation utilities for the Contact Book application.

This module provides reusable validation methods for verifying
user-provided contact information before it is processed or
stored.

The validation rules help maintain data integrity and ensure
consistent input throughout the application.
"""

class InputValidator:
    """
    Provide validation utilities for contact information.

    This utility class contains static methods used to validate
    user input before contact data is processed or stored. The
    validation methods ensure data consistency and help prevent
    invalid or incomplete information from entering the system.
    """
    
    @staticmethod
    def validate_name(name: str):
        """
        Validate a contact name.
    
        Removes leading and trailing whitespace from the provided
        name and verifies that the resulting value is not empty.
    
        Args:
            name (str):
                The contact name provided by the user.
    
        Returns:
            tuple[bool, str | None]:
                A tuple containing:
    
                - True and None if the name is valid.
                - False and an explanatory error message if the
                  validation fails.
        """
        user_name = name.strip()
        if not user_name:
            return False, "Name cannot be empty"
        
        return True, None
        
    @staticmethod    
    def validate_phone(phone: str):
        """
        Validate a phone number.
    
        The validation ensures that the phone number:
    
        - is not empty,
        - starts with the '+' character,
        - contains only numeric digits after '+',
        - has a valid minimum length.
    
        Args:
            phone (str):
                The phone number provided by the user.
    
        Returns:
            tuple[bool, str | None]:
                A tuple containing:
    
                - True and None if the phone number is valid.
                - False and an explanatory error message if the
                  validation fails.
        """
        
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