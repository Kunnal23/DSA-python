import math

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class MyDeque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def insertFront(self,x):
        newNode = Node(x)
        if self.front == None:
            self.rear = newNode
        else:
            self.front.prev = newNode
            newNode.next = self.front
        self.front = newNode
        self.sz += 1

    def insertRear(self,x):
        newNode = Node(x)
        if self.rear == None:
            self.front = newNode
        else:
            self.rear.next = newNode
            newNode.prev = self.rear
        self.rear = newNode
        self.sz += 1

    def deleteFront(self):
        if self.front == None:
            return math.inf 
        else:
            val = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            self.sz -=1
            return val
        
    def deleteRear(self):
        if self.rear == None:
            return math.inf
        else:
            val = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            self.sz -=1
            return  val
        
    def getFront(self):
        if self.front == None:
            return math.inf
        return self.front.data
    
    def getRear(self):
        if self.rear == None:
            return math.inf
        return self.rear.data
    
    def isEmpty(self):
        return (self.sz == 0)
    
    def size(self):
        return self.sz
    

d = MyDeque()
d.insertFront(10)
d.insertFront(9)
d.insertRear(20)
print(d.getFront())
print(d.getRear())
print(d.size())
print(d.deleteFront())
print(d.deleteFront())
print(d.deleteFront())
d.insertRear(40)
print(d.deleteRear())
print(d.isEmpty())
d.insertRear(400)
d.insertRear(500)
print(d.size())
print(d.getFront())
print(d.getRear())