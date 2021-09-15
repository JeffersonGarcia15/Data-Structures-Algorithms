class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def shift_linked_list(head, k):
    tail = head
    length = 1
    while tail.next is not None:
        length += 1
        tail = tail.next
    offset = abs(k) % length
    if offset == 0:
        return head
    new_tail_position = length - offset if k > 0 else offset
    new_tail = head
    for i in range(1, new_tail_position):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head
    