c,s=0,0
while True:
    x = float(input())
    if x >=0 and x <=10: s+=x;c+=1
    else: print('nota invalida')
    if c==2:
        print('media =',s/2)
        break
