class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
# O(min(n, m)) Time | O(1) Space
def zipper_lists(head_1, head_2):
    tail = head_1
    current_h1 = head_1.next
    current_h2 = head_2
    count = 0
    while current_h1 is not None and current_h2 is not None:
        if count % 2 == 0:
            tail.next = current_h2
            current_h2 = current_h2.next
        else:
            tail.next = current_h1
            current_h1 = current_h1.next
        tail = tail.next
        count += 1
    if current_h1 is not None:
        tail.next = current_h1
    if current_h2 is not None:
        tail.next = current_h2
    return head_1

# O(min(n, m)) Time | O(min(n, m)) Space
# def zipper_lists(head_1, head_2):
#     if head_1 is None and head_2 is None:
#         return None
#     if head_1 is None:
#         return head_2
#     if head_2 is None:
#         return head_1
#     next_1 = head_1.next
#     next_2 = head_2.next
#     head_1.next = head_2
#     head_2.next = zipper_lists(next_1, next_2)
#     return head_1

#  a -> b -> c
#  h1  n1

#  x -> y -> z
#  h2  n2

#  a -> x ->  result of zipper_lists(next_1, next_2)

#  b -> c 
#  h1   n1

#  y -> z
#  h2   n2

#  a -> x -> b -> y ... returning to the parent