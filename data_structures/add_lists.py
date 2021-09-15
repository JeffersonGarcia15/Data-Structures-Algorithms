class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def add_lists(head_1, head_2):
    current_1 = head_1
    current_2 = head_2
    carry = 0
    dummy_head = Node(None)
    tail = dummy_head
    
    while current_1 is not None or current_2 is not None or carry == 1:
        val_1 = 0 if current_1 is None else current_1.value
        val_2 = 0 if current_2 is None else current_2.value
        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10
        
        if current_1 is not None:
            current_1 = current_1.next
        if current_2 is not None:
            current_2 = current_2.next
        tail.next = Node(digit)
        tail = tail.next
    return dummy_head.next