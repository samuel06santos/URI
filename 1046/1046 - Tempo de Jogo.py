i,f = map(int, input().split())
t = f - i
if t <= 0:
    t += 24
print('O JOGO DUROU {} HORA(S)'.format(t))
