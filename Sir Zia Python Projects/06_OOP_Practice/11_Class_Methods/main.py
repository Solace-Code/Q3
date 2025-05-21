class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Modify class variable using cls

    @classmethod
    def display_total_books(cls):
        print("Total books:", cls.total_books)

# Example usage:
b1 = Book("1984")
b2 = Book("Brave New World")
b3 = Book("To Kill a Mockingbird")

Book.display_total_books()
