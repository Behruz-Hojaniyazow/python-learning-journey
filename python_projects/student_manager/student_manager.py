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
    '4' : 'Exit App'
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
      exit_app()
      
    else:
      print("\n❌️ Error: Invalid choice, Choose 1 to 4!")
      
if __name__ == '__main__':
  main()