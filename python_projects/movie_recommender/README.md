🎬 Movie Recommender

A modular Python CLI application for managing and discovering movies.

This project allows users to add, search, delete, display, and get movie recommendations from a categorized movie database. The application stores data in JSON format and includes validation, logging, and a clean modular architecture.

---

🚀 Features

- 🎲 Random movie recommendations by genre
- ➕ Add new movies
- 🔍 Search for movies
- ❌ Delete existing movies
- 📋 Display all movies by category
- 💾 Persistent JSON storage
- ✅ Input validation
- 📝 Logging system for debugging and monitoring
- 🏗️ Modular project architecture

---

📂 Project Structure

movie_recommender/
│
├── main.py               # Application entry point
├── movie_service.py      # Core business logic
├── storage.py            # JSON file handling
├── validators.py         # Input validation functions
├── logger_config.py      # Logging configuration
├── config.py             # Project configuration constants
├── movies.json           # Movie database
├── movies_app.log        # Log file
└── README.md

---

🏛️ Architecture

The project follows a modular design where each file has a single responsibility:

config.py

Stores project-wide constants such as:

- JSON file name
- Log file name
- Logger name

logger_config.py

Creates and configures the application logger.

storage.py

Handles:

- Loading movie data
- Saving movie data
- Creating default movie collections

validators.py

Responsible for:

- Movie name validation
- Genre validation
- Duplicate movie detection
- Duplicate genre detection

movie_service.py

Contains the application's business logic:

- Recommend movies
- Add movies
- Search movies
- Delete movies
- Display movies

main.py

Acts as the application's entry point and menu controller.

---

⚙️ Installation

Clone the repository:

git clone https://github.com/Behruz-Hojaniyazow/python-learning-journey.git

cd python-learning-journey

Run the application:

python main.py

---

📖 Usage

After launching the application, choose one of the available menu options:

1. Recommend Movie
2. Add Movie
3. Search Movie
4. Delete Movie
5. Show Movies
6. Exit

---

📝 Logging

The application uses Python's built-in logging module.

Logs are written to:

movies_app.log

The logger records:

- Application events
- Warnings
- Errors
- Unexpected exceptions

---

💾 Data Storage

Movies are stored in:

movies.json

Example structure:

{
  "Action": [
    "John Wick",
    "Mad Max"
  ],
  "Comedy": [
    "The Mask",
    "Superbad"
  ]
}

---

🛠️ Technologies Used

- Python 3
- JSON
- Logging Module
- Modular Programming Principles

---

🎯 Learning Goals

This project was originally built as a single-file application and later refactored into a modular architecture to improve:

- Maintainability
- Readability
- Scalability
- Separation of concerns
- Code organization

---

📈 Future Improvements

- Type hints
- Unit testing with pytest
- Object-oriented architecture
- Database integration (SQLite/PostgreSQL)
- GUI version
- Web version using Flask or Django

---

## 👨‍💻 Author

Behruz

- Python Developer
- Learning Software Engineering
- Building projects with Python