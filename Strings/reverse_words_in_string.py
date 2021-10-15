def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        
        if character == " ":
            print('idx and character ', idx, character)
            words.append(string[startOfWord: idx])
            print('words', words)
            startOfWord = idx
            print('startWord on ln12', startOfWord)
            print('#############################################')
        elif string[startOfWord] == " ":
            print('Hi from elif', string[startOfWord])
            words.append(" ")
            print('words in 16  ', words)
            startOfWord = idx
            print('********************************************')
    
    words.append(string[startOfWord:])
    
    reverseList(words)
    return "".join(words)
            
def reverseList(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst


print(reverseWordsInString("Jefferson is     the best")) # "best the is Jefferson"
