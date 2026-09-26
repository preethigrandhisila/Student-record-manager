Student Record Manager

A console-based Student Record Manager built with Python to efficiently add, store, validate, and retrieve student records.

The application provides a simple menu-driven interface through the VS Code terminal. It demonstrates practical implementation of file handling, regular expressions, input validation, functions, and exception handling.

---

📌 Overview

The Student Record Manager allows users to manage basic student information through a command-line interface.

Users can:

- Add new student records
- Validate email addresses using Regular Expressions
- Store student records in a text file
- Retrieve and display saved student records
- Handle invalid inputs and runtime errors gracefully

---

✨ Features

Add Student

Allows users to enter:

- Student ID
- Student Name
- Student Email

The information is validated before being saved.

Email Validation

Uses Python's Regular Expression ("re") module to validate the format of email addresses.

Example of a valid email:

preethi@gmail.com

Example of an invalid email:

preethi@gmail

File-Based Storage

Student records are stored in:

students.txt

The application uses append mode (""a"") so that adding a new record does not overwrite existing records.

Read Student Records

The application reads previously stored records from the text file and displays them in a structured format in the terminal.

Exception Handling

The application handles common errors such as:

- Invalid Student ID
- Invalid menu choice
- Invalid email format
- Empty student name
- Missing data file

---

🛠️ Technologies & Concepts

Technologies

- Python 3
- Visual Studio Code
- Git
- GitHub

Python Concepts

- Variables and data types
- Functions
- Conditional statements
- "while" loops
- User input
- String manipulation
- Regular Expressions
- File handling
- Exception handling
- "try-except"
- "ValueError"
- "FileNotFoundError"

---

📂 Project Structure

Student-Record-Manager/
│
├── student_record_manager.py
│       └── Main Python application
│
├── students.txt
│       └── Stores student records
│
└── README.md
        └── Project documentation

«"students.txt" is automatically created when the first student record is saved.»

---

⚙️ Getting Started

Prerequisites

Make sure Python 3 is installed on your system.

Check the installation using:

python --version

If that doesn't work on Windows, try:

py --version

---

Run the Application

1. Clone the repository:

git clone <your-repository-url>

2. Navigate to the project directory:

cd Student-Record-Manager

3. Open the project in VS Code.

4. Open the VS Code terminal.

5. Run the application:

python student_record_manager.py

On Windows, you can also use:

py student_record_manager.py

---

🖥️ Application Menu

When the application starts, it displays:

==================================================
          STUDENT RECORD MANAGER
==================================================
1. Add Student
2. Read Student Records
3. Exit
==================================================
Enter your choice:

---

📝 Example: Adding a Student

Enter your choice: 1

Enter Student ID: 101
Enter Student Name: Preethi
Enter Student Email: preethi@gmail.com

Student record added successfully!

The information is stored in "students.txt":

101,Preethi,preethi@gmail.com

---

📖 Example: Reading Student Records

Select option "2":

Enter your choice: 2

The application retrieves the saved records:

==================================================
             STUDENT RECORDS
==================================================
Student ID : 101
Student Name: Preethi
Student Email: preethi@gmail.com
--------------------------------------------------

---

🔐 Input Validation & Error Handling

The application validates user input before processing it.

For example, entering an invalid email:

Enter Student Email: preethi@gmail

produces:

Error: Invalid email format.

Similarly, entering text instead of a numeric Student ID is handled using exception handling, preventing the application from crashing.

---

🔄 Application Workflow

                    START
                      │
                      ▼
                Display Menu
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
     Add Student   Read Records   Exit
          │           │
          ▼           ▼
   Enter Details   Read File
          │           │
          ▼           ▼
   Validate Email  Display Records
          │
          ▼
    Save to File
          │
          └───────────► Menu

---

🎯 Learning Outcomes

This project demonstrates the ability to:

- Build a menu-driven Python application
- Create and use reusable functions
- Validate user input
- Implement Regular Expressions
- Read from and write to text files
- Handle exceptions gracefully
- Structure a small Python project
- Use Git and GitHub for version control

---

🚀 Future Enhancements

The application can be extended with:

- 🔎 Search student by ID
- ✏️ Update student information
- 🗑️ Delete student records
- 🔐 Prevent duplicate Student IDs
- 📱 Store phone numbers and additional student details
- 📊 Store records using CSV or JSON
- 🗄️ Integrate with MySQL
- 🖥️ Develop a graphical user interface

---

👩‍💻 Author

Preethi Ahalya

Computer Science & Engineering Student

---

📌 Project Status

Completed

A beginner-friendly Python project demonstrating practical use of file handling, Regular Expressions, input validation, and exception handling.