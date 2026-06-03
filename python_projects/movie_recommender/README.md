🎬 KRYOS Movie Recommender

A command-line movie recommendation and management system built with Python.

This application allows users to discover movies, manage movie collections, search for titles, organize genres, and store data permanently using JSON files.

The project was created as part of a Python learning journey focused on real-world software development concepts such as JSON handling, logging, validation, exception handling, and CRUD operations.

---

🚀 Features

🎲 Movie Recommendations

- Random movie recommendations
- Genre-based recommendations
- Dynamic genre selection

➕ Add Movies

- Add movies to existing genres
- Create entirely new genres
- Automatic JSON persistence

🔍 Search Movies

- Search movies by title
- Case-insensitive search

🗑 Delete Movies

- Delete movies safely
- Confirmation before deletion

📋 Show Movies

- Display all available genres
- Display all movies within each genre
- Movie counting per genre

💾 Data Persistence

- Automatic JSON storage
- Data remains after application restart

📝 Logging System

- Console logging
- File logging
- Error tracking
- Critical failure tracking

⚠️ Error Handling

- Missing JSON files
- Corrupted JSON files
- File I/O errors
- Unexpected exceptions
- KeyboardInterrupt support

---

🛠 Technologies Used

- Python 3
- JSON
- Logging
- Random Module
- Dictionaries
- Lists
- Functions
- Loops
- Exception Handling
- File Handling

---

📂 Project Structure

movie_recommender/
│
├── movie_recommender.py
├── movies.json
├── movies_app.log
└── README.md

---

📦 Movie Database Structure

Movies are stored inside a JSON file using the following format:

{
    "action": [
        "John Wick",
        "Extraction"
    ],
    "comedy": [
        "Mr Bean",
        "Home Alone"
    ]
}

---

🎯 Available Genres

Default genres include:

- Action
- Comedy
- Horror
- Drama
- Sci-Fi

Users can also create their own genres.

---

📋 Menu Options

1 -> Recommend Movie
2 -> Add Movie
3 -> Search Movie
4 -> Delete Movie
5 -> Show Movies
6 -> Exit App

---

🔒 Validation Rules

Genre Validation

- Genre name cannot be empty
- Duplicate genres are not allowed

Movie Validation

- Movie title cannot be empty
- Duplicate movies are not allowed

---

📝 Logging

The application uses Python's logging module.

Log Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Log File

movies_app.log

Logged Events

- Movie recommendations
- Movie additions
- Movie deletions
- Search operations
- Invalid user input
- JSON errors
- Critical system failures

---

⚠️ Error Recovery

The application safely handles:

- Missing JSON files
- Invalid JSON structure
- File access errors
- Unexpected runtime errors
- User interruption (Ctrl + C)

---

▶️ How To Run

python movie_recommender.py

---

📸 Example

===================================
Welcome to Kryos Movie Program
===================================

1 -> Recommend Movie
2 -> Add Movie
3 -> Search Movie
4 -> Delete Movie
5 -> Show Movies
6 -> Exit App

---

📚 Concepts Practiced

This project demonstrates:

- CRUD Operations
- JSON Storage
- Logging
- Exception Handling
- Random Selection
- Data Validation
- Clean Functions
- Persistent Storage
- Command Line Applications

---

🔮 Future Improvements

- Update/Edit Movies
- Favorites System
- Movie Ratings
- Watch History
- SQLite Database Integration
- OOP Refactor
- Unit Testing
- Search by Genre
- Export Movie Lists

---

👨‍💻 Author

Behruz

Built as part of a Python programming learning journey focused on creating practical projects and improving software development skills.