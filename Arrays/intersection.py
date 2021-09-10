# O(n+m) Time | O(n) Space

def intersection(a, b):
    set_a = set(a)
    return [ item for item in b if item in set_a ]


# def intersection(a, b):
#   new_set = set(a)
#   i = 0
#   new_array = []
#   while i < len(b):
#     if b[i] in new_set:
#       new_array.append(b[i])
#     i += 1
#   return new_array
