from math import ceil
try:
    inpt = input()
    n, l, d = map(int, inpt.split())
    times = ceil(((n * d) / 1000) / l)
    print(l * times)
except EOFError:
    pass
