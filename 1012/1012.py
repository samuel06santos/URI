a, b, c = (input().split(' ',3))
a, b, c = float(a),float(b),float(c)
pi = 3.14159
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}"
.format((a*c)/2, (pi*(c**2)), ((a+b)*c)/2, b**2, a*b))
