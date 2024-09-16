#set insertion
s = {10,20}
s.add(30)
print(s)
s.add(30)
print(s)
s.update([40,50])
print(s)
s.update({60,70},[80,90])
print(s)

#set removal
s = {10,20,30,40}
s.discard(30)
print(s)
s.remove(20)
print(s)
s.clear()
print(s)
s.add(50)
del s

s={10,30,20,40}
print(len(s))
print(20 in s)
print(50 in s)
