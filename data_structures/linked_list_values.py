class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# O(n) Time | O(n) Space
def linked_list_values(head):
    currentNode = head
    new_list = []
    while currentNode is not None:
        new_list.append(currentNode.value)
        currentNode = currentNode.next
    return new_list

