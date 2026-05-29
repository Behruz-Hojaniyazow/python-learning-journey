import json

json_string = '{"brand" : "Apple", "model" : "Macbook"}'

python_dict = json.loads(json_string)

print(python_dict)
print(type(python_dict))