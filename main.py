
def calculate_total(marks):
    total = sum(mark for mark, _ in marks)
    return total


def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def check_result(marks):
    if all(mark >= 40 for mark, _ in marks):
        return "PASS"
    else:
        return "FAIL"


def display_report(student, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    result = check_result(marks)

    print("\n========== STUDENT REPORT ==========")
    print(f"Student Name : {student['name']}")

    print("\nSubject Marks:")

    for subject, mark in student["subjects"].items():
        print(f"{subject:<12}: {mark}")

    print("------------------------------------")
    print(f"Total        : {total}")
    print(f"Average      : {average:.2f}")
    print(f"Grade        : {grade}")
    print(f"Result       : {result}")
    print("====================================")


# Get student name
stud_name = input("Enter student name: ")

# Validate number of subjects
while True:
    try:
        no_subject = int(input("Enter number of subjects: "))

        if no_subject > 0:
            break
        else:
            print("Number of subjects must be greater than zero.")

    except ValueError:
        print("Please enter a valid integer.")


# Get subject marks
print(f"Enter marks for {no_subject} subjects:")
marks = []

for i in range(no_subject):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {i+1}: "))

            if 0 <= mark <= 100:
                break
            else:
                print("Invalid marks! Enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    subject_name = input(f"Enter name of subject {i+1}: ")
    marks.append((mark, subject_name))


# Create student dictionary
student = {
    "name": stud_name,
    "subjects": {
        subject: mark for mark, subject in marks
    }
}


# Main menu
while True:
    print("\n===== STUDENT GRADE ANALYZER =====")
    print("1. Calculate Total")
    print("2. Calculate Average")
    print("3. Display Subject Marks")
    print("4. Calculate Grade")
    print("5. Check Pass/Fail")
    print("6. Display Full Report")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        total = calculate_total(marks)
        print(f"Total marks for {student['name']}: {total}")

    elif choice == '2':
        average = calculate_average(marks)
        print(f"Average marks for {student['name']}: {average:.2f}")

    elif choice == '3':
        print(f"Marks for {student['name']}:")

        for subject, mark in student["subjects"].items():
            print(f"{subject}: {mark}")

    elif choice == '4':
        average = calculate_average(marks)
        grade = calculate_grade(average)
        print(f"Grade for {student['name']}: {grade}")

    elif choice == '5':
        result = check_result(marks)
        print(f"Result for {student['name']}: {result}")

    elif choice == '6':
        display_report(student, marks)

    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
