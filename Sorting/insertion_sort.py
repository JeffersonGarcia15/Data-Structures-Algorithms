# In average O(n^2) Time and O(1) Space
def insertion_sort(lst):
    for i in range(len(lst)):
        previous_value = i - 1
        temp = lst[i]
        while previous_value >= 0 and temp < lst[previous_value]:
            lst[previous_value + 1] = lst[previous_value]
            previous_value -= 1
        lst[previous_value + 1] = temp
    return lst
