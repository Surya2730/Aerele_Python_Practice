from .services import add_student, view_students

def create_student():

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    add_student(name, age)

    print("Student Added Successfully!")

def display_students():

    students = view_students()

    if not students:
        print("No Students Found")
        return

    print("\nStudent List")

    for student in students:
        print(student)