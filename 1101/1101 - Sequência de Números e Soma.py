while True:
    m,n = map(int,input().split())
    if m <= 0 or n <= 0: break
    maior,menor = int((m+n+abs(m-n))/2), int(((m+n+abs(m-n))/2)-(abs(m-n)))
    l = []
    for i in range(menor, maior + 1, 1):
        l.append(i)
        print(i,end=' ')
    print('Sum={}'.format(sum(l)))
