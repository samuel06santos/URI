n = int(input())
p,a,c,s=0,0,1,''
while (c<=n):
    s+= str(p) + ' '
    p += a
    a = p - a
    if (p==0): p = 1
    c+=1
print(s[:-1])
