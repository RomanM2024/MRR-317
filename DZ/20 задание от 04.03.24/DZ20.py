n = [-2, 3, 8, -11, -4, 6]


def countN(lst):
    size = len(lst)
    if size > 1:
        mid = size // 2
        return countN(lst[:mid]) + countN(lst[mid:])
    if size == 1 and lst[0] < 0:
        return 1
    return 0


print(countN(n))


