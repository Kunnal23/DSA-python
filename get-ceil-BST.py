class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def getCeilBST(root,key):
    curr = root
    res =None
    while curr is not None:
        if curr.key == key:
            return curr.key
        elif curr.key > key:
            res = curr
            curr = curr.left
        else:
            curr = curr.right
    return res.key

root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.right.left = Node(25)
root.right.right = Node(50)
print(getCeilBST(root,40))
