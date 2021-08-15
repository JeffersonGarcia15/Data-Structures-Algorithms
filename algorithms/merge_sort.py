# Best, Average, Worst O(nlog(n)) space | O(nlog(n)) time

# def mergeSort(lst):
#     if len(lst) == 1:
#         return lst
#     middleIdx = len(lst) // 2
#     leftHalf = lst[:middleIdx]
#     rightHalf = lst[middleIdx:]
#     return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

# def mergeSortedArrays(leftHalf, rightHalf):
#     sortedArray = [None] * (len(leftHalf) + len(rightHalf))
#     k = i = j = 0
#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] <= rightHalf[j]:
#             sortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             sortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
#     while i < len(leftHalf):
#         sortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
#     while j < len(rightHalf):
#         sortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1
#     return sortedArray

# Best, Average, Worst O(nlog(n)) space | O(n) time

def mergeSort(lst):
    if len(lst) <= 1:
        return lst
    auxiliaryArray = lst[:]
    mergeSortHelper(lst, 0, len(lst) - 1, auxiliaryArray)
    return lst

def mergeSortHelper(mainArray, startIdx, endIdx, auxiliaryArray):
    if startIdx == endIdx:
        return
    middleIdx = (startIdx + endIdx) // 2
    mergeSortHelper(auxiliaryArray, startIdx, middleIdx, mainArray)
    mergeSortHelper(auxiliaryArray, middleIdx + 1, endIdx, mainArray)
    doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray)
    
def doMerge(mainArray, startIdx, middleIdx, endIdx, auxiliaryArray):
    k = startIdx
    i = startIdx 
    j = middleIdx + 1
    while i <= middleIdx and j <= endIdx:
        if auxiliaryArray[i] <= auxiliaryArray[j]:
            mainArray[k] = auxiliaryArray[i]
            i += 1
        else:
            mainArray[k] = auxiliaryArray[j]
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1

    

    
