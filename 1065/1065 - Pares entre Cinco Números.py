n = []
count = 0
for i in range(5):
    n.append(int(input()))
for i in n:
    if i % 2 == 0:
        count += 1
print(count, 'valores pares')
