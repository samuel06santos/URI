for i in range(int(input())):
    x = int(input())
    for i in range(2,x):
        if x%i == 0:
            print(x,'nao eh primo')
            break
    else: print(x,'eh primo')
