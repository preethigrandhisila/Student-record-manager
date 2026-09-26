# ============================================================
# STUDENT RECORD MANAGER
# Module 2 Assignment
# ============================================================

# Import re module for Regular Expression
# It is used to validate email addresses.
import re


# Name of the text file used to store student records
FILE_NAME = "students.txt"


# ============================================================
# FUNCTION 1: VALIDATE EMAIL
# ============================================================

def validate_email(email):
    # Regular expression pattern for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    # Check whether the email matches the pattern
    return re.match(pattern, email) is not None


# ============================================================
# FUNCTION 2: ADD STUDENT
# ============================================================

def add_student():

    try:
        # Get student ID from the terminal
        student_id = int(input("Enter Student ID: "))

        # Get student name
        name = input("Enter Student Name: ").strip()

        # Get student email
        email = input("Enter Student Email: ").strip()

        # Check whether the name is empty
        if name == "":
            raise ValueError("Student name cannot be empty.")

        # Validate the email
        if not validate_email(email):
            raise ValueError("Invalid email format.")

        # Open the text file in append mode
        # "a" means new records are added without deleting old records
        with open(FILE_NAME, "a") as file:

            # Store student details in the text file
            file.write(f"{student_id},{name},{email}\n")

        # Display success message
        print("\nStudent record added successfully!")

    # Handle invalid input
    except ValueError as e:
        print("\nError:", e)

    # Handle other unexpected errors
    except Exception as e:
        print("\nSomething went wrong:", e)


# ============================================================
# FUNCTION 3: READ STUDENT RECORDS
# ============================================================

def read_students():

    try:
        # Open the text file in read mode
        # "r" means we are reading existing data
        with open(FILE_NAME, "r") as file:

            # Read all records from the file
            records = file.readlines()

        # Check whether there are any records
        if not records:
            print("\nNo student records found.")
            return

        # Display heading
        print("\n")
        print("=" * 50)
        print("             STUDENT RECORDS")
        print("=" * 50)

        # Read each record one by one
        for record in records:

            # Remove newline character and extra spaces
            record = record.strip()

            # Ignore empty lines
            if record == "":
                continue

            # Separate ID, name and email using comma
            student_id, name, email = record.split(",")

            # Display the student information
            print("Student ID :", student_id)
            print("Student Name:", name)
            print("Student Email:", email)
            print("-" * 50)

    # If the text file does not exist
    except FileNotFoundError:
        print("\nNo student records found.")
        print("Please add a student first.")

    # Handle other errors
    except Exception as e:
        print("\nError while reading records:", e)


# ============================================================
# FUNCTION 4: MAIN MENU
# ============================================================

def main():

    # Keep the program running until the user chooses Exit
    while True:

        print("\n")
        print("=" * 50)
        print("          STUDENT RECORD MANAGER")
        print("=" * 50)
        print("1. Add Student")
        print("2. Read Student Records")
        print("3. Exit")
        print("=" * 50)

        try:
            # Get the user's menu choice
            choice = int(input("Enter your choice: "))

            # Option 1: Add student
            if choice == 1:
                add_student()

            # Option 2: Read student records
            elif choice == 2:
                read_students()

            # Option 3: Exit program
            elif choice == 3:
                print("\nThank you! Program ended.")
                break

            # Invalid menu option
            else:
                print("\nInvalid choice!")
                print("Please enter 1, 2, or 3.")

        # Handle non-numeric input
        except ValueError:
            print("\nInvalid input!")
            print("Please enter a number.")


# ============================================================
# PROGRAM STARTS HERE
# ============================================================

main()