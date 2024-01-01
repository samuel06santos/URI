while True:
    inp = int(input())
    if inp == 0:
        break
    else:
        print(sum(j**2 for j in range(1, inp+1)))
