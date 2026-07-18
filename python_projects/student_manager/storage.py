"""
Persistence layer for the Kryos Student Manager System.

This module implements the data-access layer responsible for reading and
writing student records to durable storage. By isolating all file I/O
behind a single class (:class:`JSONStudentStorage`), the rest of the
application (the service layer in particular) remains completely agnostic
to *how* or *where* data is stored — a design that follows the Single
Responsibility Principle and makes it straightforward to swap the storage
backend (e.g. to a database) in the future without touching business
logic.

Every failure mode (missing file, corrupted JSON, unexpected I/O errors)
is handled defensively and logged via the shared application logger,
ensuring the application degrades gracefully rather than crashing when
storage-related problems occur.
"""

import json
from logger_config import get_logger

class JSONStudentStorage:
    """Handles reading and writing student records to a local JSON file.

    This class encapsulates all direct interaction with the filesystem for
    student data persistence. It is designed to fail safely: any I/O or
    parsing error results in a logged diagnostic message and a safe
    fallback value (an empty list, or ``False``) rather than propagating
    an exception up to the caller.

    Attributes:
        file_name (str): The path to the JSON file used for persisting
            student records.
        logger (logging.Logger): The shared application logger, used to
            record warnings and errors encountered during file access.
    """
    
    def __init__(self, file_name: str):
        """Initialize the storage handler with a target file path.

        Args:
            file_name (str): The path to the JSON file that will be used
                to read and write student records.
        """
        
        self.file_name = file_name
        self.logger = get_logger()
        
    def load_students(self) -> list:
        """
        Reads students from a JSON file

        If the file does not exist:
        - returns an empty list

        If the file exists:
        - returns the data in the JSON

        Returns:
            list: A list of student dictionaries loaded from the JSON
            file. Returns an empty list if the file does not yet exist,
            if its contents are not valid JSON, or if any other
            unexpected error occurs while reading it.
        """

      
        try:
        
            with open(self.file_name, 'r', encoding='utf-8') as file:
                students = json.load(file)
                return students
          
        except FileNotFoundError:
            # It is normal for file not to exist (when opened for the first time) this can be done with a small warning DEBUG
            self.logger.debug(f"'{self.file_name}' not found, returned an empty list")
            return []
        
        except json.JSONDecodeError as e:
            # JSON structure is corrupted -  this is a serious error!
            self.logger.exception(f"Invalid JSON format - {e}")
            return []
        
        except Exception:
            self.logger.exception(f"Unexpected error occurred in [{self.file_name}] file")
            return []
        
    def save_students(self, students: list) -> bool:
        """
        Function that saves students information to the file as a JSON file
        Returns True if saved successfully, False otherwise.

        Args:
            students (list): The complete, up-to-date list of student
                dictionaries to persist. This function overwrites the
                entire contents of the target file with this list.

        Returns:
            bool: ``True`` if the data was written to disk successfully;
            ``False`` if an :class:`IOError` or any other unexpected
            exception occurred during the write operation.
        """
        
        try:
          
            with open(self.file_name, 'w', encoding = 'utf-8') as file:
                json.dump(
                    students,
                    file,
                    indent=4,
                    ensure_ascii=False
                )
            return True
        
        except IOError as e:
            self.logger.exception(f"File Error - {e}")
            return False
          
        except Exception as e:
            self.logger.exception("An Error occurred while saving students info")
            return False