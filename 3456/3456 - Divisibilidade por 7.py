try:
    x = int(input())
    print(x)

    while x >= 10:
        last_d = x % 10
        firsts_d = x // 10
        x = 3 * firsts_d + last_d
        print(x)
        
except EOFError:
    pass
