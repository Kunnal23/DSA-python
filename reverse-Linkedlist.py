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


#Naive-Solution
def reverseLinkedList(head):
    stack =[]
    curr = head
    while curr != None:
        stack.append(curr.key)
        curr = curr.next
    curr =head
    while curr != None:
        curr.key = stack.pop()
        curr = curr.next
    return head

#Efficient Solution
def reverseList(head):
    curr = head
    prev = None

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

head = reverseList(head)
printList(head)