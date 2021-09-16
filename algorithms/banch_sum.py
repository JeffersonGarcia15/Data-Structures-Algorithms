class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def branch_sum(root):
    values = []
    branch_sum_helper(root, 0, values)
    return values

def branch_sum_helper(current, currentSum, values):
    if current is None:
        return
    new_sum = currentSum + current.value
    if current.left is None and current.right is None:
        values.append(new_sum)
        return
    branch_sum_helper(current.left, new_sum, values)
    branch_sum_helper(current.right, new_sum, values)
