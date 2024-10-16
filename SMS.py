# Simple Student Management System using basic Python
students = []

# Function to add student
def add_student():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    grade = input("Enter student's grade: ")
    student = {'name': name, 'roll_number': roll_number, 'grade': grade}
    students.append(student)
    print("Student added successfully!\n")

# Function to view all students11
def view_students():
    if not students:
        print("No students found.\n")
    else:
        print("List of students:")
        for student in students:
            print(f"Name: {student['name']}, Roll Number: {student['roll_number']}, Grade: {student['grade']}")
        print()

# Function to search for a student by roll number
def search_student():
    roll_number = input("Enter student's roll number to search: ")
    for student in students:
        if student['roll_number'] == roll_number:
            print(f"Student Found: Name: {student['name']}, Roll Number: {student['roll_number']}, Grade: {student['grade']}\n")
            return
    print("Student not found.\n")

# Function to delete a student by roll number
def delete_student():
    roll_number = input("Enter student's roll number to delete: ")
    for student in students:
        if student['roll_number'] == roll_number:
            students.remove(student)
            print("Student removed successfully!\n")
            return
    print("Student not found.\n")

# Function to update student details
def update_student():
    roll_number = input("Enter student's roll number to update: ")
    for student in students:
        if student['roll_number'] == roll_number:
            print("What do you want to update?")
            print("1. Name")
            print("2. Grade")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                student['name'] = input("Enter new name: ")
            elif choice == 2:
                student['grade'] = input("Enter new grade: ")
            else:
                print("Invalid choice.")
            print("Student updated successfully!\n")
            return
    print("Student not found.\n")

# Main program loop
def main():
    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            update_student()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
