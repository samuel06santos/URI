a,b,c = input().split();a,b,c=float(a),float(b),float(c)
d = (b**2)-4*a*c
if d < 0 or a == 0:
    print('Impossivel calcular')
elif d == 0:
    R1 = (-b + (d**0.5))/(2*a); R2 = R1
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1,R2))
else:
    R1 = (-b + (d**0.5))/(2*a)
    R2 = (-b - (d**0.5))/(2*a)
    print("R1 = {:.5f}\nR2 = {:.5f}".format(R1,R2))
