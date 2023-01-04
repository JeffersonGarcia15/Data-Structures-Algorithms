# O(nlogn) Time and O(logn) Space complexity
def quick_sort_lomuto_partitioning(lst):
    def helper(lst, start, end):
        # Leaf level worker
        if start >= end:
            return
        # Internal level worker
        # Partitioning
        smaller_pointer = start
        for bigger_pointer in range(start + 1, end + 1):
            if lst[bigger_pointer] < lst[start]:
                smaller_pointer += 1
                lst[bigger_pointer], lst[smaller_pointer] = lst[smaller_pointer], lst[bigger_pointer]
        lst[smaller_pointer], lst[start] = lst[start], lst[smaller_pointer]
        
        # Divide step
        helper(lst, start, smaller_pointer - 1)
        helper(lst, smaller_pointer + 1, end)
    
    helper(lst, 0, len(lst) - 1)
    return lst

# p[1, 2, 3, 4] pivot_pointer < start => start = 0, end = -1 so start > end
# [1, 2, 3, 4]p pivot_pointer > end start = 7, end = 6 so start > end