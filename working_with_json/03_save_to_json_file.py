import json

players = {
  'name' : 'Federico Valverde',
  'position' : 'yarim himayachi',
  'number' : 8
}

filename = 'football_team.json'

with open(filename, 'w') as f:
  json.dump(players, f, indent=4)
    
print(f"'{filename}' successfully saved to the json file")