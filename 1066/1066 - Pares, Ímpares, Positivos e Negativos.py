n = []
for i in range(5):
    n.append(int(input()))
p,im,posi,neg = 0,0,0,0
for i in n:
    if i % 2 == 0: p += 1
    else: im += 1
    if i > 0: posi += 1
    elif i < 0: neg += 1
print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(p,im,posi,neg))
