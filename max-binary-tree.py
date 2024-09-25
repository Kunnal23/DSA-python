import math
class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def getMax(root):
    if root == None:
        return -math.inf
    else:
        lm =getMax(root.left)
        rm =getMax(root.right)
        return max(root.key,lm,rm)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(getMax(root))