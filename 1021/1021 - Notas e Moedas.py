vi = int(input().replace(".",""))
n, n2 = [100,50,20,10,5,2], [100,50,25,10,5,1]

print("NOTAS:")
for i in n:
    print(f"{vi // (i * 100)} nota(s) de R$ {i}.00")
    vi %= (i * 100)
print("MOEDAS:")
for j in n2:
    print(f"{vi // j} moeda(s) de R$ {j / 100:.2f}")
    vi %= j
