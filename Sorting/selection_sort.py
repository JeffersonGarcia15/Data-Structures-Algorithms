# O(n^2) Time, O(1) Space
def selection_sort(lst):
    for i in range(len(lst)):
        min_value = lst[i]
        min_index = i
        for j in range(i + 1, len(lst)):
            if (lst[j] < min_value):
                min_value = lst[j]
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst