i,q = input().split();i,q = int(i),int(q);v=0
if i == 1:
    v = 4
elif i == 2:
    v = 4.50
elif i == 3:
    v = 5
elif i == 4:
    v = 2
elif i == 5:
    v = 1.5
print('Total: R$ {:.2f}'.format(v*q))
