class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def findLoop(head):
    left = head.next
    right = head.next.next
    while left != right:
        left = left.next
        right = right.next.next
    left = head
    while left != right:
        left = left.next
        right = right.next
    return left