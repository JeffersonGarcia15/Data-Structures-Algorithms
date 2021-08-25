# O(n) time | O(n) Space
def pair_sum(numbers, target_sum):
    nums = {}
    for index, num in enumerate(numbers):
        currentSum = target_sum - num
        if currentSum in nums:
            return (nums[currentSum], index)
        nums[num] = index
        
print(pair_sum([3,2,5,4,1], 8))