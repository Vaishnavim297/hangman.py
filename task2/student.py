students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    mark1 = float(input("Enter Mark 1: "))
    mark2 = float(input("Enter Mark 2: "))
    mark3 = float(input("Enter Mark 3: "))

    marks = (mark1, mark2, mark3)

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\nStudent Records:")
    print("-" * 40)

    for student in students:
        print("Name :", student["name"])
        print("Age  :", student["age"])
        print("Marks:", student["marks"])
        print("Average Marks:", calculate_average(student["marks"]))
        print("-" * 40)


def calculate_average(marks):
    return sum(marks) / len(marks)


def find_topper():
    if len(students) == 0:
        print("No student records available.\n")
        return

    topper = students[0]
    highest_avg = calculate_average(topper["marks"])

    for student in students:
        avg = calculate_average(student["marks"])

        if avg > highest_avg:
            highest_avg = avg
            topper = student

    print("\nTopper Details")
    print("-" * 30)
    print("Name :", topper["name"])
    print("Age  :", topper["age"])
    print("Marks:", topper["marks"])
    print("Average Marks:", round(highest_avg, 2))
    print("-" * 30)


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        find_topper()

    elif choice == "4":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Please try again.")