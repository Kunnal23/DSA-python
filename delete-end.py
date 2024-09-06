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

def printList(head):
    i = head
    while i != None:
        print(i.key, end=' ')
        i = i.next



def deleteEnd(head):
    if head == None or head.next == None:
        return None
    curr = head
    while curr.next.next != None:
        curr = curr.next   
    curr.next = None
    return head

# def insertBeginning(head,key):
#     temp = Node(key)
#     temp.next = head
#     return temp

# def deleteBeginning(head):
#     if head == None:
#         return None
#     else:
#         return head.next

# printList(head)
head = deleteEnd(head)
printList(head)

