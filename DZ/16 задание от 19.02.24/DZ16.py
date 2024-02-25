
def avg(fn):
    def wrap(*arg):
        a = ""
        for i in arg:
            a += str(i) + ", "  # "2, 3, 3, 4, "
        print("Среднее арифметическое:", a[:-2], "=", fn(*arg) / len(arg))

    return wrap


@avg
def summa(*args):  # (2, 3, 3, 4)
    print("Сумма чисел:", ", ".join(map(str, args)), "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)
