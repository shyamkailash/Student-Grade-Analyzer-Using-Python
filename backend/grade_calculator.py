
def calculate_total(marks):
    return sum(marks.values())


def calculate_average(marks):
    total = calculate_total(marks)
    return total / len(marks)


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
    for mark in marks.values():
        if mark < 40:
            return "FAIL"

    return "PASS"


def generate_report(student_name, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    result = check_result(marks)

    return {
        "student_name": student_name,
        "subjects": marks,
        "total": total,
        "average": round(average, 2),
        "grade": grade,
        "result": result
    }
