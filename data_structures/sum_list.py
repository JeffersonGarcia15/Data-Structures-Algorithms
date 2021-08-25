class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(1) Space
# def sum_list(head):
#     currentNode = head
#     sum = 0
#     while currentNode is not None:
#         sum += currentNode.value
#         currentNode = currentNode.next
#     return sum

# O(n) Time | O(n) Space
def sum_list(head):
    if head is None:
        return 0
    return head.value + sum_list(head.next)

a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e

# 2 -> 8 -> 3 -> -1 -> 7

print(sum_list(a))  # 19
