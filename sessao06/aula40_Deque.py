from collections import deque

deq = deque('geek')

print(deq)

deq.append('y')

print(deq)

deq.appendleft('Z')

print(deq)

deq.remove('Z')

print(deq)

deq.pop()

print(deq)