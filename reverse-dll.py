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
    curr = head
    while curr != None:
        print(curr.data, end=' ')
        curr = curr.next
    print("\n")

def reverseDLL(head):
    if head == None or head.next == None:
        return head
    curr = head
    prev = None
    while curr != None:
        prev = curr
        curr.next ,curr.prev = curr.prev,curr.next
        curr = curr.prev
    return prev
printList(head)
head = reverseDLL(head)
printList(head)