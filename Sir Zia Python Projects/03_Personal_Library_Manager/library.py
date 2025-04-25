import streamlit as st

# Initialize session state for the book library
if 'books' not in st.session_state:
    st.session_state.books = []

# Book class for better structure
class Book:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

    def to_dict(self):
        return {
            "Title": self.title,
            "Author": self.author,
            "Year": self.year,
            "Genre": self.genre,
            "Read": self.read_status
        }

# Function to display books
def display_books(books):
    if not books:
        st.write("No books to display.")
    else:
        for i, book in enumerate(books, start=1):
            st.markdown(f"**{i}. {book['Title']}** by {book['Author']} ({book['Year']})")
            st.write(f"Genre: {book['Genre']} | Read: {'Yes' if book['Read'] else 'No'}")
            st.markdown("---")

# Sidebar menu
menu = st.sidebar.radio("Menu", [
    "Add a Book", 
    "Remove a Book", 
    "Search for a Book", 
    "Display All Books", 
    "Display Statistics", 
    "Exit"
])

# Add a book
if menu == "Add a Book":
    st.header("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")
    
    if st.button("Add Book"):
        if title and author and genre:
            new_book = Book(title, author, year, genre, read)
            st.session_state.books.append(new_book.to_dict())
            st.success(f"Book '{title}' added!")
        else:
            st.warning("Please fill all the fields.")

# Remove a book
elif menu == "Remove a Book":
    st.header("Remove a Book")
    title_to_remove = st.text_input("Enter the title of the book to remove")
    if st.button("Remove Book"):
        original_len = len(st.session_state.books)
        st.session_state.books = [book for book in st.session_state.books if book['Title'].lower() != title_to_remove.lower()]
        if len(st.session_state.books) < original_len:
            st.success(f"Book '{title_to_remove}' removed!")
        else:
            st.warning(f"No book found with the title '{title_to_remove}'.")

# Search for a book
elif menu == "Search for a Book":
    st.header("Search for a Book")
    query = st.text_input("Enter title or author to search")
    if query:
        results = [book for book in st.session_state.books if query.lower() in book['Title'].lower() or query.lower() in book['Author'].lower()]
        if results:
            display_books(results)
        else:
            st.info("No matching books found.")

# Display all books
elif menu == "Display All Books":
    st.header("All Books in Library")
    display_books(st.session_state.books)

# Display statistics
elif menu == "Display Statistics":
    st.header("Library Statistics")
    total = len(st.session_state.books)
    read = sum(1 for book in st.session_state.books if book['Read'])
    if total > 0:
        percentage_read = (read / total) * 100
    else:
        percentage_read = 0.0

    st.metric("Total Books", total)
    st.metric("Books Read", f"{percentage_read:.2f}%")

# Exit option (for UX only, since Streamlit apps run persistently)
elif menu == "Exit":
    st.header("Thank you for using the Book Library!")
    st.stop()