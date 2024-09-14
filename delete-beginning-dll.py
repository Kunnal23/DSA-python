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

def deleteBeg(head):
    if head == None or head.next == None:
        return None
    else:
        head.next.prev = None
        return head.next
    
printList(head)
head = deleteBeg(head)
printList(head)