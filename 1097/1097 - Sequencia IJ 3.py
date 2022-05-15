n = [7,6,5]
for i in range(1, 10, 2):
    for e, j in enumerate(n, 0):
        print('I={} J={}'.format(i, j))
        n[e] += 2
        e += 1
