# For iterative solution
# Time = O(N) where N is the number of nodes because we explore every node, swap, and insert them in queue
# All of them are constant operations 
# Space = O(N) because all of the bottom nodes were in the queue

# For recursive
# Time = O(N) because we explore all nodeToInsert
# Space = O(d) where d is the depth of the tree

# Iterative
# def invertBinaryTree(tree):
#     queue = [tree]
#     while len(queue):
#         current = queue.pop(0)
#         if current is None:
#             continue
#         swapLeftAndRight(current)
#         queue.append(current.left)
#         queue.append(current.right)
        
# def swapLeftAndRight(tree):
#     tree.left, tree.right = tree.right, tree.left

def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None 
        self.right = None 