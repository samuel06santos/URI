n = int(input())
count = 0
for i in range(n):
    i = int(input())
    if i >= 10 and i <= 20:
        count += 1
print(count, 'in')
print(n-count, 'out')
