# Step 1: Book class
class Book:
    def __init__(self, name, author, release_date):
        self.name = name
        self.author = author
        self.release_date = release_date
        self.read = False  # Track if the book has been read

    def __str__(self):
        status = "Read" if self.read else "Not Read"
        return f"{self.name} by {self.author} ({self.release_date}) - {status}"


my_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925-April-10")
print("Book Name:", my_book.name)
print("Book Author:",my_book.author)
print("Book Release Date:",my_book.release_date)
print("Book Read Status:",my_book.read)
print("\n---\n")

# Step 2–5: BookCollection class
class BookCollection:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            if not isinstance(books, list):
                raise TypeError("You must pass a list of Book objects")
            for book in books:
                if not isinstance(book, Book):
                    raise TypeError("All items in the list must be Book objects")
            self.books = books

    def __str__(self):
        if not self.books:
            return "Book Collection is Empty"
        return "\n" + "\n".join(str(book) for book in self.books)

    # Step 3: Add books
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("You can only add Book objects")
        self.books.append(book)

    # Step 4: Mark books as read
    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = True
                print(f"'{book_name}' has been marked as read")
                return
        print(f"Book '{book_name}' not found in the collection")

    # Step 5: Display collection status
    def list_books(self):
        if not self.books:
            print("No books in the collection.")
        else:
            for book in self.books:
                print(book)
        

# Create books
book1 = Book("1984", "George Orwell", "1949-06-08")
book2 = Book("Brave New World", "Aldous Huxley", "1932-01-01")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1925-04-10")

# Create a empty collection
empty_collection = BookCollection()

# Display empty collection
print("Empty collection:")
empty_collection.list_books()

# Create a collection with 2 books
collection = BookCollection([book1, book2])

# Display collection
print("\nInitial collection with 2 books:")
collection.list_books()
print()

# Mark a book as read
collection.mark_as_read("1984")

# Display updated collection
print("\nAfter marking '1984' as read, updated collection:")
collection.list_books()
print()

# Add a new book
collection.add_book(book3)

# Display final collection
print("\nAfter adding 'The Great Gatsby', final collection:")
collection.list_books()
print()