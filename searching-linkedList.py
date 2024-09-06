class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2
temp2.next = temp3
head = temp1

def searchList(head,x):
    i=1
    curr = head
    while curr != None:
        if curr.key == x:
            return i
        curr = curr.next
        i+=1
    return -1


print(searchList(head,40))