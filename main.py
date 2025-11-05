from library import Library

library = Library()

def print_header(title):
    print("\n" + "="*50)
    print(f"{title.center(50)}")
    print("="*50)

while True:
    print_header("📚 Library Management System")
    print("1. ➕ Add Book")
    print("2. 👤 Register User")
    print("3. 📖 Borrow Book")
    print("4. 🔁 Return Book")
    print("5. 📋 Show All Books")
    print("6. 🔍 Search Books")  # ← Added
    print("7. ❌ Exit")

    choice = input("\nEnter choice (1-6): ")

    if choice == '1':
        print_header("➕ Add New Book")
        title = input("Book title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        library.add_book(title, author, isbn)
        print("\n✅ Book added successfully!")

    elif choice == '2':
        print_header("👤 Register User")
        name = input("User name: ")
        library.register_user(name)
        print("\n✅ User registered successfully!")

    elif choice == '3':
        print_header("📖 Borrow Book")
        title = input("Book title: ")
        username = input("Username: ")
        print("\n" + library.borrow_book(title, username))

    elif choice == '4':
        print_header("🔁 Return Book")
        title = input("Book title: ")
        username = input("Username: ")
        print("\n" + library.return_book(title, username))

    elif choice == '5':
        print_header("📋 All Books")
        if not library.books:
            print("No books available yet.")
        else:
            for index, book in enumerate(library.books, 1):
                print(f"{index}. {book}")
        input("\nPress Enter to go back to menu...")

    elif choice == '6':
        print_header("🔍 Search Books")
        keyword = input("Enter book title or author: ")
        results = library.search_books(keyword)

        if results:
            print("\n✅ Search Results:\n")
            for index, book in enumerate(results, 1):
                print(f"{index}. {book}")
        else:
            print("\n⚠️ No books found matching your search.")

        input("\nPress Enter to return to menu...")



    elif choice == '7':

        print_header("Goodbye! 👋")

        break

