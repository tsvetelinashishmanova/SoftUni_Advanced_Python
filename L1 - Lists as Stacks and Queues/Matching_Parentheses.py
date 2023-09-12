expression = input()
parentheses = []

for index in range(len(expression)):
    if expression[index] == "(":
        parentheses.append(index)
    elif expression[index] == ")":
        closing_parenthesis = index + 1
        print(expression[parentheses.pop():closing_parenthesis])
