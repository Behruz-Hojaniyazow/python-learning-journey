🎓 Kryos Student Manager

A professional command-line Student Management System built with Python.

This project allows users to manage student records efficiently using JSON-based data storage, input validation, structured logging, and robust error handling.

---

🚀 Features

📌 Student Management

- Add new students
- View all students
- Search for students by name
- Delete students from the register

📌 Data Persistence

- Stores student data in a JSON file
- Automatically loads saved data when the program starts
- Human-readable JSON formatting

📌 Input Validation

- Prevents empty names
- Prevents invalid name formats
- Prevents duplicate student records
- Prevents negative values
- Validates age range
- Ensures scores remain within the allowed range

📌 Logging System

- Console logging for user feedback
- File logging for system errors
- Error tracking with timestamps
- Critical error reporting

📌 Error Handling

- Handles missing files safely
- Handles corrupted JSON files
- Handles invalid user input
- Gracefully exits on unexpected errors
- Supports safe interruption using Ctrl + C

📌 Student Ranking

- Automatically sorts students by score
- Displays students in descending order
- Alphabetical sorting when scores are equal

---

🛠 Technologies Used

- Python 3
- JSON
- Logging Module
- Exception Handling
- File Handling

---

📂 Project Structure

project/
│
├── main.py
├── students_info.json
├── students.log
└── README.md

---

▶️ How to Run

1. Clone the repository

git clone https://github.com/your-username/kryos-student-manager.git

2. Navigate to the project directory

cd kryos-student-manager

3. Run the program

python main.py

---

📋 Menu Options

1 -> Add Student
2 -> Show Student
3 -> Search Student
4 -> Delete Student
5 -> Exit App

---

💡 Example Student Record

{
    "name": "John",
    "age": 18,
    "score": 95
}

---

🔒 Reliability Features

- Duplicate detection
- Data validation
- Structured logging
- Persistent storage
- Exception handling
- Safe program termination

---

🎯 Learning Objectives

This project demonstrates practical usage of:

- Functions
- Loops
- Dictionaries
- Lists
- JSON storage
- Logging
- Exception handling
- Input validation
- CRUD operations
- Clean code practices

---

📈 Future Improvements

- Type Hints
- Object-Oriented Programming (OOP)
- SQLite Database Integration
- Unit Testing
- Export to CSV
- Update Student Records
- GUI Version (Tkinter/PyQt)
- REST API Version (Flask/FastAPI)

---

👨‍💻 Author

Behruz

Python Developer in Progress 🚀