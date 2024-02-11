
students = {}
n = int(input("Количество студентов: "))
s = 0
for i in range(n):
    student_name = input(str(i + 1) + "-й студент: ")
    point = int(input("Балл: "))
    students[student_name] = point
    s += point
    avrg = s / n

print("Средний балл: %.0f. Студенты с баллом выше среднего: " % avrg)
for i in students:
    if students[i] > avrg:
        print(i)
