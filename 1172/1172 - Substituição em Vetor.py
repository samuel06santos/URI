n=[]
for i in range(10):
    n.append(int(input()))
for e,j in enumerate(n,0):
    if j <= 0:
        n[e] = 1
    print('X[{}] = {}'.format(e,n[e]))
