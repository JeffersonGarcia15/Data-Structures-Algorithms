class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def cycle_check(node):
    current = node
    while current is not None:
        if current.next is None:
            return False
        if current.next.value == node.value:
            return True
        # elif 
        current = current.next
    # return False
    

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a
print(cycle_check(a)) # True

x = Node(1)
y = Node(2)
z = Node(3)

x.next = y
y.next = z
print(cycle_check(x)) #False
