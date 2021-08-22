import math
# O(n) time | O(1) space
def max_value(nums):
    max = - math.inf
    for i in range(len(nums)):
        current = nums[i]
        if current > max:
            max = current
    return max

# Tests
print(max_value([-4,1,2,9,3]))