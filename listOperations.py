l = [10,20,30,40,50]

print(l)
print(l[3])
print(l[-1])
print(l[-2])

l.append(30)
print(l)

l.insert(1,15)
print(l)

print(15 in l)

print(l.count(30))
print(l.index(30))

print(l.index(30,4,7))


l.remove(20)
print(l)

print(l.pop())
print(l)

print(l.pop(2))
print(l)

del l[1]
print(l)
del l[0:2]
print(l)

l = [10,20,30,40,50]

print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)

# if l = [10,'geeks',30,'gfg',50] 
# max min sum and sort will not work only reverse will work