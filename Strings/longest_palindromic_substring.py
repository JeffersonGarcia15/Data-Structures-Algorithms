def longestPalindromicSubstring(string):
    currentLongestString = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestSubstring(string, i - 1, i + 1)
        even = getLongestSubstring(string, i - 1, i)
        possibleLongestString = max(odd, even, key = lambda x: x[1] - x[0]) 
        currentLongestString = max(currentLongestString, possibleLongestString, key = lambda x: x[1] - x[0])
    return string[currentLongestString[0] : currentLongestString[1]]
        
def getLongestSubstring(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]

print(longestPalindromicSubstring("abaxyzzyxf")) # "xyzzyx"
print(longestPalindromicSubstring("j"))  # "j"
# print("ab"[0:1])