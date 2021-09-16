class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
def breadth_first_search(root):
    if root is None:
        return []
    queue = [ root ]
    values = []
    while queue:
        current = queue.pop(0)
        values.append(current.value)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
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

print(breadth_first_search(a))
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
