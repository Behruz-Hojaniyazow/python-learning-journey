import json
from config import FILE_NAME
from logger_config import get_logger
logger = get_logger()

def load_contacts():
  """
  Reads contacts from a JSON file.

  If the file does not exist:
  - returns an empty list

  If the file exists:
  - returns the data in the JSON
  """
  
  try:
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
      contacts = json.load(file)
      
      return contacts
      
  except FileNotFoundError:
    # It is normal for file not to exist(when opened for the first time) this can be done with a small warning (DEBUG)
    logger.debug(f"{FILE_NAME} not found, returned an empty list")
    
    return []

  except json.JSONDecodeError as e:
    # JSON structure is corrupted - this is a serious error!
    logger.exception(f"Invalid JSON format - {e}")
    
    return []
    
  except Exception as e:
    logger.exception(f"Unexpected error occured (load_contacts) - {e}")
    
    return []
    
def save_contacts(contacts):
  """Save contacts to a json file"""
  
  try:
    
    with open (FILE_NAME, 'w', encoding = 'utf-8') as file:
      json.dump(
        contacts,
        file, 
        indent=4,
        ensure_ascii=False
      )
      
  except IOError as e:
    logger.exception(f"File error - {e}")
    
  except Exception as e:
    logger.exception(f"An error occured while saving contacts - {e}")