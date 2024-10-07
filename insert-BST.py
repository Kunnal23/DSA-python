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

def insertBST(root,key):
    if root == None:
        return Node(key)
    elif root.key == key:
        return root
    elif root.key> key:
        root.left = insertBST(root.left,key)
    else:
        root.right = insertBST(root.right,key)
    return root

def insertBST(root,key):
    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.key == key:
            return root
        if key > curr.key:
            curr = curr.right
        else:
            curr = curr.left
    if parent == None:
        return Node(key)
    elif parent.key>key:
        parent.left = Node(key)
    else:
        parent.right = Node(key)
    return root


root = None
# root.left = Node(5)
# root.right = Node(30)
root = insertBST(root,35)
root = insertBST(root,3)
print(itrSearchBST(root,3)) 