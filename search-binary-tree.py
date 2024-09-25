import math
class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def searchkey(root,key):
    if root == None:
        return False
    elif root.key == key:
        return True
    elif searchkey(root.left,key)==True:
        return True
    else:
        return searchkey(root.right,key)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print(searchkey(root,50))