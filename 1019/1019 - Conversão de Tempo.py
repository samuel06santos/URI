sec = int(input())
h = sec//3600; h2 = sec % 3600
m = h2//60; m2 = h2 % 60
s = m2%60
print('{:.0f}:{:.0f}:{:.0f}'.format(h, m, s))
