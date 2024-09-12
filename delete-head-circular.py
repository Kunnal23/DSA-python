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
# head = None

def printCircular(head):
    if head == None :
        return
    print (head.key , end=" ")
    curr = head.next
    while curr != head:
        print(curr.key , end = " ")
        curr =curr.next

#Method-1
def delHead(head):
    if head.next == head or head == None:
        return None
    else:
        curr = head
        while curr.next != head:
            curr = curr.next
        curr.next = head.next
        return curr.next
    
#Method-2
def delHead2(head):
    if head.next == head or head == None:
        return None
    else:
        head.key = head.next.key
        head.next = head.next.next
        return head

printCircular(head)
print("\n")
head = delHead2(head)
printCircular(head)
