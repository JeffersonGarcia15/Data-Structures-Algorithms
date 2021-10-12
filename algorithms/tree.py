class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self, root):
        self.root = root
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return self
        else:
            current = self.root
            while current is not None:
                if value is current.value:
                    return None
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        return self
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        return self
                    current = current.right

tree = BinarySearchTree(10)
# tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(11)
tree.insert(2)
tree.insert(16)
tree.insert(7)

