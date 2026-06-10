🎓 Kryos Student Manager

A modular command-line Student Management System built with Python.

This project allows users to manage student records through a clean and structured CLI interface. Student data is stored in JSON format, validated before processing, and managed through a modular architecture that separates business logic, storage, validation, configuration, and logging.

---

✨ Features

- Add new students
- Display all students in a formatted table
- Search students by name
- Delete existing students
- Persistent JSON data storage
- Input validation for names, ages, and scores
- Duplicate student detection
- Centralized logging system
- Graceful application shutdown
- Modular and maintainable project structure

---

🏗️ Project Architecture

The project follows a modular design to improve readability, maintainability, and scalability.

student_manager/
│
├── main.py
├── config.py
├── logger_config.py
├── storage.py
├── validators.py
├── student_service.py
├── students_info.json
├── students.log
└── README.md

Module Responsibilities

Module| Responsibility
"main.py"| Application entry point and menu system
"config.py"| Centralized configuration values
"logger_config.py"| Logging configuration
"storage.py"| JSON file operations
"validators.py"| Input validation logic
"student_service.py"| Core business logic
"students_info.json"| Student database
"students.log"| Error and activity logs

---

🚀 Getting Started

Clone the Repository

git clone https://github.com/behruz-hojaniyazow/python-learning-journey.git

cd python-learning-journey

Run the Application

python main.py

---

📋 Example Menu

==============================================
💎 Welcome to the Kryos Student Manager System!
----------------------------------------------
1 -> Add Student
2 -> Show Student
3 -> Search Student
4 -> Delete Student
5 -> Exit App
==============================================

---

🛡️ Validation Rules

Name Validation

- Cannot be empty
- Cannot contain only spaces
- Supports alphabetic names
- Supports spaces, apostrophes, and hyphens

Examples:

John Smith
Anne-Marie
O'Connor

Age Validation

- Must be an integer
- Must be greater than 0
- Maximum allowed age: 120

Score Validation

- Must be numeric
- Must be between 0 and 100

---

📝 Logging

The application uses Python's built-in logging module.

Console Logs

Used for runtime information and warnings.

File Logs

Stored in:

students.log

The log file records:

- Errors
- Critical failures
- Unexpected exceptions

---

💾 Data Storage

Student records are stored in JSON format.

Example:

[
    {
        "name": "John Smith",
        "age": 18,
        "score": 92
    },
    {
        "name": "Emma Brown",
        "age": 19,
        "score": 88
    }
]

---

🔧 Technologies Used

- Python 3
- JSON
- Logging Module
- Modular Programming
- File Handling
- Exception Handling

---

📚 What I Learned

This project helped me practice:

- Python modular architecture
- Separation of concerns
- Data validation
- Logging systems
- Exception handling
- JSON data persistence
- Clean code principles
- CLI application development

---

🔮 Future Improvements

- Update student information
- Export data to CSV
- Unit testing
- Object-Oriented Programming (OOP) version
- Database integration (SQLite/PostgreSQL)
- Graphical User Interface (GUI)

## 👨‍💻 Author

Behruz

- Python Developer
- Learning Software Engineering
- Building projects with Python

---

📄 License

This project is created for educational and portfolio purposes.