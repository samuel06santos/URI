xi, yi, xf, yf = map(int,input().split())
while xi != 0 and xf != 0 and yi != 0 and yf != 0:
    maxx,minx,maxy,miny=max(xi,xf),min(xi,xf),max(yi,yf),min(yi,yf)
    if xi == xf and yi == yf: print(0)
    elif maxx - minx == (maxy - miny): print(1)
    elif xi == xf or yi == yf: print(1)
    else: print(2)
    xi, yi, xf, yf = map(int,input().split())
