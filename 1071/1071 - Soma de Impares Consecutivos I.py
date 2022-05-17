i,f,s = int(input()),int(input()), 0
if i < f: i,f = f,i
for x in range(i-1,f,-1):
    if x%2 == 1: s+=x
print(s)
