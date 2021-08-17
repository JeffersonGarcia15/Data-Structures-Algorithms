# O(log(n)) time | O(log(n)) space

# def binarySearch(lst, target):
#     return binarySearchHelper(lst, target, 0, len(lst) - 1)

# def binarySearchHelper(lst, target, left, right):
#     if left > right:
#         return -1
#     middle = (left + right) // 2
#     potentialMatch = lst[middle]
#     if potentialMatch == target:
#         return middle
#     elif target < potentialMatch:
#         return binarySearchHelper(lst, target, left, middle - 1)
#     else:
#         return binarySearchHelper(lst, target, middle + 1, right)
    
# O(log(n)) time | O(1) space

def binarySearch(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = lst[middle]
        if potentialMatch == target:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1


print(binarySearch([1,2,3,4,5,6,7], 2))