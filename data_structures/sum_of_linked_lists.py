class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    total_1 = 0
    total_2 = 0
    current_1 = linkedListOne
    current_2 = linkedListTwo
    while current_1 is not None or current_2 is not None:
        if current_1 is not None:
            total_1 += current_1.value
        if current_2 is not None:
            total_2 += current_2.value
        current_1 = current_1.next
        current_2 = current_2.next
    return total_1 + total_2