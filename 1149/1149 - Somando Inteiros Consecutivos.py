n = list(map(int,input().split()))
for i in n[1:]:
    if i >= 1: anc = i
s=n[0]
for i in range(s,s+anc):
    if s==i: continue
    s += i
print(s)
