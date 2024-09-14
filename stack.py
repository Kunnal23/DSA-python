#Method-1 (Using List)
print('Using List:')
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
top = stack[-1]
print(top)
size = len(stack)
print(size)

#Method-2 (Using deque)
print('\nUsing deque:')
from collections import deque
stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
top = stack[-1]
print(top)
size = len(stack)
print(size)