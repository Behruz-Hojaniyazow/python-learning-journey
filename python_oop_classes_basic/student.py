class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
    
  def show_info(self):
    print(
      f"My name is {self.name.title()} "
      f"and I am a Student, "
      f"I am {self.grade} st/th/rd/nd grade"
    )
    
s1 = Student("behruz", 12)
s1.show_info()