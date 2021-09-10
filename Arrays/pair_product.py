# O(n) time | O(n) Space
def pair_product(numbers, target_product):
    # nums = {}
    # for index, num in enumerate(numbers):
    #     currentProduct = target_product // num
    #     if currentProduct in nums:
    #         return (nums[currentProduct], index)
    #     nums[num] = index 
    nums = {}
    i = 0
    count = 0
    while i < len(numbers):
        currentProduct = target_product // numbers[i]
        if currentProduct in nums:
            return (nums[currentProduct], count)
        nums[numbers[i]] = count
        i += 1
        count += 1