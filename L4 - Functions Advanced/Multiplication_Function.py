def multiply(*args):
    res = 1
    for num in args:
        res *= num
    return res


print(multiply(4, 5, 6, 1, 3))
