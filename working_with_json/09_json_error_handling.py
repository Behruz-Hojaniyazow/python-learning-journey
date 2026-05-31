import json
import logging

logging.basicConfig(level=logging.ERROR)

def error_handling_json():
  """Function that handles the error with json.JSONDecodeError"""
  
  raw_json_data = "{'name' : 'Behruz'}"
  
  try:
    data = json.loads(raw_json_data)
    print(f"\nSuccessful: {data}")
    
  except json.JSONDecodeError as e:
    logging.error(f"\nInvalid Json format: {e}")
    
    data = {"name" : "Behruz"}
    
    print(f"\nAn error occurred. Default value used. {data}")
    
if __name__ == '__main__':
  error_handling_json()