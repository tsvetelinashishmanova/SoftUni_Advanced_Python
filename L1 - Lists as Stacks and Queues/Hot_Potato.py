from collections import deque

queue = deque(input().split(" "))
n_toss = int(input()) - 1

while len(queue) != 1:
    queue.rotate(-n_toss)
    print(f"Removed {queue.popleft()}")

print(f"Last is {queue[0]}")
