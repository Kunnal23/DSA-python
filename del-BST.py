class Node:
    def _init_(self,k):
        self.key=k
        self.left=None
        self.right=None

def delNode(root,key):
    if root==None:
        return
    if root.key>key:
        root.left=delNode(root.left,key)
    elif root.key<key:
        root.right=delNode(root.right,key)
    else:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            succ=getSucc(root.right,key)
            root.key=succ
            root.right=delNode(root.right,succ)
        return root

def getSucc(curr,key):
    while curr.left!=None:
        curr=curr.left
    return curr.key