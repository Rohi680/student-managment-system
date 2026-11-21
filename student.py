import sqlite3

# Connect to the database (creates students.db if it does not exist)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")
conn.commit()


def add_student():
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    course = input("Enter student course: ").strip()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if not records:
        print("No student records found.")
        return

    print("\nID | Name | Age | Course")
    print("-" * 35)
    for student in records:
        print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]}")


def search_student():
    student_id = int(input("Enter student ID: "))
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    record = cursor.fetchone()

    if record:
        print("Student found:", record)
    else:
        print("Student not found.")


def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ").strip()
    age = int(input("Enter new age: "))
    course = input("Enter new course: ").strip()

    cursor.execute(
        """UPDATE students
           SET name = ?, age = ?, course = ?
           WHERE id = ?""",
        (name, age, course, student_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


try:
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")

except ValueError:
    print("Please enter a valid number for age or student ID.")
finally:
    conn.close()
