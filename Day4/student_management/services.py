from .repository import save_student, get_students

def add_student(name, age):

    student = {
        "name": name,
        "age": age
    }

    save_student(student)

def view_students():
    return get_students()