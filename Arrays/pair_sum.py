# O(n) time | O(n) Space
def pair_sum(numbers, target_sum):
    # nums = {}
    # for index, num in enumerate(numbers):
    #     currentSum = target_sum - num
    #     if currentSum in nums:
    #         return (nums[currentSum], index)
    #     nums[num] = index
    #     print(nums)
    dict = {}
    count = 0
    i = 0
    while i < len(numbers):
        complement = target_sum - numbers[i] # 5 6 3
        if complement in dict:
            return (dict[complement], count)
        dict[numbers[i]] = count # {3:0, 2:1}
        count += 1
        i += 1
        
print(pair_sum([3,2,5,4,1], 8))