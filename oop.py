from abc import ABC, abstractmethod
from datetime import datetime, timedelta

# Abstract Class for Book
class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    @abstractmethod
    def book_type(self):
        pass

# Inheritance for PrintedBook
class PrintedBook(Book):
    def book_type(self):
        return "Printed Book"

# Inheritance for EBook
class EBook(Book):
    def book_type(self):
        return "E-Book"

# Base User Class
class User:
    def __init__(self, name):
        self.name = name
        self.__borrow_history = []

    # Encapsulation
    def add_borrow_record(self, record):
        self.__borrow_history.append(record)

    def show_borrow_history(self):
        for record in self.__borrow_history:
            print(record)

# Inheritance + Polymorphism for Member and Librarian
class Member(User):
    def borrow_book(self, book):
        borrow_date = datetime.now()
        return_date = borrow_date + timedelta(days=14)
        record = f"{self.name} borrowed '{book.title}' on {borrow_date.date()}, return by {return_date.date()}"
        self.add_borrow_record(record)
        print(record)

class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}' to library.")

# Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.book_type()})")

# --- Example Usage ---
if __name__ == "__main__":
    # Create library
    my_library = Library()

    # Create librarian
    librarian = Librarian("Alice")
    
    # Add books
    book1 = PrintedBook("1984", "George Orwell", "12345")
    book2 = EBook("Python Tricks", "Dan Bader", "67890")
    librarian.add_book(my_library, book1)
    librarian.add_book(my_library, book2)

    print("\nLibrary Collection:")
    my_library.show_books()

    # Create member
    member = Member("Bob")
    member.borrow_book(book1)

    print("\nBorrow History:")
    member.show_borrow_history()
