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

def printCircular(head):
    if head == None :
        return
    print (head.key , end=" ")
    curr = head.next
    while curr != head:
        print(curr.key , end = " ")
        curr =curr.next
printCircular(head)