n = []
for i in range(6):
    n.append(float(input()))
posi,s = 0,0
for i in n:
    if i > 0:
        posi += 1
        s += i
print('{} valores positivos\n{:.1f}'.format(posi,s/posi))
