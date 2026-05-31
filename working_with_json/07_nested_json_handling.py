import json

university = {
  'faculties' : [
    {
      'name' : 'computer engineering',
      'student_numbers' : 368
    },
    {
      'name' : 'economy',
      'student_numbers' : 289
    },
    {
      'name' : 'medicine',
      'student_numbers' : 408
    }
  ]
}

filename = 'university.json'
with open(filename, 'w', encoding='utf-8') as file:
  json.dump(university, file, indent=4, ensure_ascii=False)
  
print(f"\n'{filename}' file saved to the json file successfully!")

try:
  with open(filename, 'r', encoding='utf-8') as file:
    university_dict = json.load(file)
    
  total_students = 0
  for faculty in university_dict["faculties"]:
    total_students += faculty['student_numbers']
    
  print(f"\nOverall students: {total_students}!")
    
except FileNotFoundError:
  print(f"\n{filename} file not found!")
  
except IOError as e:
  print(f"\nFile Error - {e}")
  
except Exception as e:
  print(f"\nUnexpected Error - {e}")