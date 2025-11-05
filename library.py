from book import Book
from user import User
import json
import os

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.data_file = "library_data.json"
        self.load_data()

    def save_data(self):
        data = {
            "books": [
                {
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "is_available": book.is_available
                } for book in self.books
            ],
            "users": [
                {
                    "name": user.name,
                    "borrowed_books": [book.title for book in user.borrowed_books]
                } for user in self.users
            ]
        }

        with open(self.data_file, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if not os.path.exists(self.data_file):
            return

        with open(self.data_file, "r") as file:
            data = json.load(file)

        # Load books
        for b in data["books"]:
            book = Book(b["title"], b["author"], b["isbn"])
            book.is_available = b["is_available"]
            self.books.append(book)

        # Load users
        for u in data["users"]:
            user = User(u["name"])
            self.users.append(user)

        # Re-link borrowed books to users
        for user_data in data["users"]:
            user = self.find_user(user_data["name"])
            for book_title in user_data["borrowed_books"]:
                book = self.find_book(book_title)
                if book:
                    user.borrow_book(book)

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_data()

    def register_user(self, name):
        user = User(name)
        self.users.append(user)
        self.save_data()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user(self, name):
        for user in self.users:
            if user.name.lower() == name.lower():
                return user
        return None

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = []

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)

        return results

    def borrow_book(self, title, username):
        book = self.find_book(title)
        user = self.find_user(username)

        if not book:
            return "Book not found."
        if not user:
            return "User not registered."
        if not book.is_available:
            return "Book is already borrowed."

        if not user.can_borrow():
            return f"{username} has reached the borrow limit ({user.MAX_BORROW_LIMIT} books)."

        book.borrow()
        user.borrow_book(book)
        self.save_data()
        return f"{username} borrowed '{title}'."

    def return_book(self, title, username):
        book = self.find_book(title)
        user = self.find_user(username)

        if not book or not user:
            return "Invalid user or book."
        if book not in user.borrowed_books:
            return "This user did not borrow this book."

        if not user.can_borrow():
            return f"{username} has reached the borrow limit ({user.MAX_BORROW_LIMIT} books)."

        book.return_book()
        user.return_book(book)

        self.save_data()
        return f"{username} borrowed '{title}'."

