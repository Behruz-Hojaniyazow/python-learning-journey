📖 KRYOS Contact Book

A modular command-line Contact Book application built with Python.

This project allows users to store, search, display, and delete contacts while persisting data in a JSON file. The application follows a modular architecture with separate modules for business logic, storage, validation, configuration, and logging.

---

✨ Features

- Add new contacts
- Display all contacts
- Search contacts by name
- Delete contacts
- Prevent duplicate contact names
- Prevent duplicate phone numbers
- Validate user input
- Persistent JSON storage
- Professional logging system
- Modular and maintainable code structure

---

📂 Project Structure

contact_book/
│
├── config.py
├── contact_service.py
├── logger_config.py
├── main.py
├── storage.py
├── validators.py
├── contacts_info.json
├── app.log
└── README.md

Module Overview

"main.py"

Application entry point.

Responsibilities:

- Display menu
- Handle user choices
- Route actions to service functions
- Handle global exceptions

---

"contact_service.py"

Contains the application's core business logic.

Responsibilities:

- Add contacts
- Show contacts
- Search contacts
- Delete contacts
- Exit application

---

"storage.py"

Handles data persistence.

Responsibilities:

- Load contacts from JSON
- Save contacts to JSON
- Handle storage-related exceptions

---

"validators.py"

Contains input validation logic.

Responsibilities:

- Validate contact names
- Validate phone numbers
- Return validation results and error messages

---

"logger_config.py"

Configures the logging system.

Responsibilities:

- Create logger instance
- Configure file handler
- Configure console handler
- Apply logging formatters

---

"config.py"

Stores application-wide constants.

Responsibilities:

- JSON file configuration
- Log file configuration
- Logger configuration

---

📝 Contact Data Format

Contacts are stored inside:

contacts_info.json

Example:

[
    {
        "name": "John",
        "phone": "+1234567890"
    },
    {
        "name": "Alice",
        "phone": "+998901234567"
    }
]

---

📊 Logging

The application uses Python's built-in logging module.

Console logs:

INFO: New contact was saved successfully
WARNING: Contact creation failed

File logs ("app.log"):

[2025-08-24 15:00:00] ERROR [ContactBook:storage.py:42] Invalid JSON format

---

🚀 How to Run

Navigate to the project directory:

cd contact_book

Run the application:

python main.py

---

🛡 Validation Rules

Name Validation

- Cannot be empty

Phone Validation

- Cannot be empty
- Must start with "+"
- Must contain digits only after "+"
- Must be longer than 8 digits

Examples:

✅ Valid

+998901234567

❌ Invalid

998901234567
+99890ABC123
+123

---

🔧 Technologies Used

- Python 3
- JSON
- Logging Module
- File Handling
- Modular Programming

---

📈 Future Improvements

Possible future enhancements:

- Update contact information
- Export contacts to CSV
- Import contacts from CSV
- Contact categories
- Favorite contacts
- Pagination for large contact lists
- Unit testing
- Search by phone number

---

👨‍💻 Author

Behruz

Aspiring Python Developer focused on writing clean, modular, and maintainable code.

---

📄 License

This project is open-source and available for learning and educational purposes.