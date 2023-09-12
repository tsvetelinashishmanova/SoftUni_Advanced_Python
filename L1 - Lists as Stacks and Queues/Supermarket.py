from collections import deque

queue = deque()
command = input()

while command != "End":
    if command == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)
    command = input()

print(f"{len(queue)} people remaining.")
