# 💎 Kryos Student Manager System

A console-based, object-oriented **Student Management System** built in
Python. Kryos lets you register, search, list, and remove students from a
class register, with strict data validation, structured logging, and a
clean layered architecture that separates presentation, business logic,
validation, and persistence concerns.

> Repository: [`Behruz-Hojaniyazow/python-learning-journey`](https://github.com/Behruz-Hojaniyazow/python-learning-journey)
> Path: `python_projects/student_manager`

---

## ✨ Features

- **Add students** — interactively register students with name, age, and
  score, with live input validation and clear, emoji-annotated feedback.
- **View students** — display every registered student in a neatly
  aligned table, automatically ranked by score (highest first, name as a
  tiebreaker).
- **Search students** — case-insensitive, partial-name search that can
  return one or many matching records.
- **Delete students** — safe deletion flow with disambiguation for
  multiple matches and an explicit `yes`/`no` confirmation step before
  any data is removed.
- **Robust validation** — centralized, reusable rules ensure names
  contain only letters, ages fall within a sane human range, and scores
  fall within `0–100`.
- **Structured logging** — every meaningful event (successful actions,
  validation failures, duplicate detection, system errors) is logged to
  both the console and a rotating log file with full context (timestamp,
  source file, line number).
- **Graceful shutdown** — handles `Ctrl+C` interruptions and unexpected
  critical errors cleanly, without ever crashing with a raw traceback in
  front of the user.
- **Persistent storage** — all data is stored locally in a human-readable
  JSON file, so the class register survives between sessions.

---

## 🏗️ Architecture

Kryos follows a layered, single-responsibility design. Each file owns
exactly one concern, which makes the codebase easy to test, extend, and
reason about:

```
┌─────────────────────────────────────────────────────────┐
│                        main.py                           │
│         (Presentation layer — console UI & menu)         │
└───────────────────────────┬───────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────┐
│                    student_service.py                     │
│   (Business logic — orchestrates validation + storage)    │
└───────────┬────────────────────────────────┬──────────────┘
            │                                │
┌───────────▼──────────────┐    ┌────────────▼──────────────┐
│      validators.py        │    │        storage.py          │
│ (Input sanitation & rules)│    │  (JSON file persistence)   │
└────────────────────────────┘    └─────────────────────────────┘
            │                                │
┌───────────▼────────────────────────────────▼──────────────┐
│              config.py         status.py                  │
│      (Constants & settings)   (Result/status enum)        │
└─────────────────────────────────────────────────────────────┘
                            │
                  ┌─────────▼─────────┐
                  │  logger_config.py  │
                  │ (Shared logging)   │
                  └────────────────────┘
```

### Design principles applied

- **Separation of Concerns** — the UI never touches storage directly,
  and the storage layer never contains business rules.
- **Single Source of Truth for Outcomes** — every operation communicates
  its result through the `StudentStatus` enum rather than booleans,
  strings, or exceptions, keeping the contract between layers explicit
  and type-safe.
- **Fail-safe persistence** — the storage layer never raises an
  exception to its caller; every failure mode is caught, logged, and
  converted into a safe return value.
- **Dependency composition over inheritance** — `StudentService` is
  composed of a `JSONStudentStorage` instance and delegates to
  `StudentValidator`'s static methods, keeping each class small and
  focused.

---

## 📁 Project Structure

```
student_manager/
├── main.py              # Entry point & console UI (menu, prompts, output)
├── student_service.py   # Business logic: add / get / search / delete students
├── validators.py        # Static validation rules for name, age, and score
├── storage.py           # JSON file read/write persistence layer
├── config.py            # Centralized constants (file paths, log formats, limits)
├── status.py             # StudentStatus enum — all possible operation outcomes
├── logger_config.py      # Shared logger factory (file + console handlers)
└── README.md              # Project documentation (this file)
```

---

## ⚙️ Requirements

- Python **3.8+** (no third-party dependencies — the standard library is
  sufficient: `json`, `logging`, `enum`, `sys`).

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Behruz-Hojaniyazow/python-learning-journey.git
   cd python-learning-journey/python_projects/student_manager
   ```
2. Run the application:
   ```bash
   python main.py
   ```
3. Follow the on-screen menu to add, view, search for, or delete
   students. Type `stop` at any input prompt to cancel the current
   operation and return to the main menu.

On first run, a `students_info.json` file will be created automatically
in the working directory to store your class register, alongside a
`students.log` file that records error and critical-level events.

---

## 🖥️ Usage Example

```
==============================================
💎 Welcome to the Kryos Student Manager System!
----------------------------------------------
1 -> Add Student
2 -> Show Student
3 -> Search Student
4 -> Delete Student
5 -> Exit App
==============================================

Choose an Action: 1

--- 📁 Adding Students 📁 ---

Type 'stop' to stop adding students

[+] Requesting details for the 1st student...
--> Please enter the required information below:
Name: John Smith
Age: 21
Score: 95
✅ The student has been added successfully
```

---

## ✅ Validation Rules

| Field | Rule |
|-------|------|
| **Name** | Must not be empty; must consist only of letters (spaces, hyphens, and apostrophes are permitted as separators). |
| **Age**  | Must not be empty; must be a valid integer strictly greater than `MIN_AGE` (0) and no greater than `MAX_AGE` (120). |
| **Score**| Must not be empty; must be a valid number between `MIN_SCORE` (0) and `MAX_SCORE` (100) inclusive. Whole-number scores are stored as integers. |

All limits are defined centrally in `config.py` and can be adjusted
without touching any validation logic.

---

## 📊 Status & Error Handling

Every operation in the service layer returns a member of the
`StudentStatus` enum (defined in `status.py`), which the UI layer maps to
a clear, user-facing message:

| Status | Meaning |
|--------|---------|
| `SUCCESS` | The operation completed successfully. |
| `SAVE_ERROR` | A system-level failure occurred while writing to storage. |
| `EMPTY_NAME` / `EMPTY_AGE` / `EMPTY_SCORE` | The corresponding field was left blank. |
| `INVALID_NAME_FORMAT` / `INVALID_AGE_FORMAT` / `INVALID_SCORE_FORMAT` | The corresponding field contains characters that cannot be parsed. |
| `AGE_TOO_LOW` / `AGE_TOO_HIGH` | The age falls outside the accepted range. |
| `INVALID_SCORE_RANGE` | The score falls outside `0–100`. |
| `DUPLICATE_NAME` | A student with the same name already exists. |
| `NOT_FOUND` | No student matched the given search/delete criteria. |

This pattern keeps business logic fully decoupled from presentation —
`student_service.py` never prints anything or knows how a result will be
displayed.

---

## 📝 Logging

Logging is configured once in `logger_config.py` and shared across the
entire application via `get_logger()`:

- **Console output** — all levels (`DEBUG` and above), formatted concisely
  as `LEVEL: message`, for real-time visibility during use.
- **File output** (`students.log`) — `ERROR` and `CRITICAL` levels only,
  formatted with a full timestamp, logger name, source file, and line
  number, for later diagnosis of serious failures.

---

## 🧑‍💻 Author

**Behruz Hojaniyazow**
GitHub: [@Behruz-Hojaniyazow](https://github.com/Behruz-Hojaniyazow)
Repository: [python-learning-journey](https://github.com/Behruz-Hojaniyazow/python-learning-journey)

This project is part of an ongoing personal journey to master
professional, production-grade Python — practicing OOP design, clean
architecture, input validation, structured logging, and comprehensive
documentation.

---

## 📄 License

This project is shared for educational purposes as part of the
`python-learning-journey` repository. Feel free to explore, learn from,
and adapt the code.
