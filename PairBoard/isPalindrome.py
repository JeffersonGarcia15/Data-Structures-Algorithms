# O(n^2) time | O(n) space
# def isPalindrome(string):
#     reversedString = ''
#     for i in reversed(range(len(string))):
#         print('This is to understand the mess', string)
#         print('This is the string[i]', string[i])
#         reversedString += string[i]
#         print('reversedString', reversedString)
#     return string == reversedString

# O(n) time | O(n) space
# def isPalindrome(string):
#     reversedChars = []
#     for i in reversed(range(len(string))):
#         reversedChars.append(string[i])
#         print('reversedString', reversedChars)
#     return string == "".join(reversedChars)

# O(n) time | O(n) space
# def isPalindrome(string, i=0):
#     j = len(string) - 1 - i
#     print('This is j', j)
#     print('word of j', string[j])
#     print('IIIIIIIi', i)
#     print('string[i]', string[i])
#     return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# O(n) time | O(1) space
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True


print(isPalindrome('abcdcba'))
