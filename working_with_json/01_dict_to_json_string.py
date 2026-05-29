import json

students = {
  'name' : 'behruz',
  'surname' : 'hojaniyazow',
  'age' : 18
}

json_string = json.dumps(students, indent=4)

print(json_string)
print(type(json_string))