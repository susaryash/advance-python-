
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added successfully")

    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "borrowed successfully")
        else:
            print("Book not available")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")

    def display_books(self):
        print("Available Books:", self.books)


# Main program
l = Library()

l.add_book("Python")
l.add_book("Java")

l.display_books()

l.borrow_book("Python")
l.display_books()

l.return_book("Python")
l.display_books()
