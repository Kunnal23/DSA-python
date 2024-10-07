class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def getFloorBST(root,key):
    curr = root
    res =None
    while curr is not None:
        if curr.key == key:
            return curr.key
        elif curr.key > key:
            curr = curr.left
        else:
            res = curr
            curr = curr.right
    return res.key

root = Node(10)
root.left = Node(5)
root.right = Node(30)
print(getFloorBST(root,10))
