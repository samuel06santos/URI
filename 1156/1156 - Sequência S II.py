c = 1
for j,i in enumerate(range(2,40,2),1):
    c+= (i+1)/(2**j)
print('{:.2f}'.format(c))
