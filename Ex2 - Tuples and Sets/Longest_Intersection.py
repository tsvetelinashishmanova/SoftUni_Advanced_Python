intersections = {}

for _ in range(int(input())):
    first, second = input().split("-")
    first_start, first_end = first.split(",")
    second_start, second_end = second.split(",")
    first_set = set()
    second_set = set()
    for x in range(int(first_start), int(first_end) + 1):
        first_set.add(x)
    for x in range(int(second_start), int(second_end) + 1):
        second_set.add(x)
    intersections[len(first_set.intersection(second_set))] = list(first_set.intersection(second_set))

highest_key = max(intersections)

print(f"Longest intersection is {intersections[highest_key]} with length {highest_key}")


