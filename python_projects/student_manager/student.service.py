"""
Service (business-logic) layer for the Kryos Student Manager System.

This module defines :class:`StudentService`, the sole gateway through
which the presentation layer (``main.py``) interacts with student data.
It coordinates between three collaborators:

    * :class:`validators.StudentValidator` — sanitizes and validates raw
      user input before it is trusted.
    * :class:`storage.JSONStudentStorage` — persists and retrieves the
      canonical list of student records.
    * The shared application logger — records every significant business
      event (successful additions, validation failures, duplicate
      detection, deletions, and save errors) for auditability.

By concentrating all add/search/delete business rules in this single
class, the UI layer (``main.py``) can remain a thin presentation shell
that never needs to know about validation rules or storage mechanics.
"""

from typing import TypedDict
from validators import StudentValidator
from storage import JSONStudentStorage
from logger_config import get_logger
from status import StudentStatus

class StudentData(TypedDict):
    name: str
    age: int
    score: int | float

class StudentService:
    """Coordinates validation, persistence, and business rules for students.

    This class is the single source of truth for all operations that can
    be performed on the class register: adding, listing, searching for,
    and deleting student records. Every public method returns a
    :class:`status.StudentStatus` (or a tuple including one) so that
    calling code can react to outcomes without needing to inspect
    exceptions or raw data.

    Attributes:
        json_students (JSONStudentStorage): The storage backend instance
            used to load and save the list of student records, configured
            to use the file path defined in :data:`config.FILE_NAME`.
        logger (logging.Logger): The shared application logger, used to
            record informational, warning, and error events for every
            operation performed by this service.
    """
    
    def __init__(self, storage: JSONStudentStorage) -> None:
        """Initialize the service with its storage backend and logger."""
        
        self.storage = storage
        self.logger = get_logger()
        
    def add_student(self, name: str, age: str, score: str) -> StudentStatus:
        """Collects student data (name, age, grade)

        Validates the raw ``name``, ``age``, and ``score`` inputs in
        sequence (short-circuiting and returning immediately on the
        first validation failure), checks for a duplicate name already
        present in the class register, and — if all checks pass —
        appends a new student record and persists the updated list to
        storage.

        Args:
            name (str): The raw, unvalidated student name.
            age (str): The raw, unvalidated student age.
            score (str): The raw, unvalidated student score.

        Returns:
            StudentStatus: :attr:`StudentStatus.SUCCESS` if the student
            was validated and saved successfully;
            :attr:`StudentStatus.DUPLICATE_NAME` if a student with the
            same (case-insensitive) name already exists;
            :attr:`StudentStatus.SAVE_ERROR` if validation passed but
            persisting to storage failed; or any of the name/age/score
            specific validation failure statuses returned by
            :class:`StudentValidator`.
        """

        
        students: list[StudentData] = self.storage.load_students()
          
        # check students' name format
        is_valid, result_name = StudentValidator.validate_name(name)
        if not is_valid:
            self.logger.warning(f"Adding student failed (Name Error): {result_name.name}")
            return result_name
        clean_name = result_name
          
        # check duplicate student
        for student in students:
            if student['name'].lower() == clean_name.lower():
                self.logger.warning(f"'{clean_name.title()}' already exists")
                return StudentStatus.DUPLICATE_NAME
      
        is_valid, result_age = StudentValidator.validate_age(age)
        if not is_valid:
            self.logger.warning(f"Adding student failed (Age Error): {result_age.name}")
            return result_age
        clean_age = result_age
          
        # Ensure score stays in true format
        is_valid, result_score = StudentValidator.validate_score(score)
        if not is_valid:
            self.logger.warning(f"Adding student failed (Score Error): {result_score.name}")
            return result_score
        clean_score = result_score
          
        # Store student information in dictionary format
        student: StudentData = {
            'name' : clean_name,
            'age' : clean_age,
            'score' : clean_score
        }
          
        students.append(student)
        if self.storage.save_students(students):
            self.logger.info("Student added successfully!")
            return StudentStatus.SUCCESS
        else:
            self.logger.error("Adding student failed (System Error during save)")
            return StudentStatus.SAVE_ERROR
            
      
    def get_students(self) -> list[StudentData]:
        """Retrieves the full, unfiltered list of student records currently
        persisted in storage. This is a thin, read-only pass-through to
        the storage layer, provided so that calling code never needs to
        interact with :class:`JSONStudentStorage` directly.

        Returns:
            list: The complete list of student dictionaries, each
            containing ``name``, ``age``, and ``score`` keys. Returns an
            empty list if no students have been added yet.
        """
      
        return self.storage.load_students()
        
    def search_students(self, name: str) -> tuple[StudentStatus, list[StudentData]]:
        """Function that searches a student from the list

        Validates the provided search term, then performs a
        case-insensitive *substring* match against every student's name
        in the class register (allowing partial-name searches, e.g.
        searching "an" will match "Anna" and "Johan").

        Args:
            name (str): The raw, unvalidated name (or partial name) to
                search for.

        Returns:
            tuple[StudentStatus, list]: A two-element tuple containing
            the outcome status and the list of matching student
            dictionaries. Possible statuses are: a name-validation
            failure status paired with an empty list if ``name`` itself
            is invalid; :attr:`StudentStatus.NOT_FOUND` paired with an
            empty list if no students match; or
            :attr:`StudentStatus.SUCCESS` paired with one or more
            matching student dictionaries.
        """
      
        students: list[StudentData] = self.storage.load_students()
        
        # check whether it is in a true format
        is_valid, result_name  = StudentValidator.validate_name(name)
        if not is_valid:
            self.logger.warning(f"Searching student failed (Name Error): {result_name.name}")
            return result_name, []
        clean_name = result_name
        
        # Track whether the student exists in the register
        found_students = [
            student for student in students if clean_name.lower() in student['name'].lower()
        ]
                
        if not found_students:
            self.logger.info(f"Search failed, no students found matching '{clean_name.title()}'")
            return StudentStatus.NOT_FOUND, []
        
        plural_prefix = 'students' if len(found_students) > 1 else 'student'    
        self.logger.info(f"Search successful: Found {len(found_students)} {plural_prefix} matching '{clean_name.title()}'")
        return StudentStatus.SUCCESS, found_students
        
    def delete_students(self, name: str) -> StudentStatus:
        """Function that deletes students from the Class Register

        Validates the provided name, then removes every student whose
        name matches (case-insensitively, exact match) the target name
        from the class register and persists the updated list.

        Args:
            name (str): The raw, unvalidated exact name of the student to
                remove.

        Returns:
            StudentStatus: A name-validation failure status if ``name``
            is invalid; :attr:`StudentStatus.NOT_FOUND` if no student
            with that exact name exists; :attr:`StudentStatus.SAVE_ERROR`
            if the student was found but the updated list could not be
            persisted; or :attr:`StudentStatus.SUCCESS` if the student
            was removed and the change was saved successfully.
        """
      
        students: list[StudentData] = self.storage.load_students()
        
        is_valid, result_name = StudentValidator.validate_name(name)
        if not is_valid:
            self.logger.warning(f"Deleting student failed (Name Error): {result_name.name}")
            return result_name
        target_name = result_name
        
        updated_students = [s for s in students if s['name'].lower() != target_name.lower()]
        if len(updated_students) == len(students):
            self.logger.info(f"Deletion failed no student found named: {target_name.title()}")
            return StudentStatus.NOT_FOUND
              
        if self.storage.save_students(updated_students):
            self.logger.info(f"Student deleted successfully: Name {target_name.title()}")
            return StudentStatus.SUCCESS
        self.logger.error(f"Failed to save changes after deleting student '{target_name}'")
        return StudentStatus.SAVE_ERROR