class Contact:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone
    
  def show_contact(self):
    print(f"Name: {self.name.title()}")
    print(f"Phone number: {self.phone}")
    
phone = Contact("behruz", "+99363807476")
phone.show_contact()