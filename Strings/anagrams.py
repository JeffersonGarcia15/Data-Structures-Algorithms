# def anagrams(s1, s2):
#     return char_count(s1) == char_count(s2)

# def char_count(s):
#     count = {}
    
#     for char in s:
#         if char not in count:
#             count[char] = 0
#         count[char] += 1
#     return count

# O(n + m) Time | O(n + m) Space
# from collections import Counter

# def anagrams(s1, s2):
#     return Counter(s1) == Counter(s2)
from collections import Counter
def anagrams(s1, s2):
    return Counter(s1) == Counter(s2)


print(anagrams('cats', 'tacs'))
print(anagrams('cats', 'cars'))
