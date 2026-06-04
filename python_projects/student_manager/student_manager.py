import sys
import json
import logging

FILE_NAME = 'students_info.json'
LOG_FILE = 'students.log'
MAX_SCORE = 100

# creating a log
logger = logging.getLogger('StudentManager')
logger.setLevel(logging.DEBUG) # Accepts logs of all levels

# 1.Handlet for writing to a file (All ERROR and CRITICAL ERRORS are written to a file for analysis)
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter(
  '[%(asctime)s] %(levelname)s [%(name)s:%(filename)s:%(lineno)d] - %(message)s'
)
file_handler.setFormatter(file_formatter)

# 2.Handler for output to the console (Only for the user or programmer can see on the screen)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)

if not logger.handlers:
  # Add handlers to the logger
  logger.addHandler(file_handler)
  logger.addHandler(console_handler)

def load_students():
  """
  Reads students from a JSON file
  
  If the file does not exist:
  - returns an empty list
  
  If the file exists:
  - returns the data in the JSON
  """
  
  try:
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
      students = json.load(file)
      return students
      
  except FileNotFoundError:
    # It is normal for file not to exist (when opened for the first time) this can be done with a small warning DEBUG
    logger.debug(f"'{FILE_NAME}' not found, returned an empty list")
    return []
    
  except json.JSONDecodeError as e:
    # JSON structure is corrupted -  this is a serious error!
    logger.exception(f"Invalid JSON format - {e}")
    return []
    
  except Exception as e:
    logger.exception(f"Unexpected error occured (load_students) - {e}")
    return []
    
def save_students(students):
  """Function that saves students information to the file as a JSON file"""
  
  try:
    
    with open(FILE_NAME, 'w', encoding = 'utf-8') as file:
      json.dump(
        students,
        file,
        indent=4,
        ensure_ascii=False
      )
  
  except IOError as e:
    logger.exception(f"File Error - {e}")
    
  except Exception as e:
    logger.exception(f"An Error occured while saving students info - {e}")

def get_numbers(prompt):
  """function that only accepts numbers from the user"""
  
  # Continuously ask until valid numeric input is entered
  while True:
    try:
      val = float(input(prompt))
      if val < 0:
        print("\n❌️ Number cannot be negative!")
        continue
      
      return int(val) if val.is_integer() else val
    except ValueError:
      print("(!) Please write only numbers")

def add_student():
  """Collects student data (name, age, grade) and returns it in a list format"""
  
  students = load_students()
  order = len(students) + 1
  
  print("\nStart entering students. To stop, type 'stop' instead of the name.")
  
  while True:
    print(f"\n{order}-Enter student information!")
    name = input("Name: (or 'stop): ").strip()
    
    # Allow the user to stop adding students
    if name.lower() == 'stop':
      print("Data collection has stopped")
      break
    
    # Prevent empty student names
    if not name:
      print("❌️Name cannot be empty!")
      logger.warning("Error name left blank")
      continue
    
    if not name.replace(" ", "").isalpha():
      print("❌️Invalid name format!")
      continue
    
    # check duplicate student
    duplicate_found = False
    for student in students:
      if student['name'].lower() == name.lower():
        logger.warning(f"'{name.title()}' already exists")
        print(f"'{name.title()}' student already exists in Class Register")
        duplicate_found = True
        break
      
    if duplicate_found:
      continue
    
    age = get_numbers("Age: ")
    if age < 5 or age > 120:
      print("Invalid age!")
      continue
    
    score = get_numbers("Score: ")
    
    # Ensure score stays within valid range
    if score > MAX_SCORE:
      print("❌️ Score cannot be greater than 100!")
      logger.warning("Error: Score can't be greater than 100!")
      continue
    
    # Store student information in dictionary format
    student = {
      'name' : name,
      'age' : age,
      'score' : score
    }
    
    students.append(student)
    save_students(students)
    order += 1
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
    
    # Track whether the student exists in the register
    found = False
      
    for student in students:
      if student['name'].lower() == user_input.lower():
        logger.info(f"Successfully found student: \nName: '{student['name'].title()}' \nAge: {student['age']} \nScore: {student['score']}")
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
  
  print("\nEnter a student name to delete")
  print("or type 'stop' to stop deleting")
  while True:
    choice = input('\nName or (stop): ').strip()
    
    if not choice:
      logger.warning("Error: Name left blank")
      print("\nName cannot be empty")
      continue
    
    if choice.lower() == 'stop':
      print("\nStudent deletion stopped")
      break
    
    deleted = False
    
    for student in students[:]:
      if choice.lower() == student['name'].lower():
        deleted = True
        
        while True:
        
          confirm = input(f"\nDelete {student['name'].title()} (yes/no): ").strip().lower()
          if confirm in ('yes', 'y'):
            students.remove(student)
            save_students(students)
            
            logger.info(f"Successfully deleted: \nName: {student['name'].title()}")
            print(f"\n{student['name'].title()} was deleted successfully!")
            
            plural_suffix = 'student' if len(students) == 1 else 'students'
            print(f"\n{len(students)} {plural_suffix} left in the Class Register")
          
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
  
def main():
  
  menu_actions = {
    '1' : 'Add Student',
    '2' : 'Show Student',
    '3' : 'Search Student',
    '4' : 'Delete Student',
    '5' : 'Exit App'
  }
  
  try:
    # Main application loop
    while True:
      print('\n' + '=' * 46)
      print("💎 Welcome to the Kryos Student Manager System!")
      print("-" * 46)
      for key, value in menu_actions.items():
        print(f"{key} -> {value}")
      print("=" * 46)
    
      choice = input("\nChoose an Action: ").strip()
    
      if choice == '1':
        add_student()
    
      elif choice == '2':
        show_students()
      
      elif choice == '3':
        search_students()
      
      elif choice == '4':
        delete_students()
      
      elif choice == '5':
        exit_app()
      
      else:
        print("\n❌️ Error: Invalid choice, Choose 1 to 5!")
  
  except KeyboardInterrupt:
    # close gracefully without throwing an error when the user presses Ctrl+C
    print("\n\nProject was stopped by fhe user")
    sys.exit(0)
    
  except Exception as e:
    # Any unpected critical error in the program goes here
    logger.critical(f"A critical system error has occured and the program has stopped! Global error - {e}", exc_info=True)
    print("\nA serious system error has occured, Please contact your adminstrator")
    sys.exit(1)
    
if __name__ == '__main__':
  main()