try:
    n = int(input())

    for i in range(n):
        t, p = input().split()
        t = int(t)
        if p == "1T":
            print(f"45+{t % 45}" if t > 45 else t)
        elif p == "2T":
            print(f"90+{t % 45}" if t > 45 else 45+t)
        
except EOFError:
    pass
