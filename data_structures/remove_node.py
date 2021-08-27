# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# O(n) Time | O(1) Space
def remove_node(head, target_val):
    if head.val == target_val:
        return head.next
    prev = None
    current = head
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        prev = current
        current = current.next
    return head


x = Node("x")
y = Node("y")
z = Node("z")

x.next = y
y.next = z

# x -> y -> z

print(remove_node(x, "z"))
# x -> y
