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
# head = Node(10)
# head.next = head

def printCircular(head):
    if head == None :
        return
    print (head.key , end=" ")
    curr = head.next
    while curr != head:
        print(curr.key , end = " ")
        curr =curr.next

def delHead(head):
    if head.next == head or head == None:
        return None
    else:
        head.key = head.next.key
        head.next = head.next.next
        return head
    
def deletePos(head,pos):
    if head == None:
        return None
    elif pos == 1:
        return delHead(head)
    else:
        curr =head
        for i in range(pos-2):
            curr = curr.next
        curr.next = curr.next.next
        return head


printCircular(head)
print('\n')
head = deletePos(head,2)
printCircular(head)