class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
    
  def show_book_info(self):
    print("--- KRYOS LIBRARY ---")
    print(
      f"Book Title: {self.title.upper()}"
    )
    print(
      f"Book Author: {self.author.title()}"
    )
    print(
      f"Pages: {self.pages}"
    )
    
book = Book("little women", "behruz", 456)
book.show_book_info()