elements = set()

for _ in range(int(input())):
    compounds = input().split()
    for el in compounds:
        elements.add(el)

print(*elements, sep="\n")
