class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
            
    def insertBefore(self, nodeToInsert):
        new_node = Node(nodeToInsert)
        new_node.next = self.head
        self.head = new_node
        
    def insertAfter(self, nodeToInsert):
        new_node = Node(nodeToInsert)
        if self.head is None:
            self.head = new_node
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = new_node
        
    def insertInBetween(self, middle ,nodeToInsert):
        if middle is None:
            return
        new_node = Node(nodeToInsert)
        new_node.next = middle.next
        middle.next = new_node
        
    def remove(self, nodeToRemove):
        currentNode = self.head
        
        if currentNode is not None:
            if currentNode.value == nodeToRemove:
                self.head = currentNode.next
                currentNode = None 
                return
            
        while currentNode is not None:
            if currentNode.value == nodeToRemove:
                break
            prev = currentNode.next
            currentNode = currentNode.next
        if currentNode == None:
            return
        prev.next = currentNode.next
        currentNode = None
            
list = SinglyLinkedList()
list.head = Node("Jeff")
list2 = Node("Adilson")
list3 = Node("Lopez")

list.head.next = list2
list2.next = list3
list.insertBefore('Jefferson')
list.insertAfter('Garcia')
list.insertInBetween(list.head.next, 'Jeeeeeeeff')
list.remove('Adilson')

list.traversal()
        