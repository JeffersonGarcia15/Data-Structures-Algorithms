class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

# O(n) Time | O(1) Space
def longest_streak(head):
    count = 0
    max_streak = 0
    prev = None
    current = head
    while current is not None:
        if current.val == prev:
            count += 1
        else:
            count = 1
        prev = current.val
        if count > max_streak:
            max_streak = count
        current = current.next
    return max_streak
            

a = Node(5)
b = Node(5)
c = Node(7)
d = Node(7)
e = Node(7)
f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# 5 -> 5 -> 7 -> 7 -> 7 -> 6

print(longest_streak(a))  # 3
