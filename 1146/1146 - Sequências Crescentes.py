while True:
    x,s = int(input()), ''
    if x == 0: break
    for i in range(1,x+1):
        s+=str(i) + ' '
    print(s[:-1])
