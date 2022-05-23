n=[]
for i in range(100):
    n.append(float(input()))
for e,i in enumerate(n,0):
    if i<=10:
        print('A[{}] = {}'.format(e,i))
