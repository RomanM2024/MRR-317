# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))
# a = b = c = 5
# print(a, b, c)
# a, b, c = 7, "Hello", 9.2
# print(a, b, c)

# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 5
# b = "7"
# print(a + int(b))
# print(str(a) + b)

# a = 19
# b = 24
# print("a:", a)
# print("b:", b)
# a, b = b, a
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a:", a)  # 2
# print("b:", b)  # 1

# print("\tстрока \n"
#       "символов")
# print('     строка символов         строка символов         строка символов строка символов '
#       'строка символов    строка символов строка символов строка символов')
# print("\"program\" \n\rC:\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)

# print(46545645645646545612318787974)
# print(4.6545645645646545612318787974)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(5 / 2)
# print(5 // 2)
# print(6 // 2)
# print(6 ** 2)
# print(5 % 4)


# a = 5
# b = 7
# c = 3
# sum1 = a + b + c
# print("Сумма:", sum1)
# print("Произведение:", a * b * c)
# print("Среднее арифметическое:", sum1 / 3)

# numbers = 6 + 4 * 5 ** 2 + 7
# print(numbers)
#
# numbers = (6 + 4) * (5 ** 2 + 7)
# print(numbers)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12
#
# num *= 4  # num = num * 4
# print(num)  # 48

# a = 30
# b = 10
# print("a:", a)
# print("b:", b)
# a = a + b  # 21
# b = a - b  # 20
# a = a - b  # 1
# # a, b = b, a
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
# print("a:", a)  # 2
# print("b:", b)  # 1


# num = 4321  # 1234
# a = num % 10
# print(a)  # 1
# num = num // 10  # 432
# # print("num:", num)
# b = num % 10
# print(b)  # 2
# num = num // 10  # 43
# # print("num:", num)
# c = num % 10
# print(c)  # 3
# num = num // 10  # 4
# # print("num:", num)
# d = num % 10
# print(d)  # 4
# num = a * 1000 + b * 100 + c * 10 + d
# print(num)


# num = 4321  # 1234
# res = num % 10 * 1000  # 1000
# num //= 10  # 432
# res += num % 10 * 100  # 200
# num //= 10  # 43
# res += num % 10 * 10  # 30
# num //= 10  # 4
# res += num % 10  # 4
# print(res)


# print(int(3.8))  # 3
# a = round(3.84646456, 2)
# print(round(3.84646456))  # 4
# print(a, type(a))

# a = '5.2'
# b = 10
# c = int(a) + b
# print(c)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", end=" ", sep="---")
# print("Hello")


# name = input("Введите имя: ")
# city = input("Введите город: ")
# print(name, city)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвертое число: "))
# print("1:", a)
# print("2:", b)
# print("3:", c)
# print("4:", d)
# result = round(((a + b) / (c + d)), 2)
# print(result)

# b1 = True
# b2 = False
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5
# print(type(b1))

#  False => "", 0, 0.0, False, None
#
# print(bool("python"))
# print(bool(""))
# print(bool(10))
# print(bool(0.0))
# print(bool(False))
# print(bool(None))
#
# test = None
# print(test, type(test))
# test = 5
# print(test)

# print(7 == 7)
# print(7 == "7")
# print(2 + 5 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print(8 <= 8)
# print("привет" > "ПРИВЕТ")  # 175 > 143

# print(2 < 4 < 9)  # True : True  => True
# print(2 < 4 > 9)  # True : False  => False
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10 5 False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True => True
# print(5 - 3 < 2 or 1 + 3 < 4)  # False and False => False
# print(not 9 - 5)  # False
# print(not 9 - 9)  # True


# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# PEP20
# import this

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = input("Введите 1-сторону")
# b = input("Введите 2-сторону")
# c = input("Введите 3-сторону")
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or c == b:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")


# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# m = int(input("Введите номер месяца: "))
# if m == 1 or m == 2 or m == 12:
#     print("Зима")
# elif 3 <= m <= 5:
#     print("Весна")
# elif 6 <= m <= 8:
#     print("Лето")
# elif 9 <= m <= 11:
#     print("Осень")
# else:
#     print("Ошибка ввода данных")


# password = "admin1"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = 'суббота'
# time = 18
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье' if 9 <= time <= 12:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или нерабочее время")


# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else ("a > b" if a > b else "b > a"))

# a, b = int(input("Введите первое число")), int(input("Введите второе число"))
#
# print("На ноль делить нельзя!!!" if b == 0 else a / b)

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки и нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)  # '9' => 9
#     m = int(m)  # 'fgdfg'
# except ValueError:
#     n = str(n)  # '9'
# finally:
#     print(n + m)

# x = input("Введите первое: ")
# y = input("Введите второе: ")
# try:
#     print(int(x) + int(y))
# except ValueError:
#     print(x + y)

# x = input("Введите первое: ")
# y = input("Введите второе: ")
# try:
#     z = int(x) + int(y)
# except ValueError:
#     z = x + y
# finally:
#     print(z)

# Цикл

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 2
# while i <= 20:
#     print("i = ", i)
#     i += 2


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# print("*" * n)
# print("+-" * int(n / 2))


# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите кол-во символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Укажите кол-во символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# 1 - 5 => 1 + 3 + 5 => 9

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# j = 0
# while j < 5:
#     print(" " * j, "*", sep="")
#     j += 1


# i = 0  # 5
# while i < 5:  # 5 < 5
#     j = 0  # 4
#     while j < i:  # 4 < 4
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello":
#     print(i)

# for color in "red", "yellow", "green", 1, 20, 0.3:
#     print(color)

# print(range(9))

# range(start, stop, step)  start=0, step=1

# for i in range(100, 0, -10):
#     print(i, end=" ")
#
# print()
#
# i = 100
# while i > 0:
#     print(i, end=" ")
#     i -= 10


# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(0, h):  # 4
#     for j in range(0, w):  # 16
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:  #
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# print([i * 5 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])

# Списки (list)

# num = [9, 3, 8, 4, 1, "Hello", 2.3, True]
# print(num)
# # print(type(num))
# # print(num[0])
# # print(num[2])
# # print(num[-2])
# # print(num[7])
# # print(num[8])
# # num[1] = 100
# # num[2] += 50
# # num[8] = 2
# print(num[len(num) - 1])
# print(num[-1])

# num = []
# print(num)
# print(type(num))


# nums = list(range(1, 100, 2))
# print(nums)  # 2 4 6 8 10 12 14 16 18 20
# print(type(nums))

# nums = list("Hello")
# num = nums * 2
# print(num + [1, 2, 3])

# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(nums[i])

# for i in nums:
#     print(i)

# генератор списков
# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)  # [0, 0, 0, 0, 0]
# b = [i ** 2 for i in range(1, 6)]
# print(b)  # [0, 1, 2, 3, 4]
# c = [c * 3 for c in "list"]
# print(c)  # ['lll', 'iii', 'sss', 'ttt']

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)  # [0, 0, 0]
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# print(range(5))
# print(list(range(5)))
# s = [2, 9, 8, 7, 4, 7, 8, 9, 6]
# for i in range(len(s)):
#     print(i, "->", s[i])
# print(len(s))

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):  # 0 1 2
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
# print(s)

# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):  # 0 1 2 3 4 5 6 7 8
#     print(lst[i], end=" ")
# print()
# for i in lst:  # 10 20 30 40 50 60 70 80 90
#     print(i, end=" ")

# colors = ["red", "blue", "green"]
# for i in range(len(colors)):  # 0 1 2
#     print(colors[i], end=" ")
# print()
# for i in colors:
#     print(i, end=" ")

# n = list(range(21, 41))
# print(n)
# count = s = 0
# for i in range(len(n)):  # 0 1 2 3 4
#     if n[i] % 2 == 0:
#         count += 1  # 1 + 1 = 2
#     else:
#         s += n[i]  # 21 + 23 = 44
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i

# print("Кол-во четных элементов списка:", count)
# print("Сумма нечетных элементов списка:", s)

# n = [4, 9, 6]
# print(n)
# i = 2
# print(n[i])
# print(n[i - 1])


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# for i in range(1, len(a)):  # 1 2 3 4
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [7, 9, 3, 1, 2]
# print(a)  # [7, 9, 3, 1, 2]
# print("[0]", id(a[0]))
# print("[1]", id(a[1]))
# a[0], a[1] = a[1], a[0]
# print(a)  # [9, 7, 3, 1, 2]
# print("[0]", id(a[0]))
# print("[1]", id(a[1]))

# Срезы  - список[start:stop:step]
# s = [6, 9, 3, 7, 1, 8]
# print(s, id(s))
# b = s[5:16]
# print(b, id(b))
# i = 5
# while i > 0:
#     print(s[i])
#     i -= 1


# s = "Hello World!"
# print(s[6:-1])

# [1, 2, 3, 4, 5, 6, 7]
# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[-3:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:3]
# print(s)

# Методы списков
# dir(list)
# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# # s[len(s):] = [12]
# s.append(12)  # добавляет один элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет любое кол-во элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(-1, 'Hello')  # добавляем элемент (второй параметр) в список в заданный индекс (первый параметр)
# print(s)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
#
# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 5, 9, 2, 1, 4, 3
#     for j in b:  # 4, 2, 1, 3, 7
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
#
# print(c)

# -------15.01.24-------

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0-3
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):  # range(3, 5)
#     c.append(b[i])
# print(c)


# else:
#     for i in range(len(b)):  # 0-3
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):  # range(3, 5)
#         c.append(a[i])
# print(c)

# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# n = 2
# if n in a:
#     a.remove(n)  # удаление по значению, выбрасывает исключение ValueError - если элемента не существует

# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(1)  # удаляет элемент по заданному индексу (IndexError)
# print(second)
# print(a)
# a.clear()  # очищает список
# print(a)

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# k = int(input("Введите индекс: "))
# a.pop(k)
# print(a)

# sp = [int(input("-> "))for i in range(int(input("Введите количество чисел списка: ")))]
# x = int(input("Введите индекс: "))
# print(sp.pop(x))
# print(sp)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5)  # возвращает кол-во заданных элементов в списке
# print(num)
#
# ind = a.index(2)  # возвращает индекс заданного значения
# print(ind)
#
# a.reverse()  # разворачивает элементы списка в обратном порядке
# print(a)
#
# a.sort(reverse=True)  # сортирует элементы списка по возрастанию или по алфавиту
# print(a)
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len)
# print(s)
# print(len("Александр"))  # указывает что в элементе 9 символов

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.sort()
# n = sorted(a, reverse=True)
# print("n =", n)
# print(a)

# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# b.append(120)
# print("a =", a, id(a))
# print("b =", b, id(b))

# -------Генерация случайных данных-------

import random

# print(random.random())  # от 0 до 1 (не включительно)
# print(random.randint(0, 9))  # генерация случайного числа от 0 до 9 (включительно)
# print(random.randrange(2, 9, 2))  # randrange(start, stop, step) от 0 до 9 (9 не включается)
# print(round(random.uniform(10.5, 25.5), 2))
#
# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))  # возвращает внутри списка
#
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# random.shuffle(s)  # перемешивает элементы
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# mas = ['a', 'b', 'c']
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))

# # print(sum(mas))

# s = 0
# for i in mas:
#     s += i  # s += i  # s = 0 + 'a'
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]  # удаление максимального элемента
# print(mas)
# summa = max(mas)
# print(summa)
# mas.remove(summa)
# mas.insert(0, summa)
# print(mas)

# mas = [random.randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)  # сортировка элементов от большего к меньшему
# print(mas)

# array = [random.randint(0, 100) for i in range(10)]
# print(array)
# minimum = min(array)
# print("Min:", minimum)
# ind = array.index(minimum)
# print(ind)
# print(array[ind:])
# # del array[:ind]
# # print(array)


# --------17.01.24---------

# lst = [5, 6, 8, 9, 7]
# # # if len(lst) == 0:
# # if not lst:
# #     print("Список пустой")
# print(5 not in lst)

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# # c = a + b
# # print(c)
#
# # c = []
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
# # print("Элементы обоих списков без повторений:", c)
# # c = []
# # for i in range(len(a)):
# #     if a[i] in b and a[i] not in c:
# #         c.append(a[i])
# # print(c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# m = [
#     [1, 2, 3, 4, 9, 8],
#     [5, 6, 7],
#     [9, 10, 11, 12, 8, 3]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()


# w, h = 5, 3
# # matrix = [[0 for x in range(w)] for y in range(h)]
# # print(matrix)
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)

# import random
#
# w, h = 5, 3
# matrix = [[random.randint(1, 100) for x in range(w)] for y in range(h)]
# print(matrix)
# print()
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()

# import random
#
# w, h = 3, 4
# count = 0
# matrix = [[random.randint(-20, 20) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#         if x < 0:
#             count += 1
#     print()
# print("Количество отрицательных элементов:", count)

# Modules

# import math
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))  # 4
# print(math.floor(3.8))  # 3

# import math as m
#
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import ceil, floor
#
# print(ceil(3.2))
# print(floor(3.8))

# from math import *
#
# print(ceil(3.2))
# print(floor(3.8))

# from math import pi
#
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * pi * radius, 2))


# from math import sqrt
# a = int(input("Введите первый катет: "))
# b = int(input("Введите второй катет: "))
# print(sqrt(a ** 2 + b ** 2))


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "bel")

# seconds = time.time()
# print(seconds)
# print(time.ctime())
# print(time.ctime(4464461))
# res = time.localtime()
# print(res)
# print(res.tm_mday, ".", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("Сегодня: %B %d, %Y"))
# print(time.strftime("%B %d, %Y", time.localtime(574464461)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S"))
#
# pause = 5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "секунд")


# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
# print()
#
#
# def hello(name):
#     print("Hello", name)
#
#
# hello("Irina")
# hello("Ivan")


# def get_sum(a, b):
#     print("Hello")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print(get_sum(9, 4))
# n = 6
# m = 3
# get_sum(n, m)
# get_sum('abc', 'def')


# --------22.01.24---------


# def set_param(c=20, s="-"):
#     print(s + c)  # "-" * 20
#
# set_param()
# set_param(7)
# a = "-"
# set_param(s=a)

# def digit_sum(n, even=True):  # 9874023
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))  # 14
# print(digit_sum(38271))  # 10
# print(digit_sum(123456789))  # 20
#
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))  # 0
# print(digit_sum(38271, even=False))  # 0
# print(digit_sum(123456789, even=False))  # 0

# def display_info(name, age, nm):
#     print("Name:", name, "\nAge:", age)
#
# # display_info("Ira", 23)
# # display_info(23, "Ira")
# # display_info(age=23, name="Ira")
# display_info(nm="Igor", age=23, name="Ira")

# a = "Hello"
# b = "Hello"
# b = b + "_new"
# print(a, id(a))
# print(b, id(b))
# print(a == b)  # True
# print(a is b)  # True
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)  # True
# print(lst1 is lst2)  # False


# Изменяемые объекты - list
# Неизменяемые объекты - int, float, bool, str, tuple

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

# ------Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = [10, 20, 30]
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = "red", "blue", "green"
# print(a)
# print(type(a))

# a = (5,)  # 5, - можно так
# print(a)
# print(type(a))

# a = tuple("Hello")
# a = tuple([1, 5, 8, 9, 6])  # При значении tuple изменить список невозможно!
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])
# a[2] = 12  # ошибка данных
# print(a)

# -------24.01.24-------

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append('hi')
# print(t, id(t))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка картежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()  # ('Tom', 22, False)
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)
# # print(user[0])
# # print(user[1])
# # print(user[2])

# def func(lst):
#     return sum(lst), len(lst)
#
#
# a, b = func([2, 9, 6, 5, 8, 7, 5, 8, 7, 1, 4, 5, 4])
# print("Сумма:", a)
# print("Количество:", b)
#
# for i in 1, 2, 5, 8, 9, 5:
#     print(i)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# tpl = tuple(lst)
# print(tpl)
# lst1 = list(tpl)
# print(lst1)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries)
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")

# --------Множество (set) - неупорядоченная коллекция которая содержит только уникальные элементы

# s = {'banana', 'apple', 'orange'}
# print(s)
# print(len(s))
# print(type(s))
# for i in s:
#     print(i)

# s = ['banana', 'apple', 'orange', 'banana', 'apple']
# print(s)
# st = set(s)
# print(st)
# s1 = list(st)
# print(s1)

# a = set("Hello")
# print(type(a))
# print(a)

# s = {input("-> ") for i in range(5)}
# print(s)

# a = set("Hello")
# print(a)
# print('o' in a)
# print('a' in a)
# a.add("a")
# print(a)
# el = "e"
# if el in a:
#     a.remove(el)  # KeyError
# print(a)
# a.discard("o")
# print(a)
# a.pop()  # удаляет 1 любой элемент
# print(a)
# a.clear()  # очищает весь сет
# print(a)

# -------29.01.24--------
# print("Hello world")
# print("Данные на добавление на GitHub")

# -------31.01.24-------

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = [x for x in s if 'a' not in x]
# a = ['A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s]
# a = ['A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s if x[1] == 'c']
# print(a)
# print({'A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s if x[1] == 'c'})
# print(tuple('A' + x[1:] if x[0] == 'a' else 'B' + x[1:] for x in s if x[1] == 'c'))
# -------------------тернарное выражение q = True if условие else False ----------------------
# lst = []
# for x in s:
#     if x[1] == 'c':
#         if x[0] == 'a':
#             lst.append('A' + x[1:])
#         else:
#             lst.append('B' + x[1:])
# print(lst)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a & b  # {1, 2, 3, 4}
# # c = a - b  # {0}
# # c = a ^ b  # {0, 4}
# # c = a.union(b)
# print(c)
# # a &= b
# # a -= b
# # a ^= b
# print(a)

#  ----------Найти кол-во уникальных элементов из множеств ?

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# -----------Найти общие буквы в разных строках ?

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")

# -----------Найдите все буквы в первой строке, которые отсутствуют во второй ?

# s1 = "Python"
# s2 = "Programming languare"
# s = set(s1) - set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
# one_hobby = drawing ^ music
# print(one_hobby)
# both_hobby = drawing & music
# print(both_hobby)
#
# drawing = drawing - both_hobby
# print(drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a < b)

# frozenset
# s = frozenset ([1, 2, 3, 4, 5, 6])
# s = frozenset("Hello")
# print(s)

# -----------Словари (dict)

# set() == {}
# d = {False: "test", 1: 45, (1, 2.3): "Кортеж", True: 1, 35: [2, 3, 6, 7], 0: "один", 54: {1: 2}}
# print(d)
# # d[(1, 2.3)] = 100
# # print(d)

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))

# d1 = dict(one='one', two=2)
# print(d1)
# print(type(d1))

# d1 = dict(["one", 1, "two", 2])  # - Ошибка
# d1 = dict([("one", 1), ("two", 2)])
# print(d1)

# d = {x: x ** 2 for x in range(7)}
# print(d)

# d = {"one": 1, "two": 2, "three": 3}
# print(d)
# # print("two" in d)  # True
# # print(2 in d)  # False
# # print(len(d))  # 3
# # for i in d:
# # for key in d:
#     # print(key, "->", d[key])
#     # print(i, "->", d[i])
# key = "one"  # "four"
# del d[key]
# # if key in d:
# #     print(d[key])
# # try:
# #     print(d[key])
# # except KeyError:
# #     print("Такого ключа не существует")
# print(d)

# --------Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.--------
# {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# -105

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for x in d:
#     res *= d[x]
# print(res)  # -105


# ------Предложите пользователю ввести название 4-х элементов

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)  # {1: 'q', 2: 'w', 3: 'e', 4: 'r'}

# d = {x: input("-> ") for x in range(1, 5)}  # {1: 'q', 2: 'w', 3: 'e', 4: 'r'}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)  # {1: 'q', 2: 'w', 4: 'r'}

# d = {x: input("-> ") for x in range(1, 5)}
# print(d)
# try:
#     dislike = int(input("Какой элемент исключить: "))
#     del d[dislike]
# except (KeyError, ValueError):
#     print("Такого элемента не существует")
# print(d)

# -------05.02.24--------
# d = {'x1': 3, 'x2': 7, 'x3': [5, 6], 'x4': -1}
# print(len(d))  # 4

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670K', 3, 8500],
#     "3": ['Core-FX-6300', 6, 3700],
#     "4": ['Pentium G3230', 8, 2100],
#     "5": ['Core-i5-3450', 5, 6400],
# }
#
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Кол-во: "))
#                     goods[n][1] += count
#                 except ValueError:
#                     print("Значение некорректное. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
# for key in goods:
#     print(key, ") ", goods[key][0], " - ", goods[key][1], " шт. по ", goods[key][2], " руб.", sep="")

# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)  # {'x1': 3, 'x2': 7, 'x3': 5}
# # del d['x1']
# # d['x4'] = 10
# # print(d)  # {'x2': 7, 'x3': 5, 'x4': 10}
# print(d.values())
# print(d.keys())
# print(d.items())
# # for key, value in d.items():
# #     print(key, "->", value)
# print(list(d))  # ['x1', 'x2', 'x3']
# print(list(d.values()))  # [3, 7, 5]
# print(list(d.items()))  # [('x1', 3), ('x2', 7), ('x3', 5)]
# print(tuple(d.items()))  # (('x1', 3), ('x2', 7), ('x3', 5))
# print(set(d.items()))  # {('x1', 3), ('x3', 5), ('x2', 7)}


# d = {'x1': 3, 'x2': 7, 'x3': 5}
#
# d2 = d.copy()
# print("d =", d)  # d = {'x1': 3, 'x2': 7, 'x3': 5}
# print("d2 =", d2)  # d2 = {'x1': 3, 'x2': 7, 'x3': 5}
#
# d2["x4"] = 10
# d['x1'] = 100
#
# print("d =", d)  # d = {'x1': 100, 'x2': 7, 'x3': 5}
# print("d2 =", d2)  # d2 = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': 10}


# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# ...
# # item = d.pop("x4", "Такого ключа не существует")
# # print(item)
# # print(d)
# item2 = d.popitem()
# print(item2)
# print(d)
#
# d.clear()
# print(d)
# # s = [1, 2, 3]
# # i = s.pop(0)
# # print(i)
# # print(s)


# d = {'x1': 3, 'x2': 7, 'x3': 5}
# print(d)
# # item = d.setdefault("x4", 10)
# # print(item)
# # print(d)
# # a = {"one": 1, "two": 2, 'x1': 10}
# # print(a)
# # a = list(a.items())
# a = [('one', 1), ('two', 2), ('x1', 10)]
# print(a)
# d.update(a)
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# # z = x.copy()
# # z.update(y)
# print(z)


# d = dict.fromkeys(['a', 'b', 'c'])  # из списка создает словарь
# print(d)
# d = dict.fromkeys(['a', 'b', 'c'], 100)
# print(d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d2 = dict()
# d2['name'] = d.pop("name")
# d2['salary'] = d.pop("salary")
# print(d)
# print(d2)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)


# d = {
#       'first':{
#          1: {
#               11: "abc",
#               12: "abc",
#               113: "abc",
#          },
#          2: {
#               11: "abc"
#          },
#          3: {
#               11: "abc"
#          }},
#       'second': {
#           4: {
#               11: "abc"
#           },
#           5: {
#               11: "abc"
#      }    }}
# print(d)
# for x in d:
#       print(x)
#       for y in d[x]:
#           print("\t", y)
#               for z in d[x][y]:
#                    print("\t\t", z, ":", d[x][y][z])


# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# # d2 = {value: key for key, value in d.items()}
# d2 = {key: value for key, value in d.items() if value <= 2}
# print(d2)


#  ------------Преобразовать список в словарь!!!

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d['one'] = []
#         s = i  # s = 'one'
#     else:
#         d[s].append(i)  # d['one'].append(1)
#
# print(d)


# --------07.02.24---------

# zip()

# one = [1, 2, 3]
# two = ["one", "two", "three"]
# three = [2.5, 4.6, 8.9]
#
# d = dict(zip(one, two))
# print(d)
#
# # lst = list(zip(one, two, three))
# lst = list(zip(one))
# print(lst)

# f = {k: v for k, v in zip(one, two)}  # {1: 'one', 2: 'two', 3: 'three'}
# print(f)


# one = {"name": "Igor", "surname": "Doe", "jod": "Consultant"}
# two = {"name": "Irina", "surname": "Doe", "jod": "Manager"}
#
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)


# lst = [(1, 'one'), (2, 'two'), (3, 'three')]
# a, b = zip(*lst)  # * распаковка последовательности!
# print(a)  # (1, 2, 3)
# print(b)  # ('one', 'two', 'three')


# a = {"one": 1, "two": 2}
# b = {"three": 3, "four": 4}
# print({**a, **b})  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
#
# for k, v in {**a, **b}.items():
#     print(k, "->", v)  # one -> 1 two -> 2 three -> 3 four -> 4


# data = [5, 7, 9, 4, 1, 3, 5, 8, 6, 4]
# data = ["red", "green", "blue"]
# for num, color in enumerate(data, 1):
#     print(num, ")", color, sep="")

# j = 1
# for i in data:
#     print(j, ")", i, sep="")
#     j += 1


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
# print(func(5))
# print(func(5, 6, 7, "abc"))
# print(func())


# def summa(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(summa(1, 8, 9, 6, 5, 4, 7, 3, 5, 1, 4, 2, 6))
# print(summa(5, 4, 7, 3, 5, 1, 4))
# print(summa(4, 2, 6))


# Напишите функцию, которая принимает произвольное количество аргументов и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением.

# def to_dict(*di):
#     return dict(zip(di, di))
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))  # это вывод принта{1: 1, 2: 2, 3: 3, 4: 4}
# это вывод принта {'grey': 'grey', (2, 17): (2, 17), 3.11: 3.11, -4: -4}


# def ch(*args):
#     average = sum(args) / len(args)
#     print(average)
#     res = []
#     for num in args:
#         if average > num:
#             res.append(num)
#     return res
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(5, 9, 8, 7, 6))


# def print_scores(student, *scores):
#     print("Name:", student)
#     for score in scores:
#         print(score, end="")
#     print()
#
#
# print_scores("Roman", 5, 4, 3, 5, 4, 5, 5, 3, 5)
# print_scores("Nikita", 5, 5, 3, 5)


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
# print(func())  # {}
# print(func(name="Python"))  # {'name': 'Python'}


# def intro(**kwarks):
#     for k, v in kwarks.items():
#         print(k, "is", v)
#     print()
#
#
# intro(name="Igor", surname="Sharma", age=22)
# intro(name="Irina", surname="Wood", email="Irina@gmail.com", age=26, phone=9564743245)


# def func(a, b, *args, dd=5, **kwarks):
#     return a, b, args, kwarks, dd
#
#
# print(func(1, 2, 3, 4, 5, aa=1, bb=2, cc=3))  # (1, 2, (3, 4, 5), {'aa': 1, 'bb': 2, 'cc': 3}, 5)


# def db(**kwarks):
#     my_dict.update(**kwarks)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="Bob", age=31, weight=61, eyes_color="grey")
# print(my_dict)


# name = "Tom"  # глобальная переменная
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # локальная переменная
#     surname = "Johson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)
# hi()
# bye()
# print(name)
# print(surname)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5


# def func(a):  # a = 3
#     x = 2
#
#     def inner():
#         print("x:", x)
#         return a + x  # 5
#
#     return inner()
#
#
# print(func(3))

# --------12.02.24----------

# students = {}
#
# n = int(input("Кол-во студентов: "))
# s = 0
# for i, key in enumerate(range(n), 1):
#     name = input(str(i) + "-й студент: ")
#     point = int(input("Балл: "))
#     students[name] = point
#     s += point
#
# average = s / n
# print("Средний балл:", average)
# for key in students:
#     if students[key] > average:
#         print(key)

# sum = "Hello"
#
# print(sum)
#
# lst = [1, 2, 3, 4, 5, 6, 4]
# print(sum(lst))

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World!")


# def fun1():
#     a = 6  # 2
#
#     def fun2(b):  # b = 4
#         a = 4  # 5  # a = 6
#         print(a + b)  # 6  # a + b = 8 (10)
#
#     print("a:", a)  # 3
#     fun2(4)  # 4
#
#
# fun1()  # 1

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         # print(a)
#
#     inner()
#     t = a  # 35
#
#
# fn()
# q = x + t  # 25 + 35
# print(q)  # 60

# x = 5


# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)  # 33  55
#
#     fn2()
#     print("fn1.x =", x)  # 25  55
#
#
# fn1()

# def outer(a1, b1, a2, b2):
#     a = 0  # 1
#     b = 0  # 7
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print("a:", a)
#         # print("b:", b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]

# --------Замыкание---------

# def outer(n):  # 5
#     def inner(x):  # 10
#         return n + x  # 5 + 10 = 15
#
#     return inner
#
#
# out1 = outer(5)  # def inner(x): return n + x
# print(out1(10))  # 15
#
# out2 = outer(6)
# print(out2(4))  # 10

# print(outer(5)(10))  # 15


# def func(a):
#     return a + 2  # 5 + 2 = 7
#
#
# var = func(5)
# print(var)  # 7


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())  # Получили картеж с 3-мя переменными (2, 'line_new', [1, 2, 3, 4])


# def func(city):
#     count = 0  # 1
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()  # Москва 1
# res1()  # Москва 2
#
# res2 = func("Сочи")
# res2()  # Сочи 1
# res2()  # Сочи 2
#
# res1()  # # Москва 3


# ---------lambda - функция (выражение)----------


# def func(x, y):
#     return x + y
#
#
# print(func(2, 3))  # 5

# print((lambda x, y: x + y)(2, 3))  # 5
# print((lambda x, y: x + y)(12, 3))  # 15

# variable = (lambda x, y: x + y)
#
# print(variable(2, 3))  # 5


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))  # 29

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())


# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))
# print((lambda *args: args)("a", "b", "c"))


# c = (
#     lambda x: x * 2,  # abc_abc_
#     lambda x: x * 3,  # abc_abc_abc_
#     lambda x: x * 4,  # abc_abc_abc_abc_
# )
#
# for t in c:
#     print(t("abc_"))


# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: n + x
#
#
# f1 = outer1(5)
# print(f(10))
#
# outer2 = lambda n: lambda x: n + x
#
# f2 = outer2(5)
# print(f2(10))
#
# print((lambda n: lambda x: n + x)(5)(10))


# print((lambda n: lambda x: lambda y: n + x + y)(2)(4)(6))  # 12
# print((lambda n: lambda x: lambda y: n+x+y)(int(input("Введите 1 число: ")))(int(input("Введите 2 число: ")))
# (int(input("Введите 3 число: "))))


# def func(i):
#     return i[1]
#
#
# d = {"b": 15, "a": 7, "c": 3}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])  # Отсортировала по возрастанию {'c': 3, 'a': 7, 'b': 15}
# lst.sort(key=func)  # Такое используется реже
# print(lst)
# print(dict(lst))


# --------14.02.24----------

# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)


# def outer(a, b, c):  # 2, 4, 6
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j  # s = s + i * j
#
#     inner(a, b)  # 2, 4
#     inner(a, c)  # 2, 6
#     inner(b, c)  # 4, 6
#     return 2 * s  # 2 * 44
#
#
# print(outer(2, 4, 6))
# print(outer(5, 8, 2))
# print(outer(1, 6, 8))

# ----------------------

# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item['last_name'])
# print(res1)
# res2 = sorted(players, key=lambda item: item['rating'])
# print(res2)
# res3 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res3)

# ----------------

# a = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y]
# b = a[2](5, 3)  # 5 * 3
# print(b)  # 15

# ----------------

# b = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
# }
#
# b[3]()

# ----------------

# print((lambda a, b: a if a > b else b)(5, 3))

# print((lambda a, b, c: a if (a < b) and (b < c) else b if b < c else c)(2, 3, 1))  # 1
# print((lambda a, b, c: a if (a < b) and (b < c) else b if b < c else c)(12, 3, 5))  # 3
# print((lambda a, b, c: a if (a < b) and ((b < c) or (b > c)) else b if b < c else c)(2, 13, 5))  # 2
# print((lambda a, b, c: a if (a < b) and (a < c) else b if (b < c) and (b < a) else c)(12, 36, 15))  # 12

# ----------------

# print((lambda *args: min(args))(2, 5, 6))  # 2
# print((lambda *args: sorted(list(args))[0])(12, 5, 6))  # 5
# print((lambda *args: sorted(list(args))[-1])(2, 5, 6))  # 6

# ----------------

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lt = list(map(mult, lst))
# print(lt)
#
# lt1 = list(map(lambda t: t * 2, lst))
# print(lt1)

# ----------------

# lst = ['1', '2', '3', '4', '5']
# print(lst)  # ['1', '2', '3', '4', '5']
# print(list(map(lambda x: int(x), lst)))  # [1, 2, 3, 4, 5]
# print(list(map(int, lst)))  # [1, 2, 3, 4, 5]
# print([int(i)for i in lst])  # [1, 2, 3, 4, 5]

# ----------------

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5, 6]
# print(list(map(lambda x, y: {x, y}, st, num)))

# ----------------

# st = [9, 2, 7, 6, 5]
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: x + y, st, num)))

# ----------------

# t = ('abcd', 'abc', 'cdefg', 'def', 'gth')

# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)  # ('abc', 'def', 'gth')

# t2 = tuple(filter(lambda s: len(s) == 4, t))
# print(t2)  # ('abcd',)

# t2 = list(filter(lambda s: s * 3, t))
# print(t2)  # ['abcd', 'abc', 'cdefg', 'def', 'gth']

# ----------------

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, b)))  # [90, 76, 88, 81]

# ----------------

# from random import randint
# arr = [randint(0, 40) for i in range(10)]
# print(arr)
# print(list(filter(lambda a: 10 <= a <= 20, arr)))

# ----------------

# Вывести на экран квадраты нечетных чисел от 1 до 10
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))  # [1, 9, 25, 49, 81]
# print([x ** 2 for x in range(1, 10) if x % 2])  # [1, 9, 25, 49, 81] не четные
# print([x ** 2 for x in range(1, 10) if x % 2 == 0])  # [4, 16, 36, 64] четные

# ----------------

# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'  # 3
#
#
# def super_func(func):  # (def hello(): return 'Hello, I am func "hello"')
#     print('Hello, I am func "super_func"')  # 2
#     print(func())  # 4
#
#
# super_func(hello)  # 1

# -----------------


# def summa(a, b):
#     return a + b
#
#
# n = 5
# m = 10
# print(summa(n, m))  # 15

# -----------------


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(id(test))
# print(id(hello))
# print(test())

# -----------------

# def my_decorator(func):
#     def inner():
#         print('*' * 50)
#         func()
#         print('-' * 50)
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test')
#
#
# @my_decorator
# def hello():
#     print('Hello, I am func "func_test')
#
#
# func_test()
# hello()


# m = "Hello"
# print(m[::-1])  # olleH


# ----------19.02.24------------

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Мумладзе")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def func(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# @args_decorator
# def func1(study):
#     print("Мне нравится", study)
#
#
# func("Борис", "Елизавета", "Светлана", study="JavaScript")
# func("Владимир", "Екатерина", "Виктор")
# func1(study="HTML")

# def decor_args(arg1, arg2):
#     def decor(fn):
#         def wrap(x, y):
#             print(arg1, x, arg2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return decor
#
#
# @decor_args("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor_args("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def decor_args(arg1):
#     def decor(fn):
#         def wrap(x):
#             print(arg1*x)
#             fn(x)
#
#         return wrap
#     return decor
#
#
# @decor_args(3)
# def return_num(num):
#     return num
#
#     return num(5)


# ---------СТРОКИ----------


# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))


# print(bin(18))  # 0b10010 - двоичная
# print(oct(18))  # 0o22 - восьмеричная
# print(hex(18))  # 0x12 - шестнадцатеричная
#
# print(0b10010)  # 18
# print(0o22)  # 18
# print(0x12)  # 18
# print(0b10010 + 0x12)  # 36


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)  # Python
# print(e * 2)  # PythonPython
# print("y1" in e)  # "y" True "y1" False
# print(e[0])  # P
# print(e[1:3])  # yt


# s = "Python"  # вместо h поставить t
# # s[3] = "t"
# s = s[:3] + 't' + s[4:]  # Pytton
# print(s)


# ------- Заменить символ в строке -----------

# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == old:
#             s2 = s2 + new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_char_to_str(str1, "N", "P")
# print("str1 =", str1)
# print("str2 =", str2)

# ---------------------

# print("Привет")
# print(u"Привет")


# print("C:\\folder\\fil\nes.txt\\")  # C:\folder\files.txt
# print(r"C:\folder\files\\"[:-1])  # C:\folder\files\
# print(r"C:\folder\files" + "\\")  # C:\folder\files\


# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print(f"Меня зовут {name}. Мне {age} лет. ")


# ch = 5.26987412
#
# print(f"Число: {round(ch, 3)}")
# print(f"Число: {ch:.3f}")


# x = 10
# y = 5
# print(f"{x = }, {y = }")  # x = 10, y = 5
# print(f"{x} x {y} / 2 = {x * y / 2}")  # 10 x 5 / 2 = 25.0


# num = 74
#
# print(f"{{{{{num}}}}}")
# print("C:\\\\text")


# dir_name = 'my_doc'
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")  # home\my_doc\data.txt
# print("home\\" + dir_name + "\\" + file_name)  # home\my_doc\data.txt

# ----------21.02.24-----------

# def avg(fn):
#     def wrap(*arg):
#         print("Среднее арифметическое:", *arg, "=", fn(*arg) / len(arg))
#
#     return wrap
#
# @avg
# def summa(*args):
#     # a = ", ".join(map(str, args))
#     print("Сумма чисел:", ", ".join(map(str, args)), "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# -------------------------

# def avg(fn):
#     def wrap(*arg):
#         a = ""
#         for i in arg:
#             a += str(i) + ", "  # "2, 3, 3, 4,"
#         print("Среднее арифметическое:", a[:-2], "=", fn(*arg) / len(arg))
#
#     return wrap
#
# @avg
# def summa(*args):
#     print("Сумма чисел:", *args, "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# --------------------

# s = """
# Несколько
# строк
# """
# print(s)
#
# s1 = '''
# Несколько
# строк
# '''
# print(s1)

# s2 = ("Нес  колько \
#       строк")
# print(s2)


# ---------------------

# def square(n):
#     """Принимает число n, возвращает квадрат числа n."""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# # max(5, 5)
# # len()
# print(len.__doc__)


# ---------------

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиуса цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(max.__doc__)
# print(dict.__doc__)


# -----------------

# print(ord('a'))  # По кодировке ASCII = 97
# print(ord('#'))  # 35
# print(ord('й'))  # 1081

# -----------------

# while True:
#     n = input("-> ")
#     if n != "-1":  # -1 Выход их функции
#         print(ord(n))
#     else:
#         break

# -----------------

# s = "Test string for met"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# -----------------

# print(chr(97))
# print(chr(8364))

# -----------------
# Задача № 2

# a = 122
# b = 97
#
# if a < b:
#     a, b = b, a
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# -----------------

# print("apple" == "Apple")  # False
# print("apple" > "aPple")  # True

# -----------------
# Генерация случайного пароля

# from random import randint
#
# shortest = 7
# longest = 10
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         rand_char = chr(randint(min_ascii, max_ascii))
#         res += rand_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# ------------------
# РЕГИСТР
# s = "hello, WORLD! I am learning Python"
# print(s.capitalize())  # Hello, world! i am learning python
# print(s.lower())  # hello, world! i am learning python
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON
# print(s.title())  # Hello, World! I Am Learning Python

# ------------------

# s = "hello, WORLD! I am learning Python"
# print(s.count("h"))  # Ищет количество одинаковых символов
# print(s.count("l", 3))  #

# ------------------

# s = "hello, WORLD! I am learning Python"
#
# print(s.find("Python"))  # возвращает индекс первого вхождения подстроки в строку # 28
# print(s.find("l", 4, 20))  # 19
# print(s.rfind("l"))  # 19
#
# print(s.index("l"))  # 2
# print(s.rindex("l"))  # 19

# -------------------

# st = input("Ввести два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)

# -------------------

# s = "hello, WORLD! I am learning Python."
# ...
# print(s.startswith("I am", 14))
# print(s.index("I am"))
# print(s.endswith("on."))

# -------------------

# print(int("789"))


# print('123'.isdigit())  # True только числа
# print('123a'.isdigit())  # False
# print('12.3'.isdigit())  # False

# print('qwert'.isalpha())  # внутри строки находятся только буквы
# print('Abc123'.isalnum())  # внутри строки находятся только буквы или цифры
#
# print('abc'.islower())  # только нижний регистр
# print('ABC0123"№'.isupper())  # только верхний регистр


# n = input("Введите число: ")
# if n.isdigit():
#     n = int(n)
#     print(n * 2)


# print('py'.center(10))  # Выравнивание по центру  py
# print('py'.center(10, "-"))  # Выравнивание по центру ----py----
# print(' py '.center(10, "-"))  # Выравнивание по центру --- py ---


# print('    py    '.lstrip())  # удаление пробелов слева
# print('    py    '.rstrip())  # удаление пробелов справа
# print('    py    '.strip())  # удаление пробелов


# print('http://www.pythons.org'.strip('/:pths.org'))  # www.python
# print('http://www.pythons.org'.lstrip('/:pths').rstrip('.org'))  # www.pythons


# ---------Поиск и замена-----------

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace("Nython", "Python"))
# print(str1.replace("N", "P"))

# --------Метод join--------

# s = "-"
# seq = ("a", "b", "c")  # a-b-c Символ объединитель
# print(s.join(seq))
#
# print("..".join(['1', '99']))  # 1..99
# # print("..".join([1, 99]))  # Ошибка так не работает
# print(":".join("Hello"))  # H:e:l:l:o


# -----------------------

# print("Строка разделенная пробелами".split())  # ['Строка', 'разделенная', 'пробелами']
# print('www.python.org'.split("."))  # ['www', 'python', 'org']
# print('www.python.org'.split())  # ['www.python.org']
# print('www.python.org.ru'.split(".", 3))  # ['www', 'python', 'org', 'ru']
# print('www.python.org.ru.'.split(".", 4))  # ['www', 'python', 'org', 'ru', '']
# print('www.python.org.ru'.rsplit(".", 2))  # ['www.python', 'org', 'ru']

# -----------------------

# a = input("-> ").split()
# b = list(map(int, a))
# print(b)  # [9, 8, 7, 6, 5, 4]
# print(a)  # ['Hello', 'world']
# print(a)  # ['9', '8', '7', '6', '5', '4', '3', '2', '1']

# --------26.02.24---------
import re
import time

...

# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hello"
# reg = "[21][0-9][0-9][0-9]"
# reg = "[A-яЁё]"
# reg = "[A-Za-z]"
# reg = r"\."
# reg = r"[A-Za-z\[\]-]"
# reg = r"[^0-9]"
# reg = r"[^A-яЁёA-Za-z0-9]"

# print(re.findall(reg, s))

# print(ord('Я'))
# print(ord('a'))

# st = "Час в 24 формате от 00 до 23. 2021-06-15Т19:05. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# pattern = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(pattern, st))

# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё-та. 198673 Hello 20000000000000"
# reg = r"[20]*"
# print(re.findall(reg, s))


# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1


# d = "Цифры: 7, +17, -42, 0013, 0.3"
# reg = r'[+-]?[\d.]+'
# print(re.findall(reg, d))


# s = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r"\s#.*", "", s))  # Дата рождения: 05-03-1987
# print("Дата рождения:", re.sub('-', '.', re.sub("\\s#.*", "", s)))  # Дата рождения: 05.03.1987


# s = "autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# reg = r'\w+\s*=\s*[^;]+'
# # reg = r'[^;]+'
# print(re.findall(reg, s))


# s = "12 сентября 2024 года 56887653567"
# reg = r'\d{2,4}'
# print(re.findall(reg, s))


# s = "Я ищу совпадение в 2024 году. И я их [найду] в 2 счё_та."
# reg = r"^\w+\s\w+"  # ['Я ищу']
# # reg = r"\w+\.$"  # ['счё_та.']
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9-]{3,16}$", login)
#
#
# print(validate_login("Python-master"))

# --------28.02.24---------

# s = "12 сентября 2024 года 568789456"
# reg = r"\d{2,4}"
# print(re.findall(reg, s))

# s = "Ольга и Виталий отлично учатся"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, s))

# ------------------------

# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*\d[.\w+]*"  # ['int = 4', 'float = 4.0f', 'double = 8.0']
# # reg = r"int\s*=\s*\d[.\w]*|float\s*=\s*\d[.\w]*"
# # reg = r"(int|float)\s*=\s*\d[.\w]*"  # ['int', 'float']
# reg = r"(?:int|float)\s*=\s*\d[.\w]*"  # ['int = 4', 'float = 4.0f']
# print(re.findall(reg, s))
# print(re.search(reg, s))  # ищет первое совпадение <re.Match object; span=(0, 7), match='int = 4'>

# (?: .....) - группирующая скобка не является сохраняющей

# -----------------------

# s = "5 + 7 * 2 - 4"
# # reg = r"[+*-]"  # ['5 ', ' 7 ', ' 2 ', ' 4']
# # reg = r"\s*[+*-]\s*"  # ['5', '7', '2', '4']
# # reg = r"\s*([+*-])\s*"  # ['5', '+', '7', '*', '2', '-', '4']
# # reg = r"(\s*[+*-]\s*)"  # ['5', ' + ', '7', ' * ', '2', ' - ', '4']
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))


# -----------------------

# s = "28-02-2024"
# reg = "([0-2][0-9]|3[01])-([0-9][0-9])-([0-9][0-9][0-9][0-9])"
# print(re.findall(reg, s))  # [('28', '02', '2024')]
# print(re.search(reg, s).group())  # 28-02-2024

# s = "01-12-2024"
# reg = "(0[1-9]|[1-2][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])"
# print(re.findall(reg, s))
# print(re.search(reg, s).group())

# -----------------------

# text = """
# Самара
# Тверь
# Уфа
# Казань
# """

# s = "Самолет прилетит 10/23/2024. Будем рады Вас видеть после 10/24/2024."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# -------------------------

# s = "yandex.com and yandex.ru"
# reg = r"([a-z0-9-]{2,}\.[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))  # http://yandex.com and http://yandex.ru

# Изучить картинки папка 17!!!!


# ========== РУКУРСИЯ ===========

# def elevator(n):  # 0
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     print("=>", n)  # 1
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком вы этаже: "))
# elevator(n1)

# ------------------------

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res

# def sum_list(lst):  # [1, 3, 5, 7, 9] -> [3, 5, 7, 9] ->  [5, 7, 9] и т.д.
#     if len(lst) == 1:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, "=> lst[0]:", lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7 + 9 = 25
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# --------------------

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(18, 16))  # to_str(254, 16) => FE


# ==========04.03.24==========

# def to_str(n, base):  # 2, 10
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # convert[15] = 'F'
#     else:
#         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
#
#
# print(to_str(254, 16))  # to_str(254, 16) => FE


# =====================

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # print(names[0])
# # print(isinstance(names[0], list))
# # print(names[1])
# # print(isinstance(names[1], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# ...
# def count_items(item_list):  # ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#     count = 0  # 10
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)  # count += 2
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# ==========================

# def remove(text):  # "  Hello\nWorld "
#     if not text:  # text = ""
#         return ""
#     if text[0] == "\n" or text[0] == " ":
#         return remove(text[1:])  # ""
#     else:
#         return text[0] + remove(text[1:])  # "HelloWorld"
#
#
# print(remove("  Hello\nWorld "))  # HelloWorld


# ========= ФАЙЛЫ ==========  текстовые и бинарные папка № 19
# r - чтение

# f = open("text.txt", "r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)

# read - считывает данные с файла

# f = open("text.txt", "r")
# # f = open(r"D:\Pyhton\PyhtonPro\pythonProject\text.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()

# readline - считывает данные строки до переноса

# f = open("test2.txt", "r")
# print(f.readline())
# print(f.readline(8))  # - количество считываемых символов
# print(f.readline())
# print(f.readline())
# f.close()

# readlines - возвращает список из наших строк

# f = open("test2.txt", "r")
# print(f.readlines(16))
# print(f.readlines())
# f.close()


# f = open("test2.txt", "r")
# for line in f:
#     print(line, end="")
# f.close()

# =====================

# f = open("test2.txt", "r")
# print(len(f.readlines()))
# f.close()


# f = open("test2.txt", "r")
# count = 0
# for line in f:
#     print(line, end="")
#     count += 1
# f.close()
# print(count)


# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!\n")
# f.close()


# f = open("xyz.txt", "a")
# f.write("New text.\n")
# f.close()


# f = open("xyz.txt", "a")
# lines = ['This is line 1', '\nThis is line 2']
# f.writelines(lines)
# f.close()


# f = open("xyz.txt", "w")
# # lst = [str(i) + " " for i in range(1, 20)]
# # print(lst)
# # # for index in lst:
# # #     f.write(index + "\t")
# # f.writelines(lst)
# # f.close()


# f = open("test3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл\n")
# f.close()


# f = open('test3.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# read_file[1] = "Hello world!\n"
# print(read_file)
# f.close()

# f = open("text3.txt", "w")
# f.writelines(read_file)
# f.close()

###################

# f = open('text3.txt', 'r')
# read_file = f.readlines()
# pos = int(input("Введите индекс строки для удаления: "))
# if 0 <= pos < len()

###################


# f = open("text.txt", "r")
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()


# f = open("text.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# f = open("text2.txt", "a+")
# # print(f.write("11111 I am learning Python 11111"))
# print(f.read())
# f.close()


# with open("text2.txt", "w+") as f:
#     print(f.write('01234\n56789'))
# print(f.closed)


# with open("test2.txt", 'r') as f:
#     for line in f:
#         print(line[:3])


# ========06.03.24==========

# file_name = "res.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = map(str, lt)
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
#
# with open(file_name, 'r') as f:
#     st = f.read()
#
# print(st)
# print(type(st))
#
# nums = list(map(float, st.split()))
# print(nums)
# print(type(nums[0]))


# =========================

# a = 5

# if a == 5:
#     b = 10

# for i in range(12):
#     b = 10

# def func():
#     b = 10


# func()
# print(b)


# ======================

# def longest_worlds(file):
#     with open(file, 'r', encoding="utf-8") as text:
#         w = text.read().split()
#         print(w)
#         max_length = len(max(w, key=len))
#         res = [i for i in w if len(i) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# print(longest_worlds('text.txt'))


# ======================

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# with open('one.txt', 'r') as fr, open('two.txt', 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)


# ========= МОДЛЬ OS, OS.PATH ===========

import os
import os.path


# print(os.getcwd())  # возвращает текущую директорию
# print(os.listdir())  # возвращает список директорий и файлов
# print(os.listdir(".."))

# os.mkdir("folder1")  # создает папку
# os.makedirs("folder1/nested2/nested3")  # создает конечную директорию вместе с промежуточными

# os.rmdir("folder1")  # удаляет пустую папку
# os.rmdir("nested1/nested2/nested3")

# os.remove("res.txt")  # удаляет файл

# os.rename("", "")  # переименовывает файл и папки

# os.rename("two.txt", "nested1/two1.txt")

# os.renames("text.txt", "nested1/two1.txt")  # переименовывает папки и файлы, перемещает документы


# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\tSubdirs:", dirs)
#     print("\t\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви nested1")
#     print('-' * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print('-' * 50)
#
#
# remove_empty_dirs("nested1")


# print(os.path.split(r"D:\Pyhton\PyhtonPro\pythonProject\nested1\nested2"))
#
# print(os.path.join(r'D:\Pyhton', 'PyhtonPro', 'pythonProject', 'nested1'))

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)


# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f213.txt']
# }
#
# for dir1, files in files.items():
#     for file in files:
#         file_path = os.path.join(dir1, file)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f213.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"Текст в файле {file}")


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f213.txt

# ДЗ Вывести на экран сначала все файлы, а затем все директории, расположенные в корневой директории дерева.

# =========== 11.03.24 ==============

# print(os.path.isfile(r"nested1\nested2\one.txt"))
# print(os.path.isdir(r"nested1\nested2"))


# root = r'nested1\nested2'
# objs = os.listdir(root)
# print(objs)
# objs = list(map(lambda i: os.path.join(root, i), objs))
# print(objs)
#
# obj_sort = sorted(objs, key=os.path.isfile)
# print(obj_sort)


# ------------------------

# print(os.path.exists(r'nested1\nested2'))  # проверка на существование пути
# print(os.path.getsize(r'nested1\nested2'))  # размер документа в байтах


# ------------------------

# b = os.path.getsize(r'project.py')
# print(b, "байт")
# print(b // 1024, "килобайт")


# ------------------------

# path = "project.py"
# print(os.path.getctime(path))  # возвращает время создания файла
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла (в секундах)
#
#
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(os.path.getctime(path))))
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(os.path.getatime(path))))
# print(time.strftime("%d.%m.%y, %H:%M:%S", time.localtime(os.path.getmtime(path))))

# ==========================================================

# -------- ПАРАДИГМА ООП ---------

# инкапсуляция
# наследование
# полиморфизм
# class Name:
#    свойства (поля, переменные):
#     - статические
#     - динамические
#    методы (функции):
#     - статические - def method() @staticmethod
#     - классы - def method(cls)
#     - экземпляры - def method(self)
#    атрибуты = свойства + методы


# class Point:
#     """Класс для предоставления координат на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(type(p1))
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))

# ------------------------

# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 10
# p1.y = 20
# p1.z = 30
# print(p1.x, p1.y, p1.z)
# print(p1.__dict__)
#
# p2 = Point()
# p2.x = 100
# # p2.y = 200
# print(p2.x, p2.y)
# print(p2.__dict__)

# print(id(Point))
# print(id(p1))
# print(id(p2))

# -----------------------

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, a, b):
#         self.x = a
#         self.y = b
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
#
# p2 = Point()
# # p2.x = 50
# # p2.y = 100
# p2.set_coord(50, 100)
# # Point.set_coord(p2)

# -----------------------

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print("Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: "
#               f"{self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         self.name = name
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def set_birthday(self, birthday):  # установить дату рождения
#         self.birthday = birthday
#
#     def get_birthday(self):  # получить ДР
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
# h1.set_birthday("23.12.1990")
# print(h1.get_birthday())
# h1.print_info()

# --------------------------

# class Person:
#     skill = 10  # статическое
#     count = 0  # 2
#
#     def __init__(self, name, surname):  # Инициализатор
#         self.name = name  # динамическое
#         self.surname = surname  # динамическое
#         print("Инициализатор")
#         Person.count += 1
#
#     def __del__(self):  # финализатор (деструктор)
#         print("Удаление экземпляра:", self.__class__.__name__)
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# # p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)
#
# p3 = Person("Анна", "Долгих")
# print(p1.count)
# print(p2.count)
# print(Person.count)

# ===================13.03.2024====================

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "Выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# droid3 = Robot('P-2CO')
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
# print("\nЗдесь роботы могут проделать какую-то работу\n")
# print("Роботы закончили свою работу. Давайте их выключим")
# del droid1
# del droid2
# # del droid3
# droid3 = 5
# print("Численность роботов:", Robot.k)

# -----------------------------------------------

# =========== МОДИФИКАТОРЫ ДОСТУПА: ==============
# 1 public - self.name ==========
# 2 protected - self._name ==========
# 3 private - self.__name ==========


# class Point:
#     def __init__(self, x, y):
#         self.__x =  self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(a):
#         if (isinstance(a, int) or isinstance(a, float)):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должна быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должна быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coord())
# # p1.set_coord(100, 200)
# # print(p1.get_coord())
# p1.set_x(50)
# print(p1.get_x())
# p1.set_y(30)
# print(p1.get_y())
# # p1._Point__x = 111  # так делать не нужно!!!
# print(p1.__dict__)
# print(p1._Point__x)

# ---------------------------------------------------
# import math
#
# class Rectangle:
#     __slots__ = ["__length", "__width", "x"]
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     def set_length(self, length):
#         return self.__length
#
#     def set_width(self, width):
#         return self.__width
#
#     def
#
#     def
#
#     def
#
#     def get_perimetr(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# rect = Rectangle(4, 12)
# rect.set_length(3)
# rect.set_width(9)
# print("Длина прямоугольника:", rect.get_length())
# print("Ширина прямоугольника:", rect.get_width())
# print("Площадь прямоугольника:", rect.get_area())
# print("Периметр прямоугольника:", rect.get_perimetr())
# print("Гипотенуза прямоугольника:", rect.get_hypotenuse())
# rect.get_draw()
# rect.x = 20
# print(rect.x)
# print(rect.__dict__)

# ---------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("Сеттер")
#
#     def __get_x(self):
#         print("Геттер")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# -----------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(a):
#         if isinstance(a, int) or isinstance(a, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#
#     @x.deleter
#     def x(self):
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# # del p1.x
# print(p1.__dict__)

# ----------------------------------------------------------

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", weight.to_pound(), "фунтов")
# weight.kg = "два"

# -------------------------------------------------------------

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# p4 = Point()
# p5 = Point()
#
# print(Point.get_count())  # 5

# ============== 18.03.2024 ==================

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# ch = Change()
# print(ch.inc(10), Change.dec(10))  # 11 9

# ---------------------------------------------

# class Fact:
#
#     @staticmethod
#     def max(*args):
#         return max(args)
#
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def fact(arg):
#         factor = 1
#         for i in range(1, arg + 1):
#             # 5! = 1 * 2 * 3 * 4 * 5
#             factor *= i
#         return factor
#
#     @staticmethod
#     def avg(*args):
#         avg = sum(args) / len(args)
#         return avg
#
#
# print(Fact.max(3, 5, 7, 9))
# print(Fact.min(3, 5, 7, 9))
# print(Fact.fact(5))
# print(Fact.avg(3, 5, 7, 9))

# ------------------------------------------

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     "15.12.2024",
#     "23-10-2023",
#     "01.01.2021",
#     "12.31.2020"
# ]
#
# for d in dates:
#    if Date.is_date_valid(d):
#        date = Date.from_string(d)
#        print(date.string_to_db())
#    else:
#        print("Неправильная дата или формат строки с датой")

# date2 = Date.from_string("23-10-2023")
# print(date2.string_to_db())
# date3 = Date.from_string("15.12.2024")
# print(date3.string_to_db())

# ----------------------------------------------------------

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}.")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}.")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у Вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# ---------------------------------------------

# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall('[a-za-яё-]', fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 30:
#             raise TypeError("Вес должен быть вещественным числом от 30 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_old(year)
#         self.__old = year
#
# # Доделать!!!
#
#
# p1 = UserDate("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
#
# # p1.fio = "Соболев Игорь Николаевич"
# print(p1.fio)
# print(p1.__dict__)

# ============== 20.03.2024 ================

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         # return "(" + str(self.__x) + str(self.__y) + ")"
#         return f"({self.__x}, {self.__y})"
#
#
# # print(issubclass(Point, object))
#
#
# class Prop:  # (object)
#     def __init__(self, sp, ep, color="red", width=1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), (70, 80))
# rect.draw_rect()
# # print(issubclass(Line, Prop))
# # print(issubclass(Line, Rect))
# # print(Point.__dict__)
# # print(Line.__dict__)
#
# ------------------------------------------------------

# # DRY (Don`t Repeat Youself) - не повторяйся
# # Родительский класс

# ------------------------------------------------------

# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#
# class Rectangle(Figure):
#     def __init__(self, color, width, height):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть положительным числом")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть положительным числом")
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle("green", 10, 20, )
# print(rect.color)
# print(rect.area())

# ------------------------------------------------------

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, px, solid, red):
#         super().__init__(width, height)
#         self.px = px
#         self.solid = solid
#         self.red = red
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Рамка: {self.px} {self.solid} {self.red}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# shape2 = RectBorder(600, 300, "1px", "solid", "red")
# shape2.show_rect()

# ----------------------------------------------------------

# class Vector(set):
#     def __str__(self):
#         return " ".join(map(str, self))
#         # return " ".join(self)
#
#
# v = Vector({1, 2, 3})
# print(v)
# print(type(v))

# -----------------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp: Point, ep: Point = None):
#         if ep is None:
#             self._sp = sp
#         else:
#             self._sp = sp
#             self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(12, 18), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()

# =============== 25.03.2024 ===================

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     # def draw(self):
#     #     print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     ...
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(30, 30)))
#
# for f in figs:
#     f.draw()


# ============ Абстрактные методы ===============
# Абстрактный класс

# from abc import ABC, abstractmethod


# class Chess(ABC):  # абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):  # абстрактный метод это метод без реализации
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q.draw()
# q.move()

# -------------------------------------------------------
# Создайте базовый класс "Стол"

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())  ## {'_width': 20, '_length': 10} 200
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())  ## {'_width': 20, '_length': 20} 400
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())  ## {'_radius': 20} 1257

# ----------------------------------------------------------
from abc import ABC, abstractmethod
# Создайте базовый абстрактный класс "Валюта"


# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def show(self):
#         print(f"= {self.convert_to_rub():.2f} RUB")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_value()
#     elem.show()
#
# print("*" * 50)
# for elem in e:
#     elem.print_value()
#     elem.show()

# ============= ИНТЕРФЕЙСЫ ================

# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#
#
# ch = GrandChild()
# ch.display1()
# ch.display2()

# ------------------------------------------------------

# =============== ВЛОЖЕННЫЕ КЛАССЫ ==================

# def func():
#     x = 5
#
#     def inner():
#         a = 10
#         print(x)
#
#     inner()
#     print(a)
#
#
# func()

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("outer_method")
#
#     def instance_method(self):
#         print("instance_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Вложенный метод", MyOuter.age, self.obj.name)
#             MyOuter.outer_method()
#             self.obj.instance_method()
#
#
# out = MyOuter('внешний')
# print(out.name)
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# -------------------------------------------------------

# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#         self.dg = self.DarkGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#     class DarkGreen:
#         def __init__(self):
#             self.name = "Dark Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# g2 = outer.dg
# g2.display()

# -----------------------------------------------------

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# # my_os = comp.OS
# # my_cpu = comp.CPU
# my_os = Computer().OS
# my_cpu = Computer().CPU
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# --------------------------------------------------------

# ================ 27.03.2024 ====================

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок"), Cat("Мурзик")]
# print(cat)

# class Point:
#     def __init__(self, *args):
#         self.coord = args  # tuple(1, 2, 5)
#         self.color = "red"
#         self.width = 2
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(1, 2, 5)
# print(len(p))
#
# s = list((1, 2))
# print(len(s))

# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', '__length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# # p1.z = 30
# # print(p1.z)
# p1.length = 20
# print(p1.length)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt1 = Point(1, 2)
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 3
# print(pt3.z)

# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()


# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса АA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#         # B.__init__(self)
#         super().__init__()
#         C.__init__(self)
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color="red", width=1):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Styles.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)   #
# l1.draw()
#
# print(Line.mro())
# class Goods:
#     def __init__(self, name, weight, price):
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#         super().__init__()
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init Mixin")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
#
# n1 = NoteBook("HP", 1.5, 35000)
# n1.save_sell_log()

# ------------------------------------------------------
# ============ ПЕРЕГРУЗКА ОПЕРАТОРОВ ===================
# ============ 01.04.2024 ==============================

# 24 * 60 * 60 = 86400 - число секунд в одном дне

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     # def __add__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError("Правый операнд должен быть типом Clock")
#     #     return Clock(self.sec + other.sec)
#     #
#     # def __eq__(self, other):
#     #     if not isinstance(other, Clock):
#     #         raise ArithmeticError("Правый операнд должен быть типом Clock")
#     #     if self.sec == other.sec:
#     #         return True
#     #     return False
#     #
#     # def __ne__(self, other):
#     #     return not self.__eq__(other)
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# c1["hour"] = 11
# c1["min"] = 24
# c1["sec"] = 59
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())

# c1 = Clock(100)
# c2 = Clock(200)
# # c4 = Clock(300)
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c4.get_format_time())
# # c3 = c1 + c2 + c4
# # print(c3.get_format_time())
# # c1 += c2
# # print(c1.get_format_time())
# # if c1 == c2:
# #     print("Время равно")
# # else:
# #     print("Время разное")
#
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время равно")

# -----------------------------------------------------------

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):  # 10 >= 5
#             off = key + 1 - len(self.marks)  # 10 + 1 - 5 = 6
#             self.marks.extend([None] * off)  # [5, 5, 3, 4, 5, None, None, None, None, None, None]
#
#         self.marks[key] = value  # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# print([None] * 6)
# lst = [5, 5, 3, 4, 5]
# lst.extend([None, None, None, None, None, None])
# print(lst)

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]  # 0, 5
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)


# ================= Полиморфизм ====================

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())

# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     @abstractmethod
#     def info(self):
#         pass
#
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#
# class Cat(Animal):
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} мяукает"
#
#
# class Dog(Animal):
#
#     def info(self):
#         return f"Я Собака. Меня зовут {self.name}. Мой возраст {self.age}"
#
#     def make_sound(self):
#         return f"{self.name} гавкает"
#
#
# cat1 = Cat("Пушок", 2.5)
# dog1 = Dog("Мухтар", 4)
#
# for animal in (cat1, dog1):
#     print(animal.info())
#     print(animal.make_sound())

# print(dog1.info())
# print(dog1.make_sound())

# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.last_name} {self.first_name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, speciality, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, speciality, group, rating, topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()

# =================== 04.04.24 =======================

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()

# ------------------------------------------------------

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" Hello World! "))
#
#
# class StripChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s2 = StripChars("?:!.; ")
# print(s1(" Hello World! "))

# ------------------------------------------------------

# ============= Класс как декоратор ====================

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         # print('Перед вызовом функции')
#         # res = self.fn(x, y)
#         # print('После вызова функции')
#         # return res
#         return f"Перед вызовом функции\n{self.fn(x, y)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# ----------------------------------------------------------------

# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, x, y):
#         ...
#         return f"Результат: {self.fn(x, y)}"
#
#
# @Power
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(2, 3))

# -------------------------------------------------------------------

# class MyDecorator:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции\n{self.fn(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, c=5, b=2))  # 2, 5, 2


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             return f"Перед вызовом функции\n{self.arg} {args[0]} x {args[1]} = {fn(*args, **kwargs)}\nПосле вызова " \
#                    f"функции"
#
#         return wrap
#
#
# @MyDecorator("Произведение:")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# -----------------------------------------------------------------

# class Power:
#
#     def __init__(self, power):
#         self.power = power
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print("args:", args)  # (2, 4)
#             print("kwargs", kwargs)  # {}
#             return f"Результат: {func(*args, **kwargs) ** self.power}"
#         return wrapper
#
#
# @Power(3)
# def func_test(a, b):
#     return a * b
#
#
# print(func_test(2, 4))  # 512
# print(func_test(b=3, a=5))  # 3375

# ---------------------------------------------------------------

# class Power:
#
#     def __init__(self, power):
#         self.power = power
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             # print("args:", args)
#             # print("kwargs:", kwargs)
#             return f"Результат: {func(*args, **kwargs) ** self.power}\n"
#         return wrapper
#
#
# @Power(3)
# def func_test(a, b):
#     return a / b
#
#
# print(func_test(4, 2))
# print(func_test(b=4, a=2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Некрасов")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Инициализатор ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(5))
# print(obj.doubler(5))


# ======================= Дескриптор ============================

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def get(self):
#         return self.__value
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__value = value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     if not isinstance(value, str):
#     #         raise TypeError(f"{value} должно быть строкой")
#     #     self.__surname = value
#
#
# p = Person("Иван", "Петров")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())

# Дескриптор (__get__, __set__, __set_name__, __delete__)

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Петров")
# p.surname = "Иванов"
# # print(p.name)
# # print(p.surname)

# -------------------------------------------------------------


# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError(f"Значение {self.name} должно быть положительным")
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple_order = Order('apple', 5, 10)
# apple_order.quantity = 15
# print(apple_order.price)
# print(apple_order.total())
# print(apple_order.__dict__)

# ================= 08.04.2024 ====================

from car import electrocar


e_car = electrocar.ElectroCar("Tesla", "T", 2018, 99000)
e_car.show_car()
e_car.description_battery()
