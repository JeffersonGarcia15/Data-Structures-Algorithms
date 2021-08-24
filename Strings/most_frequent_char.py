from collections import Counter
# O(n) time | O(n) space
def most_frequent_char(s):
    count = Counter(s)
    max = None
    
    for i in s:
        if max is None or count[i] > count[max]:
            max = i
    return max