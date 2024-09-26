from collections import deque
class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    q =deque()
    q.append(root)
    while len(q)>0:
        curr = q.popleft()
        print(curr.key)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(60)
root.left.left = Node(40)
root.left.right = Node(50)
printLevelOrder(root)