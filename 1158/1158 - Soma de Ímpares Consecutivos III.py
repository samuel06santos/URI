c = int(input())
while c > 0:
    x,y = map(int,input().split())
    s,anc=0,0
    if not x&1: x+=1
    while anc != y:
        s+=x
        anc+=1
        x+=2
    print(s)
    c-=1
