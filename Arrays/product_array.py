# O(n) Time | O(n) Space
def product_array(nums):
    products = [1 for _ in range(len(nums))]

    left_current_product = 1
    for i in range(len(nums)):
        products[i] = left_current_product
        left_current_product *= nums[i]

    right_current_product = 1
    for i in reversed(range(len(nums))):
        products[i] *= right_current_product
        right_current_product *= nums[i]

    return products
