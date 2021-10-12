#O(n) Time | O(n) Space

def runLengthEncoding(string):
    encodedCharactersList = []
    characterCounter = 1
    
    for i in range(1, len(string)):
        currentCharacter = string[i]
        previousCharacter = string[i - 1]
        
        if currentCharacter != previousCharacter or characterCounter == 9:
            encodedCharactersList.append(str(characterCounter))
            encodedCharactersList.append(previousCharacter)
            characterCounter = 0
        characterCounter += 1
    encodedCharactersList.append(str(characterCounter))
    encodedCharactersList.append(string[len(string) - 1])

    return "".join(encodedCharactersList)