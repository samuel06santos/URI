x = int(input())
for i in range(x):
    a,b = map(int,input().split())
    if b == 0: print('divisao impossivel')
    else: print(a/b)
