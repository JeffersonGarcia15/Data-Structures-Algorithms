# O(n) time | O(1) space
# def validateSubsequence(array, subsequence):
#     arrIdx = 0
#     seqIdx = 0
#     while arrIdx < len(array) and seqIdx < len(subsequence):
#         if array[arrIdx] == subsequence[seqIdx]:
#             seqIdx += 1
#             print('seqIdx', seqIdx)
#         arrIdx += 1
#     return seqIdx == len(subsequence)

def validateSubsequence(array, subsequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(subsequence):
            break
        if subsequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(subsequence)

print(validateSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]))