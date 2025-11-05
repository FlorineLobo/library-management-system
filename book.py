from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrowed_date = None
        self.due_date = None

    def borrow(self):
        self.is_available = False
        self.borrowed_date = datetime.now().date()
        self.due_date = self.borrowed_date + timedelta(days=14)  # 14-day loan

    def return_book(self):
        self.is_available = True
        self.borrowed_date = None
        self.due_date = None

    def __str__(self):
        status = "Available" if self.is_available else f"Borrowed (Due: {self.due_date})"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
