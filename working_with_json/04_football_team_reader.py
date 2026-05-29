import json

filename = 'football_team.json'

try:
  with open(filename, 'r') as file:
    info_team = json.load(file)
  
  print(info_team)
  print(info_team['name'])
  
except FileNotFoundError:
  print(f"\n{filename} file not found, Please run the writer script first")
  
except IOError as e:
  print(f"\nFile Error - {e}")
  
except Exception as e:
  print(f"\nUnexpected error - {e}")