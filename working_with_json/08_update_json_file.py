import json

def file_read_update():
  """Function that reads info from the file"""
  
  default_config = None

  filename = 'config.json'

  try:
    with open(filename, 'r', encoding='utf-8') as file:
      default_config = json.load(file)
  
    if not default_config:
      print(f"\n'{filename}' file is empty")
      return None
  
    default_config['volume'] = 100
  
  except FileNotFoundError:
    print(f"\n'{filename}' file not found, Please run the writer script first")
  
  except json.JSONDecodeError:
    print(f"\nThe '{filename}' file is empty or corrupt! Restoring default configuration...")
    default_config = {'theme' : 'dark', 'volume' : 80}
    
  except IOError as e:
    print(f"\nFile Error - {e}")
  
  except Exception as e:
    print(f"\nUnexpected Error - {e}")
    
  return default_config
  
def save_file(updates):
  """Function that saves the updated file to the file"""
  
  filename = 'config.json'
  
  if not updates:
    print("\nNoting found to save")
    return
  
  with open(filename, 'w', encoding='utf-8') as file:
    json.dump(updates, file, indent=4)
  
  print(f"\n'{filename}' file updated successfully!")
  
new_config = file_read_update()
save_file(new_config)