class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# O(n) Time | O(n) Space
def create_linked_list(values):
    temporary_head = Node(None)
    tail = temporary_head
    for new_node in values:
        tail.next = Node(new_node)
        tail = tail.next
    return temporary_head.next


print(create_linked_list(["h", "e", "y"]))

# h -> e -> y
