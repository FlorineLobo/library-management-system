class User:
    MAX_BORROW_LIMIT = 3  # You can change this number anytime

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < User.MAX_BORROW_LIMIT

    def borrow_book(self, book):
        if not self.can_borrow():
            return False
        self.borrowed_books.append(book)
        return True

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        return f"User: {self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]}"
