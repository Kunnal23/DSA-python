#  i/p: l=[10,20,30,40]
#  o/p: 25.0

#  i/p: l= [30,60,40]
#  o/p: 43.33

def meanList(l):
    sum = 0
    n = len(l)
    for x in l:
        sum+=x
    avg = sum/n
    return avg

l=[10,20,30,40]
print(meanList(l))

l= [30,60,40]
print(meanList(l))


# Using In-built Function
def avgList(l):
    return sum(l)/len(l)

l= [30,60,40]
print(avgList(l))