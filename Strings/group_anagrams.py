# O(wnlogn) where w is the number of words we have to iterate, and nlogn is there because we are using sorted()
# O(wn) Space where w is the number of words and n is the length longest word 

def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWords = "".join(sorted(word))
        if sortedWords in anagrams:
            anagrams[sortedWords].append(word)
        else:
            anagrams[sortedWords] = [word]
    return list(anagrams.values())
        
print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"])) # [['yo', 'oy'], ['flop','olfp'], ['act', 'tac','cat'], ['foo']]