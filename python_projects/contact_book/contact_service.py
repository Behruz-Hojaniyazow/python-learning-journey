from enum import Enum, auto
from storage import JSONContactStorage
from validators import InputValidator
from logger_config import get_logger
from config import FILE_NAME

class ContactStatus(Enum):
    SUCCESS = auto()
    EMPTY_NAME = auto()
    DUPLICATE_NAME = auto()
    DUPLICATE_PHONE = auto()
    INVALID_PHONE = auto()
    SAVE_ERROR = auto()
    NOT_FOUND = auto()

class ContactService:
  
    def __init__(self):
        self.logger = get_logger()
        self.json_contacts = JSONContactStorage(FILE_NAME)
      
    def add_contact(self, name: str, phone_number: str):
        """Validate, process, and save a new contact to the storage."""
        
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
        Read and return all saved contacts from the storage.
        Returns an empty list if no contacts exist.
        """
      
        return self.json_contacts.load_contacts()
      
    def search_contact(self, query: str):
        """Search a contact by name from the storage."""
      
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
        """Delete a contact from the storage by exact name match."""
      
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