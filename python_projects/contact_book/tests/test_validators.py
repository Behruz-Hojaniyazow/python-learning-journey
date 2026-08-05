"""
Unit tests for the InputValidator module.

This module contains a comprehensive suite of unit tests for verifying
input validation logic within the Contact Book application. It covers edge cases,
whitespace sanitization, formatting constraints, and error messages for names
and phone numbers.
"""

import unittest
from validators import InputValidator

class TestInputValidator(unittest.TestCase):
    """
    Test suite for the InputValidator class.

    Executes automated tests to ensure name and phone number inputs adhere to
    application business rules and return accurate validation status tuples.
    """
    
    # ---------------------------------------------------------
    # 1-PART: validate_name METHOD TESTS
    # ---------------------------------------------------------
    
    def test_validate_name_valid_input(self):
        """Test that a valid standard name passes validation with no error message."""
        
        #Arrange
        valid_name = "Behruz"
        
        #Act
        is_valid, error_msg = InputValidator.validate_name(valid_name)
        
        #Assert
        self.assertTrue(is_valid)
        self.assertIsNone(error_msg)
        
    def test_validate_name_whitespaces(self):
        """Test that names with leading or trailing whitespaces are accepted and stripped."""
        
        name_with_spaces = "  Behruz "
        
        is_valid, error_msg = InputValidator.validate_name(name_with_spaces)
        
        self.assertTrue(is_valid)
        self.assertIsNone(error_msg)
        
    def test_validate_name_empty_or_spaces_only(self):
        """Test that empty strings and whitespace-only inputs fail name validation."""
        
        invalid_names = ["", " ", "\n", "\t"]
        
        for name in invalid_names:
            with self.subTest(name=name):
                
                is_valid, error_msg = InputValidator.validate_name(name)
                
                self.assertFalse(is_valid)
                self.assertEqual(error_msg, "Name cannot be empty")
                
                
    # ---------------------------------------------------------
    # 2-PART: validate_phone METHOD TESTS
    # ---------------------------------------------------------
    
    def test_validate_phone_valid_numbers(self):
        """Test that properly formatted international phone numbers pass validation."""
        
        valid_phones = ["+99363807476", "+99364277230", "+99363849125"]
        
        for phone in valid_phones:
            with self.subTest(phone=phone):
                
                is_valid, error_msg = InputValidator.validate_phone(phone)
                
                self.assertTrue(is_valid)
                self.assertIsNone(error_msg)
                
    def test_validate_phone_empty(self):
        """Test that empty or whitespace-only phone inputs fail validation."""
        
        empty_phones = ["", " "]
        
        for phone in empty_phones:
            with self.subTest(phone=phone):
                
                is_valid, error_msg = InputValidator.validate_phone(phone)
                
                self.assertFalse(is_valid)
                self.assertEqual(error_msg, "Phone number cannot be empty")
                
    def test_validate_phone_missing_plus_sign(self):
        """Test that phone numbers lacking a leading '+' sign are rejected."""
        
        phone = "99363807476"
        
        is_valid, error_msg = InputValidator.validate_phone(phone)
        
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "Phone number must start with '+'")
        
    def test_validate_phone_contains_letters_or_symbols(self):
        """Test that phone numbers with non-digit characters after '+' fail validation."""
        
        invalid_phones = ["+993AB80KH G", "++993AS 6790", "+993    78904"]
        for phone in invalid_phones:
            with self.subTest(phone=phone):
                
                is_valid, error_msg = InputValidator.validate_phone(phone)
                
                self.assertFalse(is_valid)
                self.assertEqual(error_msg, "Only digits are allowed after '+'")
                
    def test_validate_phone_too_short(self):
        """Test that phone numbers below the minimum length threshold fail validation."""
        
        short_phone = "+1234567"
        
        is_valid, error_msg = InputValidator.validate_phone(short_phone)
        
        self.assertFalse(is_valid)
        self.assertEqual(error_msg, "Phone number must be longer than 8 digits")
        
if __name__ == "__main__":
    unittest.main()