grades = {}

for _ in range(int(input())):
    name, grade = tuple(input().split())
    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for student in grades.keys():
    avg_grade = sum([float(x) for x in grades[student]]) / len(grades[student])
    print(f"{student} -> {' '.join(grades[student])} (avg: {avg_grade:.2f})")



