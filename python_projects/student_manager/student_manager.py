import sys

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
  
  students_list = []
  order = 1
  
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
      continue
    
    age = get_numbers("Age: ")
    score = get_numbers("Score: ")
    
    # Ensure score stays within valid range
    if score > 100:
      print("❌️ Score cannot be greater than 100!")
      continue
    
    # Store student information in dictionary format
    student = {
      'name' : name,
      'age' : age,
      'score' : score
    }
    
    students_list.append(student)
    print("✅️ Student added successfully!")
    order += 1
  return students_list
  
def show_students(students):
  """Outputs name, age, and scores to the console in a nice table format"""
  if not students:
    print("\n(!) Student list is empty")
    return
  
  print('\n' + '=' * 43)
  print(f"{"Student name":<18} | {"Age":<6} | {"Score":<5}")
  print('-' * 43)
  
  for student in students:
    print(
      f"{student['name'].title():<18} | "
      f"{student['age']:<6} | "
      f"{student['score']:<5}"
      )
    print("=" * 43)
    
def search_students(students):
  """function that seraches a student from the list"""
  
  if not students:
    print("\n(!) Student list is empty")
    return
  
  while True:
    print("\nType (stop) to finish searching")
    user_input = input("\nEnter the name of the student you are looking for: ").strip()
    
    if user_input.lower() == 'stop':
      print("\nSearch stopped, Thanks!")
      break
    
    # Track whether the student exists in the register
    found = False
      
    for student in students:
      if student['name'].lower() == user_input.lower():
        print("\nYes! This student is in the Class Register")
        print(f"Name {student['name'].title()} | Age {student['age']} | Score {student['score']}")
        found = True
        break
    if not found:
      print(f"\nUnfortunately! a student named {user_input} is not in Class Register!")
      
def save_students(students):
  """Function that saves students information into to the file as a txt file"""
  
  filename = 'student_info.txt'
  
  if not students:
    print("\nNo student information found to save!")
    return
  
  try:
    
    with open(filename, 'w', encoding = 'utf - 8') as f:
      for student in students:
        formatted_info = f"{student['name'].title():<15} | {student['age']:<6} | {student['score']:<5}\n"
        f.write(formatted_info)
        
      if len(students) > 1:
        print(f"\n{len(students)} students information saved successfully!")
        
      else:
        print(f"\n{len(students)} student information saved successfully!")
  
  except IOError as e:
    print(f"\nFile Error - {e}")
    
  except Exception as e:
    print(f"\nUnexpected Error - {e}")
    
def delete_students(students):
  """Function that deletes students from the Class Register"""
  
  if not students:
    print("\nNo students found to delete")
    return
  
  print("\nEnter a student name to delete")
  print("or type 'stop' to stop deleting")
  while True:
    choice = input('\nName or (stop): ').strip()
    
    if not choice:
      print("\nName cannot be empty")
      continue
    
    if choice == 'stop':
      print("\nStudent deletion stopped")
      break
    
    deleted = False
    
    for student in students[:]:
      if choice.lower() == student['name'].lower():
        
        while True:
        
          confirm = input(f"\nDelete {student['name'].title()} (yes/no): ").strip().lower()
          if confirm in ('yes', 'y'):
            students.remove(student)
          
            print(f"\n{student['name'].title()} was deleted successfully!")
          
            if len(students) > 1:
              print(f"{len(students)} students left in the Class Register")
          
            else:
              print(f"{len(students)} student left in the Class Register")
          
            return
        
          elif confirm in ('no', 'n'):
            print(f"\n{student['name'].title()} was not deleted!")
            return
        
          else:
            print("\nPlease type 'yes or no'!")
          
    if not deleted:
      print(f"\nNo student found named {choice.title()}!")
      
def exit_app():
  """Exit the application gracefully"""
  print("\nThank you for using Kryos Student Manager! GoodBye!")
  sys.exit()
  
def main():
  
  students = []
  
  menu_actions = {
    '1' : 'Add Student',
    '2' : 'Show Student',
    '3' : 'Search Student',
    '4' : 'Save Students to the file',
    '5' : 'Delete Student',
    '6' : 'Exit App'
  }
  
  # Main application loop
  while True:
    print('\n' + '=' * 43)
    print("💎 Welcome to the Kryos Student Manager System!")
    print("-" * 43)
    for key, value in menu_actions.items():
      print(f"{key} -> {value}")
    print("=" * 43)
    
    choice = input("\nChoose an Action: ").strip()
    
    if choice == '1':
      new_students = add_student()
      students.extend(new_students)
    
    elif choice == '2':
      show_students(students)
      
    elif choice == '3':
      search_students(students)
      
    elif choice == '4':
      save_students(students)
      
    elif choice == '5':
      delete_students(students)
      
    elif choice == '6':
      exit_app()
      
    else:
      print("\n❌️ Error: Invalid choice, Choose 1 to 4!")
      
if __name__ == '__main__':
  main()