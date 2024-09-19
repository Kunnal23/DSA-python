from collections import deque
class MyDS:
    def __init__(self):
        self.dq = deque()
    
    def insertMin(self,x):
        self.dq.appendleft(x)

    def insertMax(self,x):
        self.dq.append(x)

    def getMin(self):
        return self.dq[0]
    
    def getMax(self):
        return self.dq[-1]
    
    def extractMin(self):
        return self.dq.popleft()

    def extractMax(self):
        return self.dq.pop()
    
d = MyDS()
d.insertMax(10)
d.insertMin(2)

print(d.getMax())
print(d.getMin())
print(d.extractMin())
# print(d.extractMax())
# print(d.getMin())