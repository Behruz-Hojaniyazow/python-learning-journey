📖 KRYOS Contact Book

A simple yet powerful command-line Contact Book application built with Python.

This project allows users to manage contacts efficiently using a JSON-based storage system. It includes contact creation, searching, deletion, data persistence, logging, validation, error handling, and graceful application shutdown.

---

🚀 Features

- ➕ Add new contacts
- 📋 Display all contacts
- 🔍 Search contacts by name
- 🗑️ Delete contacts
- 💾 Automatic JSON data storage
- 🚫 Duplicate contact prevention
- 🚫 Duplicate phone number prevention
- ☎️ International phone number validation ("+998901234567")
- 🔤 Alphabetical contact sorting
- 📝 Logging system
- ⚠️ Error handling and recovery
- 🛑 Graceful application shutdown
- 📂 Persistent data storage

---

🛠 Technologies Used

- Python 3
- JSON
- Logging Module
- File Handling
- Functions
- Loops
- Dictionaries
- Lists
- Exception Handling

---

📂 Project Structure

contact_book/
│
├── contact_book.py
├── contacts_info.json
├── app.log
└── README.md

---

📌 Contact Data Structure

Each contact is stored as a dictionary:

{
    "name": "John Doe",
    "phone": "+998901234567"
}

All contacts are stored inside a JSON file.

---

🔒 Validation Rules

Name Validation

- Name cannot be empty.

Phone Number Validation

- Must start with "+"
- Must contain only digits after "+"
- Must be longer than 8 characters
- Duplicate phone numbers are not allowed

Examples:

✅ Valid

+998901234567
+447123456789
+12025550123

❌ Invalid

998901234567
+99890abc123
+123

---

📋 Menu Options

1 -> Add Contact
2 -> Show Contacts
3 -> Search Contacts
4 -> Delete Contact
5 -> Exit App

---

📝 Logging System

The application uses Python's logging module.

Log Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Logged Events

- Contact creation
- Contact deletion
- Search operations
- Invalid user input
- JSON errors
- File errors
- Critical system failures

Log records are automatically written to:

app.log

---

⚠️ Error Handling

The application safely handles:

- Missing JSON files
- Invalid JSON format
- File I/O errors
- Unexpected exceptions
- KeyboardInterrupt ("Ctrl + C")

This prevents the program from crashing unexpectedly.

---

💾 Data Persistence

Contacts are automatically saved after:

- Adding a contact
- Deleting a contact

Data remains available after restarting the application.

---

🎯 Learning Objectives

This project was built to practice:

- Functions
- JSON handling
- File operations
- Logging
- Exception handling
- CRUD operations
- Data validation
- Python project structure
- Clean code principles

---

▶️ How To Run

python contact_book.py

---

📸 Example

========================================
Welcome to KRYOS Contact Book!
----------------------------------------
1 -> Add Contact
2 -> Show Contacts
3 -> Search Contacts
4 -> Delete Contact
5 -> Exit App
========================================

---

📈 Future Improvements

- Update/Edit Contact
- Export Contacts
- Import Contacts
- Contact Categories
- Favorites System
- SQLite Database Support
- Object-Oriented Refactor (OOP)
- Unit Testing

---

👨‍💻 Author

Behruz

Built as part of a Python learning journey focused on writing real-world projects and improving software development skills.

---

# 📜 License

This project is open-source and available for learning and educational purposes.