def isSorted(l):
    n = len(l)
    i=1
    while i<n:
        if l[i]<l[i-1]:
            return False
        i=i+1
    return True


l = [10,20,30,40]
print(isSorted(l))

# Method-2
def isSorted(l):
    sl=sorted(l)
    if sl==l:
        return True
    else:
        return False