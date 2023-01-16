import random
def find_kth_largest_element(nums, k):
    def helper(nums, start, end, k):
        if start == end:
            return
        smaller = start
        pindex = random.randint(start, end)
        nums[pindex], nums[start] = nums[start], nums[pindex]
        for bigger in range(start + 1, end + 1):
            if nums[bigger] < nums[start]:
                smaller += 1
                nums[bigger], nums[smaller] = nums[smaller], nums[bigger]
        nums[start], nums[smaller] = nums[smaller], nums[start]
        if smaller == len(nums) - k:
            return nums[smaller]
        elif smaller < len(nums) - k:
            helper(nums, smaller + 1, end, k)
        else:
            helper(nums, start, smaller - 1, k)
    helper(nums, 0, len(nums) - 1, k)
    return nums[len(nums) - k]
print(find_kth_largest_element([3, 2, 1, 5, 6, 4], 2)) # 5
print(find_kth_largest_element([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)) # 4