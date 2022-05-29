import math as m
c=int(input())
while c!=0:
    b,exp=map(int,input().split())
    result=int(exp*m.log10(b))
    print('{}'.format(result+1))
    c-=1
