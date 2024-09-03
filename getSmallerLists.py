def getSmaller(l,x):
    res=[]
    for i in l:
        if i<x:
            res.append(i)
    return res

l=[10,20,30,40,50]
x=10
print(getSmaller(l,x))
