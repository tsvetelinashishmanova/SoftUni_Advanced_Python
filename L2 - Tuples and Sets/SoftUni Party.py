guests = set()

for _ in range(int(input())):
    number = input()
    guests.add(number)

guest = input()

while guest != "END":
    guests.remove(guest)
    guest = input()

print(len(list(guests)))
print(*sorted(guests), sep="\n")

