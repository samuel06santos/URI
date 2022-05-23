n=[]
a=int(input())
for i in range(10):
    n.append(a)
    a*=2
    print('N[{}] = {}'.format(i,n[i]))
