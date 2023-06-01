students = {}

for _ in range(int(input())):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(grade)

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f'{student} -> {" ".join(["%.2f" % grade for grade in grades])} (avg: {avg_grade:.2f})')