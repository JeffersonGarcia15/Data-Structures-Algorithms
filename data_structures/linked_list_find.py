class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# O(n) Time | O(1) Space
def linked_list_find(head, target):
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next
    return False

# O(n) Time | O(n) Space
# def linked_list_find(head, target):
#     if head is None:
#         return False
#     if head.value == target:
#         return True
#     return linked_list_find(head.next, target)



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(linked_list_find(a, "c"))  # True
