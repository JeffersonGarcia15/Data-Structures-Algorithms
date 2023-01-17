# O(k) Time and O(k) Auxiliary Space
# def raise_int_to_power(n, k):
#     if k == 0:
#         return 1
#     else:
#         return n * raise_int_to_power(n, k - 1)

# O(k) Time and O(1) Auxiliary Space
def raise_int_to_power(n, k):
    result = 1
    for _ in range(1, k + 1):
        result *= n
    return result