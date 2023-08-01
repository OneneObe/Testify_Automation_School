""" Create a program that prints out the odd numbers in an
array. Sample array: a. [1, 2, 3, 4, 5, 6] b. [ 34, 2, 9, 91, 19,
401, 0 ]
"""


def print_odd(num):
    odd_num = []
    for i in num:
        if i % 2 != 0:
            odd_num.append(i)

    print(odd_num)


print_odd([1, 2, 3, 4, 5, 6])
print_odd([34, 2, 9, 91, 19, 401, 0])
