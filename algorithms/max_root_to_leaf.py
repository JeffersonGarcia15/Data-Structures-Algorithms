class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_path_sum(root):
    if root is None:
        return float("-inf")
    if root.left is None and root.right is None:
        return root.value
    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)

    return root.value + max(max_left, max_right)


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

print(max_path_sum(a))  # -> 18
