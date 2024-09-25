class Node:
    def __init__(self,k):
        self.key = k
        self.left = None
        self.right = None

def inorder(root):
    if root !=None:
        inorder(root.left)
        print(root.key , end=" ")
        inorder(root.right)

def preorder(root):
    if root !=None:
        print(root.key , end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root !=None:
        postorder(root.left)
        postorder(root.right)
        print(root.key , end=" ")

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)
print("Inorder :")
inorder(root)
print("\nPreorder :")
preorder(root)
print("\nPostorder :")
postorder(root)