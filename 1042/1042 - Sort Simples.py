a,b,c = input().split();a,b,c = int(a),int(b),int(c)
if a > b and a > c:
    t = a
    if b > c:
        s = b; f = c
    else:
        s = c; f = b
if b > a and b > c:
    t = b
    if a > c:
        s = a; f = c
    else:
        s = c; f = a
if c > a and c > b:
    t = c
    if a > b:
        s = a; f = b
    else:
        s = b; f = a
print('{}\n{}\n{}\n\n{}\n{}\n{}'.format(f,s,t,a,b,c))
