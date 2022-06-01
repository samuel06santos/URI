n = []
n.append(input())
for i in range(2):
    n.append(float(input()))
print('TOTAL = R$ {:.2f}'.format((n[2]*0.15)+n[1]))
