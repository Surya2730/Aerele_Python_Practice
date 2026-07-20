from student_management import create_student, display_students
from student_management.config import APP_NAME, VERSION

print(APP_NAME)
print("Version:", VERSION)

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        print("Good Bye")
        break

    else:
        print("Invalid Choice")