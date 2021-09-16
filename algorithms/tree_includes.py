class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def tree_includes(root, target):
    if root is None:
        return False
    stack = [ root ]
    while stack:
        current = stack.pop()
        if current.value == target:
            return True
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return False


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(tree_includes(a, "e"))  # -> True
