def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = 0
    j = len(numbers) - 1
    while i < j:
        if (numbers[j] + numbers[i]) == target:
            return [i, j]
        elif (numbers[j] + numbers[i]) > target:
            j -= 1
        else:
            i += 1
    return [-1, -1]
