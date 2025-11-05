# 📚 Library Management System (Python OOP)

A clean and well-structured **Library Management System** built using **Object-Oriented Programming in Python**, with **persistent data storage** using JSON.  
This project demonstrates real-world application of classes, objects, encapsulation, inheritance concepts, and clean code design.

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| Add Books | Store book information (title, author, ISBN) |
| Register Users | Add library members |
| Borrow Books | Tracks borrowed books and availability |
| Return Books | Updates records when books are returned |
| Search Books | Search by title or author keyword |
| JSON Data Storage | Data stays saved even after closing program |
| Borrow Limits | Users can borrow up to 3 books |
| Borrow & Due Dates | Automatically sets a 14-day due date |

---

## 🏗️ Project Structure

library-management-system/
│
├── book.py # Book class with due date tracking
├── user.py # User class with borrow limit
├── library.py # Core library logic + JSON save/load
├── main.py # Menu UI / Program entry point
└── library_data.json # Persistent storage

yaml
Copy code

---

## ▶️ How to Run

1. Install Python 3.8+
2. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/library-management-system.git
Navigate into project:

bash
Copy code
cd library-management-system
Run the program:

bash
Copy code
python main.py
🔧 Future Enhancements (Planned)
Late return fines

GUI using Tkinter / PyQt

Web version (Flask or FastAPI)

User login system

🤝 Contributing
Pull requests are welcome!
If you'd like to help improve features or add UI, feel free to open an issue.

📜 License
This project is open-source under the MIT License.

⭐ If you found this project helpful, consider giving the repo a Star!
yaml
Copy code

---

## 🎉 After you commit README.md
Run:

```bash
git add README.md
git commit -m "Added professional README"
git push