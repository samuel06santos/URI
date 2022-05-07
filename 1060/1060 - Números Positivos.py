n = []
count = 0
for i in range(6):
    n.append(float(input()))
for i in n:
    if i > 0:
        count+=1
print(count ,'valores positivos')
