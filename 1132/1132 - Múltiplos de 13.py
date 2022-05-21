x,y=int(input()),int(input())
anc,s=0,0
if y<x: anc=y;y=x;x=anc
for i in range(x,y+1):
    if i%13!=0: s+=i
print(s)
