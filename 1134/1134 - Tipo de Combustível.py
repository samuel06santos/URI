a,g,d=0,0,0
while True:
    i = int(input())
    if i>=1 and i<=4:
        if i==1: a+=1
        elif i==2: g+=1
        elif i==3: d+=1
        elif i==4: break
    else: continue
print('MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}'.format(a,g,d))
