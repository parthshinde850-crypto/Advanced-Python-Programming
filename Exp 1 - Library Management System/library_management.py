
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False



class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")



class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"Patron '{patron.name}' registered successfully.")

    def borrow_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            patron.borrow_book(book)
        else:
            print("Patron or Book not found.")

    def return_book(self, patron_id, isbn):
        patron = None
        book = None

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        for b in self.books:
            if b.isbn == isbn:
                book = b
                break

        if patron and book:
            patron.return_book(book)
        else:
            print("Patron or Book not found.")

    def display_books(self):
        print("\n------ Library Books ------")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"Title : {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN  : {book.isbn}")
            print(f"Status: {status}")
            print("---------------------------")

    def display_patrons(self):
        print("\n------ Registered Patrons ------")
        for patron in self.patrons:
            print(f"Name      : {patron.name}")
            print(f"Patron ID : {patron.patron_id}")

            if patron.borrowed_books:
                print("Borrowed Books:")
                for book in patron.borrowed_books:
                    print(f"  - {book.title}")
            else:
                print("Borrowed Books: None")

            print("-------------------------------")




library = Library()


book1 = Book("Python Programming", "Guido van Rossum", "101")
book2 = Book("Data Structures", "Mark Allen", "102")
book3 = Book("Machine Learning", "Andrew Ng", "103")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


patron1 = Patron("Parth", "P001")
patron2 = Patron("Rahul", "P002")

library.register_patron(patron1)
library.register_patron(patron2)


print("\nBorrowing Books...")
library.borrow_book("P001", "101")
library.borrow_book("P002", "102")


library.display_books()
library.display_patrons()

print("\nReturning Book...")
library.return_book("P001", "101")


library.display_books()
library.display_patrons()