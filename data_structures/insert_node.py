class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def insert_node(head, value, index):
    value = Node(value)
    if index == 0:
        value.next = head
    count = 0
    current = head
    while current is not None:
        if count == index - 1:
            temp = current.next
            current.next = value
            current.next.next = temp
        count += 1
        current = current.next
    return head



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(insert_node(a, 'x', 2))
# a -> b -> x -> c -> d
