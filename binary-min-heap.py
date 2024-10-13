import math
class MyMinHeap:
    def __init__(self,l=[]): #Build Heap
        self.arr=l
        i = (len(l)-2)//2
        while i>= 0 :
            self.minHeapify(i)
            i=i-1

    def parent(self,i):
        return(i-1)//2
    def lChild(self,i):
        return (i*2+1)
    def rChild(self,i):
        return (i*2+2)


    def insert(self,x): #Insert
        arr=self.arr
        arr.append(x)
        i=len(arr)-1
        while i>0 and arr[self.parent(i)]>arr[i]:
            p=self.parent(i)
            arr[i],arr[p]=arr[p],arr[i]
            i=p

    def minHeapify(self,i):  #Heapification
        arr = self.arr
        lt = self.lChild(i)
        rt = self.rChild(i)
        smallest = i
        n = len(arr)
        if lt<n and arr[lt]< arr[smallest]:
            smallest = lt
        if rt<n and arr[rt]< arr[smallest]:
            smallest = rt
        if smallest != i:
            arr[smallest],arr[i] = arr[i],arr[smallest]
            self.minHeapify(smallest)

    def extractMin(self): #Extract Smallest value(root)
        arr =self.arr
        n = len(arr)
        if n == 0:
            return math.inf
        res = arr[0]
        arr[0]=arr[n-1]
        arr.pop()
        self.minHeapify(0)
        return res

    def decreaseKey(self, i, x):  #Exchange a particular key with a smaller value
        arr = self.arr
        arr[i] = x
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]
            i = p
        # If it's still not a valid heap, call minHeapify (in case of increase)
        # self.minHeapify(i) (Use this function to exchange Key with any Value)
        
    def deleteKey(self,i): #Delete a particular key
        n= len(self.arr)
        if i>n:
            return
        else:
            self.decreaseKey(i,-math.inf)
            self.extractMin()

    def delKey(self,i):  #Delete a particular key
        arr = self.arr
        arr[i]= arr[-1]
        arr.pop()
        self.minHeapify(i)

s=MyMinHeap([10,44,48,20,30,40,50,35,38,45])
# s.arr=[10,20,30,40,50,35,38,45]
s.delKey(3)
# s.decreaseKey(5,5)
# s.minHeapify(0)
# s.insert(12)
print(s.arr)
# s.extractMin()
# print(s.arr)