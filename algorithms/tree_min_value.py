import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def tree_min_value(root):
    stack = [ root ]
    min_value = math.inf
    while stack:
        current = stack.pop()
        if current.value < min_value:
            min_value = current.value
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return min_value


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1
print(tree_min_value(a))  # -> -2
