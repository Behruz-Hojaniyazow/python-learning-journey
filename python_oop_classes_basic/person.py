class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def say_hello(self):
    print(f"Hello, My name is {self.name.title()} and \nI am {self.age} years old")

p1 = Person("behruz", 18)
p1.say_hello()