from collections import deque

queue1 = deque(['A', 'B', 'C', 'D'])
queue2 = deque(['A', 'B', 'C', 'D'])

queue1.rotate(-1)
queue2.rotate(1)

print(queue1)
print(queue2)