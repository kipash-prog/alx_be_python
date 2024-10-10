from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

   

if __name__ == "__main__":
    main()
