def fio():
    names = input("Введите фамилию, имя, отчество: ").split()
    return f'{names[0]} {names[1][0]}.{names[2][0]}.'.title()


print(fio())
