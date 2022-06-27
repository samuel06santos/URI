for i in range(int(input())):
    x,y = map(str, input().split())
    sli = min(len(x),len(y))
    m = x if len(x)>len(y) else y
    s=''
    for j in range(sli):
       s += x[j] + y[j]
    s+= m[sli:]
    print(s)
