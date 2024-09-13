class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)
head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1

def insertBeg(head,x):
    newNode = Node(x)
    if head == None:
        return newNode
    else:
        curr = head
        newNode.next=curr
        curr.prev = newNode
        return newNode

def insertBeg2(head,x):
    newNode = Node(x)
    if head != None:
        head.prev = newNode
    newNode.next = head
    return newNode
    


def printList(head):
    i = head
    while i != None:
        print(i.data, end=' ')
        i = i.next
    print("\n")

printList(head)
head = insertBeg2(head,5)
head = insertBeg2(head,50)
printList(head)