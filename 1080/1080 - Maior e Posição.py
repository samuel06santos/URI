n = []
for i in range(100):
    n.append(int(input()))
a = n[0]
for c,i in enumerate(n,0):
    b = n[c]
    maior = int((a + b + abs(a-b))/2)
    a = maior
print('{}\n{}'.format(maior,(n.index(maior)+1)))
