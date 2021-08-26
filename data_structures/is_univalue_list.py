# O(n) Time | O(1) Space
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
def is_univalue_list(head):
    current = head
    while current is not None:
        if current.val == head.val:
            current = current.next
        else:
            return False
    return True
