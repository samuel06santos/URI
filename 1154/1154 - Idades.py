n = []
while True:
    x = int(input())
    if x<0: break
    else: n.append(x)
print('{:.2f}'.format(sum(n)/len(n)))
