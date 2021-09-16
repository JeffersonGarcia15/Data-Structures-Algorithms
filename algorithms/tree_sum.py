class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def tree_sum(root):
    if root is None:
        return 0
    stack = [ root ]
    total = 0
    while stack:
        current = stack.pop()
        total += current.value
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return total


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

print(tree_sum(a))  # -> 21
