🎓 Kryos Student Manager

A robust command-line Student Management System built with Python.

This project demonstrates practical use of file handling, JSON data storage, logging, exception handling, input validation, and CRUD operations. It allows users to efficiently manage student records through an interactive terminal interface.

---

🚀 Features

Student Management

- Add new students
- View all students
- Search students by name
- Delete students from the register

JSON-Based Storage

- Persistent data storage using JSON
- Automatic data loading on startup
- Human-readable JSON formatting

Input Validation

- Prevents empty names
- Validates name format
- Prevents duplicate student records
- Prevents negative values
- Validates age range
- Restricts scores to valid limits

Logging System

- Console logging for user feedback
- File logging for error tracking
- Timestamped log records
- Critical error reporting

Error Handling

- Handles missing files safely
- Handles corrupted JSON files
- Handles invalid user input
- Gracefully exits on unexpected errors
- Supports safe termination with Ctrl + C

Student Ranking

- Sorts students by score (highest first)
- Uses alphabetical sorting when scores are equal

---

🛠 Technologies Used

- Python 3
- JSON
- Logging
- Exception Handling
- File Handling

---

📂 Project Structure

python-learning-journey/
│
└── python_projects/
    │
    └── student_manager/
        │
        ├── student_manager.py
        ├── students_info.json
        ├── students.log
        └── README.md

---

▶️ How to Run

1. Clone the Repository

git clone https://github.com/behruz-hojaniyazow/python-learning-journey.git

2. Navigate to the Project Folder

cd python-learning-journey/python_projects/student_manager

3. Run the Application

python student_manager.py

---

📋 Menu Options

1 -> Add Student
2 -> Show Student
3 -> Search Student
4 -> Delete Student
5 -> Exit App

---

📄 Example Student Record

{
    "name": "John",
    "age": 18,
    "score": 95
}

---

🔒 Reliability Features

- Duplicate student detection
- Data validation
- Structured logging
- Persistent JSON storage
- Exception handling
- Safe program termination

---

🎯 Concepts Practiced

This project demonstrates practical experience with:

- Functions
- Loops
- Dictionaries
- Lists
- JSON Storage
- Logging
- Exception Handling
- Input Validation
- CRUD Operations
- Clean Code Principles

---

📈 Future Improvements

- Type Hints
- Object-Oriented Programming (OOP)
- Dataclasses
- SQLite Integration
- Unit Testing
- CSV Export
- Student Record Updates
- GUI Version (Tkinter)
- REST API Version (Flask/FastAPI)

---

👨‍💻 Author

Behruz Hojaniyazow

Python Developer | Learning by Building Real Projects 🚀

GitHub: https://github.com/behruz-hojaniyazow