def onlyOdd(l):
    for x in l:
        y=l.count(x)
        if y%2!=0:
            return x
    else:
        return None
    

l=[10,20,30,40,10,20,30]
print(onlyOdd(l))

# Method-2 : Using Bitwise XOR(^)
# x^x = 0
# x^0 = x   
def findOdd(l):
    res = 0
    for x in l:
        res = res^x
    return res

print(findOdd(l))