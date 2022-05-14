while True:
    x,y = input().split(); x,y = int(x),int(y)
    if x == 0 or y == 0: break
    if x > 0:
        if y > 0: print('primeiro')
        if y < 0: print('quarto')
    if x < 0:
        if y > 0: print('segundo')
        if y < 0: print('terceiro')
