class MyQueue:
    def __init__(self,c):
        self.l = [None]*c
        self.cap = c
        self.sz = 0
        self.front = 0

    def getFront(self):
        if self.sz == 0:
            return None
        else:
            return self.l[self.front]
        
    def getRear(self):
        if self.sz == 0:
            return None
        else:
            rear = (self.front+self.sz-1)%self.cap
            return self.l[rear]
        
    def enque(self,x):
        if self.sz == self.cap:
            return
        else:
            rear = (self.front+self.sz-1)%self.cap
            rear =(rear+1)%self.cap
            self.l[rear]= x
            self.sz+=1

    def dequeue(self):
        if self.sz == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front+1)%self.cap
            self.sz -= 1
            return res
        
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return (self.sz == 0)
    
    def isFull(self):
        return (self.sz==self.cap)


q = MyQueue(5)
q.enque(10)
q.enque(20)
q.enque(30)
print(q.dequeue())
print(q.size())
q.enque(40)
print(q.getFront())
print(q.getRear())
print(q.isEmpty())
print(q.isFull())