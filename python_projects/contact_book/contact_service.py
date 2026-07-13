"""
Business logic for the Contact Book application.

This module provides the ContactService class responsible for
managing contact creation, searching, deletion, validation,
duplicate detection, and interaction with the storage layer.

It also defines ContactStatus, an enumeration used to represent
the outcome of contact-related operations throughout the
application.
"""

from enum import Enum, auto
from storage import JSONContactStorage
from validators import InputValidator
from logger_config import get_logger
from config import FILE_NAME

class ContactStatus(Enum):
    """
    Define the possible outcomes of contact-related operations.

    This enumeration provides standardized status codes returned
    by the ContactService methods. Using predefined status values
    improves code readability, simplifies error handling, and
    ensures consistent communication between the service layer
    and the user interface.
    """
    
    SUCCESS = auto()
    EMPTY_NAME = auto()
    DUPLICATE_NAME = auto()
    DUPLICATE_PHONE = auto()
    INVALID_PHONE = auto()
    SAVE_ERROR = auto()
    NOT_FOUND = auto()

class ContactService:
    """
    Manage all contact-related business operations.

    This service acts as the application's business layer,
    coordinating validation, contact management, logging,
    duplicate detection, searching, deletion, and persistent
    storage.

    The class delegates data persistence to JSONContactStorage
    and input validation to InputValidator while providing a
    clean interface for the application's user interface.

    Attributes:
        logger (logging.Logger):
            Configured logger used to record application events,
            warnings, and errors.

        json_contacts (JSONContactStorage):
            Storage manager responsible for loading and saving
            contact data to the JSON file.
    """
  
    def __init__(self):
    """
    Initialize the contact service.

    Creates and configures the application logger and initializes
    the JSON storage handler responsible for loading and persisting
    contact data.

    Attributes:
        logger (logging.Logger):
            Configured logger instance used for application logging.

        json_contacts (JSONContactStorage):
            Storage manager responsible for reading and writing
            contact data to the JSON file.
    """
        self.logger = get_logger()
        self.json_contacts = JSONContactStorage(FILE_NAME)
      
    def add_contact(self, name: str, phone_number: str):
        """
        Create and save a new contact after validating the provided data.
    
        This method performs a complete contact creation workflow,
        including input sanitization, name validation, duplicate
        detection, phone number validation, and persistent storage.
    
        If the contact is successfully saved, a success status is
        returned. Otherwise, an appropriate status describing the
        validation or storage failure is returned.
    
        Args:
            name (str):
                Name of the contact to be created.
    
            phone_number (str):
                Phone number associated with the contact.
    
        Returns:
            tuple[ContactStatus, str | None]:
                A tuple containing:
    
                - ContactStatus.SUCCESS if the contact was created.
                - ContactStatus.EMPTY_NAME if the name is empty.
                - ContactStatus.DUPLICATE_NAME if the name already exists.
                - ContactStatus.INVALID_PHONE if the phone number is invalid.
                - ContactStatus.DUPLICATE_PHONE if the phone number already exists.
                - ContactStatus.SAVE_ERROR if saving the contact fails.
    
                The second value contains an error message only when
                phone number validation fails; otherwise it is None.
        """
        
        contacts = self.json_contacts.load_contacts()
        
        user_name = name.strip()
        # Validate name input
        is_valid, error_detail = InputValidator.validate_name(user_name)
        if not is_valid:
            self.logger.warning("Contact creation failed: name left blank")
            return ContactStatus.EMPTY_NAME, None
                                  
        # check duplicate name
        for contact in contacts:
            if contact['name'].lower() == user_name.lower():
                self.logger.warning(f"Contact creation failed: Duplicate name ({user_name.title()})")
                return ContactStatus.DUPLICATE_NAME, None
          
        phone_num = phone_number.strip()
        # check phone number format
        is_valid, error_detail = InputValidator.validate_phone(phone_num)
        if not is_valid:
            self.logger.warning(error_detail)
            return ContactStatus.INVALID_PHONE, error_detail
          
        # check duplicate phone numbers
        for contact in contacts:
            if contact['phone'] == phone_num:
                self.logger.warning(f"Contact creation failed: Duplicate phone number ({phone_num})")
                return ContactStatus.DUPLICATE_PHONE, None
                
        # Create Contact dictionary
        new_contact = {
            'name' : user_name,
            'phone' : phone_num
        }
          
        # Save contact
        contacts.append(new_contact)
        if self.json_contacts.save_contacts(contacts):
            self.logger.info(f"Contact created successfully: {user_name.title()} ({phone_num})")
            return ContactStatus.SUCCESS, None
        else:
            self.logger.error(f"Failed to save  contact: ({user_name.title()})")
            return ContactStatus.SAVE_ERROR, None
      
    def get_contacts(self) -> list:
        """
        Retrieve all stored contacts.

        Loads every contact from the configured JSON storage and
        returns them as a list. If no contacts exist, an empty list
        is returned.
    
        Returns:
            list[dict]:
                A list containing all stored contact dictionaries.
                Returns an empty list if no contacts are available.
        """
      
        return self.json_contacts.load_contacts()
      
    def search_contact(self, query: str):
        """
        Search for contacts whose names match the given query.
    
        The search is case-insensitive and performs a partial match,
        allowing users to find contacts by entering either a full
        name or a portion of it.
    
        Args:
            query (str):
                Name or partial name used as the search keyword.
    
        Returns:
            tuple[ContactStatus, list]:
                A tuple containing:
    
                - ContactStatus.SUCCESS and a list of matching contacts.
                - ContactStatus.EMPTY_NAME if the search query is empty.
                - ContactStatus.NOT_FOUND if no matching contacts exist.
        """
      
        contacts = self.json_contacts.load_contacts()
        
        clean_query = query.strip().lower()
        # Validate a user name
        is_valid, error_detail = InputValidator.validate_name(clean_query)
        if not is_valid:
            self.logger.warning(f"Searching contact failed: name left blank")
            return ContactStatus.EMPTY_NAME, []
        
        # PROFESSIONAL LOG: Who is the user looking for?
        self.logger.info(f"Searching for a contact, Search query: '{clean_query.title()}'")
        
        found_contact = []
        for contact in contacts:
            if clean_query.lower() in contact['name'].lower():
                found_contact.append(contact)
              
        if not found_contact:
            # We write at INFO level because this is not an error, just a result not found
            self.logger.info(f"Search result: No contact matched '{clean_query.title()}'")
            return ContactStatus.NOT_FOUND, []
            
        self.logger.info(f"Search result: '{clean_query.title()}' contact found")
        return ContactStatus.SUCCESS, found_contact
          
    def delete_contact(self, name: str):
        """
        Delete a contact using an exact name match.
    
        The provided name is normalized before comparison. If a
        matching contact exists, it is removed from storage and the
        updated contact list is saved.
    
        Args:
            name (str):
                Exact name of the contact to remove.
    
        Returns:
            ContactStatus:
                - ContactStatus.SUCCESS if the contact was deleted.
                - ContactStatus.EMPTY_NAME if the provided name is empty.
                - ContactStatus.NOT_FOUND if no matching contact exists.
                - ContactStatus.SAVE_ERROR if the updated contact list
                  could not be saved.
        """
      
        contacts = self.json_contacts.load_contacts()
        
        target_name = name.strip().lower()
        is_valid, error_detail = InputValidator.validate_name(target_name)
        if not is_valid:
            self.logger.warning(f"Deleting contact failed: name left blank")
            return ContactStatus.EMPTY_NAME
        
        updated_contacts = [c for c in contacts if c['name'].lower() != target_name]
        if len(updated_contacts) == len(contacts):
            self.logger.info(f"Deletion failed: '{target_name.title()}' not found")
            return ContactStatus.NOT_FOUND
            
        if self.json_contacts.save_contacts(updated_contacts):
            self.logger.info(f"Contact successfully deleted: {target_name.title()}")
            return ContactStatus.SUCCESS
            
        return ContactStatus.SAVE_ERROR