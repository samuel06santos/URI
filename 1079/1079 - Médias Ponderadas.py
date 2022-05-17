i = 0; x = int(input())
while not i == x:
    a,b,c = map(float, input().split())
    mp = (a*2+b*3+c*5)/10
    print('{:.1f}'.format(mp))
    i += 1
