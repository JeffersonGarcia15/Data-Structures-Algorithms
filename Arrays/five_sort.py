# O(n) Time | O(n) Space
def five_sort(nums):
    # left = 0
    # right = len(nums) - 1
    # while left < right:
    #     if nums[right] == 5:
    #         right -= 1
    #     elif nums[left] == 5:
    #         nums[left], nums[right] = nums[right], nums[left]
    #         left += 1
    #     else:
    #         left += 1
    # return nums
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] == 5 and nums[right] != 5:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[right] == 5:
            right -= 1
        if nums[left] != 5:
            left += 1
    return nums