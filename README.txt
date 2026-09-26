# 🎓 Student Record Manager

A lightweight, menu-driven command-line application for managing student records — built in Python with simple, persistent file-based storage.

## ✨ Features

- **Add Student Records** — Capture student ID, name, and email through an interactive prompt
- **Email Validation** — Ensures every email address follows a proper format using regex before it's saved
- **View All Records** — Display all stored student records in a clean, readable format
- **Persistent Storage** — Records are saved to a local text file (`students.txt`) and persist across sessions
- **Robust Error Handling** — Gracefully handles invalid input, empty fields, and missing files
- **Simple CLI Menu** — Intuitive numbered menu for easy navigation

## 🛠️ Requirements

- Python 3.x
- No external dependencies (uses only Python's built-in `re` module)

## 🚀 Getting Started

1. Clone or download the project files
2. Run the script:
   ```bash
   python student_record_manager.py
   ```
3. Follow the on-screen menu to add or view student records

## 📋 Usage

Upon launching, you'll be presented with the following menu:

```
==================================================
          STUDENT RECORD MANAGER
==================================================
1. Add Student
2. Read Student Records
3. Exit
==================================================
```

### Adding a Student
Select option `1` and enter:
- Student ID (numeric)
- Student Name
- Student Email (validated automatically)

### Viewing Records
Select option `2` to display all saved student records in a formatted list.

### Exiting
Select option `3` to close the program.

## 📁 Data Storage

All student records are stored in a plain text file named `students.txt`, located in the same directory as the script. Each record is saved as a comma-separated line:

```
101,John Doe,john.doe@example.com
102,Jane Smith,jane.smith@example.com
```

> **Note:** This file is created automatically the first time a student record is added.

## ⚠️ Error Handling

The application handles common issues gracefully, including:
- Empty or invalid names
- Improperly formatted email addresses
- Non-numeric menu selections
- Missing or empty data file on first run

## 📌 Notes

- This project is intended as a simple, educational demonstration of file handling, input validation, and menu-driven program design in Python.
- For larger datasets or multi-user access, consider migrating to a database (e.g., SQLite) in future iterations.

## 📄 License

This project is free to use and modify for personal or educational purposes.
