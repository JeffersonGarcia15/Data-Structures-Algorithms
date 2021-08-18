# O(nlogn) time | O(n) space

# def sortedSquaredArray(array):
#     sortedSquares = [0 for _ in array]
    
#     for idx in range(len(array)):
#         value = array[idx]
#         sortedSquares[idx] = value * value
        
#     sortedSquares.sort()
#     return sortedSquares


def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]
        
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares
        