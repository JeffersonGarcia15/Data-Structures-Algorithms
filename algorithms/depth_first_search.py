class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
def depth_first_search(root):
    if root is None:
        return []
    stack = [ root ]
    values = []
    while stack:
        current = stack.pop()
        values.append(current.value)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    return values
        
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
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

print(depth_first_search(a))
#   -> ['a', 'b', 'd', 'e', 'c', 'f']
