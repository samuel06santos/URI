try:
    T = int(input())
    r = list(map(int, input().split())).count(T)
    print(r)
except EOFError:
    pass
