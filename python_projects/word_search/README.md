🎯 Kryos Word Guessing Game

A console-based Word Guessing Game built with Python using a clean modular architecture, input validation, logging, and error handling.

📖 Overview

Kryos Word Guessing Game is an interactive terminal game where the computer randomly selects an English word and the player attempts to guess it one letter at a time.

The project was designed to practice:

- Python functions
- Modular programming
- Input validation
- Logging
- Error handling
- Dictionaries and sets
- Clean project structure
- Professional code organization

---

🚀 Features

🎲 Random Word Selection

The game randomly chooses a word from a predefined English word list.

🔍 Letter Guessing System

Players guess one letter at a time until the entire word is revealed.

✅ Input Validation

The program validates user input and prevents invalid entries.

🔄 Duplicate Letter Detection

Previously entered letters are detected and rejected.

📊 Attempt Counter

The game tracks the number of attempts made by the player.

📝 Logging System

Important events are recorded using Python's logging module.

Examples:

- Game started
- Correct guesses
- Incorrect guesses
- Validation errors
- Game completion
- Application exit

🛑 Stop Command

Players can exit the current game at any time using the configured stop command.

🎮 Interactive Menu

A simple menu system allows users to:

1. Start a new game
2. Exit the application

⚠️ Error Handling

The application includes graceful handling of:

- Invalid input
- KeyboardInterrupt (Ctrl + C)
- Unexpected runtime errors

---

📁 Project Structure

word_guessing_game/
│
├── main.py
├── word_service.py
├── english_words.py
├── validator.py
├── logger_config.py
├── config.py
└── README.md

File Descriptions

File| Purpose
main.py| Application entry point and menu system
word_service.py| Core game logic
english_words.py| Word database creation
validator.py| User input validation
logger_config.py| Logging configuration
config.py| Application constants and settings

---

🛠️ Technologies Used

- Python 3
- Logging Module
- Random Module

---

▶️ How to Run

python main.py

---

🎯 Learning Objectives

This project demonstrates:

- Modular software design
- Separation of concerns
- Clean code principles
- Function-based architecture
- Input validation techniques
- Logging best practices
- Error handling strategies

---

📷 Example Gameplay

I have chosen a word.
Can you guess it?

Word: _ _ _ _ _

ATTEMPT - 1
Enter a letter: A

'A' letter is correct!

Word: A _ _ _ _

---

🔮 Future Improvements

- Difficulty levels
- Categories of words
- Score system
- Leaderboard
- Save game feature
- Hint system
- Multiplayer mode

---

👨‍💻 Author

Behruz Hojaniyazow

GitHub:
https://github.com/Behruz-Hojaniyazow

---

📄 License

This project is open-source and available for educational purposes.