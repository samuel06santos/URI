for _ in range(int(input())):
    try:
        print(sum(list(map(int, input().split("+")))))
    except:
        print("skipped")
    
