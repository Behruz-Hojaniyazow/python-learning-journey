# 📇 KRYOS Contact Book Manager

A clean, console-based **Contact Book** application written in Python. It follows a layered architecture (UI → Service → Storage) with centralized logging, input validation, and persistent JSON storage — making it easy to maintain, test, and extend.

---

## ✨ Features

- ➕ **Add contacts** with name and phone number validation
- 📋 **List all contacts**, sorted alphabetically by name
- 🔍 **Search contacts** by partial or full name match
- 🗑️ **Delete contacts**, with confirmation and disambiguation when multiple matches are found
- 🧠 **Duplicate detection** for both names and phone numbers
- 💾 **Persistent storage** in a human-readable JSON file
- 🪵 **Structured logging** to both console and file (`app.log`)
- 🛡️ **Graceful error handling**, including safe shutdown on `Ctrl+C`

---

## 🗂️ Project Structure

```
contact_book/
│
├── main.py              # Entry point — CLI menu and user interaction
├── contact_service.py   # Business logic layer (ContactService, ContactStatus)
├── storage.py           # Data persistence layer (JSONContactStorage)
├── validators.py        # Input validation logic (InputValidator)
├── logger_config.py     # Centralized logger configuration
├── config.py            # Application-wide constants
│
├── contacts_info.json   # Auto-generated data file (contact storage)
├── app.log              # Auto-generated log file
└── README.md
```

---

## 🏗️ Architecture

The project follows a simple **separation of concerns** design:

```
┌─────────────┐      ┌──────────────────┐      ┌────────────────────┐
│   main.py   │ ───► │ contact_service.py│ ───► │     storage.py     │
│ (UI / CLI)  │      │ (business logic)  │      │ (JSON persistence) │
└─────────────┘      └──────────────────┘      └────────────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │ validators.py│
                       └──────────────┘

              All layers share a common logger from logger_config.py
```

- **`main.py`** never touches the JSON file directly — it only calls `ContactService` methods and reacts to the returned `ContactStatus`.
- **`ContactService`** contains all business rules (validation, duplicate checks, status reporting) and delegates raw read/write operations to `JSONContactStorage`.
- **`JSONContactStorage`** is solely responsible for reading and writing `contacts_info.json`, with robust exception handling.
- **`InputValidator`** provides static, reusable validation methods with no side effects.
- **`logger_config.py`** exposes a single `get_logger()` function so every module logs through the same configured logger instance.

---

## ⚙️ Requirements

- Python **3.8+** (uses `enum.auto`, f-strings, and type hints)
- No external dependencies — the project relies only on the Python standard library (`json`, `logging`, `enum`, `sys`)

---

## 🚀 Installation & Usage

1. Clone or download the project folder:

   ```bash
   git clone https://github.com/Behruz-Hojaniyazow/python-learning-journey.git
   cd python-learning-journey/python_projects/contact_book
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Use the on-screen menu to navigate:
   ```
   ========================================
      Welcome to KRYOS Contact Book!
   ----------------------------------------
   1 -> Add Contact
   2 -> Show Contacts
   3 -> Search Contacts
   4 -> Delete Contacts
   5 -> Exit app
   ========================================

   Choose an action:
   ```

4. Type `stop` at any prompt (Add / Search / Delete) to return to the main menu.

---

## 📱 Phone Number Rules

A phone number is considered valid only if it meets **all** of the following:

| Rule | Example (valid) | Example (invalid) |
|------|------------------|--------------------|
| Must not be empty | `+998901234567` | *(empty string)* |
| Must start with `+` | `+998901234567` | `998901234567` |
| Only digits allowed after `+` | `+998901234567` | `+99890abc4567` |
| Must be **longer than 8 characters** (including `+`) | `+998901234567` | `+1234567` |

---

## 💾 Data Storage Format

Contacts are stored in `contacts_info.json` as a list of objects:

```json
[
    {
        "name": "John Doe",
        "phone": "+998901234567"
    },
    {
        "name": "Jane Smith",
        "phone": "+15551234567"
    }
]
```

- The file is created automatically on the first successful `save_contacts()` call.
- If the file doesn't exist yet, `load_contacts()` safely returns an empty list instead of raising an error.
- If the JSON file becomes corrupted, the error is logged at `ERROR` level and an empty list is returned instead of crashing the app.

---

## 🪵 Logging

Logging is centralized through `logger_config.get_logger()` and writes to **two destinations**:

| Handler | Level | Destination | Purpose |
|---------|-------|-------------|---------|
| Console Handler | `INFO` and above | Terminal | Real-time feedback for the user/developer |
| File Handler | `ERROR` and above | `app.log` | Persistent record of errors and critical failures for later analysis |

Log format used in `app.log`:
```
[2026-07-12 14:32:10,123] ERROR [ContactBook:storage.py:60] - File error - [Errno 13] Permission denied
```

---

## 🧾 Status Codes (`ContactStatus`)

All service-layer methods return a `ContactStatus` enum value so the UI layer can react appropriately without parsing strings:

| Status | Meaning |
|--------|---------|
| `SUCCESS` | Operation completed successfully |
| `EMPTY_NAME` | Name field was left blank |
| `DUPLICATE_NAME` | A contact with this name already exists |
| `DUPLICATE_PHONE` | A contact with this phone number already exists |
| `INVALID_PHONE` | Phone number failed validation rules |
| `SAVE_ERROR` | Failed to write data to the storage file |
| `NOT_FOUND` | No matching contact was found (search/delete) |

---

## 🛡️ Error Handling

- **`KeyboardInterrupt` (Ctrl+C):** The application exits gracefully with a friendly message instead of printing a traceback.
- **Unexpected exceptions:** Caught at the top level in `main()`, logged as `CRITICAL` with full traceback (`exc_info=True`), and the user is shown a generic, non-technical error message before the app exits.
- **File I/O errors:** Handled explicitly in `storage.py` (`FileNotFoundError`, `json.JSONDecodeError`, `IOError`), each logged with appropriate context.

---

## 🗺️ Roadmap Ideas

- [ ] Add contact editing (update name/phone of an existing contact)
- [ ] Export/import contacts to/from CSV
- [ ] Add unit tests for `validators.py` and `contact_service.py`
- [ ] Support multiple phone numbers per contact
- [ ] Add a configuration option to change log level via `config.py`

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**KRYOS Contact Book Manager** — built with a focus on clean architecture, robust validation, and reliable logging.
