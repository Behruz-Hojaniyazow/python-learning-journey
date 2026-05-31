import json


students = [
  {
    'behruz' : {
      'active' : False,
      'job' : None,
      'high rated' : True
    },
    'mahmut' : {
      'active' : True,
      'job' : None,
      'high rated' : True
    }
  }
]

json_string = json.dumps(students, indent=4)

print(json_string)
print(type(json_string))