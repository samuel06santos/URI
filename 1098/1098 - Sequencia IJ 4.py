i,n = 0, [1,2,3]
while i <= 2:
    for e, k in enumerate(n,0):
        print('I={} J={}'.format(i,k))
        n[e] += 0.2
        n[e] = int(n[e]) if n[e] == 1 or n[e] == 2 or n[e] == 3 or n[e] == 4 or n[e] == 5 else round(n[e],1)
    i += 0.2;i = int(i) if i == 1.0 or i == 2.0 else round(i,1)
