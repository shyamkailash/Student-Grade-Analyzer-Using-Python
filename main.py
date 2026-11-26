def calculate_total(marks):
    total = sum(mark for mark, _ in marks)
    return total




def calculate_average(marks):
    total = calculate_total(marks)
    average = total / len(marks)
    return average




stud_name=input("Enter student name: ")
while True:
    try:
        no_subject = int(input("Enter number of subjects: "))

        if no_subject > 0:
            break
        else:
            print("Number of subjects must be greater than zero.")

    except ValueError:
        print("Please enter a valid integer.")
print(f"Enter marks for {no_subject} subjects:")
marks = []
for i in range(no_subject):
    while True:
        mark = float(input(f"Enter marks for subject {i+1}: "))
        if 0 <= mark <= 100:
            break
        else:
            print("Invalid marks! Enter marks between 0 and 100.")
    subject_name = input(f"Enter name of subject {i+1}: ")
    marks.append((mark, subject_name))
average = calculate_average(marks)
while True:
    print("\n===== STUDENT GRADE ANALYZER =====")
    print("1. Calculate Total")
    print("2. Calculate Average")
    print("3. Display Subject Marks")
    print("4. Calculate Grade")
    print("5. Check Pass/Fail")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        total = calculate_total(marks)
        print(f"Total marks for {stud_name}: {total}")

    elif choice == '2':
        print(f"Average marks for {stud_name}: {average:.2f}")

    elif choice == '3':
        print(f"Marks for {stud_name}:")
        for mark, subject in marks:
            print(f"{subject}: {mark}")

    elif choice == '4':
        if average >= 90:
            grade = "A"

        elif average >= 80:
            grade = "B"

        elif average >= 70:
            grade = "C"

        elif average >= 60:
            grade = "D"

        else:
            grade = "F"
        print(f"Grade for {stud_name}: {grade}")

    elif choice == '5':
        if all(mark >= 40 for mark, _ in marks):
            print(f"Result for {stud_name}: PASS")
        else:
            print(f"Result for {stud_name}: FAIL")

    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
