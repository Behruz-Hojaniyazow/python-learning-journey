import json
from config import FILE_NAME
from logger_config import get_logger

logger = get_logger()

def load_students():
  """
  Reads students from a JSON file
  
  If the file does not exist:
  - returns an empty list
  
  If the file exists:
  - returns the data in the JSON
  """
  
  try:
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
      students = json.load(file)
      return students
      
  except FileNotFoundError:
    # It is normal for file not to exist (when opened for the first time) this can be done with a small warning DEBUG
    logger.debug(f"'{FILE_NAME}' not found, returned an empty list")
    return []
    
  except json.JSONDecodeError as e:
    # JSON structure is corrupted -  this is a serious error!
    logger.exception(f"Invalid JSON format - {e}")
    return []
    
  except Exception:
    logger.exception(f"Unexpected error occurred in load_students")
    return []
    
def save_students(students):
  """
  Function that saves students information to the file as a JSON file
  Returns True if saved successfully, False otherwise.
  """
  
  try:
    
    with open(FILE_NAME, 'w', encoding = 'utf-8') as file:
      json.dump(
        students,
        file,
        indent=4,
        ensure_ascii=False
      )
    return True
  
  except IOError as e:
    logger.exception(f"File Error - {e}")
    return False
    
  except Exception:
    logger.exception(f"An Error occurred while saving students info")
    return False