def CalculateTotal(marks):
    total=0

    for mark in marks:
        total=total+mark
    return total

def AverageCalculate(marks):
    total=CalculateTotal(marks)
    avg=total/len(marks)
    return avg

def get_grade(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "First Division"
    elif avg >= 40:
        return "Pass"
    else:
        return "Fail"

def build_report(student):
    name = student["name"]
    marks = student["marks"]

    total = CalculateTotal(marks)
    avg = AverageCalculate(marks)
    grade = get_grade(avg)

    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", grade)
    print()

def get_top_students(records):
    top = list(filter(
        lambda s:AverageCalculate(s["marks"]) >= 75,
        records.values()
    ))
    return top
def average_marks(*marks):
    total = 0
    for m in marks:
        total = total + m
    return total / len(marks)

def class_summary(**options):
    for key, value in options.items():
        print(key, ":", value)

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)
def show_message():
    message = "This is a local variable"
    print(message)

students = {
    "S101": {"name": "vidhi", "marks": [78, 65, 88]},
    "S102": {"name": "vidhu", "marks": [35, 72, 61]},
    "S103": {"name": "vidushi", "marks": [80, 85, 90]}
}
print("===== STUDENT PERFORMANCE REPORT =====")

for sid, student in students.items():
    print("Student ID:", sid)
    build_report(student)

names = list(map(lambda s: s["name"], students.values()))
print("Student Names:", names)
top_students = get_top_students(students)
top_names = list(map(lambda s: s["name"], top_students))
print("High Performers:", top_names)
print("Average of given marks:", average_marks(70, 80, 90))
class_summary(title="Class Report", passing_mark=40)
print("Recursive Sum from 1 to 5:", find_sum(5))
show_message()