a,b = int(input()),int(input());anc=0
if b>a: anc=a;a=b;b=anc
for i in range(b+1,a):
    if i%5==2 or i%5==3: print(i)
