from datetime import datetime

class Address:
    
    def __init__(self, home: int, street: str, district: str, province: str):
        
        self.home = home
        self.street = street
        self.district = district
        self.province = province
        
    def __str__(self) -> str:
        
        address = f"Home address is {self.home}, {self.street.title()} street, "
        address += f"{self.district.title()} district, {self.province.title()} province"
        
        return address

class Person:
  
    def __init__(self, name: str, born_year: int):
        self.name = name
        self.born_year = born_year
    
    @property    
    def age(self) -> int:
        current_year = datetime.now().year
        return current_year - self.born_year
    
    def __str__(self) -> str:
        info = f"\nName: {self.name.title()}, Born Year: {self.born_year}, Age: {self.age}"
        return info
        
class Student(Person):
    
    def __init__(self, name: str, born_year: int, student_id: str, grade: int, address: Address):
        super().__init__(name, born_year)
        self.student_id = student_id
        self.grade = grade
        self.address = address # Address object (Composition)
    
    def __str__(self) -> str:
        person_info = super().__str__()
        student_info = f"\nStudent ID: {self.student_id}, Grade: {self.grade}"
        address_info = f"\nAddress: {self.address}"
        
        return person_info + student_info + address_info
        
def main():
    
    student_address1 = Address(
        home=12, 
        street="Yoldash Mirzayew", 
        district="Ak-Gala", 
        province="Dashoguz"
    )
    student1=Student(
        name="Behruz", 
        born_year=2008, 
        student_id="112233", 
        grade=11, 
        address=student_address1
    )
    
    print(student1)
    
if __name__ == "__main__":
    main()