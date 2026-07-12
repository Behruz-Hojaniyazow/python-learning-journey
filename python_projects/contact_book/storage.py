import json
from logger_config import get_logger

class JSONContactStorage:
    
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.logger = get_logger()
      
    def load_contacts(self) -> list:
        """
        Reads contacts from a JSON file.
    
        If the file does not exist:
        - returns an empty list
      
        If the file exists:
        - returns the data in the JSON
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
        """Save contacts to a json file"""
      
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