class MyDeque:
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
        
    def insertRear(self,x):
        if self.sz == self.cap:
            return
        else:
            rear = (self.front+self.sz-1)%self.cap
            self.l[rear]= x
            self.sz+=1

    def insertFront(self,x):
        if self.sz == self.cap:
            return
        else:
            self.front = (self.front-1)%self.cap
            self.l[self.front]= x
            self.sz += 1

    def deleteFront(self):
        if self.sz == 0:
            return None
        else:
            res = self.l[self.front]
            self.front = (self.front+1)%self.cap
            self.sz -= 1
            return res
    
    def deleteRear(self):
        if self.sz == 0:
            return None
        else:
            rear = (self.front+self.sz-1)%self.cap
            res = self.l[rear]

            self.sz -= 1
            return res

    def size(self):
        return self.sz
    
    def isEmpty(self):
        return (self.sz == 0)

    def isFull(self):
        return (self.sz==self.cap)

q = MyDeque(5)
q.insertFront(10)
q.insertFront(20)
q.insertFront(30)
print(q.deleteRear())
print(q.size())
q.insertRear(40)
print(q.deleteFront())
print(q.getFront())
print(q.getRear())
print(q.isEmpty())
print(q.isFull())