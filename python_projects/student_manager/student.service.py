import sys
from storage import (
  load_students,
  save_students
)
from validators import (
  validate_name,
  validate_age,
  validate_score
)
from logger_config import get_logger

logger = get_logger()

def add_student():
  """Collects student data (name, age, grade) and returns it in a list format"""
  
  students = load_students()
  order = len(students) + 1
  
  print("\nStart entering students. To stop, type 'stop' instead of the name.")
  
  while True:
    print(f"\n{order}-Enter student information!")
    name = input("Name: (or stop): ").strip()
    
    # Allow the user to stop adding students
    if name.lower() == 'stop':
      print("Data collection has stopped")
      break
    
    # check students' name format
    is_valid, cleaned_name = validate_name(name)
    if not is_valid:
      logger.warning(f"{cleaned_name}")
      print(f"\n{cleaned_name}")
      continue
    
    # check duplicate student
    duplicate_found = False
    for student in students:
      if student['name'].lower() == cleaned_name.lower():
        logger.warning(f"'{name.title()}' already exists")
        print(f"'{name.title()}' student already exists in Class Register")
        duplicate_found = True
        break
      
    if duplicate_found:
      continue
    
    age = input("Age: ")
    is_valid, validated_age = validate_age(age)
    if not is_valid:
      logger.warning(f"{validated_age}")
      print(f"\n{validated_age}")
      continue
    
    score = input("Score: ")
    
    # Ensure score stays in true format
    is_valid, validated_score = validate_score(score)
    if not is_valid:
      logger.warning(f"{validated_score}")
      print(f"\n{validated_score}")
      continue
    
    # Store student information in dictionary format
    student = {
      'name' : cleaned_name,
      'age' : validated_age,
      'score' : validated_score
    }
    
    students.append(student)
    order += 1
    if save_students(students):
      print("✅️ Student has been added successfully!")
      logger.info("Student added successfully!")
  
def show_students():
  """Outputs name, age, and scores to the console in a nice table format"""
  students = load_students()
  
  if not students:
    print("\n(!) Student list is empty")
    return
  
  sorted_students = sorted(students, key=lambda x: (-x['score'], x['name'].lower()))
  
  print('\n' + '=' * 43)
  print(f"{'Student name':<18} | {'Age':<6} | {'Score':<5}")
  print('-' * 43)
  
  for ind, student in enumerate(sorted_students, start=1):
    print(
      f"{ind}."
      f"{student['name'].title():<16} | "
      f"{student['age']:<6} | "
      f"{student['score']:<5}"
      )
    print("-" * 43)
    
def search_students():
  """function that seraches a student from the list"""
  
  students = load_students()
  
  if not students:
    print("\n(!) Student list is empty")
    return
  
  while True:
    print("\nType (stop) to stop searching")
    user_input = input("\nEnter the name of the student you are looking for: ").strip()
    
    if user_input.lower() == 'stop':
      print("\nSearch stopped, Thanks!")
      break
    
    # check whether it is in a true format
    is_valid, cleaned_name  = validate_name(user_input)
    if not is_valid:
      logger.warning(f"{cleaned_name}")
      print(f"\n{cleaned_name}")
      continue
    
    # Track whether the student exists in the register
    found = False
      
    for student in students:
      if student['name'].lower() == cleaned_name.lower():
        logger.info(f"Successfully student found: Name: '{student['name'].title()}'")
        print("\nYes! This student is in the Class Register")
        print(f"Name {student['name'].title()} | Age {student['age']} | Score {student['score']}")
        found = True
        break
    if not found:
      logger.info(f"Search failed, no students found named {user_input.title()}")
      print(f"\nUnfortunately! a student named {user_input.title()} is not in Class Register!")
    
def delete_students():
  """Function that deletes students from the Class Register"""
  
  students = load_students()
  
  if not students:
    print("\nNo students found to delete")
    return
  
  print("Type 'stop' to stop deleting")
  while True:
    print("\nEnter a student name to delete")
    choice = input('Name or (stop): ').strip()
    
    if choice.lower() == 'stop':
      print("\nStudent deletion stopped")
      break
    
    is_valid, cleaned_name = validate_name(choice)
    if not is_valid:
      logger.warning(f"{cleaned_name}")
      print(f"\n{cleaned_name}")
      continue
    
    deleted = False
    
    for student in students[:]:
      if cleaned_name.lower() == student['name'].lower():
        deleted = True
        
        while True:
        
          confirm = input(f"\nDelete {student['name'].title()} (yes/no): ").strip().lower()
          if confirm in ('yes', 'y'):
            students.remove(student)
            if save_students(students):
              logger.info(f"Successfully deleted: \nName: {student['name'].title()}")
              print(f"\n{student['name'].title()} was deleted successfully!")
            
              plural_suffix = 'student' if len(students) == 1 else 'students'
              print(f"\n{len(students)} {plural_suffix} left in the Class Register")
            else:
              print("\nFailed to save changes")
          
            break
        
          elif confirm in ('no', 'n'):
            print(f"\n{student['name'].title()} was not deleted!")
            break
        
          else:
            print("\nPlease type 'yes or no'!")
          
    if not deleted:
      logger.warning(f"Deleting Failed, No student found named '{choice.title()}'")
      print(f"\nNo student found named {choice.title()}!")
      
def exit_app():
  """Exit the application gracefully"""
  print("\nThank you for using Kryos Student Manager! GoodBye!")
  sys.exit()