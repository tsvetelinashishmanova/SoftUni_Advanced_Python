symbols = {}
text = list(input())

for el in text:
    if el not in symbols:
        symbols[el] = 0
    symbols[el] += 1

sorted_dict = dict(sorted(symbols.items(), key=lambda item: item[0]))

for key, value in sorted_dict.items():
    print(f"{key}: {value} time/s")

