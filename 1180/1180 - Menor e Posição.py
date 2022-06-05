c=int(input())
n=list(map(int,input().split()))
m,p=n[0],1
for j,i in enumerate(n,0):
    if i < m: m,p=i,j
print('Menor valor: %d\nPosicao: %d' %(m,p))
