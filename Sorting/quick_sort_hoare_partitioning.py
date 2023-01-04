# O(nlogn) Time and O(logn) Space complexity
def quick_sort_hoare_partitioning(lst):
    def helper(lst, start, end):
        # Leaf level worker
        if start >= end:
            return
        # Partitioning
        smaller = start + 1
        bigger = end
        while smaller <= bigger:
            if lst[smaller] < lst[start]:
                smaller += 1
            elif lst[bigger] > lst[start]:
                bigger -= 1
            else:
                lst[smaller], lst[bigger] = lst[bigger], lst[smaller]
                smaller += 1
                bigger -= 1
        lst[start], lst[bigger] = lst[bigger], lst[start]
        
        # Divide
        helper(lst, start, bigger - 1)
        helper(lst, smaller, end)
    
    helper(lst, 0, len(lst) - 1)
    return lst

print(quick_sort_hoare_partitioning([3, 4, 4, 6, 2, 5, 7]))