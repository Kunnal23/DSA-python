class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def itrSearchBST(root,key):
    curr = root
    while curr is not None:
        if curr.key == key:
            return True
        if key > curr.key:
            curr = curr.right
        else:
            curr = curr.left
    return False

def searchBST(root,key):
    if root is None:
        return False
    elif root.key == key:
        return True
    elif root.key > key:
        return searchBST(root.left,key)
    else:
        return searchBST(root.right,key)

root = Node(10)
root.left = Node(5)
root.right = Node(30)
print(itrSearchBST(root,30))