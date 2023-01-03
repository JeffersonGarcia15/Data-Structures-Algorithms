# O(nlog(n)) Time, O(n) Space
def merge_sort(lst):
    def helper(lst, start, end):
        # Leaf level worker
        if start == end:
            return
        # Internal Worker
        mid = (end + start) // 2
        helper(lst, start, mid)
        helper(lst, mid + 1, end)
        auxiliary_list = []
        i = start
        j = mid + 1
        while i <= mid and j <= end:
            if lst[i] < lst[j]:
                auxiliary_list.append(lst[i])
                i += 1
            else:
                auxiliary_list.append(lst[j])
                j += 1
        while i <= mid:
            auxiliary_list.append(lst[i])
            i += 1
        while j <= end:
            auxiliary_list.append(lst[j])
            j += 1
        
        lst[start:end + 1] = auxiliary_list
    helper(lst, 0, len(lst) - 1)
    return lst
        
        
"""
        O       0
      /   \     
     O     O    1
   /  \   /  \
  O    O O    O 2  
    O <---
     
  O O O O O O O h    
[1, 3, 4, 6] [2, 5, 7]
"""
# def merge_sort(array):
    
#     if len(array) <= 1:
#         return array
#     auxiliaryArray = array[:]
#     mergeSortHelper(array, 0, len(array) - 1, auxiliaryArray)
#     return array

# def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
#     if startIdx == endIdx:
#         return
#     middleIdx = (startIdx + endIdx) // 2
#     mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
#     mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
#     doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)

# def doMerge(mainArray, startIdx, middleIdx,endIdx, auxiliaryArray):
#     k = startIdx
#     i = startIdx
#     j = middleIdx + 1
#     print(auxiliaryArray)
    
#     while i <= middleIdx and j <= endIdx:
#         if auxiliaryArray[i] <= auxiliaryArray[j]:
#             mainArray[k] = auxiliaryArray[i]
#             i += 1
#         else:
#             mainArray[k] = auxiliaryArray[j]
#             j += 1
#         k += 1
#     while i <= middleIdx:
#         mainArray[k] = auxiliaryArray[i]
#         i += 1
#         k += 1
#     while j <= endIdx:
#         mainArray[k] = auxiliaryArray[j]
#         j += 1
#         k += 1
                