class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        """Attempts to check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"The book '{title}' has been checked out.")
                    return True
                else:
                    print(f"The book '{title}' is already checked out.")
                    return False
        print(f"The book '{title}' was not found in the library.")
        return False

    def return_book(self, title):
        """Attempts to return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                    return True
                else:
                    print(f"The book '{title}' was not checked out.")
                    return False
        print(f"The book '{title}' was not found in the library.")
        return False

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books are currently available.")
