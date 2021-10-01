# O(n) Time because we are iterating, O(min(n, a)) where n is the length of the string, and a is the number of unique characters in the string
def non_repeating_substring(string):
    if string == '':
        return 0
    visited = {}
    longest = [0, 1]  # starts at idx 0 and ends at idx 0 if only 1 char
    left = 0
    for i, character in enumerate(string):
        if character in visited:
            # To know where pointer will move once a duplicate char is found
            left = max(left, visited[character] + 1)
        if longest[1] - longest[0] < i + 1 - left:
            longest = [left, i + 1]
        visited[character] = i
    return longest[1] - longest[0]
