class Node:
    def __init__(self,data):
        self.key = data
        self.next = None

temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp4 = Node(40)
head = temp1
temp1.next = temp2
temp2.next = temp3
temp3.next = temp4
temp4.next = head
tail = temp4
# head = None
def printCircular(head):
    if head == None :
        return
    print (head.key , end=" ")
    curr = head.next
    while curr != head:
        print(curr.key , end = " ")
        curr =curr.next

#Method-1 when tail is defined
def insertCircularBeginning(head,x):
    newNode = Node(x)
    if head == None:
        newNode.next = newNode
        return newNode
    newNode.next = head
    tail.next = newNode
    return newNode

#Method-2 (Time:Big-O(n))
def insertBeg(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next
    curr.next = temp
    temp.next = head
    return temp

#Method-3 (Time:Theta(1))
def insertBeg2(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    else:
        temp.next = head.next
        head.next = temp
        head.key,temp.key = temp.key,head.key
        return head

head = insertCircularBeginning(head,15)
head = insertBeg2(head,19)
printCircular(head)

