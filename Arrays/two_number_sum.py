# O(n^2) time | O(1) space
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             print('keeping track of j', j)
#             secondNum = array[j]
#             print('value of secondNum', secondNum)
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []

# O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         if targetSum - num in nums:
#             return [targetSum - num, num]
#         else:
#             nums[num] = True
#     return []

# O(nlog(n)) time | O(1) space
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []



# print(twoNumberSum([3,5,-4,8,11,1,-1,6], 10))