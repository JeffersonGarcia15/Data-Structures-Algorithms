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

# def linked_list_values(head):
#     new_list = []
#     helper(head, new_list)
#     return new_list

# def helper(head, new_list):
#     if head is None:
#         return
#     new_list.append(head.value)
#     helper(head.next, new_list)

