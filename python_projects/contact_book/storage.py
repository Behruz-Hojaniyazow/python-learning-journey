"""
Persistent storage implementation for the Contact Book application.

This module provides the JSONContactStorage class, which is
responsible for reading contact data from a JSON file and
saving updated contact information back to persistent storage.

It isolates all file system operations from the application's
business logic while providing centralized error handling and
logging.
"""

import json
from logger_config import get_logger

class JSONContactStorage:
    """
    Provide JSON-based persistent storage for contact data.

    This class is responsible for reading contact information
    from a JSON file and writing updated contact collections
    back to the same file.

    It serves as the application's data access layer, isolating
    all file system operations from the business logic while
    providing centralized error handling and logging.

    Attributes:
        file_name (str):
            Path to the JSON file used for persistent storage.

        logger (logging.Logger):
            Configured logger used to record storage-related
            events, warnings, and exceptions.
    """
    
    def __init__(self, file_name: str):
        """
        Initialize the JSON storage manager.
    
        Creates a storage instance responsible for loading and saving
        contact data to a JSON file. A configured logger is also
        initialized for recording storage-related events and errors.
    
        Args:
            file_name (str):
                Path to the JSON file used for persistent contact
                storage.
    
        Attributes:
            file_name (str):
                Name or path of the JSON storage file.
    
            logger (logging.Logger):
                Configured logger used for debugging and error
                reporting.
        """
    
        self.file_name = file_name
        self.logger = get_logger()
      
    def load_contacts(self) -> list:
        """
        Load all contacts from the JSON storage file.
    
        Attempts to read and deserialize the configured JSON file.
        If the file does not exist, is empty, or contains invalid
        JSON data, an empty list is returned and the appropriate
        event is logged.
    
        Returns:
            list[dict]:
                A list of contact dictionaries loaded from the JSON
                file. Returns an empty list if the file cannot be
                read or contains invalid data.
        """
        
        try:
          
            with open(self.file_name, 'r', encoding='utf-8') as file:
                contacts = json.load(file)
              
            return contacts
            
        except FileNotFoundError:
            # It is normal for file not to exist(when opened for the first time) this can be done with a small warning (DEBUG)
            self.logger.debug(f"{self.file_name} not found, returned an empty list")
            
            return []
      
        except json.JSONDecodeError as e:
            # JSON structure is corrupted - this is a serious error!
            self.logger.exception(f"Invalid JSON format in [{self.file_name}]- {e}")
            
            return []
          
        except Exception as e:
            self.logger.exception(f"Unexpected error occured (load_contacts) - {e}")
            
            return []
        
    def save_contacts(self, contacts : list) -> bool:
        """
        Save the contact list to the JSON storage file.
    
        Serializes the provided contact collection and writes it to
        the configured JSON file using UTF-8 encoding and formatted
        indentation for improved readability.
    
        Any file system or unexpected errors are logged before the
        method returns a failure status.
    
        Args:
            contacts (list):
                A list containing the contact dictionaries to be
                written to the storage file.
    
        Returns:
            bool:
                True if the contacts were successfully written to
                the JSON file; otherwise, False.
        """
      
        try:
        
            with open (self.file_name, 'w', encoding = 'utf-8') as file:
                json.dump(
                  contacts,
                  file, 
                  indent=4,
                  ensure_ascii=False
                )
            return True
          
        except IOError as e:
            self.logger.exception(f"File error - {e}")
            return False
        
        except Exception as e:
            self.logger.exception(f"An error occured while saving contacts - {e}")
            return False