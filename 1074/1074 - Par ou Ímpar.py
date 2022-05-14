a = int(input())
n = []
for i in range(a):
    n.append(int(input()))
for i in n:
    if i == 0: print('NULL')
    if i % 2 == 0 and i > 0: print('EVEN POSITIVE')
    if i % 2 == 0 and i < 0: print('EVEN NEGATIVE')
    if i % 2 == 1 and i > 0: print('ODD POSITIVE')
    if i % 2 == 1 and i < 0: print('ODD NEGATIVE')
