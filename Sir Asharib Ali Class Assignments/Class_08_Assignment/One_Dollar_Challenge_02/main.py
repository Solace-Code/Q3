class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book}")

    def borrow_book(self, index):
        if 0 <= index < len(self.books):
            if self.books[index].borrow():
                print(f"You borrowed: {self.books[index].title}")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid book number.")

    def return_book(self, index):
        if 0 <= index < len(self.books):
            self.books[index].return_book()
            print(f"You returned: {self.books[index].title}")
        else:
            print("Invalid book number.")


def main():
    library = Library()

    while True:
        print("\n📚 --- Library Menu ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            index = int(input("Enter book number to borrow: ")) - 1
            library.borrow_book(index)

        elif choice == "4":
            index = int(input("Enter book number to return: ")) - 1
            library.return_book(index)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
