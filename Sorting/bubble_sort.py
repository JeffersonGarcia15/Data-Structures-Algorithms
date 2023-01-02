# O(n^2) Time, O(1) Space
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in reversed(range(i + 1,len(lst))):
            if (lst[j] < lst[j - 1]):
                (lst[j], lst[j - 1]) = (lst[j - 1], lst[j])
    return lst