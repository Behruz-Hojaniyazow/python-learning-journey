import pickle
from models import StudentData

class StudentStorage:
    
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        
    def load_students(self) -> list[StudentData]:
        
        try:
            with open(self.file_name, 'rb') as file:
                students: list[StudentData] = pickle.load(file)
                return students
                
        except FileNotFoundError:
            #print("Error: File not found! The program may be running for the first time.")
            return []
            
        except EOFError:
            print("Error: File found, but it is empty! Nothing could be read.")
            return []
            
        except pickle.UnpicklingError:
            print("Error: The file is corrupt or not in the correct Pickle format!")
            return []
            
        except Exception as e:
            print(f"Unexpected error occured - {e}")
            return []
            
    def save_students(self, students: list[StudentData]) -> bool:
        
        try:
            with open(self.file_name, "wb") as file:
                pickle.dump(students, file)
            return True
            
        except OSError as e:
            print(f"Critical error: There was a problem writing to the file. Reason: {e}")
            return False
            
        except pickle.PicklingError as e:
            print(f"Error: This object cannot be saved using Pickle. Reason: {e}")
            return False
            
        except Exception as e:
            print(f"Unexpected error occured - {e}")
            return False