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

#Method-1
def reverseList(head):
    if head == None or head.next == None:
        return head
    rest_head = reverseList(head.next)
    res_tail = head.next
    res_tail.next = head
    head.next= None
    return rest_head

#Method-2
def reverseList2(curr,prev=None):
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return reverseList2(next,curr)


head = reverseList2(head)
printList(head)