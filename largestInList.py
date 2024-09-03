def largest(l):
    l1 = sorted(l)
    return l1[-1]

# print(largest([1,20,10]))

def getMax(l):
    if not l:
        return None
    else:
        max = l[0]
        for x in l:
            if x > max:
                max=x
        return max
    
print(getMax([1,20,10]))