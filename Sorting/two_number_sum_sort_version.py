# Brute Force: O(n^2) Time and O(1) Auxiliary Space
# def two_number_sum_sort_version(lst, target):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] + lst[j] == target:
#                 return [lst[i], lst[j]]
#     return []

# # Transform and conquer - Presorting - Input rearrangement: Time O(nlogn) Space O(1)
# def two_number_sum_sort_version(lst, target):
#     lst.sort()
#     i = 0
#     j = len(lst) - 1
    
#     while i < j:
#         if lst[i] + lst[j] == target:
#             print(lst[i], lst[j])
#             return [lst[i], lst[j]]
#         elif lst[i] + lst[j] < target:
#             i += 1
#         else:
#             j -= 1
#     return []

# Transform and conquer - Representation change - Hash-Table: Time O(n) Space O(n)
def two_number_sum_sort_version(lst, target):
    hashSet = set()
    for number in lst:
        if number not in hashSet:
            hashSet.add(number)
        if (target - number) in hashSet:
            return [target - number, number]
    return []
            
# print(two_number_sum_sort_version([5, 4, 1, 2], 5))