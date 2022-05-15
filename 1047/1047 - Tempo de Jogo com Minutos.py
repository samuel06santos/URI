hi,mi,hf,mf = map(int, input().split())
th = hf - hi
tm = mf - mi
if tm < 0: tm += 60; th -= 1
if tm == 0 and th <= 0: th += 24
if th < 0: th += 24
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(th,tm))
