class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size : int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count : int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author},Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print(f"Error: Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

library = Library()
book = Book("Pride and Prejudice","Jane Austen")
ebook = EBook("Snow Crash", " Neal Stephenson", 500)
print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
library.add_book(book)
library.add_book(ebook)
library.add_book(print_book)
library.list_books()
