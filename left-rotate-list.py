l=[10,20,30,40,50]
d=2

# l = l[d:]+l[:d]
# print(l)

from collections import deque
dq = deque(l)
dq.rotate(-d)
l = list(dq)
print (l)