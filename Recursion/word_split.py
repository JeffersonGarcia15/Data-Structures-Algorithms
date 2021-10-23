def wordSplit(phrase, listOfWords, output = None):
    if output is None:
        output = []
    for word in listOfWords:
        if phrase.startswith(word):
            output.append(word)
            return wordSplit(phrase[len(word):], listOfWords, output)
    return output