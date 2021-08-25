class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# O(n) Time | O(1) Space
def get_node_value(head, index):
  current = head
  counter = 0

  while current is not None:
    if counter == index:
      return current.val
    current = current.next
    counter += 1

# O(n) Time | O(n) Space
# def get_node_value(head, index):
    # if head is None:
    #     return None
    # if index == 0:
    #     return head.val
    # return get_node_value(head.next, index - 1)


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2))  # 'c'
