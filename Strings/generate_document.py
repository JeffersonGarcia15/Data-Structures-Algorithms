from collections import Counter

def generateDocument(characters, document):
    charactersCounterObject = Counter(characters)
    
    for char in document:
        if char not in charactersCounterObject or charactersCounterObject[char] == 0:
            return False
        charactersCounterObject[char] -= 1
    return True