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
# head = None

def printList(head):
    i = head
    while i != None:
        print(i.data, end=' ')
        i = i.next
    print("\n")

def insertEnd(head,x):
    newNode = Node(x)
    if head == None:
        return newNode
    else:
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr
        return head

printList(head)
head = insertEnd(head,5)
head = insertEnd(head,50)
printList(head)
