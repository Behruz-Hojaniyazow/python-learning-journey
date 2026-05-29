import json

info_me = {
  'name' : 'behruz',
  'surname' : 'hojaniyazow',
  'age' : 18,
  'country' : 'turkmenistan'
}

json_string = json.dumps(info_me, indent=4)

print(json_string)
print(type(json_string))