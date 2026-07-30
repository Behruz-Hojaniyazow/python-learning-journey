"""
Entry point and presentation layer for the Kryos Student Manager System.

This module implements the console-based user interface (UI) of the
application. It is intentionally kept free of business logic and data
validation — those responsibilities are delegated to
:class:`student_service.StudentService` and the validation layer — so that
this module's sole concern is orchestrating user interaction:

    * Rendering menus and prompts.
    * Collecting and forwarding raw user input to the service layer.
    * Translating :class:`status.StudentStatus` results into human-readable,
      emoji-annotated feedback messages.
    * Handling graceful shutdown on user interruption (``Ctrl+C``) and on
      unexpected critical failures.

Module-level constants:
    logger (logging.Logger): The application-wide logger instance, used to
        record critical, unexpected failures for later diagnosis.
    students (StudentService): The single service-layer instance through
        which all student data operations (add, search, show, delete) are
        performed for the lifetime of the running application.
    COMMON_ERRORS (dict[StudentStatus, str]): A mapping of validation and
        lookup failure statuses (shared across multiple UI actions) to
        their corresponding user-facing error/warning messages.
"""

import sys
from typing import NoReturn
from student_service import StudentService
from logger_config import get_logger
from status import StudentStatus
from storage import JSONStudentStorage
from config import FILE_NAME

storage = JSONStudentStorage(FILE_NAME)
logger = get_logger()
students = StudentService(storage)

COMMON_ERRORS = {
    StudentStatus.EMPTY_NAME : "❌️ Error: Name cannot be empty",
    StudentStatus.DUPLICATE_NAME : "⚠️ Warning: This student is already in Class register",
    StudentStatus.INVALID_NAME_FORMAT : "❌️ Error: The name must consist only of letters",
    StudentStatus.EMPTY_AGE : "❌️ Error: Age cannot be empty",
    StudentStatus.AGE_TOO_LOW : "❌️ Error: The entered age is too low",
    StudentStatus.AGE_TOO_HIGH : "❌️ Error: Age cannot be greater than 120",
    StudentStatus.INVALID_AGE_FORMAT : "❌️ Error: The age must consist only of numbers",
    StudentStatus.EMPTY_SCORE : "❌️ Error: Score cannot be empty",
    StudentStatus.INVALID_SCORE_FORMAT : "❌️ Error: The score must consist only of numbers",
    StudentStatus.INVALID_SCORE_RANGE : "❌️ Error: The score must be between 1 and 100",
    StudentStatus.NOT_FOUND : "⚠️ Entered name not found from the Class Register"
}

def ui_add_student() -> None:
    """Run the interactive "Add Student" workflow.

    Repeatedly prompts the user for a student's name, age, and score,
    forwarding each complete set of inputs to
    :meth:`StudentService.add_student` for validation and persistence.
    The loop continues indefinitely, allowing the user to register
    multiple students in a single session, until the user types ``stop``
    at any of the three prompts (name, age, or score), at which point the
    function returns control to the calling menu.

    For each submission attempt, the resulting :class:`StudentStatus` is
    translated into a corresponding success or error message (drawn from a
    local ``ACTION_MESSAGES`` mapping or the shared :data:`COMMON_ERRORS`
    mapping) and printed to the console.

    Side Effects:
        * Prints prompts, ordinal labels (e.g. "1st", "2nd", "3rd"), and
          result messages to stdout.
        * Persists newly added students via the service layer.

    Returns:
        None
    """
    
    print("\n--- 🗂 Adding Students 🗂 ---")
    
    ACTION_MESSAGES = {
        StudentStatus.SUCCESS : "✅️ The student has been added successfully",
        StudentStatus.SAVE_ERROR : "❌️ System Error: Unable to save student"
    }
    
    while True:
        print("\nType 'stop' to stop adding students")
        
        order = len(students.get_students()) + 1
        if 11 <= order % 100 <= 13:
            suffix = 'th'
        else:
            suffix = {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(order % 10, 'th')
        print(f"\n[+] Requesting details for the {order}{suffix} student...")
        print(f"--> Please enter the required information below:")
        
        name = input("Name: ").strip()
        if name.lower() == 'stop':
            print("\nAdding students stopped")
            break
        
        age = input("Age: ").strip()
        if age.lower() == 'stop':
            print("\nAdding students stopped")
            break
        
        score = input("Score: ").strip()
        if score.lower() == 'stop':
            print("\nAdding students stopped")
            break
        
        result = students.add_student(name, age, score)
        message = ACTION_MESSAGES.get(result) or COMMON_ERRORS.get(result, f"Unexpected status: {result.name}")
        
        print(message)
        
def ui_search_students() -> None:
    """Run the interactive "Search Student" workflow.

    Guards against searching an empty class register by informing the
    user and returning early if no students have been added yet.
    Otherwise, repeatedly prompts the user for a name (or partial name)
    to search for, delegates the lookup to
    :meth:`StudentService.search_students`, and prints all matching
    records in a formatted, human-readable block.

    The loop continues until the user types ``stop`` at the name prompt.

    Side Effects:
        * Prints status messages, match counts, and formatted student
          details (name, age, score) to stdout.

    Returns:
        None
    """
    
    print("\n--- 🔍 Searching Student 🔎 --- ")
    
    if not students.get_students():
        print("\n📂 There're no students to search, first add students")
        return
    
    ACTION_MESSAGES = {
        StudentStatus.SUCCESS : "✅️ Student found successfully"
    }
    
    while True:
        print("\nType 'stop' to stop searching")
        name = input("Enter a student's name: ").strip()
        if name.lower() == 'stop':
            print("\nSearching students stopped")
            break
        
        status, result = students.search_students(name)
        message = ACTION_MESSAGES.get(status) or COMMON_ERRORS.get(status, f"Unexpected status: {status.name}")
        print(message)
        
        if result:
            plural_suffix = 'students' if len(result) > 1 else 'student'
            print(f"\n🔍 Found {len(result)} {plural_suffix} matching your '{name.title()}'")
            print("-" * 40)
            for s in result:
                print(
                    f"Name: {s['name'].title()}\n"
                    f"Age: {s['age']}\n"
                    f"Score: {s['score']}"
                )
                print("-" * 40)

def ui_show_students() -> None:
    """Display all registered students in a formatted, ranked table.

    Retrieves the full list of student records via
    :meth:`StudentService.get_students`. If the class register is empty,
    informs the user and returns early. Otherwise, sorts the students by
    descending score (with name, case-insensitively, as a tiebreaker) and
    renders them as an aligned, tabular console listing showing each
    student's rank, name, age, and score.

    Side Effects:
        * Prints a formatted table (header, separators, and one row per
          student) to stdout.

    Returns:
        None
    """
    
    all_students = students.get_students()
    if not all_students:
        print("\nThere're no students to show, first add students")
        return
    
    sorted_students = sorted(all_students, key=lambda x: (-x['score'], x['name'].lower()))
    
    print("\n" + "=" * 43)
    print(f" {'Student Name':<18} | {'Age':<6} | {'Score':<5}")
    print("-" * 43)
    for index, student in enumerate(sorted_students, start=1):
        print(
            f"{index}. {student['name'].title():<16} | "
            f"{student['age']:<6} | "
            f"{student['score']:<5}"
        )
        print("-" * 43)
    
def ui_delete_students() -> None:
    """Run the interactive "Delete Student" workflow.

    Guards against deleting from an empty class register by informing the
    user and returning early if no students have been added yet.

    For each search term entered by the user, this function:
        1. Delegates the lookup to :meth:`StudentService.search_students`.
        2. If the lookup itself fails (e.g. no match found), prints the
           corresponding error and prompts again.
        3. If exactly one match is found, selects it automatically.
        4. If multiple matches are found, displays a numbered list and
           prompts the user to select one by number (or ``0`` to cancel
           the current deletion attempt).
        5. Displays the selected student's full details and asks for a
           final ``yes``/``no`` confirmation before actually deleting the
           record via :meth:`StudentService.delete_students`.

    The outer loop continues until the user types ``stop`` at the name
    prompt.

    Side Effects:
        * Prints prompts, match listings, confirmation requests, and
          result messages to stdout.
        * Permanently removes a student record from storage upon
          confirmed deletion.

    Returns:
        None
    """
    
    print("\n--- 🗑 Deleting Students 🗑 ---")
    
    if not students.get_students():
        print("\nThere are no students to delete, first add students")
        return
    
    ACTION_MESSAGES = {
        StudentStatus.SUCCESS : "✅️ Student deleted successfully",
        StudentStatus.SAVE_ERROR : "❌️ System Error: Unable to delete student"
    }
        
    while True:
        print("\nType 'stop' to stop deleting students")
        name = input("Enter a student name to delete: ").strip()
        if name.lower() == 'stop':
            print("\nDeleting students stopped")
            break
        
        status, result = students.search_students(name)
        if status != StudentStatus.SUCCESS:
            message = COMMON_ERRORS.get(status, f"Unexpected status: {status.name}")
            print(message)
            continue
        
        if result:
            if len(result) == 1:
                selected_student = result[0]
            
            else:
                print(f"\nFound {len(result)} students matching your {name.title()}")
                print("-" * 35)
                for index, student in enumerate(result, start=1):
                    print(f"{index}. {student['name'].title()}")
                print("-" * 35)
                
                choice = input("\nEnter the number of the student to delete (or '0' to cancel): ").strip()
                
                if choice == '0':
                    print("\n🛑 Deletion cancelled")
                    continue
                
                if not choice.isdigit() or not (1 <= int(choice) <= len(result)):
                    print("\n❌️ Invalid selection, Please enter a valid number")
                    continue
                    
                selected_student = result[int(choice) - 1]
                
            print(
                f"\n📌 Target:\n"
                f"     Name: {selected_student['name'].title()}\n"
                f"     Age: {selected_student['age']}\n"
                f"     Score: {selected_student['score']}"
                )
            confirm = input(f"\nDelete: {selected_student['name'].title()} (yes/no): ").strip()
            
            if confirm.lower() in ('yes', 'y'):
                delete_result = students.delete_students(selected_student['name'])
                message = ACTION_MESSAGES.get(delete_result, f"Unexpected status: {delete_result.name}")
                print(message)
            elif confirm.lower() in ('no', 'n'):
                print("\n🛑 Deletion cancelled")
                
            
            else:
                print("\n⚠️ Please enter only (yes/no)")

def ui_exit_app() -> NoReturn:
    """Terminate the application gracefully.

    Prints a farewell message to the user and immediately exits the
    Python interpreter via :func:`sys.exit`.

    Side Effects:
        * Prints a goodbye message to stdout.
        * Terminates the running process.

    Returns:
        None: This function does not return; it always exits the process.
    """
    
    print("\nThank you for using Kryos Student Manager System, Goodbye 👋🏼")
    sys.exit()            
            
def main() -> None:
    """Run the main application loop for the Kryos Student Manager System.

    Builds the top-level ``menu_actions`` dispatch table, mapping each
    menu option number to a display label and its corresponding UI
    handler function, then enters an infinite loop that:

        1. Renders the main menu.
        2. Prompts the user to choose an action.
        3. Dispatches to the selected handler function, or prints an
           error message for an invalid choice.

    The loop is wrapped in exception handling to ensure the application
    always exits gracefully:

        * ``KeyboardInterrupt`` (raised when the user presses ``Ctrl+C``)
          is caught and results in a clean, user-friendly shutdown message
          followed by a normal (exit code ``0``) process termination.
        * Any other unhandled ``Exception`` is treated as a critical,
          unexpected system failure: it is logged with a full traceback
          via the application logger, a generic user-facing error message
          is printed, and the process exits with a non-zero (``1``) exit
          code to signal failure to the calling environment.

    Side Effects:
        * Prints the menu, prompts, and any dispatched handler's output
          to stdout.
        * May write a critical-level entry to the log file on unexpected
          failure.
        * Terminates the process on ``Ctrl+C``, unexpected error, or via
          the "Exit App" menu option.

    Returns:
        None
    """
  
    menu_actions = {
      '1' : {'text' : 'Add Student', 'func' : ui_add_student},
      '2' : {'text' : 'Show Student', 'func' : ui_show_students},
      '3' : {'text' : 'Search Student', 'func' : ui_search_students},
      '4' : {'text' : 'Delete Student', 'func' : ui_delete_students},
      '5' : {'text' : 'Exit App', 'func' : ui_exit_app}
    }
    
    try:
        # Main application loop
        while True:
            print('\n' + '=' * 46)
            print("💎 Welcome to the Kryos Student Manager System!")
            print("-" * 46)
            for key, value in menu_actions.items():
                print(f"{key} -> {value['text']}")
            print("=" * 46)
          
            choice = input("\nChoose an Action: ").strip()
          
            if choice in menu_actions:
                menu_actions[choice]['func']()
            
            else:
                print("\n❌️ Error: Invalid choice, Choose 1 to 5!")
    
    except KeyboardInterrupt:
        # close gracefully without throwing an error when the user presses Ctrl+C
        print("\n\nProject was stopped by the user")
        sys.exit(0)
      
    except Exception:
        # Any unexpected critical error in the program goes here
        logger.critical(f"A critical system error has occurred.", exc_info=True)
        print("\nA serious system error has occurred, Please contact your administrator")
        sys.exit(1)
    
if __name__ == '__main__':
    main()