from collections import deque

parenthesis = deque(input())
opening_parenthesis = deque()

while parenthesis:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in "({[":
        opening_parenthesis.append(current_parenthesis)
    elif not opening_parenthesis:
        print("NO")
        break
    else:
        if f"{opening_parenthesis.pop() + current_parenthesis}" not in "()[]{}":
            print("NO")
            break
else:
    print("YES")
