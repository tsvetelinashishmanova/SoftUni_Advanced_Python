usernames = set()

for _ in range(int(input())):
    name = input()
    usernames.add(name)

print(*usernames, sep="\n")
