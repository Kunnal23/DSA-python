import math
class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
# head -> front
# tail -> rear 

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sz = 0
    
    def enque(self,x):
        newNode =  Node(x)
        if self.head == None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.sz +=1

    def size(self):
        return self.sz
    
    def dequeue(self):
        if self.head == None:
            return math.inf
        else:
            val = self.head.data
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            self.sz-=1
            return val
    
    def isEmpty(self):
        return (self.sz==0)
    
    def getFront(self):
        if self.head == None:
            return math.inf
        return self.head.data
    
    def getRear(self):
        if self.head == None :
            return math.inf
        return self.tail.data

q = MyQueue()
q.enque(10)
q.enque(20)
q.enque(30)
print(q.dequeue())
print(q.size())
q.enque(40)
print(q.getFront())
print(q.getRear())
print(q.isEmpty())


