class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

# temp1 = Node(10)
# temp2 = Node(20)
# temp3 = Node(30)
# temp1.next = temp2
# temp2.next = temp3
# head = temp1
# tail = temp3

def printList(head):
    i = head
    while i != None:
        print(i.key, end=' ')
        i = i.next

def insertBeginning(head,key):
    newNode = Node(key)
    newNode.next = head
    return newNode

def insertEnd(head,key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head

# printList(head)
head = None
head = insertBeginning(head,40)
head = insertEnd(head,50)
printList(head)