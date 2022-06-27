nd = [6,2,5,5,4,5,6,3,7,6]
for i in range(int(input())):
    number = str(input())
    s = 0
    for j in number:
        s += nd[int(j)]
    print(s, 'leds')
