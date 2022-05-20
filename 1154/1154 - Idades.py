n = []
while True:
    x = int(input())
    if x<0: break
    else: n.append(x)
print(sum(n)/len(n))
