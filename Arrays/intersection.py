# O(n+m) Time | O(n) Space

def intersection(a, b):
    set_a = set(a)
    return [ item for item in b if item in set_a ]