# 🎓 Student Manager System

A simple and beginner-friendly terminal-based Python application for managing student records.

This project allows users to:

- Add students
- View all students
- Delete students
- Save student information into a text file
- Read saved student records from a file

The project was built to practice Python fundamentals, clean code structure, file handling, and exception handling.

---

# 🚀 Features

✅ Add new students to the class register  
✅ Display all students in a clean formatted table  
✅ Delete students with confirmation system  
✅ Save student records into a `.txt` file  
✅ Read saved student records from another Python file  
✅ Handles file errors using `try-except`  
✅ Prevents empty input values  
✅ Clean and readable terminal output  
✅ Beginner-friendly project structure  

---

# 🛠️ Technologies Used

- Python 3
- File Handling
- Functions
- Loops
- Lists & Dictionaries
- Exception Handling
- String Formatting

---

# 📂 Project Structure

```bash
student_manager/
│
├── student_manager.py
├── student_file_reader.py
├── student_info.txt
└── README.md
```

---

# 📄 File Descriptions

## `student_manager.py`

Main program file.

Contains features such as:

- Add students
- Show students
- Delete students
- Save students into a file

## `student_file_reader.py`

Reads and displays student records stored inside `student_info.txt`.

Features:

- Reads file safely
- Handles empty files
- Handles missing files
- Displays formatted output
- Shows total student count

## `student_info.txt`

Text file where all student information is saved.

Example:

```text
John           | 18 | 95
Alice          | 17 | 89
```

---

# ▶️ How to Run

## Run the Main Program

```bash
python student_manager.py
```

## Run the Student File Reader

```bash
python student_file_reader.py
```

---

# 📝 Example Output

```text
========================================
Student Name      | Age   | Score
----------------------------------------
1. John           | 18    | 95
2. Alice          | 17    | 89
========================================
2 student records found!
```

---

# ⚠️ Error Handling

This project includes exception handling for:

- Empty file detection
- Missing file detection
- Invalid inputs
- General file errors
- Unexpected errors

---

# 🎯 Learning Goals

This project was created to improve skills in:

- Python programming
- File handling
- Clean code writing
- Function design
- Terminal applications
- Exception handling
- Data formatting

---

# 📌 Future Improvements

- ✏️ Update student information
- 🚫 Duplicate student protection
- 📊 Export to CSV
- 🖥️ GUI version using Tkinter
- 🗂️ Database integration

---

# 👨‍💻 Author

**Behruz**

# 📜 License

This project is open-source and available for learning and educational purposes.