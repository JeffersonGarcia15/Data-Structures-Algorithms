# Write a method, digitalRoot(num). It should sum the digits of a positive integer. If it is greater than or equal to 10, sum the digits of the resulting number.
# Keep repeating until there is only one digit in the result, called the "digital root". Do not use string conversion within your method.
import math


def digitalRoot(num):
    while num >= 10:
        num = helperRoot(num)
    return num


def helperRoot(num):
    current_root = 0
    while num > 0:
        current_root += num % 10
        num = math.floor(num // 10)
    return current_root


# def digitalRoot(11):
#     while 11 >= 10:
#         num = helperRoot(11) Send num(11) to the helper
#     return num


# def helperRoot(11):
#     current_root = 0
#     while 11 > 0:
#         0 += num % 10 current_root = 1
#         num = math.floor(num // 10) num ==> 1
#     return current_root

# def digitalRoot(5):
#     while 5 >= 10: We just need to return because 5 is NOT >= 10
#         do something in here
#     return 5

# Example 1
print(digitalRoot(11)) # 2
# Example 2
print(digitalRoot(5)) # 5


