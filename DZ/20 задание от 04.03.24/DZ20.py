# n = [-2, 3, 8, -11, -4, 6]
#
#
# def countNegative(lst):
#     size = len(lst)
#     if size > 1:
#         mid = size // 2
#         return countNegative(lst[:mid]) + countNegative(lst[mid:])
#     if size == 1 and lst[0] < 0:
#         return 1
#     return 0
#
#
# print(countNegative(n))

def negative_numbers(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + negative_numbers(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative_numbers(lst))
