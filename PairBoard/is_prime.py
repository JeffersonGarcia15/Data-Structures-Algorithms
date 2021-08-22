import math
# O(n) time | O(1) space
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, (n)):
#         if n % i == 0:
#             return False
#     return True

# O(log(n)) time | O(1) space
def is_prime(n):
    if n < 2: return False
    for i in range(2, math.floor((math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))
