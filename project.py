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
#    свойства (поля, переменные)
#     - статические
#     - динамические
#    методы (функции)
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

# -----------------------------------------------------


