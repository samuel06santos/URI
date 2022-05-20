c = int(input())
for i in range(c):
    a,b = map(int, input().split())
    anc,s=0,0
    if a > b: anc=a;a=b;b=anc
    for j in range(a+1,b):
        if j&1: s+=j
    print(s)
