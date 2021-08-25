class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# O(n) Time | O(1) Space
def reverse_list(head):
    current = head
    prev = None
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# O(n) Time | O(n) Space
# def reverse_list(head, prev = None):
#     if head is None:
#         return prev
#     next = head.next
#     head.next = prev
#     return reverse_list(next, head)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a))  # f -> e -> d -> c -> b -> a
